#!/usr/bin/env python3
"""Compare exact number bits and text with Go and a pinned hard parsing corpus."""
import gzip
import json
import os
from pathlib import Path
import struct
import subprocess
import tempfile

from suite import ROOT


def compare(exe, inputs, expected, directory, label):
    assert len(inputs) == len(expected) and inputs, 'empty or incomplete number corpus'
    # Bounded batches keep the request pool small without exposing private reset helpers.
    for start in range(0, len(inputs), 10000):
        batch = inputs[start:start + 10000]
        result = subprocess.run([str(exe)], input=b''.join(batch), capture_output=True,
                                timeout=60, cwd=ROOT)
        (directory / (label + '.stderr.log')).write_bytes(result.stderr)
        assert result.returncode == 0, f'{label}: exit {result.returncode}: {result.stderr!r}'
        actual = result.stdout.splitlines(keepends=True)
        want = expected[start:start + len(batch)]
        if actual != want:
            (directory / (label + '.actual.log')).write_bytes(result.stdout)
            for i, (got, value) in enumerate(zip(actual, want)):
                if got != value:
                    raise AssertionError(f'{label} case {start+i}: {batch[i]!r}: '
                                         f'got {got!r}, want {value!r}')
            raise AssertionError(f'{label}: {len(actual)} output lines, want {len(want)}')
    print(f'PASS {label}: {len(inputs)} exact results')


# gauge: the functions of #575, how many results each one prints, and the allowed difference
# from Go in ulps of the result bits (0 = bit-identical). dump mode prints
# "<name> <i> <input bits...> <result bits>" lines; both sides generate the inputs from the same
# seed, GAUGE_N random values plus the edge cases.
GAUGE_FUNCS = [
    # expm1's, the inverse hyperbolics' and sincos' arithmetic is Go's, but the compilers fuse
    # multiply-adds differently (arm64 fuses, x86-64 does not, and Go and Tin do not fuse the
    # same products: design/stdlib_verified.md, "gauge: the corpus check"), so these five are
    # allowed exactly one ulp, and never more. FMA is exact everywhere (the software port).
    ('expm1', 1, 1), ('asinh', 1, 1), ('acosh', 1, 1), ('atanh', 1, 1), ('sincos', 2, 1),
    ('logb', 1, 0), ('f32bits', 1, 0), ('f32frombits', 1, 0),
    ('dim', 1, 0), ('remainder', 1, 0), ('nextafter', 1, 0), ('nextafter32', 1, 0), ('fma', 1, 0),
    # #575's second half: erf, erfc, erfcinv and gamma are bit-identical; erfinv uses Log and
    # lgamma uses Log and Sin, so they inherit the documented one-ulp log difference.
    ('erf', 1, 0), ('erfc', 1, 0), ('erfcinv', 1, 0), ('gamma', 1, 0), ('erfinv', 1, 1),
]

# lgamma's result can lose precision through cancellation (nadj - lgamma near its zero
# crossings), which turns the inherited one-ulp Log difference into a few ulps of the result;
# it is checked with a relative tolerance instead, and the sign must match exactly.
GAUGE_RELATIVE = [('lgamma', 2, (1e-14, 1e-13))]

GAUGE_INPUTS = 120000


def ulps(a, b):
    """ulps is the distance in ulps between two f64 bit patterns, or None if incomparable.

    NaNs compare equal (their payloads are not part of a function's contract), equal values are
    zero apart, and values of different signs only match when both are zero.
    """
    xa = struct.unpack('<d', struct.pack('<Q', a))[0]
    xb = struct.unpack('<d', struct.pack('<Q', b))[0]
    if xa != xa and xb != xb:
        return 0
    if xa != xa or xb != xb:
        return None
    if xa == xb:
        return 0
    if (xa < 0) != (xb < 0):
        return None
    return abs(a - b)


def gauge_relative(root, work, name, results, tolerance):
    """gauge_relative checks one function whose result may cancel, with a relative tolerance."""
    env = dict(os.environ, TIN_ROOT=str(root), GAUGE_N=str(GAUGE_INPUTS), GAUGE_FUNC=name)
    outs = []
    for exe in (work / 'gauge-go', work / 'gauge-tin'):
        result = subprocess.run([str(exe), 'dump'], capture_output=True, check=True,
                                cwd=root, env=env, timeout=300)
        outs.append([line.split() for line in result.stdout.splitlines()])
    want, got = outs
    assert len(got) == len(want) > GAUGE_INPUTS, f'gauge {name}: line counts differ'
    worst_rel = 0.0
    differing = 0
    bad = 0
    for i, (a, b) in enumerate(zip(want, got)):
        assert a[:-results] == b[:-results], f'gauge {name} case {i}: inputs differ'
        g = struct.unpack('<d', struct.pack('<Q', int(a[-2], 16)))[0]
        t = struct.unpack('<d', struct.pack('<Q', int(b[-2], 16)))[0]
        if a[-1] != b[-1]:
            bad += 1
        if g != g and t != t:
            continue
        if g == t:  # includes equal infinities and signed zeros
            continue
        absolute = abs(t - g)
        relative = absolute / abs(g) if g != 0 else 0.0
        if absolute != 0:
            differing += 1
            worst_rel = max(worst_rel, relative)
        if g != g or t != t or absolute > tolerance[0] + tolerance[1] * abs(g):
            bad += 1
    assert bad == 0, f'gauge {name}: {bad} of {len(got)} results outside the tolerance'
    print(f'PASS gauge {name}: {len(got)} inputs, {len(got) - differing} bit-identical, '
          f'worst relative difference {worst_rel:.2e}')
    return len(got) * results


