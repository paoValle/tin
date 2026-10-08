#!/usr/bin/env python3
"""Long expression chains compile in time near-linear in their length (#713).

A chain `x + x + ... + x` of n terms took time n^3 to compile: the checker's untyped-constant
test and the range analysis's is_const each walked the whole left spine at every level. Each
shape below is generated with N terms and must compile within LIMIT seconds (it takes well under
one; the old compiler needed minutes) and print the right value.
"""
import subprocess
import tempfile
import time
from pathlib import Path

from suite import ROOT

N = 3000
LIMIT = 30


def program(decl, expr):
    return f'package main\n\nimport "say"\n\nfn main() {{\n\t{decl}\n\tlet t = {expr}\n\tsay.Line(t)\n}}\n'


def shapes():
    xs = ["x"] * N
    yield "x + x + ...", program("mut x = 1", " + ".join(xs)), str(N)
    yield "x + 1 + 1 + ...", program("mut x = 1", "x + " + " + ".join(["1"] * N)), str(N + 1)
    yield "1 + 1 + ... + x", program("mut x = 1", " + ".join(["1"] * N) + " + x"), str(N + 1)
    yield "x + (x + (...))", program("mut x = 1", "(x + " * (N - 1) + "x" + ")" * (N - 1)), str(N)
    yield "x +% x +% ...", program("mut x = 1", " +% ".join(xs)), str(N)
    yield "x * 1 - 0 + ...", program("mut x = 1", " + ".join(["x * 1 - 0"] * N)), str(N)
    yield "f64 x + 0.5 + ...", program("mut x = 1.0", "x + " + " + ".join(["0.5"] * N)), str(1 + N // 2)
    yield "str s + \"a\" + ...", program('mut s = "q"', "len(s + " + " + ".join(['"a"'] * N) + ")"), str(N + 1)


def main():
    tinc = ROOT / "bin/tinc"
    with tempfile.TemporaryDirectory(prefix="ctime-", dir=ROOT / "bin") as tmp:
        work = Path(tmp)
        for name, src, want in shapes():
            source = work / "chain.tin"
            source.write_text(src)
            exe = work / "chain"
            start = time.monotonic()
            subprocess.run([str(tinc), "-o", str(exe), str(source)], check=True, timeout=LIMIT, cwd=ROOT)
            took = time.monotonic() - start
            got = subprocess.run([str(exe)], capture_output=True, text=True, timeout=10, check=True).stdout.strip()
            assert got == want, f"{name}: printed {got!r}, want {want!r}"
            print(f"PASS compile time: {name} ({N} terms) in {took:.2f} s")


if __name__ == "__main__":
    main()
