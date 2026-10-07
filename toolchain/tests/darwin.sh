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