def gauge(root, work):
    """gauge checks every #575 function against Go over 120,000 inputs."""
    env = dict(os.environ, TIN_ROOT=str(root), GAUGE_N=str(GAUGE_INPUTS))
    tin = work / 'gauge-tin'
    subprocess.run([str(root / 'bin/tinc'), '-o', str(tin), 'bench/ref/gauge/corpus.tin'],
                   check=True, cwd=root, env=env, timeout=120)
    go = work / 'gauge-go'
    subprocess.run(['go', 'build', '-o', str(go), './bench/ref/gauge'], check=True, cwd=root,
                   timeout=120)
    total = 0
    for name, results, allowed in GAUGE_FUNCS:
        outs = []
        for exe in (go, tin):
            run = dict(env, GAUGE_FUNC=name)
            result = subprocess.run([str(exe), 'dump'], capture_output=True, check=True,
                                    cwd=root, env=run, timeout=300)
            outs.append([line.split() for line in result.stdout.splitlines()])
        want, got = outs
        assert len(got) == len(want) > GAUGE_INPUTS,             f'gauge {name}: {len(got)} tin and {len(want)} go lines, want more than {GAUGE_INPUTS}'
        bad = within = 0
        for i, (a, b) in enumerate(zip(want, got)):
            assert a[:-results] == b[:-results], f'gauge {name} case {i}: inputs differ: {a} vs {b}'
            for bits_a, bits_b in zip(a[-results:], b[-results:]):
                d = ulps(int(bits_a, 16), int(bits_b, 16))
                if d is None or d > allowed:
                    bad += 1
                    if bad < 4:
                        print(f'  gauge {name} case {i}: Go {bits_a}, Tin {bits_b}')
                elif d > 0:
                    within += 1
        assert bad == 0, f'gauge {name}: {bad} of {len(got)} results beyond {allowed} ulp of Go'
        total += len(got) * results
        exact = (len(got) * results) - within
        print(f'PASS gauge {name}: {len(got)} inputs, {exact} bit-identical, {within} within '
              f'{allowed} ulp')
    for name, results, tolerance in GAUGE_RELATIVE:
        total += gauge_relative(root, work, name, results, tolerance)
    print(f'PASS gauge: {total} results, {len(GAUGE_FUNCS) + len(GAUGE_RELATIVE)} functions, '
          f'at least {GAUGE_INPUTS} inputs each')
    return total


def main():
    directory = ROOT / 'bin/ci/number'
    directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, TIN_ROOT=str(ROOT))
    subprocess.run(['python3', str(ROOT / 'tools/gen/gen_number_powers.py'), '--check'],
                   check=True, cwd=ROOT, timeout=10)
    with tempfile.TemporaryDirectory(prefix='number-', dir=directory) as tmp:
        work = Path(tmp)
        exe = work / 'number'
        subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(exe),
                        'tools/ci/fixtures/number.tin'], check=True, cwd=ROOT, env=env,
                       timeout=60)
        subprocess.run(['go', 'run', './bench/ref/number', str(work)], check=True,
                       cwd=ROOT, timeout=60)
        gauge(ROOT, work)
        # mint's faults read like strconv's under mint's own name (#521).
        expected_go = [line.replace(b'ERR strconv.', b'ERR mint.', 1)
                       for line in (work / 'expected.txt').read_bytes().splitlines(keepends=True)]
        compare(exe, (work / 'input.txt').read_bytes().splitlines(keepends=True),
                expected_go, directory, 'Go-strconv-fmt')
        rows = gzip.decompress((ROOT / 'tools/ci/data/parse-number-f64.txt.gz').read_bytes())
        inputs, expected = [], []
        for row in rows.splitlines():
            bits, number = row.split(b' ', 1)
            inputs.append(b'P\t' + number + b'\n')
            expected.append(str(int(bits, 16)).encode() + b'\n')
        compare(exe, inputs, expected, directory, 'parse-number-fxx')
        (directory / 'results.json').write_text(json.dumps(
            {'passed': True, 'go_cases': len((work / 'input.txt').read_bytes().splitlines()),
             'hard_cases': len(inputs)}, indent=2) + '\n')


if __name__ == '__main__':
    main()
