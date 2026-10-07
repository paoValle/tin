"""tinc -symbols: the declarations of a program as JSON lines (toolchain/docs/TOOLING.md 3.3)."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def tinc():
    """bin/tinc, built from the seed first when it is not there yet (the unit tests run before the bootstrap step)."""
    path = ROOT / 'bin/tinc'
    if not path.exists():
        subprocess.run(['make', '-s', '-C', str(ROOT), 'bin/tinc'], check=True, timeout=600)
    return path

PROGRAM = '''package main

import "say"

// Point is a place.
// It has two fields.
type Point struct {
	X i64
	Y i64
}

type Shape enum {
	Circle(f64)
	Empty
}

const Limit = 10

let counter i64 = 0

// Dist is the distance to the origin, squared.
fn (p Point) Dist() i64 {
	return p.X * p.X + p.Y * p.Y
}

fn (p mut Point) Move(dx i64, dy i64) {
	p.X += dx
}

fn helper(a i64) i64 {
	return a + Limit
}

fn main() {
	let p = Point{X: 1, Y: 2}
	say.Line(p.Dist(), helper(1), counter)
}
'''


def symbols(path, *flags):
    r = subprocess.run([str(tinc()), '-symbols', *flags, str(path)], capture_output=True, text=True,
                       env={'TIN_ROOT': str(ROOT), 'PATH': '/usr/bin:/bin'}, timeout=60)
    return r.returncode, [json.loads(line) for line in r.stdout.splitlines()], r.stderr


class Symbols(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / 'prog.tin'
        self.path.write_text(PROGRAM)

    def tearDown(self):
        self.dir.cleanup()

    def mine(self, syms):
        return {(s['kind'], s['name']): s for s in syms if s['file'] == str(self.path)}

    def test_declarations(self):
        code, syms, _ = symbols(self.path)
        self.assertEqual(code, 0)
        mine = self.mine(syms)
        self.assertEqual(sorted(mine), [('const', 'Limit'), ('fn', 'helper'), ('fn', 'main'), ('method', 'Dist'),
                                        ('method', 'Move'), ('type', 'Point'), ('type', 'Shape'), ('var', 'counter')])
        point = mine[('type', 'Point')]
        self.assertEqual((point['line'], point['col'], point['endCol'], point['sig'], point['exported']),
                         (7, 6, 11, 'type Point struct', True))
        self.assertEqual(point['doc'], 'Point is a place.\nIt has two fields.')
        self.assertEqual(point['members'], [{'name': 'X', 'detail': 'i64'}, {'name': 'Y', 'detail': 'i64'}])
        dist = mine[('method', 'Dist')]
        self.assertEqual((dist['recv'], dist['sig'], dist['doc']),
                         ('Point', 'fn (p Point) Dist() i64', 'Dist is the distance to the origin, squared.'))
        self.assertEqual(mine[('method', 'Move')]['recv'], 'Point')
        self.assertEqual(mine[('method', 'Move')]['sig'], 'fn (p mut Point) Move(dx i64, dy i64)')
        helper = mine[('fn', 'helper')]
        self.assertEqual((helper['line'], helper['col'], helper['exported'], helper['recv']), (30, 4, False, ''))
        self.assertEqual(mine[('const', 'Limit')]['sig'], 'const Limit = 10')
        self.assertEqual(mine[('var', 'counter')]['sig'], 'let counter i64 = 0')
        self.assertEqual([m['name'] for m in mine[('type', 'Shape')]['members']], ['Circle', 'Empty'])

    def test_packages_come_with_their_names(self):
        twine = subprocess.run([str(tinc()), '-symbols', '-edition', '1', str(ROOT / 'toolchain/tests/v2/twine.tin')],
                               capture_output=True, text=True, env={'TIN_ROOT': str(ROOT)}, timeout=60).stdout
        names = {(json.loads(l)['pkg'], json.loads(l)['name']) for l in twine.splitlines()}
        self.assertIn(('twine', 'Split'), names)
        self.assertIn(('twine', 'Join'), names)

    def test_errors_do_not_hide_the_declarations(self):
        self.path.write_text(PROGRAM.replace('return a + Limit', 'return a + Missing'))
        code, syms, err = symbols(self.path)
        self.assertEqual(code, 1)
        self.assertIn('E103', err)
        self.assertIn(('fn', 'helper'), self.mine(syms))


if __name__ == '__main__':
    unittest.main()
