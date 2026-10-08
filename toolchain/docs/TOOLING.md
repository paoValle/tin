# Tin tooling: commands, builds, tests, benchmarks

Everything lives in one tree (`~/Desktop/tin`). Nothing outside it is needed to build
Tin: the checked-in seed compiler builds the compiler, which builds everything else. Go
is used only by the HTTP conformance tools, benchmarks and reference programs; Docker only
for Linux testing.

## 1. Installing

For prebuilt archives, the checksum-verifying installer and the multi-architecture
Docker builder, see [DISTRIBUTION.md](DISTRIBUTION.md). The commands below install
from a source checkout.

```sh
make install                    # builds bin/tinc from seed/ and links `tin` into $(PREFIX)/bin
make install PREFIX=~/.local    # a per-user install: no privileges, ~/.local/bin must be on PATH
make && sudo make install       # a system-wide install where $(PREFIX)/bin is root-owned
```

`PREFIX` defaults to `/opt/homebrew` on a Mac with Homebrew there and to `/usr/local`
everywhere else (Linux, a Mac without Homebrew); an explicit `PREFIX` always wins.
`$(PREFIX)/bin` is created if missing. On most Linux systems `/usr/local/bin` is
root-owned, so either install per user or build first as yourself and run only the
install step with `sudo` (so `bin/` stays yours). The link points into this tree:
moving or deleting the tree breaks it.

`tin` is a shell script (`./tin`); `bin/tinc` is the compiler binary.

## 2. The `tin` command

| command | does |
|---|---|
| `tin FILE.tin [ARGS...]` | compile and run (temporary executable, removed after) |
| `tin run A.tin B.tin -- ARGS` | compile several files as one program and run it |
| `tin build FILE.tin... [-o OUT] [--target T] [--strip] [-g]` | write an executable (default name: the first file without `.tin`); `--strip` leaves out a Linux executable's symbol table (§8); `-g` adds DWARF line tables and function names (§8.2) |
| `tin asm FILE.tin...` | print the generated ARM64 assembly (clang syntax) |
| `tin fix -edition 1 FILE.tin...` | rewrite edition-0 (Go-like) files to edition 1 in place (LANGUAGE.md §22) |
| `tin audit secrets [-edition 1] FILE.tin...` | check the program and list every place a `secret` leaves the checker's protection: each `reveal(x)` and each secret passed to a library parameter declared `secret`, as `file:line:col: ...` sorted by position, then a count; exit status 1 (with the errors) when the program does not check |
| `tin test [-bench] [-run REGEX] [-json] [DIR]` | build DIR (default `.`) with its `*_test.tin` files and run every `TestXxx(t mut crucible.T)`, then `BenchmarkXxx(b mut crucible.B)` with `-bench`; exit status 1 when a test fails, 2 for a wrong test signature (see §5.1); `-run REGEX` runs only the tests and benchmarks whose names match (a lasso regular expression, found anywhere in the name), `-json` prints events instead of text (§5.2) |
| `tin replay CAPSULE --against BUILD [--live KIND]... [--save-test NAME --issue N]` | run a recorded request again with every effect served from its capsule, and report the first divergence (see §8.1) |
| `tin fix -edition 1 FILE.tin...` | translate each file to edition 1 in place, and declare `mut` every `let` the program reassigns (E711). A file whose translation does not parse as edition 1, or changes when translated again, is left unchanged with the reason (for example a `const` in a nested block, which has to move by hand); exit status 1 when any file was left unchanged |
| `tin vendor [DIR]` | copy every package `DIR/tin.mod` requires (transitively, from local source directories) into `DIR/vendor/<path>` and write `DIR/tin.lock` with each vendored file's SHA-256 (see §2.1) |
| `tin check [-json] [-overlay FILE=PATH]... FILE.tin...` | lex, parse and check the program and write nothing: exit 0 when it is correct, 1 with the errors (text form, or one JSON object per line with `-json`, §3.1); `-overlay` reads FILE's content from PATH, so an editor checks what is typed, not what is saved |
| `tin caps FILE.tin...` | check the program and print, per package, the capabilities (`net`, `files`, `spawn`, `exec`, `unsafe`) its exported functions can reach |
| `tin suite` | run the compiler's strict test suite (`tools/dev/v2test.sh`) |
| `tin bootstrap` | rebuild the compiler with itself; the binaries must be identical |
| `tin version` | version and compiler checksum |

