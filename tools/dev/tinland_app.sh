#!/bin/sh
# Builds Tinland.app (macOS): the editor from products/tinland/main.tin in an application bundle, so it has its own Dock icon,
# name in the menu bar, and opens from Finder. Usage: tools/dev/tinland_app.sh [OUTPUT_DIR]   (default bin/)
# Open a folder from the command line with: open -a bin/Tinland.app --args /path/to/folder
set -eu
cd "$(dirname "$0")/../.." || exit 1
[ "$(uname -s)" = Darwin ] || { echo "Tinland runs on macOS" >&2; exit 1; }
out=${1:-bin}
app="$out/Tinland.app"
make -s bin/tinc
rm -rf "$app"
mkdir -p "$app/Contents/MacOS" "$app/Contents/Resources"
bin/tinc -o "$app/Contents/MacOS/Tinland" products/tinland/main.tin
cat > "$app/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleName</key><string>Tinland</string>
	<key>CFBundleDisplayName</key><string>Tinland</string>
	<key>CFBundleIdentifier</key><string>org.tin.tinland</string>
	<key>CFBundleExecutable</key><string>Tinland</string>
	<key>CFBundlePackageType</key><string>APPL</string>
	<key>CFBundleVersion</key><string>1</string>
	<key>CFBundleShortVersionString</key><string>0.1</string>
	<key>LSMinimumSystemVersion</key><string>12.0</string>
	<key>NSHighResolutionCapable</key><true/>
	<key>NSPrincipalClass</key><string>NSApplication</string>
</dict>
</plist>
PLIST
echo "built $app"
