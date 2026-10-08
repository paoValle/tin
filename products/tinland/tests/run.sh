#!/bin/sh
# Tinland's tests. The UI framework's layout (tests/programs/ui_layout.tin) is portable and runs everywhere; on macOS the
# editor driven by a script, without a window (tests/scripts/editor.script), must print what tests/golden/editor.out holds and
# write a PNG of its pixels. Usage: run.sh [COMPILER]
set -eu
cd "$(dirname "$0")/../../.." || exit 1
compiler=${1:-bin/tinc}
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
for name in ui_layout project; do
	"$compiler" -o "$tmp/$name" "products/tinland/tests/programs/$name.tin"
	"$tmp/$name" > "$tmp/$name.out"
	cmp "$tmp/$name.out" "products/tinland/tests/golden/$name.out" || { echo "FAIL tinland $name"; exit 1; }
	echo "PASS tinland $name"
done
if [ "$(uname -s)" != Darwin ]; then
	echo "SKIP tinland editor tests: not macOS"
	exit 0
fi
"$compiler" -o "$tmp/tinland" products/tinland/main.tin
script=$(sed "s|@PNG@|$tmp/editor.png|" products/tinland/tests/scripts/editor.script)
case $compiler in /*) tinc=$compiler ;; *) tinc=$PWD/$compiler ;; esac
TINLAND_TINC="$tinc" TINLAND_SCRIPT="$script" "$tmp/tinland" > "$tmp/editor.out"
cmp "$tmp/editor.out" products/tinland/tests/golden/editor.out || { echo "FAIL darwin editor"; exit 1; }
[ "$(head -c 4 "$tmp/editor.png" | od -An -c | tr -d ' ')" = '211PNG' ] || { echo "FAIL darwin editor snapshot"; exit 1; }
echo "PASS darwin editor"
