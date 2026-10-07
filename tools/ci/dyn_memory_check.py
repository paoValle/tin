#!/usr/bin/env python3
"""A dyn value replaced in long-lived memory is released (#618): a global, a struct field, a
?dyn field, a slice element (stored or copied) and a map value, each replaced a million
times, keep the peak RSS of a few thousand replacements."""
import os
import subprocess
import sys
from suite import ROOT


def peak_kib(argv):
    """Runs argv with stdout to /dev/null; returns its exit status, its peak RSS in KiB (the
    program's own VmHWM) and stderr."""
    with open(os.devnull, 'wb') as null:
        result = subprocess.run(argv, stdout=null, stderr=subprocess.PIPE, timeout=120)
    lines = result.stderr.split()
    kib = int(lines[-1]) if lines else -1
    return result.returncode, kib, result.stderr


def main():
    if not sys.platform.startswith('linux'):
        print('SKIP dyn memory: peak RSS is measured on Linux')
        return
    out = ROOT / 'bin/ci/dyn'
    out.mkdir(parents=True, exist_ok=True)
    exe = out / 'dyn_memory'
    subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(exe), 'tools/ci/fixtures/dyn_memory.tin'],
                   check=True, cwd=ROOT, timeout=120)
    report = []
    for what in ('field', 'opt', 'global', 'slice', 'copy', 'map'):
        peaks = []
        for n in (10_000, 1_000_000):
            code, kib, err = peak_kib([str(exe), what, str(n)])
            assert code == 0, (what, n, code, err)
            peaks.append(kib)
        print(f'{what}: peak {peaks[0]} KiB at 10k, {peaks[1]} KiB at 1M')
        # Before #618 every replaced object stayed: about 30 MB more at a million. The
        # margin only absorbs measurement noise.
        assert peaks[1] <= peaks[0] + 4096, (what, peaks)
        report.append(f'{what} {peaks[1]} KiB')
    print('PASS dyn memory: a million replacements each, ' + ', '.join(report))


if __name__ == '__main__':
    main()
