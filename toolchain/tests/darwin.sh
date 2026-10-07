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
for name in display; do
	"$compiler" -o "$tmp/$name" "toolchain/tests/darwin/$name.tin"
	"$tmp/$name" > "$tmp/$name.out"
	cmp "$tmp/$name.out" "toolchain/tests/darwin/$name.out" || { echo "FAIL darwin $name"; exit 1; }
	echo "PASS darwin $name"
done
