#!/bin/sh
# Regenerates products/tinland/icon/Tinland.icns from tools/dev/tinland_icon.tin (macOS with a GPU and iconutil).
set -eu
cd "$(dirname "$0")/../.." || exit 1
make -s bin/tinc
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
mkdir "$tmp/Tinland.iconset"
bin/tinc -o "$tmp/icon" tools/dev/tinland_icon.tin
"$tmp/icon" "$tmp/Tinland.iconset"
iconutil -c icns "$tmp/Tinland.iconset" -o products/tinland/icon/Tinland.icns
echo "wrote products/tinland/icon/Tinland.icns"
