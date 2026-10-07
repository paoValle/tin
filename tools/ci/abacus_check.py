#!/usr/bin/env python3
"""Compare abacus with Go's math/big over 100,000 random operand pairs (sizes 0 to 4096 bits,
mixed signs, the edge values 0, ±1, ±2^63, ±2^64 and powers of two ±1).

Both sides generate the operands from the same seed and print a hash per operation; on a mismatch
the check reruns both in dump mode and reports the first differing case.
"""
import os
import subprocess
import tempfile
from pathlib import Path

from suite import ROOT

PAIRS = 100000
# One process per batch: a whole 100,000-pair run in one process is OOM-killed on the Linux
# runners, so the corpus generates any range of pairs alone (ABACUS_START and ABACUS_N).
BATCH = 10000


def run(exe, env, mode=None):
    args = [str(exe)] + ([mode] if mode else [])
    return subprocess.run(args, capture_output=True, check=True, cwd=ROOT, env=env,
                          timeout=600).stdout.decode().splitlines()


def first_difference(env, go, tin):
    want = run(go, env, 'dump')
    got = run(tin, env, 'dump')
    for i, (a, b) in enumerate(zip(want, got)):
        if a != b:
            return f'line {i + 1}: Go {a!r}, Tin {b!r}'
    return f'{len(got)} tin lines against {len(want)} go lines'


def main():
    directory = ROOT / 'bin/ci/abacus'
    directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, TIN_ROOT=str(ROOT), ABACUS_N=str(PAIRS))
    with tempfile.TemporaryDirectory(prefix='abacus-', dir=directory) as tmp:
        work = Path(tmp)
        tin = work / 'abacus-tin'
        subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(tin), 'tools/ci/fixtures/abacus.tin'],
                       check=True, cwd=ROOT, env=env, timeout=300)
        go = work / 'abacus-go'
        subprocess.run(['go', 'build', '-o', str(go), './bench/ref/abacus'], check=True,
                       cwd=ROOT, timeout=300)
        ops = None
        for start in range(0, PAIRS, BATCH):
            batch = dict(env, ABACUS_START=str(start), ABACUS_N=str(BATCH))
            want = run(go, batch)
            got = run(tin, batch)
            if got != want:
                detail = first_difference(batch, go, tin, start)
                raise AssertionError(f'abacus: results differ from math/big: {detail}')
            names = [line.split()[0] for line in got]
            if ops is None:
                ops = names
            assert names == ops, 'abacus: the operation set changed between batches'
        assert len(ops) == 16, f'abacus: {len(ops)} operations, want 16'
        print(f'PASS abacus: {len(ops)} operations on {PAIRS} operand pairs in '
              f'{PAIRS // BATCH} batches match Go\'s math/big ({", ".join(ops)})')


if __name__ == '__main__':
    main()
