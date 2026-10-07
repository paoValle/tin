#!/usr/bin/env python3
"""Generate tools/gen/arch/fe25519-arm64.S and fe25519-amd64.S: seal's fe_mul and fe_sq (mod
2^255 - 19, five limbs in radix 2^51) as assembly leaves (#488), the same arithmetic as the
Tin code tools/gen/gen_fe25519.py writes (toolchain/std/seal/fe25519.tin): each coefficient is
a sum of 64x64-bit products in 128 bits (a product past limb 4 wraps with factor 19, folded
into the operand), then carried back below 2^52. The product tables below are checked on a
model against Python integers before anything is written.

  fe_mul_hw(h, f, g), fe_sq_hw(h, f): the addresses of five u64 limbs; h may alias f or g.

arm64 uses mul/umulh and adds/adc; x86-64 uses BMI2 mulx (the CPU check is bmi2_cpu).
Constant time: straight-line code. Relocation-free; r15 and x28 (the core context) are untouched."""
import argparse
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[2]
P = (1 << 255) - 19
M51 = (1 << 51) - 1
M64 = (1 << 64) - 1

# Each coefficient is a list of (f-side operand, g-side operand); operands are limb names or
# premultiplied ones (f1x19, f0x2, ...).
MUL_PRE = [('f1x19', 'f1', 19), ('f2x19', 'f2', 19), ('f3x19', 'f3', 19), ('f4x19', 'f4', 19)]
MUL_ROWS = [[(f'f{i}x19' if i + (k - i) % 5 >= 5 else f'f{i}', f'g{(k - i) % 5}') for i in range(5)] for k in range(5)]
SQ_PRE = [('f0x2', 'f0', 2), ('f1x2', 'f1', 2), ('f1x38', 'f1', 38), ('f2x38', 'f2', 38), ('f3x38', 'f3', 38),
          ('f3x19', 'f3', 19), ('f4x19', 'f4', 19)]
SQ_ROWS = [
    [('f0', 'f0'), ('f1x38', 'f4'), ('f2x38', 'f3')],
    [('f0x2', 'f1'), ('f2x38', 'f4'), ('f3x19', 'f3')],
    [('f0x2', 'f2'), ('f1', 'f1'), ('f3x38', 'f4')],
    [('f0x2', 'f3'), ('f1x2', 'f2'), ('f4x19', 'f4')],
    [('f0x2', 'f4'), ('f1x2', 'f3'), ('f2', 'f2')],
]
# The order the coefficients are computed in: r4 first, so that each carry is used as soon as it exists.
ORDER = [4, 0, 1, 2, 3]


def model(pre, rows, f, g):
    """The leaf's arithmetic on Python integers (what the assembly computes)."""
    env = {f'f{i}': f[i] for i in range(5)} | {f'g{i}': g[i] for i in range(5)}
    for name, base, k in pre:
        env[name] = (env[base] * k) & M64
    r = [sum(env[a] * env[b] for a, b in row) for row in rows]
    assert all(v < 1 << 128 for v in r)
    c = [(v >> 51) & M64 for v in r]
    lo = [v & M51 for v in r]
    s = [(lo[0] + c[4] * 19) & M64] + [(lo[i] + c[i - 1]) & M64 for i in range(1, 5)]
    h = [((s[0] & M51) + (s[4] >> 51) * 19) & M64] + [((s[i] & M51) + (s[i - 1] >> 51)) & M64 for i in range(1, 5)]
    return h


def check():
    rnd = random.Random(488)
    lim = [0, 1, M51, M51 + 1, (1 << 52) - 1, 19, 1 << 50]
    for _ in range(20000):
        f = [rnd.choice(lim) if rnd.random() < .3 else rnd.getrandbits(52) for _ in range(5)]
        g = [rnd.choice(lim) if rnd.random() < .3 else rnd.getrandbits(52) for _ in range(5)]
        fv = sum(f[i] << (51 * i) for i in range(5))
        gv = sum(g[i] << (51 * i) for i in range(5))
        for pre, rows, gg in ((MUL_PRE, MUL_ROWS, g), (SQ_PRE, SQ_ROWS, f)):
            h = model(pre, rows, f, gg)
            hv = sum(h[i] << (51 * i) for i in range(5))
            other = gv if gg is g else fv
            assert hv % P == fv * other % P, (f, gg)
            assert all(x < 1 << 52 for x in h)


# ---------------- AArch64 ----------------

MASK_A = '#0x7ffffffffffff'


