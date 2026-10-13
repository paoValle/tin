#!/bin/sh
# Sets up a workspace checkout: clones usetin/docs next to this checkout and links it into the tree as
# toolchain/docs and design, so the checks that read the documentation (docs_check, diagnostics_check,
# the libc inventory guard, gendoc --check) run as before. Usage: tools/dev/setup.sh [DOCS_DIR]
# (DOCS_DIR defaults to ../docs).
set -eu
cd "$(dirname "$0")/../.." || exit 1
docs=${1:-../docs}
if [ ! -d "$docs/.git" ]; then
	git clone -q git@github.com:usetin/docs.git "$docs"
fi
docs=$(cd "$docs" && pwd)
for p in toolchain/docs design; do
	if [ -d "$p" ] && [ ! -L "$p" ]; then
		echo "setup: $p is a real directory; this tree is from before the repositories were split (remove it and run again)" >&2
		exit 1
	fi
	rm -f "$p"
done
ln -s "$docs" toolchain/docs
ln -s "$docs/design" design
echo "setup: linked $docs as toolchain/docs and design"
