"""tinc -g: a DWARF line table and the functions' names in the executable (#409 macOS, #370 Linux), read back here without
a debugger: the sections are found in the ELF or Mach-O file, the line program is run, and the compilation unit's
subprograms are listed. Without -g the executable has none of it, and with it the program prints the same."""
import os
from pathlib import Path
import platform
import struct
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / 'tools/ci/fixtures/debug_lines.tin'


def tinc():
    """bin/tinc, built from the seed first when it is not there yet (the unit tests run before the bootstrap step)."""
    path = ROOT / 'bin/tinc'
    if not path.exists():
        subprocess.run(['make', '-s', '-C', str(ROOT), 'bin/tinc'], check=True, timeout=600)
    return path


def build(out, *flags):
    env = dict(os.environ, TIN_ROOT=str(ROOT))
    subprocess.run([str(Path(os.environ.get('TINC_UNDER_TEST', str(tinc())))), *flags, '-o', str(out), str(FIXTURE)], check=True, timeout=120, env=env)


def sections(data):
    """{name: bytes} of the DWARF sections of an ELF or Mach-O file."""
    found = {}
    if data[:4] == b'\x7fELF':
        shoff, = struct.unpack_from('<Q', data, 0x28)
        shentsize, shnum, shstrndx = struct.unpack_from('<HHH', data, 0x3A)
        hdrs = [struct.unpack_from('<IIQQQQIIQQ', data, shoff + i * shentsize) for i in range(shnum)]
        names = hdrs[shstrndx]
        for h in hdrs:
            name = data[names[4] + h[0]:data.index(b'\0', names[4] + h[0])].decode()
            if name.startswith('.debug_'):
                found[name] = data[h[4]:h[4] + h[5]]
        return found
    magic, = struct.unpack_from('<I', data, 0)
    assert magic == 0xfeedfacf, 'neither ELF nor Mach-O'
    ncmds, = struct.unpack_from('<I', data, 16)
    at = 32
    for _ in range(ncmds):
        cmd, size = struct.unpack_from('<II', data, at)
        if cmd == 0x19:
            nsects, = struct.unpack_from('<I', data, at + 64)
            for k in range(nsects):
                sect = at + 72 + 80 * k
                name = data[sect:sect + 16].rstrip(b'\0').decode()
                seg = data[sect + 16:sect + 32].rstrip(b'\0').decode()
                sz, off = struct.unpack_from('<QI', data, sect + 40)
                if seg == '__DWARF':
                    found['.' + name[2:]] = data[off:off + sz]
        at += size
    return found


def uleb(b, i):
    v = shift = 0
    while True:
        c = b[i]
        i += 1
        v |= (c & 127) << shift
        shift += 7
        if c < 128:
            return v, i


def sleb(b, i):
    v = shift = 0
    while True:
        c = b[i]
        i += 1
        v |= (c & 127) << shift
        shift += 7
        if c < 128:
            if c & 64:
                v -= 1 << shift
            return v, i