def arm64(name, pre, rows, square):
    """x0 = h, x1 = f, x2 = g. f in x3-x7, g in x8-x12, premultiplied limbs after them; the
    accumulator is x17 (lo) and x1 (hi), the product temporaries x2 and the last free register;
    h is parked in x19, and the carries and sums in x20-x27."""
    regs = {f'f{i}': f'x{3 + i}' for i in range(5)}
    nxt = 8
    if not square:
        regs |= {f'g{i}': f'x{8 + i}' for i in range(5)}
        nxt = 13
    out = [f'\t.globl {name}', f'\t.type {name}, %function', f'{name}:',
           '\tstp\tx19, x20, [sp, #-80]!', '\tstp\tx21, x22, [sp, #16]', '\tstp\tx23, x24, [sp, #32]',
           '\tstp\tx25, x26, [sp, #48]', '\tstr\tx27, [sp, #64]',
           '\tmov\tx19, x0', '\tldp\tx3, x4, [x1]', '\tldp\tx5, x6, [x1, #16]', '\tldr\tx7, [x1, #32]']
    if not square:
        out += ['\tldp\tx8, x9, [x2]', '\tldp\tx10, x11, [x2, #16]', '\tldr\tx12, [x2, #32]']
    th = 'x0' if not square else 'x16'
    out.append(f'\tmov\t{th}, #0')
    cur = None
    for pname, base, k in pre:
        if cur != k:
            out.append(f'\tmov\tx17, #{k}')
            cur = k
        regs[pname] = f'x{nxt}'
        out.append(f'\tmul\tx{nxt}, {regs[base]}, x17')
        nxt += 1
    lo, hi, tl = 'x17', 'x1', 'x2'
    m4, c4, cs = 'x20', 'x21', ['x22', 'x23']
    S = ['x24', 'x25', 'x26', 'x27']
    prev = None
    ci = 0
    for k in ORDER:
        row = rows[k]
        a, b = row[0]
        out += [f'\tmul\t{lo}, {regs[a]}, {regs[b]}', f'\tumulh\t{hi}, {regs[a]}, {regs[b]}']
        for a, b in row[1:]:
            out += [f'\tmul\t{tl}, {regs[a]}, {regs[b]}', f'\tumulh\t{th}, {regs[a]}, {regs[b]}',
                    f'\tadds\t{lo}, {lo}, {tl}', f'\tadc\t{hi}, {hi}, {th}']
        if k == 4:
            out += [f'\textr\t{c4}, {hi}, {lo}, #51', f'\tand\t{m4}, {lo}, {MASK_A}']
            continue
        c = cs[ci]
        ci ^= 1
        out += [f'\textr\t{c}, {hi}, {lo}, #51', f'\tand\t{lo}, {lo}, {MASK_A}']
        if k == 0:
            out += [f'\tmov\t{tl}, #19', f'\tmadd\t{S[0]}, {c4}, {tl}, {lo}']
        else:
            out.append(f'\tadd\t{S[k]}, {lo}, {prev}')
        prev = c
    out.append(f'\tadd\t{m4}, {m4}, {prev}')  # s4
    s = S + [m4]
    out += [f'\tlsr\t{th}, {s[4]}, #51', f'\tmov\t{tl}, #19', f'\tand\t{lo}, {s[0]}, {MASK_A}',
            f'\tmadd\t{lo}, {th}, {tl}, {lo}', f'\tstr\t{lo}, [x19]']
    for i in range(1, 5):
        out += [f'\tand\t{lo}, {s[i]}, {MASK_A}', f'\tadd\t{lo}, {lo}, {s[i - 1]}, lsr #51',
                f'\tstr\t{lo}, [x19, #{8 * i}]']
    out += ['\tldr\tx27, [sp, #64]', '\tldp\tx25, x26, [sp, #48]', '\tldp\tx23, x24, [sp, #32]',
            '\tldp\tx21, x22, [sp, #16]', '\tldp\tx19, x20, [sp], #80', '\tret', f'\t.size {name}, .-{name}']
    return out


# ---------------- x86-64 (BMI2) ----------------


