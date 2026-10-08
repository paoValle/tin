# Tinland

An editor written entirely in Tin, laid out like Zed: a project panel with the folder tree, tabs, the editor, a status bar
with the panel buttons, a command palette and a project search, drawn on the GPU with Metal. The pieces: the editing engine
(`packages/textedit`), the window (`packages/gpuwin`, Objective-C classes defined from Tin that AppKit calls), the GPU canvas
(`packages/metal`), the macOS binding (`packages/appkit`), and the application (`app/`, `workspace/`, `ui/`, `render/`,
`project/`, `editor/`, `language/`; ARCHITECTURE.md says what each is for). It runs on macOS: per AGENTS.md the editor is a
development tool, and Linux is the deployment platform for servers, not for this.

```
bin/tinc -o tinland products/tinland/main.tin
./tinland [folder or file...]
```

For an application with its own Dock icon and name in the menu bar, `tools/dev/tinland_app.sh` builds `bin/Tinland.app`
(`open -a bin/Tinland.app --args /path/to/folder`).

## Keys

| | |
|---|---|
| Cmd+O, Cmd+Shift+O | open a file, open a folder |
| Cmd+P, Cmd+Shift+P | go to file (fuzzy), command palette |
| Cmd+B, Cmd+J, Ctrl+` | show or hide the project panel, the output panel, the terminal (a shell in the project folder: colors, history, arrows, Cmd+V pastes) |
| Cmd+\ , Cmd+Shift+\ | split the editor to the right, close the split (each pane has its own tabs) |
| Cmd+= , Cmd+- , Cmd+0 | zoom in, out, reset the code font |
| Cmd+Shift+F | search in the project (Return runs it; Aa, ab and .* switch case, whole word and regular expression) |
| Cmd+Alt+N, Cmd+Alt+Shift+N | new file, new folder in the selected folder (the File menu also has Rename and Delete) |
| Cmd+S (Shift: Save As), Cmd+N, Cmd+W, Cmd+Q | save, new tab, close tab, quit (each asks about unsaved changes) |
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
| Cmd+Shift+B or Cmd+click, Cmd+Alt+Left | go to the declaration of the name (in another file too), and back |
| Ctrl+Q | quick info: the signature and documentation of the name |
| Ctrl+Space, or typing a `.` | completion: names after `pkg.`, methods and fields after another dot, the package's names (Up and Down choose, Tab or Return accepts, Escape closes) |
| Cmd+R | compile and run the file with `tinc` (output in a panel; click a compiler message to jump to it) |

Every key command is also in the menu bar. Errors are underlined while you type: after a pause the compiler checks the text (`tinc -check -json` with the
unsaved buffer as an overlay), the line gets a red mark and its message shows in the status line.

Double click selects a word, triple click a line; the wheel scrolls what is under the mouse; the divider beside the project panel drags; the title bar moves the window (a double click zooms it); a right click in the project panel opens a menu (new file, new folder, rename, delete). The folder and the open files come back at the next start when no path is given. Lines git sees as added, changed or removed have a mark in the gutter.

## Without a window

`TINLAND_SCRIPT` runs a sequence of steps against the editor with no window, printing what a test needs to see
(the script language is at the top of `editor/script.tin`); `snap:path.png` draws the text area on the GPU and writes the pixels (nothing is written on a machine without a GPU).
`tests/scripts/editor.script` is the test that runs in CI on macOS (`tests/run.sh`). How the packages fit together is in
[ARCHITECTURE.md](ARCHITECTURE.md).