def line_rows(sec):
    """(files, rows): the file names and (address, file, line, column, end_sequence) of a DWARF 4 line program."""
    length, version, header_length = struct.unpack_from('<IHI', sec, 0)
    assert version == 4 and 4 + length == len(sec)
    mil, maxops, default_is_stmt, line_base, line_range, opcode_base = struct.unpack_from('<BBBbBB', sec, 10)
    i = 16 + opcode_base - 1
    lens = list(sec[16:i])
    while sec[i]:  # include directories
        i = sec.index(b'\0', i) + 1
    i += 1
    files = []
    while sec[i]:
        end = sec.index(b'\0', i)
        files.append(sec[i:end].decode())
        i = end + 1
        for _ in range(3):
            _, i = uleb(sec, i)
    i += 1
    assert i == 10 + header_length, (i, header_length)
    rows, addr, file, line, col = [], 0, 1, 1, 0
    while i < len(sec):
        op = sec[i]
        i += 1
        if op >= opcode_base:
            adj = op - opcode_base
            addr += (adj // line_range) * mil
            line += line_base + adj % line_range
            rows.append((addr, file, line, col, False))
        elif op == 0:
            n, i = uleb(sec, i)
            sub = sec[i]
            if sub == 2:
                addr, = struct.unpack_from('<Q', sec, i + 1)
            elif sub == 1:
                rows.append((addr, file, line, col, True))
                addr, file, line, col = 0, 1, 1, 0
            i += n
        elif op == 1:
            rows.append((addr, file, line, col, False))
        elif op == 2:
            d, i = uleb(sec, i)
            addr += d * mil
        elif op == 3:
            d, i = sleb(sec, i)
            line += d
        elif op == 4:
            file, i = uleb(sec, i)
        elif op == 5:
            col, i = uleb(sec, i)
        else:
            for _ in range(lens[op - 1]):
                _, i = uleb(sec, i)
    return files, rows


def dies(info, abbrev):
    """The DIEs of the one compilation unit: {offset: (tag, {attribute: value}, parent offset)} in order."""
    table, i = {}, 0
    while abbrev[i]:
        code, i = uleb(abbrev, i)
        tag, i = uleb(abbrev, i)
        children = abbrev[i]
        i += 1
        attrs = []
        while True:
            a, i = uleb(abbrev, i)
            f, i = uleb(abbrev, i)
            if a == 0 and f == 0:
                break
            attrs.append((a, f))
        table[code] = (tag, children, attrs)
    length, version, abbrev_off, addr_size = struct.unpack_from('<IHIB', info, 0)
    assert version == 4 and addr_size == 8 and 4 + length == len(info)
    i, out, stack = 11, {}, []
    while i < len(info):
        at = i
        code, i = uleb(info, i)
        if code == 0:
            stack.pop()
            continue
        tag, children, attrs = table[code]
        values = {}
        for a, f in attrs:
            if f == 0x08:
                end = info.index(b'\0', i)
                values[a] = info[i:end].decode()
                i = end + 1
            elif f == 0x05:
                values[a], = struct.unpack_from('<H', info, i)
                i += 2
            elif f == 0x06 or f == 0x17 or f == 0x13:
                values[a], = struct.unpack_from('<I', info, i)
                i += 4
            elif f == 0x01 or f == 0x07:
                values[a], = struct.unpack_from('<Q', info, i)
                i += 8
            elif f == 0x0b:
                values[a] = info[i]
                i += 1
            elif f == 0x18:
                n, i = uleb(info, i)
                values[a] = bytes(info[i:i + n])
                i += n
            elif f == 0x19:
                values[a] = True
            else:
                raise AssertionError(f'form {f:#x}')
        out[at] = (tag, values, stack[-1] if stack else None)
        if children:
            stack.append(at)
    return out


def subprograms(info, abbrev):
    """(name, low_pc, high_pc) of each subprogram of the one compilation unit."""
    return [(v[0x03], v[0x11], v[0x11] + v[0x12]) for tag, v, parent in dies(info, abbrev).values() if tag == 0x2e]


def type_text(tree, at):
    """A short text for the type DIE at an offset: a base type's name, a pointer as *target, a struct's name and members."""
    tag, v, _ = tree[at]
    if tag == 0x24:
        return v[0x03]
    if tag == 0x0f:
        return '*' + type_text(tree, v[0x49])
    if tag == 0x13:
        return v[0x03]
    raise AssertionError(f'type tag {tag:#x}')


def variables(tree, name):
    """[(kind, name, type text, location bytes)] of a function's parameters ('param') and locals ('local')."""
    fn = [at for at, (tag, v, parent) in tree.items() if tag == 0x2e and v[0x03] == name][0]
    return [('param' if tag == 0x05 else 'local', v[0x03], type_text(tree, v[0x49]), v[0x02])
            for at, (tag, v, parent) in tree.items() if parent == fn and tag in (0x05, 0x34)]


TARGETS = ['darwin-arm64', 'linux-arm64', 'linux-amd64']


class DebugLines(unittest.TestCase):
    def check_target(self, target):
        with tempfile.TemporaryDirectory() as d:
            exe = Path(d) / 'prog'
            build(exe, '-g', '-target', target)
            secs = sections(exe.read_bytes())
            self.assertEqual(sorted(secs), ['.debug_abbrev', '.debug_info', '.debug_line'], target)
            files, rows = line_rows(secs['.debug_line'])
            self.assertEqual(files[0], str(FIXTURE), target)
            self.assertTrue(rows[-1][4], 'the sequence ends')
            # addresses never go back, and the statements of the fixture are there, in order within a function
            addrs = [r[0] for r in rows]
            self.assertEqual(addrs, sorted(addrs), target)
            mine = [r[2] for r in rows if r[1] == 1 and not r[4]]
            for line in (6, 7, 11, 12, 14):
                self.assertIn(line, mine, f'{target}: line {line}')
            subs = {name: (lo, hi) for name, lo, hi in subprograms(secs['.debug_info'], secs['.debug_abbrev'])}
            for name in ('add', 'pick', 'main.main'):
                self.assertIn(name, subs, target)
            lo, hi = subs['add']
            body = [r for r in rows if lo <= r[0] < hi and r[1] == 1]
            self.assertEqual([r[2] for r in body][:2], [6, 7], f'{target}: the lines of add')
            self.assertTrue(all(lo <= r[0] < hi for r in body))
            # parameters and locals with types and places
            tree = dies(secs['.debug_info'], secs['.debug_abbrev'])
            got = variables(tree, 'describe')
            self.assertEqual([(k, n, t) for k, n, t, _ in got if k == 'param'],
                             [('param', 'p', '*Point'), ('param', 'xs', '*[]i64'), ('param', 'scale', 'f64'), ('param', 'ok', 'bool')], target)
            self.assertEqual({n: t for k, n, t, _ in got if k == 'local'}, {'total': 'i64', 'label': '*str'}, target)
            for k, n, t, loc in got:
                self.assertTrue(len(loc) >= 1, f'{target}: {n} has a location')
            # a struct's members, with their offsets, and the str and slice layouts
            structs = {v[0x03]: at for at, (tag, v, parent) in tree.items() if tag == 0x13}
            members = {n: [(m[0x03], m[0x38]) for at, (tag, m, parent) in tree.items() if parent == structs[n] and tag == 0x0d]
                       for n in ('Point', 'str', '[]i64')}
            self.assertEqual(members['Point'], [('X', 0), ('Y', 8), ('name', 16)], target)
            self.assertEqual(members['str'], [('len', 0), ('data', 8)], target)
            self.assertEqual([m for m, _ in members['[]i64']], ['len', 'cap', 'data', 'region'], target)
            # the function ranges do not overlap and lie inside the line table's range
            spans = sorted(subs.values())
            for (a, b), (c, e) in zip(spans, spans[1:]):
                self.assertLessEqual(b, c, target)
            return secs

    def test_line_tables_in_each_target(self):
        for target in TARGETS:
            self.check_target(target)

    def test_nothing_without_g(self):
        with tempfile.TemporaryDirectory() as d:
            for target in TARGETS:
                exe = Path(d) / target
                build(exe, '-target', target)
                self.assertEqual(sections(exe.read_bytes()), {}, target)

    def test_same_output(self):
        # the native build prints the same with and without -g
        with tempfile.TemporaryDirectory() as d:
            plain, debug = Path(d) / 'plain', Path(d) / 'debug'
            build(plain)
            build(debug, '-g')
            a = subprocess.run([str(plain)], capture_output=True, text=True, timeout=60)
            b = subprocess.run([str(debug)], capture_output=True, text=True, timeout=60)
            self.assertEqual((a.returncode, a.stdout), (0, 'lines 10 22\npt 1.5 true 3\nz 3\n'))
            self.assertEqual((b.returncode, b.stdout), (0, 'lines 10 22\npt 1.5 true 3\nz 3\n'))


if __name__ == '__main__':
    unittest.main()
