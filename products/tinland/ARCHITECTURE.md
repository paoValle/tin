# Tinland: architecture

Tinland is an editor written entirely in Tin. It is built the way Zed is: a small platform layer, its own GPU-drawn UI
framework, and the editor's features as packages on top of it. This page says what each package is for and what may import
what, so the product can grow (a project panel, search, a terminal, extensions) without turning into one large file.

## The packages

```
products/tinland/
  main.tin        package main: the entry point; reads the command line and starts the app
  app/            the application: the window loop, the menu bar, the application's settings
  workspace/      what a window holds: title bar, docks (the project panel), panes with tabs, the status bar   (planned)
  editor/         the text editor: a buffer, its view, selections, completion, diagnostics, commands
  project/        folders: the file tree, ignore rules, project-wide search                                       (planned)
  ui/             the UI framework: geometry, colors, text, a tree of elements, layout, input, focus, themes      (planned)
  language/       what Tinland knows about Tin: asking tinc for declarations and errors, building, running, formatting
  tests/          scripts, fixtures and golden output for the macOS tests (run.sh)
  vscode/         the VS Code extension (separate, not part of the application)

packages/
  appkit/         the macOS binding: windows, events, menus, panels, the clipboard, Objective-C classes defined from Tin
  metal/          the Metal binding and the GPU canvas the UI framework draws on                                   (planned)
  textedit/       the text buffer engine and the Tin syntax highlighter (no UI, no operating system)
  tinsym/         the compiler's declarations and errors, name resolution and completion (shared with tin lsp)
  tinjson/        a JSON reader and writer
  tinfmt/         the whitespace formatter (shared with tin fmt)
```

Zed's crates and ours: `gpui` is `ui` over `metal` and `appkit`; `editor`, `project`, `workspace`, `language`, `text` are the
packages of the same name (`text` is `textedit`); its `lsp` client is `language` once it speaks the Language Server Protocol
(today it runs tinc directly); `theme` and `ui` components live in `ui`.

## Layers

A package may import only what is below it:

```
main
  app
    workspace
      editor      project
        ui          language
          metal, appkit, textedit, tinsym, tinjson, tinfmt     (packages/, no knowledge of Tinland)
```

- **`packages/`** know nothing of Tinland. `appkit` and `metal` are the only code that touches the operating system; a Linux
  or Windows port is another binding with the same shape plus a backend in `ui`.
- **`ui`** knows nothing of editing: it draws, lays out and routes input. **`editor`** and **`project`** are built from `ui`
  elements and know nothing of each other; **`workspace`** puts them in a window.
- **`language`** has no windows: paths and text in, declarations, errors and output back.
- A feature gets a package of its own when it has its own state and tests (a terminal, a git panel), not a folder inside
  another package.

## Today and next

What is here now is the first editor: it draws on the CPU into a bitmap and polls for events (`editor/render.tin`,
`app/app.tin`). The plan, in the order it is built:

1. **Callbacks and classes** (done): `@callback` lets AppKit call Tin functions, and `appkit.NewClass` defines Objective-C
   classes from Tin, so a view receives its own events instead of the application polling for them.
2. **A GPU canvas** (`metal`): a Metal layer, a pipeline for rectangles and one for glyphs from an atlas that CoreText fills.
3. **The UI framework** (`ui`): elements (boxes with flex layout, text, scroll areas, lists), hit testing, focus, themes.
4. **The editor on the framework**, then **`workspace`** (title bar, project panel, tabs, status bar, panels) and **`project`**
   (open a folder, the file tree, search), replacing the CPU renderer.
5. More: quick open, a terminal panel, git status, settings and keymaps as files.
