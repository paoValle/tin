"""The files that are formatted stay formatted: `tin fmt -l` lists none of them.

The tree is converted to the formatter's rules directory by directory (about one file in eight differs today, and
reformatting a file others are changing costs them a rebase, so a directory is announced before it is added). A directory
joins the gate by being added to FORMATTED, and its files then fail this test the day they stop conforming; to fix them,
run `tin fmt -w` on them."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]

# Globs from the repository root.
FORMATTED = [
    'products/tinland/app/*.tin',
    'packages/textedit/*.tin',
    'packages/appkit/*.tin',
    'packages/tinfmt/*.tin',
    'packages/tinjson/*.tin',
    'packages/tinsym/*.tin',
    'tools/fmt/*.tin',
    'tools/lsp/*.tin',
    'tools/gen/genfixes.tin',
    'toolchain/tests/darwin/*.tin',
    'toolchain/tests/v2/textedit_*.tin',
    'toolchain/tests/v2/tinfmt.tin',
    'toolchain/tests/v2/tinsym.tin',
]


def tinc():
    """bin/tinc, built from the seed first when it is not there yet (the unit tests run before the bootstrap step)."""
    path = ROOT / 'bin/tinc'
    if not path.exists():
        subprocess.run(['make', '-s', '-C', str(ROOT), 'bin/tinc'], check=True, timeout=600)
    return path


class FormattedFiles(unittest.TestCase):
    def test_nothing_to_format(self):
        files = sorted(str(p) for pattern in FORMATTED for p in ROOT.glob(pattern))
        self.assertGreater(len(files), 30)
        with tempfile.TemporaryDirectory() as d:
            exe = Path(d) / 'tinfmt'
            subprocess.run([str(tinc()), '-o', str(exe), str(ROOT / 'tools/fmt/main.tin')], check=True, timeout=300)
            r = subprocess.run([str(exe), '-l', *files], capture_output=True, text=True, timeout=300)
        self.assertEqual((r.returncode, r.stdout), (0, ''), 'tin fmt -w these files:\n' + r.stdout)


if __name__ == '__main__':
    unittest.main()
