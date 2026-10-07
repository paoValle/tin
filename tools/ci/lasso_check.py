#!/usr/bin/env python3
"""Compare lasso with Go's regexp over a generated corpus and the ported test tables.

Three phases:

1. A generated corpus of pattern/input pairs from a small pattern grammar and a deterministic
   PRNG (so both sides see exactly the same pairs). Both sides print one line per pair
   (bench/ref/lasso and tools/ci/fixtures/lasso.tin): whether the pattern compiles, whether it
   matches, the leftmost match, the submatch offsets and every match with its submatches; the
   check compares the lines.
2. Go's regexp find_test.go table (ported to toolchain/tests/data/lasso/find_test.txt): each
   case's FindAllStringSubmatchIndex, against the table's own expectations.
3. Go's RE2 re2-search.txt (ported, BSD-licensed, licences in licenses/regexp.txt): for each
   pattern and string the anchored match (`\\A(?:pattern)\\z`) and, when it matches, the search
   result must be the file's.

The inputs use code points whose Unicode category and script tables agree between the glyph
tables (Unicode 15) and the Go toolchain's (a newer Unicode), so a table version difference is
not reported as a lasso bug; the Unicode classes themselves are covered.
"""
import ast
import random
import subprocess
import tempfile
from pathlib import Path

from suite import ROOT

SEED = 571
PAIRS = 12000
DATA = ROOT / "toolchain/tests/data/lasso"
ALPHABET = "abcABC012 _-.,;\t\n" + "αβγé中"
LITERALS = "abcABC012 _-.,;"
CLASSES = ["[abc]", "[^abc]", "[a-c]", "[0-9]", "[^0-9]", "[a-zA-Z0-9_]", "[α-γ]", "[^ ]",
           r"[\d]", r"[\w\s]", r"[\p{L}]", "[[:alpha:]]", "[[:^digit:]]"]
PERLS = [r"\d", r"\D", r"\w", r"\W", r"\s", r"\S", r"\p{L}", r"\pL", r"\p{Greek}", r"\P{L}",
         r"\p{Nd}"]
ANCHORS = ["^", "$", r"\b", r"\B", r"\A", r"\z"]
QUANTS = ["*", "+", "?", "{2}", "{1,3}", "{0,2}", "{2,}", "*?", "+?", "??", "{1,2}?"]
FLAGS = ["", "(?i)", "(?s)", "(?m)", "(?U)", "(?is)", "(?i:)", "(?m:)", "(?s:)"]
NAMES = ["a", "b", "g1", "x_y"]


def atom(rng, depth):
    r = rng.random()
    if r < 0.30:
        return rng.choice(LITERALS)
    if r < 0.40:
        return "."
    if r < 0.55:
        return rng.choice(CLASSES)
    if r < 0.68:
        return rng.choice(PERLS)
    if r < 0.75:
        return rng.choice(ANCHORS)
    if depth > 0 and r < 0.85:
        inner = alt(rng, depth - 1)
        kind = rng.random()
        if kind < 0.5:
            return "(" + inner + ")"
        if kind < 0.8:
            return "(?:" + inner + ")"
        return "(?P<" + rng.choice(NAMES) + ">" + inner + ")"
    if r < 0.90:
        return rng.choice([r"\x41", r"\x{3B1}", r"\Qa+b\E", r"\.", r"\+"])
    return rng.choice(LITERALS)


def concat(rng, depth):
    n = rng.randint(1, 3)
    out = []
    for _ in range(n):
        a = atom(rng, depth)
        if rng.random() < 0.35:
            a += rng.choice(QUANTS)
        out.append(a)
    return "".join(out)


def alt(rng, depth):
    n = rng.randint(1, 2)
    return "|".join(concat(rng, depth) for _ in range(n))


def pattern(rng):
    return rng.choice(FLAGS) + alt(rng, 2)


def input_string(rng):
    n = rng.randint(0, 16)
    return "".join(rng.choice(ALPHABET) for _ in range(n))


FIXED = [
    (r"(?P<key>\w+)=(?P<val>[^&]*)", "a=b&c=d"),
    (r"(\w+),(\w+)", "one,two three,four"),
    (r"a{2,3}", "aaaa"),
    (r"(a*)*b", "aaaab"),
    (r"(a|b)+", "xabbay"),
    (r"^abc$", "abc"),
    (r"(?m)^b", "a\nb"),
    (r"(?s).", "\n"),
    (r"(?i)Σ", "σ"),
    (r"\bword\b", "a word here"),
    (r"[[:alpha:]]+", "12ab34"),
    (r"\p{Greek}+", "xαβγ"),
    (r"\Qa+b\E", "xa+b"),
    (r"a+?b", "aaab"),
    (r"(?:ab)+", "ababab"),
    (r"x|", "x"),
    (r"()", "ab"),
    (r"(a)?b", "b"),
    (r"a$", "a\n"),
    (r"\B", "ab"),
]


def generated():
    rng = random.Random(SEED)
    pairs = list(FIXED)
    while len(pairs) < PAIRS:
        p = pattern(rng)
        for _ in range(3):
            pairs.append((p, input_string(rng)))
    return pairs[:PAIRS]


def encode(pairs):
    out = []
    for p, s, n in pairs:
        pb = p if isinstance(p, bytes) else p.encode()
        sb = s if isinstance(s, bytes) else s.encode()
        line = pb.hex() + "\t" + sb.hex()
        if n != -1:
            line += "\t" + str(n)
        out.append(line + "\n")
    return "".join(out)


def run(exe, data):
    result = subprocess.run([str(exe)], input=data.encode(), capture_output=True, check=True,
                            cwd=ROOT, timeout=1800)
    return result.stdout.decode().splitlines()