Targets (`--target`): `darwin-arm64` (default on a Mac), `linux-arm64` (default on
arm64 Linux), `linux-amd64` (supported and tested natively). Cross-compiling needs nothing extra: the
compiler contains every backend and writes Mach-O or ELF itself.

Every program is edition 1: a file without a `package` clause is an error (E001). Old programs are
translated with `tin fix -edition 1`.

### 2.1 Dependencies: `tin.mod`, `tin vendor`, `tin.lock`

A dependency is imported by path (`import "github.com/ana/geo"`) and read only from
`vendor/github.com/ana/geo` next to the program. Builds never fetch anything. The details
are in [PACKAGES.md](PACKAGES.md).

```sh
cat tin.mod
#   module example.com/app
#   require github.com/ana/geo ../geo        local directory: a checkout or a mirror
tin vendor                                   # vendor/github.com/ana/geo/... and tin.lock
tin build main.tin                           # offline; refuses a vendored file whose hash changed
```

A dependency's own `tin.mod` declares its capabilities (`caps net files`). The compiler
rejects a call from a vendored package that can reach anything else (`E804 CAPABILITY`,
at the call, with the path to the entry point). `tin vendor` copies each package's
capabilities into `tin.lock`, so an upgrade that asks for more shows up in review.
`tin caps main.tin` prints what each package can reach.

With a `tin.lock`, every vendored file must have the hash the lock records, and every
other listed file is checked too. A changed byte stops the build before the file is
parsed: `E111 LOCK_MISMATCH` names the file and both hashes. Review the change, then run
`tin vendor` again to accept it.

## 3. The compiler, `tinc`

```text
tinc [-o OUT] [-S] [-edition 1] [-target darwin-arm64|linux-arm64|linux-amd64] FILE.tin...
```

