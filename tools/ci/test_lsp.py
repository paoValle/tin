"""tin lsp: the language server answers over standard input and output (diagnostics, outline, definition, hover,
completion), with the editor's unsaved text as what is checked."""
import json
import os
from pathlib import Path
import platform
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def tinc():
    """bin/tinc, built from the seed first when it is not there yet (the unit tests run before the bootstrap step)."""
    path = ROOT / 'bin/tinc'
    if not path.exists():
        subprocess.run(['make', '-s', '-C', str(ROOT), 'bin/tinc'], check=True, timeout=600)
    return path

PROGRAM = '''package main

import "say"
import "twine"

// Point is a place.
type Point struct {
	X i64
	Y i64
}

// Dist is the distance to the origin, squared.
fn (p Point) Dist() i64 {
	return p.X * p.X + p.Y * p.Y
}

fn helper(a i64) i64 {
	return a + 1
}

type Other struct {
	Z i64
}

fn (o Other) Ping() i64 {
	return o.Z
}

fn main() {
	let p = Point{X: 1, Y: 2}
	let parts = twine.Split("a,b", ",")
	let o = Other{Z: 3}
	say.Line(p.Dist(), o.Ping(), helper(1), len(parts))
}
'''


class Client:
    def __init__(self, exe, cwd):
        env = dict(os.environ, TIN_ROOT=str(ROOT), TINLSP_TINC=str(tinc()))
        self.p = subprocess.Popen([str(exe)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env, cwd=cwd)
        self.next = 1

    def send(self, message):
        body = json.dumps(message).encode()
        self.p.stdin.write(b'Content-Length: %d\r\n\r\n' % len(body) + body)
        self.p.stdin.flush()

    def receive(self):
        length = None
        while True:
            line = self.p.stdout.readline()
            if line in (b'\r\n', b''):
                break
            if line.lower().startswith(b'content-length:'):
                length = int(line.split(b':')[1])
        return json.loads(self.p.stdout.read(length))

    def request(self, method, params):
        self.next += 1
        self.send({'jsonrpc': '2.0', 'id': self.next, 'method': method, 'params': params})
        while True:
            message = self.receive()
            if message.get('id') == self.next:
                return message

    def notify(self, method, params):
        self.send({'jsonrpc': '2.0', 'method': method, 'params': params})

    def open(self, path, text):
        self.notify('textDocument/didOpen', {'textDocument': {'uri': 'file://' + str(path), 'languageId': 'tin', 'version': 1, 'text': text}})
        return self.diagnostics()

    def change(self, path, text):
        self.notify('textDocument/didChange', {'textDocument': {'uri': 'file://' + str(path), 'version': 2},
                                               'contentChanges': [{'text': text}]})
        return self.diagnostics()

    def diagnostics(self):
        while True:
            message = self.receive()
            if message.get('method') == 'textDocument/publishDiagnostics':
                return message['params']['diagnostics']


class LanguageServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.work = tempfile.TemporaryDirectory()
        cls.exe = Path(cls.work.name) / 'tinlsp'
        os_name = 'darwin' if platform.system() == 'Darwin' else 'linux'
        subprocess.run([str(tinc()), '-o', str(cls.exe), str(ROOT / 'tools/lsp/main.tin'),
                        str(ROOT / f'tools/lsp/exec_{os_name}.tin')], check=True, timeout=300, env=dict(os.environ, TIN_ROOT=str(ROOT)))

    @classmethod
    def tearDownClass(cls):
        cls.work.cleanup()

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / 'prog.tin'
        self.path.write_text(PROGRAM)
        self.client = Client(self.exe, self.dir.name)
        reply = self.client.request('initialize', {'processId': None, 'rootUri': None, 'capabilities': {}})
        self.caps = reply['result']['capabilities']
        self.uri = 'file://' + str(self.path)

    def tearDown(self):
        self.client.request('shutdown', None)
        self.client.notify('exit', None)
        self.assertEqual(self.client.p.wait(timeout=30), 0)
        self.client.p.stdin.close()
        self.client.p.stdout.close()
        self.dir.cleanup()

    def at(self, text, needle, nth=0):
        """The LSP position of the start of needle in text (the nth time)."""
        index = -1
        for _ in range(nth + 1):
            index = text.index(needle, index + 1)
        line = text.count('\n', 0, index)
        column = len(text[:index].split('\n')[-1].encode('utf-16-le')) // 2
        return {'line': line, 'character': column}

    def test_capabilities(self):
        for name in ('definitionProvider', 'hoverProvider', 'documentSymbolProvider', 'completionProvider', 'textDocumentSync'):
            self.assertTrue(self.caps[name], name)

    def test_diagnostics_follow_the_unsaved_text(self):
        self.assertEqual(self.client.open(self.path, PROGRAM), [])
        broken = PROGRAM.replace('return a + 1', 'return a + missing')
        diagnostics = self.client.change(self.path, broken)
        self.assertEqual(len(diagnostics), 1)
        d = diagnostics[0]
        self.assertEqual((d['code'], d['source'], d['severity']), ('E103', 'tinc', 1))
        start = self.at(broken, 'missing')
        self.assertEqual(d['range'], {'start': start, 'end': {'line': start['line'], 'character': start['character'] + len('missing')}})
        self.assertEqual(self.client.change(self.path, PROGRAM), [])
        self.assertEqual(self.path.read_text(), PROGRAM)

    def test_columns_are_utf16(self):
        text = PROGRAM.replace('return a + 1', 'say.Line("é日本 🙂", missing)\n\treturn a + 1')
        diagnostics = self.client.open(self.path, text)
        self.assertEqual(len(diagnostics), 1)
        self.assertEqual(diagnostics[0]['range']['start'], self.at(text, 'missing'))

    def test_outline_definition_and_hover(self):
        self.client.open(self.path, PROGRAM)
        td = {'uri': self.uri}
        outline = self.client.request('textDocument/documentSymbol', {'textDocument': td})['result']
        self.assertEqual(sorted((s['name'], s['kind']) for s in outline),
                         [('Dist', 6), ('Other', 23), ('Ping', 6), ('Point', 23), ('helper', 12), ('main', 12)])
        pos = self.at(PROGRAM, 'helper(1)')
        found = self.client.request('textDocument/definition', {'textDocument': td, 'position': pos})['result']
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['uri'], self.uri)
        self.assertEqual(found[0]['range']['start'], self.at(PROGRAM, 'helper', 0))
        hover = self.client.request('textDocument/hover', {'textDocument': td, 'position': pos})['result']
        self.assertIn('fn helper(a i64) i64', hover['contents']['value'])
        method = self.at(PROGRAM, 'Dist()', 1)
        hover = self.client.request('textDocument/hover', {'textDocument': td, 'position': method})['result']
        self.assertIn('Dist is the distance to the origin, squared.', hover['contents']['value'])
        # a name in another package: the definition is in that package's file
        pos = self.at(PROGRAM, 'Split')
        found = self.client.request('textDocument/definition', {'textDocument': td, 'position': pos})['result']
        self.assertTrue(any(f['uri'].endswith('/twine/twine.tin') for f in found), found)
        # nothing at a keyword or a blank
        self.assertEqual(self.client.request('textDocument/definition', {'textDocument': td, 'position': {'line': 0, 'character': 1}})['result'], [])

    def test_completion(self):
        self.client.open(self.path, PROGRAM)
        td = {'uri': self.uri}
        pos = self.at(PROGRAM, 'Split')
        items = self.client.request('textDocument/completion', {'textDocument': td, 'position': pos})['result']['items']
        labels = {i['label'] for i in items}
        self.assertIn('Split', labels)
        self.assertIn('Join', labels)
        self.assertNotIn('main', labels)
        items = self.client.request('textDocument/completion', {'textDocument': td, 'position': self.at(PROGRAM, 'say.Line')})['result']['items']
        labels = {i['label'] for i in items}
        self.assertTrue({'helper', 'Point', 'main', 'twine', 'say', 'return'} <= labels, labels)
        # after a local's dot: the members of its type, and only those
        pos = self.at(PROGRAM, 'Dist()', 1)
        items = self.client.request('textDocument/completion', {'textDocument': td, 'position': pos})['result']['items']
        labels = {i['label'] for i in items}
        self.assertEqual(labels, {'Dist', 'X', 'Y'})
        pos = self.at(PROGRAM, 'Ping()', 1)
        items = self.client.request('textDocument/completion', {'textDocument': td, 'position': pos})['result']['items']
        self.assertEqual({i['label'] for i in items}, {'Ping', 'Z'})
        # plain completion offers the locals of the function
        items = self.client.request('textDocument/completion', {'textDocument': td, 'position': self.at(PROGRAM, 'say.Line')})['result']['items']
        details = {i['label']: i['detail'] for i in items}
        self.assertEqual((details['p'], details['o'], details['parts']), ('Point', 'Other', '[]str'))
        # go to the declaration of a local
        found = self.client.request('textDocument/definition', {'textDocument': td, 'position': self.at(PROGRAM, 'p.Dist')})['result']
        self.assertEqual(found[0]['range']['start'], self.at(PROGRAM, 'p = Point'))

    def test_workspace_symbols_and_unknown_requests(self):
        self.client.open(self.path, PROGRAM)
        found = self.client.request('workspace/symbol', {'query': 'dist'})['result']
        self.assertEqual([s['name'] for s in found], ['Dist'])
        reply = self.client.request('textDocument/nothing', {})
        self.assertEqual(reply['error']['code'], -32601)


if __name__ == '__main__':
    unittest.main()