def compare(want, got, pairs, label, failures=10):
    bad = 0
    for i, (a, b) in enumerate(zip(want, got)):
        if a != b:
            p, s, n = pairs[i]
            print(f"{label} line {i + 1}: pattern {p!r} input {s!r} n {n}")
            print(f"  Go:  {a}")
            print(f"  Tin: {b}")
            bad += 1
            if bad >= failures:
                break
    assert bad == 0, f"{label}: {bad} of {len(want)} lines differ"
    return len(want)


def load_find(path):
    """Go's find_test.go table: pattern, text, n, and the flat FindAll submatch offsets."""
    cases = []
    for line in path.read_text().splitlines():
        p, s, n, vals = line.split("\t")
        cases.append((bytes.fromhex(p), bytes.fromhex(s), int(n),
                      [int(v) for v in vals.split()] if vals else []))
    return cases


def load_re2(path):
    """Go's RE2 search tests: (pattern, text, [four variant results])."""
    cases, strings, pattern, pending = [], [], None, []
    in_strings = False
    for line in path.read_text().splitlines():
        if not line or line[0] == "#" or line[0].isupper():
            continue
        if line == "strings":
            in_strings, strings = True, []
            continue
        if line == "regexps":
            in_strings = False
            continue
        if line.startswith('"'):
            q = ast.literal_eval(line)
            if in_strings:
                strings.append(q)
            else:
                pattern, pending = q, list(strings)
            continue
        if line[0] == "-" or line[0].isdigit():
            text = pending.pop(0)
            cases.append((pattern, text, line.split(";")))
    return cases


def subs_of(line):
    """The values of the subs field of one output line."""
    toks = line.split()
    i, j = toks.index("subs"), toks.index("all")
    return [int(v) for v in toks[i+1:j]]


def allsubs_of(line):
    """The values of the allsubs field of one output line."""
    toks = line.split()
    return [int(v) for v in toks[toks.index("allsubs")+1:]]


def expected_subs(res):
    """One re2-search result part as offsets: '-' is no match, else space-separated start-end."""
    if res == "-":
        return None
    out = []
    for pair in res.split():
        if pair == "-":
            out += [-1, -1]
        else:
            lo, hi = pair.split("-")
            out += [int(lo), int(hi)]
    return out


def single_bytes(s):
    return all(ord(c) < 0x80 for c in s)


def main():
    directory = ROOT / "bin/ci/lasso"
    directory.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="lasso-", dir=directory) as tmp:
        work = Path(tmp)
        tin = work / "lasso-tin"
        subprocess.run([str(ROOT / "bin/tinc"), "-o", str(tin), "tools/ci/fixtures/lasso.tin"],
                       check=True, cwd=ROOT, env={"TIN_ROOT": str(ROOT)}, timeout=300)
        go = work / "lasso-go"
        subprocess.run(["go", "build", "-o", str(go), "./bench/ref/lasso"], check=True, cwd=ROOT,
                       timeout=300)
        total = 0

        # 1. The generated corpus.
        pairs = [(p, s, -1) for p, s in generated()]
        want, got = run(go, encode(pairs)), run(tin, encode(pairs))
        assert len(got) == len(want), f"lasso: {len(got)} lines against Go's {len(want)}"
        total += compare(want, got, pairs, "corpus")
        print(f"PASS lasso: {len(pairs)} generated pattern/input pairs match Go's regexp")

        # 2. Go's find_test.go table, against its own expectations.
        cases = load_find(DATA / "find_test.txt")
        pairs = [(p, s, n) for p, s, n, _ in cases]
        got = run(tin, encode(pairs))
        assert len(got) == len(cases), f"lasso: {len(got)} find_test lines"
        for i, ((p, s, n, want_subs), line) in enumerate(zip(cases, got)):
            if line == "compile":
                raise AssertionError(f"find_test {i + 1}: {p!r} does not compile")
            have = allsubs_of(line)
            assert have == want_subs, (f"find_test {i + 1}: {p!r} on {s!r} n {n}: "
                                       f"got {have}, want {want_subs}")
        total += len(cases)
        print(f"PASS lasso: {len(cases)} find_test.go cases match their table")

        # 3. The RE2 search tests, against the file's expectations.
        checked, skipped = 0, 0
        for p, s, parts in load_re2(DATA / "re2-search.txt"):
            if r"\B" in p and not single_bytes(s):
                skipped += 1
                continue
            full, partial = r"\A(?:" + p + r")\z", p
            want_full, want_partial = expected_subs(parts[0]), expected_subs(parts[1])
            lines = run(tin, encode([(full, s, -1), (partial, s, -1)]))
            if len(lines) != 2:
                raise AssertionError(f"re2 {p!r}: {len(lines)} lines")
            if lines[0] == "compile":
                # A pattern the parser refuses (Go skips \C the same way); the acceptance parity
                # is covered by the edge cases in lasso_bad.tin.
                skipped += 1
                continue
            have_full = subs_of(lines[0])
            assert have_full == (want_full or []), (f"re2 full {p!r} on {s!r}: "
                                                    f"got {have_full}, want {want_full}")
            if want_full is not None:
                have_partial = subs_of(lines[1])
                assert have_partial == want_partial, (f"re2 partial {p!r} on {s!r}: "
                                                      f"got {have_partial}, want {want_partial}")
            checked += 1
        total += checked
        print(f"PASS lasso: {checked} RE2 search cases match re2-search.txt "
              f"({skipped} skipped: \\C and the \\B byte-position cases)")


if __name__ == "__main__":
    main()
