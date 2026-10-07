# Tinland

A text editor written entirely in Tin: the editing engine (`packages/textedit`), the window and drawing
(`packages/appkit`, which reaches AppKit and CoreGraphics through `@framework` externs, with no C and no
callbacks: events are polled, and a menu item or the close button appends itself to an `NSMutableArray` the
loop reads), and the application (`app/`). It runs on macOS: per AGENTS.md the editor is a development tool, and Linux is the deployment platform for servers, not for this.

```
bin/tinc -o tinland products/tinland/app/*.tin
./tinland [file...]
```

## Keys

| | |
|---|---|
| Cmd+O, Cmd+S (Shift: Save As), Cmd+N, Cmd+W, Cmd+Q | open, save, new tab, close tab, quit (each asks about unsaved changes) |
| Cmd+1 to 9, Ctrl+Tab | switch tabs |
| Cmd+Z, Cmd+Shift+Z | undo, redo |
| Cmd+X, C, V, A | cut, copy, paste, select all (a cut or copy without a selection takes the line) |
| Cmd+F, Cmd+G (Shift: backwards) | find as you type; Tab switches to the replacement, Return replaces, Cmd+Return replaces all |
| Cmd+L | go to line |
| Cmd+/ | comment or uncomment lines |
| Cmd+D, Cmd+Shift+K, Alt+Up/Down | duplicate, delete, move lines |
| Cmd+[ and Cmd+] , Tab, Shift+Tab | unindent, indent |
| Alt+Left/Right, Cmd+Left/Right/Up/Down | by word, line start/end, document start/end |
| Cmd+Shift+I | format the file with the rules of `tin fmt` |
| Cmd+R | compile and run the file with `tinc` (output in a panel; click a compiler message to jump to it) |

Every key command is also in the menu bar. Errors are underlined while you type: after a pause the compiler checks the text (`tinc -check -json` with the
unsaved buffer as an overlay), the line gets a red mark and its message shows in the status line.

Double click selects a word, triple click a line; the wheel scrolls; Escape closes the output panel.

## Without a window

`TINLAND_SCRIPT` runs a sequence of steps against the editor with no window, printing what a test needs to see
(the script language is at the top of `app/script.tin`); `snap:path.png` draws the editor and writes the pixels.
`toolchain/tests/darwin/editor.script` is the test that runs in CI on macOS.