- `-o OUT`: write the executable (default `a.out`). `-S`: print assembly instead.
- `-edition 1`: read the program's files as edition 1 (LANGUAGE.md). Without the flag each
  file is read in the edition it is written in. Edition 0, the Go-like syntax before it, is
  retired (#226): the compiler refuses it (E090) and only `tin fix -edition 1` reads it.
- `-audit-secrets`: check the program and print its secret audit instead of building
  (`tin audit secrets`; LANGUAGE.md §18).
- The standard library is found through `$TIN_ROOT` or, without it, relative to the
  executable (`<root>/bin/tinc` means `<root>/lib`). The `tin` script sets `TIN_ROOT`.
- Strict programs get the package `toolchain/runtime/` (its `*_<os>.tin` and `*_<os>_<arch>.tin`
  files only for the target) automatically; imports are resolved as in LANGUAGE.md §1.
- Errors print as `file:line:col: error E502 TYPE_ARG_COUNT: message` (code and name from
  [ERRORS.md](ERRORS.md)), every error in one run; the exit code is 1. A compiler crash prints a backtrace only under a debugger (see §8).
- `-check`: lex, parse and check the program through every analysis pass, and stop before generating code (`tin check`).
  `-json` prints each error as a JSON object on standard output (§3.1); `-overlay FILE=PATH` (repeatable) reads
  FILE's content from PATH.
- `-symbols`: check the program and print every declaration of every loaded file (the program's, its packages' and the
  runtime's) as JSON lines on standard output instead of building (§3.3). Errors, if any, print as usual on standard
  error and the exit status is 1, but the declarations are printed too.
- `-g`: put a DWARF line table and the functions' names in the executable (§8.2); the code is the same as without it.
- `-caps`: check the program and print the capabilities each package can reach instead of
  building (`tin caps`; PACKAGES.md, "Capabilities").
- `-fix -edition 1 FILE.tin` prints the file translated to edition 1 (`tin fix`, which also
  checks the result before writing it).
- `-hash FILE...` prints `<sha256> FILE` for each file (the `tin.lock` lines `tin vendor`
  writes) and builds nothing.
- `TINC_TRACE=1` prints each function as it is generated (to find which one crashes the
  code generator).

### 3.1 Diagnostics as JSON (protocol version 1)

`tinc -check -json FILE.tin...` prints one JSON object per error, one per line, on standard output (nothing when the
program checks; exit status 1 otherwise). Fields:

| field | meaning |
|---|---|
| `file` | the path as given (`""` for an error with no position, such as E120) |
| `line`, `col` | where it starts, 1-based, the column in bytes; both 0 for an error with no position |
| `endLine`, `endCol` | where it ends (exclusive): the end of the token at the start (an identifier or number, a string or rune literal, a comment's line, otherwise one character) |
| `code`, `name` | `"E502"`, `"TYPE_ARG_COUNT"` ([ERRORS.md](ERRORS.md)) |
| `severity` | `"error"` (reserved for future warnings) |
| `message` | the text of the text form after `code name: ` |
| `fix` | the `Fix:` paragraph of the code's entry in [ERRORS.md](ERRORS.md) (`""` when it has none); `tools/gen/genfixes.tin` makes `toolchain/compiler/fixes.tin` from the page, and `tools/ci/diagnostics_check.py` requires every example to print the page's |

The text form and the JSON form carry the same code, name, position and message; `tools/ci/diagnostics_check.py` checks
this for every example in ERRORS.md. The compiler stops at the first syntax error, so a file that does not parse
reports one error; a file that parses reports every checker error. `tin lsp` publishes the same objects.
### 3.2 Formatting: `tin fmt`

`tin fmt` (the package `packages/tinfmt`, the command `tools/fmt`) rewrites whitespace and nothing else: formatting never
changes a token (`tinc -tokens` of the file is the same before and after, which `tools/ci/test_tinfmt.py` checks over the
tests and the examples) and formatting twice changes nothing. The rules:

- **Indentation** is tabs, one level for each line that has an open bracket (`(`, `[`, `{`), so `f(a, fn() {` indents its
  body once, and a line that starts by closing brackets (`}`, `})`, `} else {`) is indented as the line that opened them. A
  line that continues an expression (the line before ends in a binary operator or `=`, or it starts with `&&`, `||` or `.name`)
  is indented one more level.
- **Trailing whitespace** is removed; `\r\n` becomes `\n`; the file ends with one newline.
- **Blank lines**: at most one in a row, none at the start of the file, after an opening bracket or before a closing one.
- **`//`** is followed by one space (`///` and `////` are left alone) and preceded by one space after code.
- **Commas** are followed by one space and not preceded by one.
- **Operators** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`, `+%=`, `-%=`, `*%=`, `==`, `!=`,
  `<=`, `>=`, `&&`, `||` and `=>` have one space on each side where there was none. Arithmetic operators are left as written.
- **Left as written**: the spaces inside a line (so aligned fields and aligned trailing comments stay aligned), strings, raw
  strings (every line of one, including its indentation), rune literals, the order and line breaks of the code.

The tree is converted directory by directory: `tools/ci/test_fmt_gate.py` fails when `tin fmt -l` lists a file of the
directories it names (the Tinland editor and its packages, `tin lsp`, `tin fmt`, the new tests), and a directory joins
that list when the change that converts it is announced, like #226. Today about one file in eight of the rest differs
(`tin fmt -l toolchain packages` lists them).

## 4. Make targets

| target | does |
|---|---|
| `make` / `make bin/tinc` | build the compiler from the host's seed (`toolchain/seed/tinc-<os>-<arch>`) |
| `make bootstrap` | `bin/tinc` builds `bin/s2/tinc`, which builds `bin/s3/tinc` (with `TIN_ROOT` set to the tree, because the compiler is a strict program that loads `toolchain/runtime`); they must be byte-identical |
| `make seed` | bootstrap, then refresh the host's seed from `bin/s3/tinc` |
| `make test` | the strict suite |
| `make linux-test` | cross-compile every strict test for linux-arm64 and run it in an arm64 container (`tools/dev/linuxtest.sh`) |
| `make linux-bootstrap` | cross-compile a Linux compiler, then in the container it must rebuild itself identically; refreshes `toolchain/seed/tinc-linux-arm64` |
| `make linux-amd64-bootstrap` | the same for x86-64 in `tin-debian-amd64` (emulated on an arm64 Mac); refreshes `toolchain/seed/tinc-linux-amd64` |
| `make bench` | the CPU benchmarks vs Go (`bench/run.py`) |
| `make install` | link `tin` into `$(PREFIX)/bin` (created if needed; see §1 for the default) |
| `make dist` | package the native compiler, library and sources in a versioned archive with a SHA-256 checksum |
| `make print-VAR` | print a Makefile variable (e.g. `make print-SELF`, the compiler's sources) |
| `make clean` | remove `bin/` |

Rule of the tree: before anything is called done, `make bootstrap` reaches the fixed
point and `make test` (plus `make linux-test` when the library or backend changed)
passes.

## 5. Tests

| suite | where | how it checks |
|---|---|---|
| strict tests | `toolchain/tests/v2/*.tin` | `tools/dev/v2test.sh`: compiles and runs each and compares its output with `NAME.out` exactly, line order included (#626; a test whose order may vary has a `NAME.sorted` marker saying why, and only its lines are sorted first); `NAME_bad.tin` must fail to compile with exactly `NAME_bad.err` |
| diagnostic codes | `toolchain/docs/ERRORS.md` | `tools/dev/v2test.sh` runs `tools/ci/diagnostics_check.py`: the compiler's codes, the page and the `.err` files agree, and every example on the page compiles to exactly the output it shows |
| assembly checks | `toolchain/tests/v2/*_asm.tin` + `*_asm.check` | `tools/dev/v2test.sh`: compiles with `-S` and matches the listing against ordered `CHECK:`/`CHECK-NOT:` lines, lit-style; a `[arm64]`/`[amd64]` line selects a section, lines before any section apply to every CPU |
| Linux | same files | `tools/dev/linuxtest.sh`: cross-compiles for linux-arm64, runs in `tin-debian-arm64`, compares with the same `.out` files |
| HTTP conformance | `bench/http/conformance` | 26 edge cases against a running server: `bin/conformance -addr 127.0.0.1:9180 -pid PID` |
| x86-64 encoder | `tools/dev/x64fuzz` | `tools/dev/x64fuzz/run.sh [COUNT] [SEED]`: random instructions vs `x86_64-linux-gnu-objdump` |
| stdlib vs Go | `bench/ref/NAME/main.go` | the same cases written with Go's library; outputs diffed (see design/stdlib_verified.md) |

### 5.1 Testing your own code: `*_test.tin`

<!-- tin-prelude
fn Area(w i64, h i64) i64 {
	return w * h
}

fn clampPos(x i64) i64 {
	return max(x, 0)
}

fn parse(s str) !i64 {
	return len(s)
}
-->
```tin
// geo_test.tin, next to geo.tin (same package; private names are visible)
package geo

import "crucible"

fn TestArea(t mut crucible.T) {
	crucible.Equal(mut t, "2x3", Area(2, 3), 6)   // any comparable type
	t.True("clamp", clampPos(-1) == 0)
	let (n, err) = parse("12")
	t.NoFault("parse", err)
	crucible.Equal(mut t, "parsed", n, 2)
	if t.Failed() {
		t.Log("printed only when the test fails")
	}
}

fn BenchmarkArea(b mut crucible.B) {
	for i in 0..b.N {
		Area(i, 3)
	}
}
```

`tin test ./geo` prints `--- PASS: TestArea` / `--- FAIL: ...` with the failure messages,
then `PASS: N tests` or `FAIL: ...` (exit status 1). `tin test -bench ./geo` also runs each
benchmark, doubling `b.N` until it takes a second, and prints ns/op. `*_test.tin` files are
never part of a normal build or import. Underneath, `tin test` writes a runner calling each
test through `crucible.Run` and compiles the package with `tinc -entry pkg.TinTestMain`.

As in Go, a test is a `TestXxx` (or benchmark `BenchmarkXxx`) in a `*_test.tin` file whose
`Xxx` does not start with a lowercase letter (`Testify` is an ordinary function). It must be
declared on one line as `fn TestXxx(name mut crucible.T) {` (`mut crucible.B` for a
benchmark); any other signature is reported as `FILE:LINE: wrong signature for TestXxx`
with exit status 2, so no test is skipped silently.

Adding a strict test: write `toolchain/tests/v2/NAME.tin` with deterministic output (no times
or addresses), run it, check every line by hand, in order, then save
`bin/t > toolchain/tests/v2/NAME.out`. The suite compares the output exactly, so the order a
program prints in is part of what the test checks (#626). Only a test whose order truly
varies (cores or tasks finishing in any order) sorts: save `bin/t | LC_ALL=C sort` and add
`NAME.sorted` with one line saying why. `v2test.sh` never creates expected files itself.

Adding a compiler error: report it with `err_code(pos, "E5NN NAME")` (or `err_code_at`,
`err_code_quoted`), reusing the code of the rule it enforces or adding one: a new entry in
`toolchain/docs/ERRORS.md`, in code order, with the rule, an example, the exact output and the fix.
Never renumber or reuse a code; when a diagnostic goes away, its entry stays, marked `Retired:`.

Writing to files in tests: use paths under `/tmp/tin-test-*` (they work on macOS and
Linux).

### 5.2 Test events (`tin test -json`, protocol version 1)

`tin test -json` prints one JSON object per line on standard output, as the tests run, so a reader can follow them
incrementally. Fields: `event`, `test` (the function name, `""` for the summary) and, by event:

| `event` | when | more fields |
|---|---|---|
| `run` | a test starts | |
| `output` | for each line the test printed (`say` and the like) and each `t.Log` or failed check | `message` |
| `pass`, `fail` | a test ends | `elapsed_ms` |
| `bench` | a benchmark ends (with `-bench`) | `n`, `ns_per_op` |
| `summary` | at the end | `pass`, `fail` |

Exit statuses are those of the text form (1 when a test failed, 2 for a wrong signature or a bad `-run` pattern).
The lines a test prints are taken from the runtime's 64 KiB output buffer: a test that prints more than that, or
whose output is a terminal, has the rest written directly as plain lines between events, so a reader should skip
lines that do not start with `{`. A failed check's message is an `output` event (`label: got X, want Y`); a failure's
position is not known, so an editor maps a failure to the test function and the label.

## 6. Linux on a Mac (Docker)

Images (built locally, all native arm64 except where noted):

| image | contents | used for |
|---|---|---|
| `tin-debian-arm64` | debian:bookworm-slim (glibc 2.36) | running tests |
| `tin-bench-arm64` | the above + wrk, procps | benchmarks, conformance |
| `tin-debian-amd64` | debian:bookworm-slim amd64 (emulated) | x86-64 correctness |
| `golang:1.27` | Debian 13 + Go + gcc | C probes, Go builds |

Re-create them with:

```sh
docker pull --platform linux/arm64 debian:bookworm-slim && docker tag debian:bookworm-slim tin-debian-arm64
docker pull --platform linux/amd64 debian:bookworm-slim && docker tag debian:bookworm-slim tin-debian-amd64
printf 'FROM tin-debian-arm64\nRUN apt-get update -qq && apt-get install -y -qq wrk procps\n' | docker build -t tin-bench-arm64 -
```

(after pulling both platforms, the bare `debian:bookworm-slim` tag points at the last
one pulled: always use the `tin-*` tags or `--platform`.)

Running something by hand:

```sh
tin build --target linux-arm64 app.tin -o bin/linux/app
docker run --rm -v "$PWD/bin/linux":/w tin-debian-arm64 /w/app
```

Go binaries for the container: `GOOS=linux GOARCH=arm64 go build -o bin/linux/x ./dir`.

## 7. Benchmarks

| script | measures |
|---|---|
| `bench/http/run_wrk.sh CORES THREADS CONNS SECS ROUNDS` | anvil vs fasthttp vs net/http on macOS under wrk: req/s, p99, req per server CPU-second, RSS (medians) |
| `bench/http/run_pipelined.sh "1 2 4"` | the same with 16 pipelined requests per write (wrk Lua script) |
| `bin/linux/bench.sh` (inside `tin-bench-arm64`) | the same comparison on Linux |
| `bench/v2/NAME.tin` + `NAME.go` | CPU benchmarks; build both, time with `/usr/bin/time -l`, outputs must be identical |
| `bench/dispatch/dispatch.tin` | shape dispatch against a hand-written call (Tin only, no Go twin): ns/op of each and their ratio; see PERFORMANCE.md section 5 |
| `bench/dispatch/dyn.tin` | dynamic shape dispatch against a direct method call; reports ns/op and pool bytes, with a paired assembly check in `toolchain/tests/v2/shapes_dyn_asm.tin` |
| `examples/demo.tin` + `examples/demo_go` | the mixed demo (primes, sort, SHA-256, JSON, maps), self-timing |
| `bench/http/hammer` | a Go load generator (wrk-like) with exact latency histograms |
| `bench/router/router.tin` + `bench/router/go` | routing cost with 1, 20 and 200 routes: a lookup (`Match`) and a whole request through the router (`Run`), against chi's `Find` and `ServeHTTP` |
| `bench/http/routes.tin` | `/json` and `/plaintext` behind a router of `ROUTES` routes (port 9180, like `examples/api.tin`), for routing inside a served request |
| `bench/v04/run.py` | `GET /users/{id}` through Redis over MySQL, Tin vs Go + chi under wrk2: max req/s, req per CPU-second, p50/p99/p99.9 at a fixed rate, RSS (needs Redis, MySQL seeded by `bench/v04/seed.py`, and `WRK2`) |

Servers used: `examples/api.tin` (port 9180, `TIN_CORES=n`), `bench/http/fast` (fasthttp,
9182), `bench/http/gonet` (net/http, 9181), with `GOMAXPROCS=n`. Results and analysis:
[PERFORMANCE.md](PERFORMANCE.md).

## 8. Debugging

| tool | use |
|---|---|
| `tin asm file.tin` / `tinc -S` | read the generated code |
| `tools/dev/try.sh COMPILER FILE.tin` | compile and run; if the compiler crashes, print its backtrace under lldb |
| `tools/dev/crash.sh PROGRAM ARGS` | run under lldb and print a Tin backtrace on a crash (`tools/dev/tinbt.py` walks frame pointers) |
| `TINC_TRACE=1 tinc ...` | which function the backend was generating |
| panics | print the message and a backtrace (inlined frames are missing) |
| `lldb bin/t` | symbols are present (function names as `pkg.Name`, `Type.Method`) |

A compiler change that breaks the compiler itself: build with the previous good
compiler (`bin/s3/tinc` or the seed), never overwrite the seed until `make bootstrap`
passes.

**Profiling a Linux service** (#351). A Linux executable carries section headers and a
symbol table (`.symtab`) naming every function as `pkg.Name`, `pkg.Type.Method` or a
generated name (`keep$N`), with its size. The table is not loaded; it costs about 4% of
the file (33 KiB of the compiler's 812 KiB) and `tin build --strip` (`tinc -strip`) leaves
it out. `nm`, `addr2line -f`, `perf` and `gdb` read it:

```sh
perf record -g -p "$(pidof api)" -- sleep 10    # sample the running server for ten seconds
perf report --sort symbol                         # time per Tin function
```

Frames are walked with the frame pointers Tin always keeps (`perf record -g`, or
`--call-graph fp`). Source lines come from DWARF, which `-g` adds (§8.2): `perf annotate` and
`gdb list` then show the source.

### 8.2 Source lines for a debugger and a profiler: `-g`

`tin build -g` (`tinc -g`) adds three DWARF 4 sections to the executable, `.debug_line`, `.debug_info` and `.debug_abbrev`,
on macOS (a `__DWARF` segment with `__debug_line`, `__debug_info` and `__debug_abbrev`), Linux arm64 and Linux amd64. The
line table has a row for each statement (file, line and column, 1-based, as in the compiler's messages); `.debug_info` has
one compilation unit with a subprogram for each function, named as in the symbol table (`pkg.Name`), with its address range
and the line it is declared on. The addresses are the final ones, so there is nothing to relocate and a position-independent
macOS executable is slid by the debugger. The code is the same as without `-g` except that a statement boundary stops the
backend from fusing across it, so an optimized sequence can differ in a few instructions; `-S` ignores the flag.

```sh
tin build -g prog.tin -o prog
lldb prog -o "breakpoint set -f prog.tin -l 12" -o run -o bt     # stops at the line, backtrace with names and lines
perf annotate -s main.main                                       # Linux: the source beside the machine code
```

The unit also lists the program's own globals: a per-core global is a word of the core's context block, addressed from the
context register (`x28`, `r15`), a shared one has its address (`target variable` in lldb, `info variables` in gdb).
Each subprogram lists its parameters and local variables with their types and where they live: a register (a
callee-saved register, or a float register) or a slot of the frame, addressed from the frame pointer (`x29`, `rbp`). The
types follow the layouts of RUNTIME.md section 1: integers, `bool` and floats are base types; a `str` is a pointer to
`{len, data}`; a slice a pointer to `{len, cap, data, region}`; a struct a pointer to its fields with their offsets (a value
struct is the structure itself); anything else (a map, a function, an enum, an optional number) is its word, shown as a
number. A debugger shows them as it does a C program's:

```text
(lldb) frame variable
(Point *) p = 0x000000016fdfe3d0
([]i64 *) xs = 0x0000000104cd0010
(long) a = 40
(lldb) p *p
(Point) { X = 10, Y = 20, name = 0x000000010000e338 }
(lldb) p label->len
(long) 5
```

Limits: a variable's place is the one the backend gave it for the whole function, and a register or slot shared by
variables whose lifetimes do not overlap shows the other's value outside its own; a variable captured by a closure (it lives in
a heap cell), a `dyn` value, a `?T` over a number and a value struct global have no place yet; there is no unwinding information (frame pointers
are followed), no lexical blocks and no inlined calls. `lldb` shows a `str` or a slice as a pointer to its structure
(`p label->len`); `command script import tools/dev/tin_lldb.py` (or that line in `~/.lldbinit`) makes it show the text and the
first elements: `label = "pt"`, `xs = len=3 cap=3 [4, 5, 6]`. The language of the unit is C, which is what debuggers need to print values.

`tools/ci/test_dwarf.py` reads the sections back for all three targets without a debugger.

### 8.1 Replaying a recorded request: `tin replay`

A server records a request's effects in a capsule when it runs with `TIN_REPLAY_DIR` and
`TIN_REPLAY_KEY` set (the switches are listed in `design/interface_replay.md` §1). `tin replay` runs that request again:

```sh
TIN_REPLAY_KEY=<64 hex digits> tin replay spool/00001700000000000000-000-1.tcap --against server.tin
```

- `--against BUILD` is the program to run: a binary, or a `FILE.tin` that `tin` builds
  first. It can be a later build than the one that recorded the capsule.
- Run it with the configuration the server was recording under (the same environment
  variables, `TIN_REPLAY_SECRET_HEADERS` included): effect keys hold what the program sent,
  such as a service's URL, so another address is a divergence. `examples/checkout.tin` is a
  worked example: record a failed checkout against Redis and a payment service, then replay it
  with neither running.
- BUILD runs with `TIN_REPLAY_CAPSULE` set. Its `anvil.Serve` (or `Router.Serve`) does not
  listen. It opens the capsule, checks the tag under `TIN_REPLAY_KEY`, and refuses a schema or
  effect kind the build does not list (`replay.Kinds`). Then it sends the recorded request once
  through the handler or router on one core. Every effect that goes through the replay hook
  gets its recorded result or fault, and none is performed. The clients (clock, randomness,
  HTTP, Redis, SQL, files) join the hook in #241's recording slices.
- The request's peer is the recorded one: `q.RemoteAddr()` and `q.ClientIP()` answer as they
  did when it was recorded (`ClientIP` with this build's `anvil.TrustedProxies`). A capsule of
  schema 1 has no peer, and both answer "".
- Replay stops at the first **divergence**: an effect whose kind or key differs from the next
  recorded one (a different call, or a different order), or an effect after the last one. From
  then on every effect of the request fails with the divergence; replay never falls through to
  a live call.
- `--live KIND` (repeatable, a kind without `@version`, such as `wire.http` or `redis`) makes
  that kind's calls for real. They are still compared with the recording, which they consume.
- The report goes to standard output, followed by the response body:

  ```text
  replay: status 500 (recorded 500)
  replay: divergence at effect 0: got wire.http@1 "POST ...", recorded redis@1 "GET cart:7"
  replay: 2 recorded effects not served
  charge failed: ...
  ```

  The second line appears only after a divergence, and the third only if some recorded effects
  were not used.
- Exit status: 0 when nothing diverged and every recorded effect was used; 3 when the replay
  diverged or left effects; 4 when the capsule cannot be read (wrong key or damaged, unsupported
  schema or kind, missing `TIN_REPLAY_KEY`); 2 for a usage error.
- `--save-test NAME --issue N` (BUILD must be a `FILE.tin`, without `--live`) runs the replay. If
  it exits 0, it turns the capsule into a regression case: `toolchain/tests/regressions/NAME.tin` (a copy
  of `FILE.tin`), `toolchain/tests/regressions/NAME.tcap` (the capsule sealed again under a public test
  key), and an entry in `cases.json` (`"replay": {"capsule", "key"}`; the expected output is this
  replay's report and body). `tools/ci/regressions.py` runs the program with the replay switches
  and checks the exit status and output, so CI replays the request on every change. Fix the bug
  first, then save the replay against the fixed build: the case then fails if the old behaviour
  comes back. The saved capsule can be read by anyone. Secret headers are already handles, but
  check the request and the recorded results before you commit them.
- Only the request is replayed. Code that runs before `Serve` (`main`, eager initializers,
  `use` resources, `on app.start`) runs as usual, live. A BUILD that never calls `Serve`
  ignores the capsule.

## 9. Repository layout

```text
tin                 the tin command (shell script)
Makefile            builds, bootstraps, tests
toolchain/compiler/           the compiler (COMPILER.md)
toolchain/runtime/            the runtime (RUNTIME.md)
toolchain/std/<package>/      each standard-library package, one directory each (toolchain/std/README.md)
packages/<package>/           servers, clients and protocols (anvil, wire, tls, redis, mysql, postgres, kafka, websocket, ...)
toolchain/tests/v2/           strict tests and expected outputs
toolchain/seed/               tinc-darwin-arm64, tinc-linux-arm64, tinc-linux-amd64: the compilers that start a build
examples/           api.tin (HTTP server), tasks.tin, redis.tin, mysql.tin, websocket.tin, demo.tin, demo_go/
bench/              v2/ CPU benchmarks, http/ HTTP benchmarks and tools, v04/ the service benchmark, ref/ Go references
tools/              ci/ (the CI checks), dev/ (v2test.sh, dist.py, debugging helpers, x64fuzz/), gen/ (gendoc.py, gencoverage.tin, table generators)
toolchain/docs/               this documentation
products/           programs built with Tin (tinland/: editor tooling)
design/             design decisions, interfaces, verification, roadmap
bin/                build output (ignored)
```

## 10. Version control

The tree is ready to become a git repository: `.gitignore` excludes `bin/` and scratch
output, every generated file can be regenerated (`make`, `tools/gen/gendoc.py`,
`tools/gen/gencoverage.tin`), seeds are
plain files, and no script depends on a machine-specific path.

```sh
git init && git add -A && git commit -m "Tin v0.3"
```

Suggested workflow after that: one branch per milestone; a branch merges only when
`make bootstrap`, `make test` and `make linux-test` pass; seeds change only in commits
where the bootstrap passed, together with the compiler change that needed them.

## 11. Regenerating the docs

`python3 tools/gen/gendoc.py` rewrites `toolchain/docs/STDLIB.md` from the comments in `toolchain/std/` and `packages/`
(package comment, then one line per exported function, type and constant). Write a
one-line comment above every exported declaration.

`bin/tinc -o /tmp/gencoverage tools/gen/gencoverage.tin && /tmp/gencoverage` rewrites
`toolchain/docs/COVERAGE.md` from the maintained inventory in `design/coverage.md`.

`python3 tools/dev/legacy2tin.py [--analyze FILE]... FILE...` converts files of the compiler's untyped word
dialect to typed edition 1 written with `i64` words (#228); a one-time migration tool, kept until the
dialect is gone.

`python3 tools/gen/gen_unicode.py` rewrites `toolchain/std/glyph/tables.tin` and `toolchain/runtime/printable.tin` (the Unicode
tables) from Go's `unicode/tables.go`; it needs a Go tree only to read that one file.

## Integer overflow checks

Integer `+ - *`, negation and signed `/` are checked in user code, library packages and
tools (#362, LANGUAGE.md section 6): an overflow panics, in a handler that request's 500.
`+% -% *%` and `@wrap fn` wrap where that is the intent. The runtime (`toolchain/runtime/`) and
the compiler keep the machine's arithmetic. `TINC_OVERFLOW` sets the scope at compile time,
for measurements and audits only: `0` no checks, `1` user code, `2` also library packages
and tools (the default), `3` also the runtime and the compiler (they do not run that way
yet: their intended wraps are not marked). The cost is in
[PERFORMANCE.md](PERFORMANCE.md#integer-overflow-checks-linux).

## CPU cancellation safepoints

**A program that starts cores** (`anvil.Serve`, `hearth.Run`) gets CPU cancellation
safepoints by default (#341): loop back-edges and function entries in its own code poll, so a
handler that never waits cannot hold its core past its deadline or a drain. The standard
library (the library (`toolchain/std/`, `packages/`, `toolchain/runtime/`)) does not poll: its loops are bounded by their input. `tin build --nopolls`
(`tinc -nopolls`, or `TINC_POLLS=0`) turns them off. A program that starts no cores (a CLI,
a benchmark) has no polls unless asked: `tin build --polls` / `tin run --polls`
(`tinc -polls`, `TINC_POLLS=1`) put them in every function outside `toolchain/runtime/`. The cost
is in [PERFORMANCE.md](PERFORMANCE.md#cpu-cancellation-safepoints).

With polls, loop back-edges and function entries observe watchdog cancellation.
A `within` deadline unwinds to its owner, runs defers, and returns its fault. A request
spinning past its deadline gets HTTP 504 and the core serves queued requests. Linux SIGTERM
drain also stops a spinning request at the grace deadline. `@nopoll fn kernel(...) ...`
(edition 1) omits polls in that function; calls into other functions may still poll. Trusted
`toolchain/runtime/` functions never poll. Without polls, waits still observe deadlines and
cancellation; CPU-bound code has no cancellation guarantee, and the monitor thread still ends
the process at a SIGTERM that a held core 0 cannot read (#429).
