"""lldb summaries for Tin values in a program built with tinc -g (toolchain/docs/TOOLING.md 8.2).

Load them with `command script import tools/dev/tin_lldb.py` (or put that line in ~/.lldbinit). A `str` is a pointer to
[length][bytes] and a slice a pointer to [len, cap, data, region]; the debug information describes both as structures, and
these summaries show the text and the first elements instead of the raw pointers:

    (str *) label = "pt"
    ([]i64 *) xs = len=3 cap=3 [4, 5, 6]
"""
import lldb

MAX_BYTES = 200
MAX_ELEMENTS = 8


def str_summary(valobj, internal_dict):
    address = valobj.GetValueAsUnsigned()
    if address == 0:
        return 'nil'
    target = valobj.GetTarget().GetProcess()
    error = lldb.SBError()
    length = target.ReadUnsignedFromMemory(address, 8, error)
    if error.Fail() or length > 1 << 30:
        return '<unreadable>'
    shown = min(length, MAX_BYTES)
    data = target.ReadMemory(address + 8, shown, error) if shown else b''
    if error.Fail():
        return '<unreadable>'
    text = data.decode('utf-8', errors='replace')
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"' + ('...' if length > shown else '')


def slice_summary(valobj, internal_dict):
    if valobj.GetValueAsUnsigned() == 0:
        return 'nil'
    header = valobj.Dereference()
    length = header.GetChildMemberWithName('len').GetValueAsSigned()
    cap = header.GetChildMemberWithName('cap').GetValueAsSigned()
    data = header.GetChildMemberWithName('data')
    out = 'len=%d cap=%d' % (length, cap)
    elem = data.GetType().GetPointeeType()
    size = elem.GetByteSize()
    address = data.GetValueAsUnsigned()
    if length <= 0 or size == 0 or address == 0:
        return out
    items = []
    for i in range(min(length, MAX_ELEMENTS)):
        value = data.CreateValueFromAddress('e%d' % i, address + i * size, elem)
        items.append(value.GetSummary() or value.GetValue() or '?')
    return out + ' [' + ', '.join(items) + (', ...' if length > MAX_ELEMENTS else '') + ']'


def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('type summary add -F tin_lldb.str_summary "str *"')
    debugger.HandleCommand('type summary add -x -F tin_lldb.slice_summary "^\\[\\].* \\*$"')
