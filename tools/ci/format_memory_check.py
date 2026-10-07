#!/usr/bin/env python3
"""Formatting in a plain program runs in the memory of its results: say.Line takes no pool
memory per call, and an interpolation or say.Fmt no more than the string it returns (#553)."""
import os
import subprocess
import sys
from suite import ROOT


def peak_kib(argv):
    """Runs argv with stdout to /dev/null; returns its exit status, its peak RSS in KiB (the
    program's own VmHWM: a child's ru_maxrss includes the Python that forked it) and stderr."""
    with open(os.devnull, 'wb') as null:
        result = subprocess.run(argv, stdout=null, stderr=subprocess.PIPE, timeout=120)
    lines = result.stderr.split()
    kib = int(lines[-1]) if lines else -1
    return result.returncode, kib, result.stderr


def main():
    if not sys.platform.startswith('linux'):
        print('SKIP format memory: peak RSS is measured on Linux')
        return
    out = ROOT / 'bin/ci/format'
    out.mkdir(parents=True, exist_ok=True)
    exe = out / 'format_memory'
    subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(exe), 'tools/ci/fixtures/format_memory.tin'],
                   check=True, cwd=ROOT, timeout=120)
    peaks = {}
    for what, n in [('line', 10_000_000), ('itoa', 1_000_000), ('interp', 1_000_000), ('fmt', 1_000_000)]:
        code, kib, err = peak_kib([str(exe), what, str(n)])
        assert code == 0, (what, code, err)
        peaks[what] = kib
        print(f'{what} x{n}: peak {kib} KiB')
    # 10 million lines used to take about 3 GB (304 bytes a line); now a few MiB of heap.
    assert peaks['line'] < 16 * 1024, peaks
    # A string from interpolation or say.Fmt costs what the same string made by + costs.
    for what in ('interp', 'fmt'):
        assert peaks[what] <= peaks['itoa'] * 1.1, peaks
    print(f'PASS format memory: 10M say.Line in {peaks["line"]} KiB; 1M interpolations '
          f'{peaks["interp"]} KiB, say.Fmt {peaks["fmt"]} KiB, + and Itoa {peaks["itoa"]} KiB')


if __name__ == '__main__':
    main()
