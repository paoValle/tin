#!/bin/sh
# Builds Tinland.app (macOS): the editor from products/tinland/main.tin in an application bundle with its icon, so it has its own
# Dock icon and name in the menu bar and opens from Finder (VERSION in the environment sets the version it reports; the VERSION file otherwise). The release workflow zips it (Tinland-VERSION-darwin-arm64.zip). Usage: tools/dev/tinland_app.sh [OUTPUT_DIR]   (default bin/)
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
cp products/tinland/icon/Tinland.icns "$app/Contents/Resources/Tinland.icns"
version=${VERSION:-$(cat VERSION)}
cat > "$app/Contents/Info.plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleName</key><string>Tinland</string>
	<key>CFBundleDisplayName</key><string>Tinland</string>
	<key>CFBundleIdentifier</key><string>org.tin.tinland</string>
	<key>CFBundleExecutable</key><string>Tinland</string>
	<key>CFBundlePackageType</key><string>APPL</string>
	<key>CFBundleIconFile</key><string>Tinland</string>
	<key>CFBundleVersion</key><string>$version</string>
	<key>CFBundleShortVersionString</key><string>$version</string>
	<key>LSMinimumSystemVersion</key><string>12.0</string>
	<key>NSHighResolutionCapable</key><true/>
	<key>NSPrincipalClass</key><string>NSApplication</string>
</dict>
</plist>
PLIST
# an ad-hoc signature (no developer identity): enough for the system to run the bundle as one unit
codesign --force --deep --sign - "$app" >/dev/null 2>&1 || true
echo "built $app"
