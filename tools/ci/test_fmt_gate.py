"""The tree stays formatted: `tin fmt -l` lists no tracked .tin file except those named in EXCLUDED.

The excluded files are not formatted on purpose: the hot files (AGENTS.md rule 6: no reformatting of existing code in them,
so work in flight is not disturbed), and files whose position in the source is part of what a test checks (expected error
positions, recorded effect sites, vendored files with a hash in a tin.lock, edition 0 syntax, the VS Code fixtures).
To fix a file this test names, run `tin fmt -w` on it."""
import fnmatch
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]

# fnmatch patterns on paths from the repository root ('*' also matches '/').
EXCLUDED = [
    'toolchain/compiler/check.tin', 'toolchain/compiler/lower.tin', 'toolchain/compiler/region.tin',
    'toolchain/compiler/parse.tin', 'toolchain/compiler/inline.tin', 'toolchain/compiler/gen*.tin',
    'toolchain/runtime/runtime*.tin', 'packages/anvil/anvil*.tin',
    '*_bad.tin',
    'toolchain/tests/edition1/*',
    'tools/ci/fixtures/*',
    'toolchain/tests/fixtures/*',
    '*/vendor/*',
    'products/tinland/vscode/*',
]


def tinc():
    """bin/tinc, built from the seed first when it is not there yet (the unit tests run before the bootstrap step)."""
    path = ROOT / 'bin/tinc'
    if not path.exists():
        subprocess.run(['make', '-s', '-C', str(ROOT), 'bin/tinc'], check=True, timeout=600)
    return path


def tracked():
    out = subprocess.run(['git', 'ls-files', '*.tin'], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return [f for f in out.splitlines() if ' ' not in f]


class FormattedFiles(unittest.TestCase):
    def test_nothing_to_format(self):
        files = [f for f in tracked() if not any(fnmatch.fnmatch(f, pattern) for pattern in EXCLUDED)]
        self.assertGreater(len(files), 500)
        with tempfile.TemporaryDirectory() as d:
            exe = Path(d) / 'tinfmt'
            subprocess.run([str(tinc()), '-o', str(exe), str(ROOT / 'tools/fmt/main.tin')], check=True, timeout=300)
            r = subprocess.run([str(exe), '-l', *(str(ROOT / f) for f in files)], capture_output=True, text=True, timeout=600)
        self.assertEqual((r.returncode, r.stdout), (0, ''), 'tin fmt -w these files:\n' + r.stdout)

    def test_the_excluded_files_exist(self):
        # a pattern that matches nothing is a leftover
        files = tracked()
        for pattern in EXCLUDED:
            self.assertTrue(any(fnmatch.fnmatch(f, pattern) for f in files), f'{pattern} matches no file')


if __name__ == '__main__':
    unittest.main()
