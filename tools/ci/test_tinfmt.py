"""tin fmt: the whitespace formatter is idempotent, keeps every token, and its modes work."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]

UNFORMATTED = 'package main\n\nimport "say"\n\n\nfn main() {\n    let x=1\n  if x==1 {\n\t\tsay.Line("a",x)\n    }\n\n}\n'
FORMATTED = 'package main\n\nimport "say"\n\nfn main() {\n\tlet x = 1\n\tif x == 1 {\n\t\tsay.Line("a", x)\n\t}\n}\n'


def tin_fmt(*args, stdin=None):
    r = subprocess.run([str(ROOT / 'tin'), 'fmt', *args], capture_output=True, text=True, input=stdin, timeout=120)
    return r.returncode, r.stdout, r.stderr


def tokens(path):
    r = subprocess.run([str(ROOT / 'bin/tinc'), '-tokens', str(path)], capture_output=True, timeout=60)
    # the lines are "file:line:col KIND text": the place differs when the layout does, the rest must not
    return r.returncode, [line.split(b' ', 1)[1] if b' ' in line else line for line in r.stdout.split(b'\n')]


class FormatCommand(unittest.TestCase):
    def test_stdin(self):
        code, out, _ = tin_fmt('-stdin', stdin=UNFORMATTED)
        self.assertEqual((code, out), (0, FORMATTED))

    def test_list_diff_and_write(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / 'a.tin', Path(d) / 'b.tin'
            a.write_text(UNFORMATTED)
            b.write_text(FORMATTED)
            code, out, _ = tin_fmt('-l', d)
            self.assertEqual((code, out.split()), (1, [str(a)]))
            code, out, _ = tin_fmt('-d', str(a))
            self.assertEqual(code, 1)
            self.assertIn('-    let x=1', out)
            self.assertIn('+\tlet x = 1', out)
            patched = Path(d) / 'patched.tin'
            patched.write_text(UNFORMATTED)
            subprocess.run(['patch', '-s', str(patched)], input=out, text=True, check=True, timeout=30)
            self.assertEqual(patched.read_text(), FORMATTED)
            self.assertEqual(a.read_text(), UNFORMATTED)
            code, out, _ = tin_fmt(str(a))
            self.assertEqual((code, out, a.read_text()), (0, '', FORMATTED))
            code, out, _ = tin_fmt('-l', d)
            self.assertEqual((code, out), (0, ''))

    def test_usage_errors(self):
        self.assertEqual(tin_fmt()[0], 2)
        self.assertEqual(tin_fmt('-x', 'a.tin')[0], 2)
        self.assertEqual(tin_fmt('/nonexistent/a.tin')[0], 2)

    def test_tests_are_idempotent_and_keep_every_token(self):
        exe = Path(tempfile.mkdtemp()) / 'tinfmt'
        subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(exe), str(ROOT / 'tools/fmt/main.tin')], check=True, timeout=120)
        def fmt(text):
            r = subprocess.run([str(exe), '-stdin'], capture_output=True, text=True, input=text, timeout=60)
            return r.returncode, r.stdout, r.stderr
        # the strict tests and the examples: formatting twice changes nothing, and formatting never changes a token
        files = sorted(p for pattern in ('toolchain/tests/v2/*.tin', 'examples/*.tin') for p in ROOT.glob(pattern)
                       if not p.name.endswith('_bad.tin'))
        self.assertGreater(len(files), 100)
        with tempfile.TemporaryDirectory() as d:
            for path in files:
                code, once, err = fmt(path.read_text())
                self.assertEqual(code, 0, f'{path}: {err}')
                code, twice, _ = fmt(once)
                self.assertEqual(once, twice, f'{path}: formatting twice changed it')
                copy = Path(d) / path.name
                copy.write_text(once)
                self.assertEqual(tokens(copy), tokens(path), f'{path}: formatting changed the tokens')


if __name__ == '__main__':
    unittest.main()
