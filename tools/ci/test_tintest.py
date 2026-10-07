"""tin test: builds a package with its *_test.tin files and reports each TestXxx."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]

LIB = '''package geo

// Area is the area of a w by h rectangle.
fn Area(w i64, h i64) i64 {
	return w * h
}

fn clampPos(x i64) i64 {
	if x < 0 {
		return 0
	}
	return x
}
'''

TESTS = '''package geo

import "crucible"

fn TestArea(t mut crucible.T) {
	crucible.Equal(mut t, "2x3", Area(2, 3), 6)
}

fn TestPrivate(t mut crucible.T) {
	t.True("clamp", clampPos(-1) == 0)
}
'''

FAILING = '''package geo

import "crucible"

fn TestWrong(t mut crucible.T) {
	crucible.Equal(mut t, "area", Area(2, 2), 5)
}
'''

# Issue #94: any parameter name and spacing; Testify is not a test (Go's rule).
SPELLINGS = '''package geo

import "crucible"

fn TestSpaced( t  mut  crucible.T ) {
	t.True("spaced", true)
}

fn  TestOtherName(tt mut crucible.T) {
	crucible.Equal(mut tt, "area", Area(1, 1), 1)
}

fn Testify(x i64) i64 {
	return x
}

fn BenchmarkSpaced(bb  mut crucible.B) {
}
'''

BAD_SIGNATURES = '''package geo

import "crucible"

fn TestNoParam() {
}

fn BenchmarkTakesT(b mut crucible.T) {
}
'''

APP = '''package main

import "say"

fn double(x i64) i64 {
	return 2 * x
}

fn main() {
	say.Line(double(2))
}
'''

APP_TEST = '''package main

import "crucible"

fn TestDouble(t mut crucible.T) {
	crucible.Equal(mut t, "double", double(21), 42)
}
'''


# The same package and tests in edition 1 (#226): fn declarations, found and run alike.
LIB_ED1 = '''package geo

// Area is the area of a w by h rectangle.
fn Area(w i64, h i64) i64 {
	return w * h
}
'''

TESTS_ED1 = '''package geo

import "crucible"

fn TestArea(t mut crucible.T) {
	crucible.Equal(mut t, "2x3", Area(2, 3), 6)
}

fn TestNoParam() {
}
'''


# Output a test prints, and a log line, are events of that test (-json).
CHATTY = '''package geo

import "crucible"
import "say"

fn TestLoud(t mut crucible.T) {
	say.Line("hello from the test")
	t.Log("a logged line")
	crucible.Equal(mut t, "area", Area(2, 2), 4)
}

fn TestBroken(t mut crucible.T) {
	crucible.Equal(mut t, "area", Area(2, 2), 5)
}

fn TestOther(t mut crucible.T) {
	t.True("fine", true)
}
'''


def tin_test(files, *args):
    with tempfile.TemporaryDirectory() as d:
        for name, text in files.items():
            (Path(d) / name).write_text(text)
        r = subprocess.run([str(ROOT / 'tin'), 'test', *args, d], capture_output=True, text=True, timeout=120)
        return r.returncode, r.stdout + r.stderr


class TinTestCommand(unittest.TestCase):
    def test_edition1_package(self):
        code, out = tin_test({'geo.tin': LIB_ED1, 'geo_test.tin': TESTS_ED1.replace('fn TestNoParam() {\n}\n', '')})
        self.assertEqual(code, 0, out)
        self.assertIn('--- PASS: TestArea', out)
        code, out = tin_test({'geo.tin': LIB_ED1, 'geo_test.tin': TESTS_ED1})
        self.assertEqual(code, 2, out)
        self.assertIn('wrong signature for TestNoParam, must be: fn TestNoParam(t mut crucible.T)', out)

    def test_library_package_passes(self):
        code, out = tin_test({'geo.tin': LIB, 'geo_test.tin': TESTS})
        self.assertEqual(code, 0, out)
        self.assertIn('--- PASS: TestArea', out)
        self.assertIn('--- PASS: TestPrivate', out)
        self.assertIn('PASS: 2 tests', out)

    def test_failure_sets_exit_status(self):
        code, out = tin_test({'geo.tin': LIB, 'geo_test.tin': TESTS, 'wrong_test.tin': FAILING})
        self.assertEqual(code, 1, out)
        self.assertIn('--- FAIL: TestWrong', out)
        self.assertIn('area: got 4, want 5', out)

    def test_any_parameter_name_and_spacing(self):
        code, out = tin_test({'geo.tin': LIB, 'geo_test.tin': SPELLINGS})
        self.assertEqual(code, 0, out)
        self.assertIn('--- PASS: TestSpaced', out)
        self.assertIn('--- PASS: TestOtherName', out)
        self.assertIn('PASS: 2 tests', out)

    def test_wrong_signature_is_an_error(self):
        code, out = tin_test({'geo.tin': LIB, 'geo_test.tin': TESTS, 'bad_test.tin': BAD_SIGNATURES})
        self.assertEqual(code, 2, out)
        self.assertIn('bad_test.tin:5: wrong signature for TestNoParam, must be: fn TestNoParam(t mut crucible.T)', out)
        self.assertIn('bad_test.tin:8: wrong signature for BenchmarkTakesT, must be: fn BenchmarkTakesT(b mut crucible.B)', out)
        self.assertNotIn('--- ', out)

    def test_main_package(self):
        code, out = tin_test({'main.tin': APP, 'main_test.tin': APP_TEST})
        self.assertEqual(code, 0, out)
        self.assertIn('--- PASS: TestDouble', out)

    def test_run_picks_tests_by_pattern(self):
        files = {'geo.tin': LIB, 'geo_test.tin': TESTS}
        code, out = tin_test(files, '-run', '^TestArea$')
        self.assertEqual(code, 0, out)
        self.assertIn('--- PASS: TestArea', out)
        self.assertNotIn('TestPrivate', out)
        self.assertIn('PASS: 1 tests', out)
        code, out = tin_test(files, '-run', 'Priv|Nothing')
        self.assertEqual(code, 0, out)
        self.assertIn('--- PASS: TestPrivate', out)
        self.assertNotIn('TestArea', out)
        code, out = tin_test(files, '-run', '(')
        self.assertEqual(code, 2, out)
        self.assertIn('bad pattern', out)

    def test_json_events(self):
        code, out = tin_test({'geo.tin': LIB, 'geo_test.tin': CHATTY}, '-json')
        self.assertEqual(code, 1, out)
        events = [json.loads(line) for line in out.splitlines()]
        kinds = [(e['event'], e['test']) for e in events]
        self.assertEqual(kinds, [
            ('run', 'TestLoud'), ('output', 'TestLoud'), ('output', 'TestLoud'), ('pass', 'TestLoud'),
            ('run', 'TestBroken'), ('output', 'TestBroken'), ('fail', 'TestBroken'),
            ('run', 'TestOther'), ('pass', 'TestOther'), ('summary', '')])
        self.assertEqual(events[1]['message'], 'hello from the test')
        self.assertEqual(events[2]['message'], 'a logged line')
        self.assertEqual(events[5]['message'], 'area: got 4, want 5')
        self.assertIsInstance(events[3]['elapsed_ms'], int)
        self.assertEqual((events[-1]['pass'], events[-1]['fail']), (2, 1))

    def test_json_with_run(self):
        code, out = tin_test({'geo.tin': LIB, 'geo_test.tin': CHATTY}, '-json', '-run', 'Other')
        self.assertEqual(code, 0, out)
        events = [json.loads(line) for line in out.splitlines()]
        self.assertEqual([(e['event'], e['test']) for e in events],
                         [('run', 'TestOther'), ('pass', 'TestOther'), ('summary', '')])

    def test_no_test_files(self):
        code, out = tin_test({'geo.tin': LIB})
        self.assertEqual(code, 0, out)
        self.assertIn('no *_test.tin files', out)


if __name__ == '__main__':
    unittest.main()