def amd64(name, pre, rows, square):
    """rdi = h, rsi = f, rdx = g (moved to rcx). Operands are read from memory: f at rsi, g at
    rcx, the premultiplied limbs in the frame at rsp (56 bytes), the sums s0-s3 at rsp+64.
    r8/r9 accumulate (lo/hi), r10/r11 hold a product, rbx = r4's low bits, rbp = c4, r12/r13
    the carries, r14 = mask51."""
    mem = {f'f{i}': f'[rsi+{8 * i}]' for i in range(5)}
    if not square:
        mem |= {f'g{i}': f'[rcx+{8 * i}]' for i in range(5)}
    out = [f'\t.globl {name}', f'\t.type {name}, @function', f'{name}:']
    out += ['\tpush\trbx', '\tpush\trbp', '\tpush\tr12', '\tpush\tr13', '\tpush\tr14', '\tsub\trsp, 96']
    if not square:
        out.append('\tmov\trcx, rdx')
    out.append('\tmov\tr14, 0x7ffffffffffff')
    for n, (pname, base, k) in enumerate(pre):
        out += [f'\timul\trax, {mem[base]}, {k}', f'\tmov\t[rsp+{8 * n}], rax']
        mem[pname] = f'[rsp+{8 * n}]'
    prev = None
    ci = 0
    cs = ['r12', 'r13']
    for k in ORDER:
        row = rows[k]
        a, b = row[0]
        out += [f'\tmov\trdx, {mem[a]}', f'\tmulx\tr9, r8, {mem[b]}']
        for a, b in row[1:]:
            out += [f'\tmov\trdx, {mem[a]}', f'\tmulx\tr11, r10, {mem[b]}', '\tadd\tr8, r10', '\tadc\tr9, r11']
        out.append('\tshld\tr9, r8, 13')
        if k == 4:
            out += ['\tmov\trbp, r9', '\tmov\trbx, r8', '\tand\trbx, r14']
            continue
        c = cs[ci]
        ci ^= 1
        out += [f'\tmov\t{c}, r9', '\tand\tr8, r14']
        if k == 0:
            out += ['\timul\trax, rbp, 19', '\tadd\tr8, rax']
        else:
            out.append(f'\tadd\tr8, {prev}')
        out.append(f'\tmov\t[rsp+{64 + 8 * k}], r8')
        prev = c
    out.append(f'\tadd\trbx, {prev}')  # s4
    out += ['\tmov\trax, rbx', '\tshr\trax, 51', '\timul\trax, rax, 19', '\tmov\tr9, [rsp+64]', '\tmov\tr8, r9',
            '\tand\tr8, r14', '\tadd\tr8, rax', '\tmov\t[rdi], r8']
    for i in range(1, 5):
        cur = 'rbx' if i == 4 else f'[rsp+{64 + 8 * i}]'
        out += [f'\tmov\tr8, {cur}', '\tand\tr8, r14', '\tshr\tr9, 51', '\tadd\tr8, r9', f'\tmov\t[rdi+{8 * i}], r8']
        if i < 4:
            out.append(f'\tmov\tr9, {cur}')
    out += ['\tadd\trsp, 96', '\tpop\tr14', '\tpop\tr13', '\tpop\tr12', '\tpop\trbp', '\tpop\trbx', '\tret',
            f'\t.size {name}, .-{name}']
    return out


HEADER_X = """// fe_mul_hw and fe_sq_hw for seal (#488), x86-64 with BMI2 (mulx; the CPU check is bmi2_cpu).
// Generated by tools/gen/gen_fe25519_asm.py; do not edit. tools/gen/gen_aes_hw.py turns them into
// toolchain/compiler/aes_hw.tin. Relocation-free, never touches r15 (the core context); rbx, rbp and
// r12-r14 are saved. Straight-line: no branch or address depends on the operands.
.intel_syntax noprefix
.text
"""


HEADER_A = """// fe_mul_hw and fe_sq_hw for seal (#488), AArch64. Generated by tools/gen/gen_fe25519_asm.py; do not
// edit. tools/gen/gen_aes_hw.py turns them into toolchain/compiler/aes_hw.tin. Relocation-free; they
// use x0-x17 and the callee-saved x19-x27 (saved here) and keep x28 (the core context). Straight-line:
// no branch or address depends on the operands.
\t.text
"""


def render():
    a = [HEADER_A, '// fe_mul_hw(h x0, f x1, g x2): h = f*g mod 2^255-19, limbs below 2^52 in and out.']
    a += arm64('fe_mul_hw', MUL_PRE, MUL_ROWS, False)
    a += ['', '// fe_sq_hw(h x0, f x1): h = f*f.']
    a += arm64('fe_sq_hw', SQ_PRE, SQ_ROWS, True)
    x = [HEADER_X, '// fe_mul_hw(h rdi, f rsi, g rdx): h = f*g mod 2^255-19, limbs below 2^52 in and out.']
    x += amd64('fe_mul_hw', MUL_PRE, MUL_ROWS, False)
    x += ['', '// fe_sq_hw(h rdi, f rsi): h = f*f.']
    x += amd64('fe_sq_hw', SQ_PRE, SQ_ROWS, True)
    return {'fe25519-amd64.S': '\n'.join(x) + '\n', 'fe25519-arm64.S': '\n'.join(a) + '\n'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    check()
    for name, text in render().items():
        path = ROOT / 'tools/gen/arch' / name
        if args.check:
            assert path.read_text() == text, f'{name} is stale: run tools/gen/gen_fe25519_asm.py'
        else:
            path.write_text(text)
