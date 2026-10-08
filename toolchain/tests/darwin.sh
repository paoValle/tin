#!/bin/sh
# macOS-only tests: the platform bindings (@framework externs, packages/appkit) run on a Mac; elsewhere
# the file says so and passes, since the binding does not exist there.
set -eu
cd "$(dirname "$0")/../.." || exit 1
compiler=${1:-bin/tinc}
if [ "$(uname -s)" != Darwin ]; then
	echo "SKIP darwin tests: not macOS"
	exit 0
fi
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
for name in display objc number bitmap; do
	"$compiler" -o "$tmp/$name" "toolchain/tests/darwin/$name.tin"
	"$tmp/$name" > "$tmp/$name.out"
	cmp "$tmp/$name.out" "toolchain/tests/darwin/$name.out" || { echo "FAIL darwin $name"; exit 1; }
	echo "PASS darwin $name"
done
# the editor app, driven by its script (no window): the text it ends up with, and a snapshot of its pixels
"$compiler" -o "$tmp/tinland" products/tinland/app/*.tin
script=$(sed "s|@PNG@|$tmp/editor.png|" toolchain/tests/darwin/editor.script)
case $compiler in /*) tinc=$compiler ;; *) tinc=$PWD/$compiler ;; esac
TINLAND_TINC="$tinc" TINLAND_SCRIPT="$script" "$tmp/tinland" > "$tmp/editor.out"
cmp "$tmp/editor.out" toolchain/tests/darwin/editor.out || { echo "FAIL darwin editor"; exit 1; }
[ "$(head -c 4 "$tmp/editor.png" | od -An -c | tr -d ' ')" = '211PNG' ] || { echo "FAIL darwin editor snapshot"; exit 1; }
echo "PASS darwin editor"
# lldb with the Tin summaries: a program built with -g stops at a breakpoint and shows its str and slice parameters (skipped
# where lldb cannot launch a process, such as a machine without debugger permission)
if command -v lldb >/dev/null 2>&1; then
	TIN_ROOT="$PWD" "$compiler" -g -o "$tmp/debug_lines" tools/ci/fixtures/debug_lines.tin
	line=$(grep -n 'say.Line(label' tools/ci/fixtures/debug_lines.tin | cut -d: -f1)
	printf 'command script import tools/dev/tin_lldb.py\nbreakpoint set -f debug_lines.tin -l %s\nrun\nframe variable\nquit\n' "$line" > "$tmp/lldb.cmds"
	lldb -b -s "$tmp/lldb.cmds" "$tmp/debug_lines" > "$tmp/lldb.out" 2>&1 || true
	if grep -q 'stop reason = breakpoint' "$tmp/lldb.out"; then
		grep -q 'len=3 cap=3 \[4, 5, 6\]' "$tmp/lldb.out" && grep -q '"pt"' "$tmp/lldb.out" && grep -q 'scale = 1.5' "$tmp/lldb.out" || { cat "$tmp/lldb.out"; echo "FAIL darwin lldb"; exit 1; }
		echo "PASS darwin lldb"
	else
		echo "SKIP darwin lldb: it did not stop at the breakpoint"
	fi
fi
