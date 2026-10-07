#!/usr/bin/env python3
"""Float map keys against Go (#643): toolchain/tests/v2/map_float_keys.tin and its Go twin
bench/ref/map_float_keys print the same lines, which are the test's expected output. +0 and -0
are one key, and a NaN key is never found, deleted or overwritten, for f64 keys and for struct
keys holding an f64."""
import os
import subprocess
import tempfile
from pathlib import Path

from suite import ROOT


def main():
    want = (ROOT / 'toolchain/tests/v2/map_float_keys.out').read_text()
    go = subprocess.run(['go', 'run', './bench/ref/map_float_keys'], cwd=ROOT, capture_output=True,
                        text=True, check=True, timeout=180).stdout
    assert go == want, 'Go twin differs from map_float_keys.out:\n' + go
    directory = ROOT / 'bin/ci'
    directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, TIN_ROOT=str(ROOT))
    with tempfile.TemporaryDirectory(prefix='float-keys-', dir=directory) as tmp:
        exe = Path(tmp) / 'map_float_keys'
        subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(exe), 'toolchain/tests/v2/map_float_keys.tin'],
                       check=True, cwd=ROOT, env=env, timeout=120)
        tin = subprocess.run([str(exe)], cwd=ROOT, capture_output=True, text=True, check=True,
                             timeout=60).stdout
    assert tin == go, 'Tin differs from Go:\n' + tin
    print(f'PASS float keys: Tin and Go agree on {len(go.splitlines())} lines (-0, NaN, struct keys, chunked map)')


if __name__ == '__main__':
    main()
