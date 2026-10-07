# Design: value layouts (#631, #632)

Status: proposal, 2026-10-07. Decides how structs can be stored inline, and how optional
numbers are represented, before any code (AGENTS.md rule 5). #633 (frame allocation for values
that never escape) builds on section 1; #632 is section 2.

Today every struct, enum and `[N]T` is a reference to its own allocation, and `?T` over a number
or `bool` is a one-field box (#353). Both are simple and safe, and both cost an allocation and a
dependent load per value:

| case | today | inline |
|---|---|---|
| `[]P` of one million `P{x, y i64}` | 50 MB, a pointer chase per element | 16 MB, contiguous |
| `Rect{min, max Point}` | three allocations | one |
| `[]?i64` of one million values | a box per value, 16 MB of boxes plus the slice | 16 MB flat |
| `?i64` result of a lookup | an allocation per call | two registers |
| a global `?i64 = 5` | needs `keep(5)` | a plain value |

## 1. Value structs (#631)

### Decision: a second struct kind, `value struct`

```tin
type Point value struct {
	x f64
	y f64
}
```

`value` is a contextual word before `struct` in a type declaration; it is not reserved. Option 3
of #631, chosen because:

- **Nothing changes for existing code.** A plain `struct` stays a reference with identity
  (`same`), never nil, shared on assignment. Code that relies on that (a `mut` parameter that a
  callee modifies, a struct stored in two places on purpose) keeps working.
- **The cost is in the type**, where design_foundations principle 1 wants it: a reader sees at
  the declaration that `Point` is copied.
- The other options make one struct type mean two things. Option 1 (references into a slice's
  storage, guarded by the region checker) has dangling references as its failure mode, which
  E641's machinery could only partly catch. Option 2 (elements copied out, fields written
  through) makes `ps[i]` and `p` behave differently for the same type.
- It subsumes the roadmap's value-array item (design/roadmap.md, "Value arrays `[N]T`") for the
  cases that item cares about: fixed-size keys and embedded buffers (section 1.6).

### 1.1 Semantics

A `value struct` is a value, as in Go:

- **Assignment, argument passing, returning, storing into a field, element or map entry copy
  it.** `let q = p; q.x = 1` leaves `p` as it was.
- **It has a zero value** when every field has one (numbers, `bool`, `str`, slices, optionals,
  inline arrays and other such value structs): every field zero. `mut p Point` with no
  initializer, `make([]Point, n)` and `[N]Point` are then allowed. A field of reference-struct,
  map, func or `dyn` type has no zero value, so E203 still applies to a value struct holding one.
- **No identity**: `same(a, b)` on value structs is a compile error (it would compare copies).
- **`==` is unchanged**: structs already compare by value, field by field (#352, E237), and a
  value struct follows the same rule, including E237 for a struct holding a slice, map, func,
  `dyn` value or optional.
- **Map keys are unchanged**: a struct made only of keys is a key, hashed and compared by value
  (`f64` by bits), and copied in (LANGUAGE.md, Maps). A value struct is a key under the same
  rule, hashed from its inline bytes, and an inline array of keys (section 1.6) is a key.
- **`mut` parameters and receivers** (E702 today allows only references): a `mut` value struct
  is passed as the address of the caller's storage (a local, a field, an element `ps[i]`) for
  the duration of the call. Every use of the parameter as a value copies it, so the address
  itself can never be stored or returned; the only operations through it are field reads and
  writes and passing it on as `mut`. `ps[i].scale(2)` updates the element in place. A call
  that passes `ps[i]` as `mut` and can also grow `ps` (an argument `mut ps`, or a callee that
  grows it, #627's `al_fn_grows`) is E641, since the growth would move the element out from
  under the address; this is the places model #627 added, applied to one more kind of place.
- **Map entries**: `m[k].x = v` on a map of value structs is a compile error, as in Go (the entry
  is a copy); the fix is `mut p = m[k]; p.x = v; m[k] = p`. Reference-struct maps keep today's
  meaning.
- **Printing, `argo`** work as for reference structs (`{1 2}`, JSON objects).
- **`keep`** of a value struct with no reference fields is a plain copy, with no allocation; a
  global of such a type needs no `keep`. With reference fields (section 1.4), `keep` keeps those
  fields.
- **Generics** need nothing new: instances are monomorphized, so `T` = `Point` gets the inline
  layout and copy semantics in that instance.
- **`dyn`**: a value struct can implement shapes; converting it to `dyn S` copies it into one
  allocation (the object word points at the copy). Phase B, section 1.7.
- **Optionals**: `?Point` is section 2's tagged value, inline.

### 1.2 Layout

- A value struct's **alignment** is its widest field's (at most 8) and its **width**
  (`type_width`) is its size rounded up to that alignment, not to 8: a value struct of three `u8`
  is 3 bytes wide, aligned 1, so `[]RGB` is 3 bytes per element.
- `layout_struct` today places fields by width, 16 down to 1 (so a field is naturally aligned
  because its width is a power of two). With value-struct fields of any width it places them by
  alignment instead, 8 down to 1, which gives the same layout for every existing struct (each of
  today's widths is its own alignment, and the 16-byte `dyn` field has alignment 8 and still
  goes first among the 8-aligned fields).
- Inline everywhere: a value struct field occupies its width inside the enclosing object; a slice
  of value structs has that stride; a local lives in the frame (one slot per 8 bytes, as two-word
  values do today); a map value of value-struct type is stored in a cell like #567's dyn cells
  when it is wider than a word.
- `elem_size`, `type_width`, `field_offset`, `mk_mem` and `EX_ELEM` already take a width; what
  is new is that the width can exceed 16 and that a "load" of a wide value is a copy (below).

### 1.3 Code generation and ABI

Values of 1 to 16 bytes reuse the two-register paths that `dyn` values have (design_dyn.md §1):
locals in one or two frame words, arguments and results in one or two integer registers, fields
and elements loaded and stored as one or two words. Wider values:

- **Locals and temporaries** are frame areas; an expression of value type evaluates **into a
  destination address** rather than into registers (the existing `EX_MEM`/`EX_ELEM` address
  forms, plus a frame-area address).
- **Arguments wider than 16 bytes**: the caller copies the value into its own frame and passes
  the address; the callee owns that copy (it may modify it, since the caller's value is a separate
  copy). Same on arm64 and x86-64, a Tin-internal convention (no C calls take value structs).
- **Results wider than 16 bytes**: the caller passes a hidden destination address (x8 on arm64,
  as AAPCS64 does; the first argument register on x86-64) and the callee writes the result there.
- **Copies** of up to 64 bytes are unrolled word moves; larger ones call the runtime's `memmove`.
- Frame size grows with value locals; #570's large-frame support and page probes already cover
  frames past 4 KiB, and #570 part 3's slot sharing extends to value areas by live range.

**As built in phase A1 (#631, 2026-10-07).** One representation for every size, simpler than
the register paths above and the same on both back ends: an expression of value struct type is
the address of its bytes. A local is a frame area (`Sym.addr`, `words`), a field or element is
its inline bytes (`EX_MEM`/`EX_ELEM` of value struct type generate an address, no load), a
parameter's word is its caller's address (read-only unless `mut`), and a global's word is the
address of a long-lived block made at startup. Every store (`let`, assignment, field, element,
`append`, a multi-result binding) copies the bytes (`gen_value_store`, `rt_append_mem`), and a
literal is built in a zeroed frame area. A result is returned as a pool copy (`rt_vdup`) that the
caller copies again; the hidden destination of 1.3 and the two-register path for values up to 16
bytes are the next step (A2), with inline arrays (1.6). The region checker sees no reference in
a value struct (`has_ptr` is 0, `rc_counted` is 0), since none flows: its bytes are copied.

**As built in phase A2, results (#631).** A function whose one result is a value struct (any
size) takes a hidden destination: x8 on arm64 (as AAPCS64 does), r10 on x86-64, which no
argument, temporary or closure descriptor uses at a call. Its prologue stores it in a frame word,
and `return v` copies v's bytes there and returns that address, so the caller's view is
unchanged: the result is the address of its bytes. Every call of such a function (direct, method,
generic instance, function value, closure or `dyn` method: the call's type decides) gets a frame
area of its own, assigned per function after inlining and just before the frame is laid out
(`value_dests`), and the caller puts its address in the register last before the branch. A
`return f(...)` of such a call passes the function's own destination on, so a chain of them
writes the result once. A function with several results still returns each value struct as a
pool copy. The two-register path for values up to 16 bytes is left for later: with no
allocation on the result path, it would save one copy of at most 16 bytes per call.

**As built in phase B, copies (#669).** Two copies the A1 representation made are gone:
- **`for p in ps`** over a slice of value structs reads each element in place when the loop body
  cannot change one: it calls no function and assigns only to variables that are not value struct
  parameters (`view_safe_stmt`, checked after the body). `p`'s word then holds the element's
  address (`Sym.view`), as a parameter's does, instead of a frame area holding a copy. Otherwise
  `p` stays a copy taken before the body runs, as Go's is.
- **A nested literal** (`Particle{pos: Vec{...}}`) whose value struct holds no reference is built
  in its field's bytes: its temporary becomes a view of the field (`lit_in_place`). With
  references it is still built apart and copied, since the region pass would see its stores as
  stores into the temporary.

### 1.4 Reference fields

A value struct may hold references (`str`, slices, maps, reference structs, `?T`). Inline storage
then carries pointers that the memory model must see:

- **Region checker**: a value's region bits are the union of its reference fields'; storing a
  value struct is checked like storing each of its reference fields, so a request-memory `str`
  inside a value stored into a global is the same error as storing the `str` itself.
- **Reference counts (#176)**: a long-lived slot holding a value struct counts each of its
  reference fields; the generated `drop` for a slice of value structs walks the elements and
  drops their fields (`arrdrop$N` with the element's field offsets). `rc_counted` of a value
  struct is "has a counted field".
- **`keep`** copies the value and keeps each reference field (a `keep$N` that takes and returns
  the value).

### 1.5 What a value struct cannot do

- `same`, as above. `nil`: a value struct is never nil; `?Point` is the optional.
- A value struct cannot contain itself, directly or through other value structs (its size would be
  infinite): `type Node value struct { next ?Node }` is an error. It may hold a reference struct
  or a slice of itself (`kids []Node`), which is how recursive values are built.
- Converting between a value struct and a reference struct with the same fields is not implicit.

### 1.6 Arrays

Inside a `value struct`, a field `b [16]u8` is an **inline value array**: 16 bytes in the struct,
copied with it, compared and hashed by value. So the fixed-size keys of the roadmap item are

```tin
type UUID value struct {
	b [16]u8
}
```

which works as a map key and as a field of any struct with no allocation. Outside a value struct,
`[N]T` keeps today's meaning (a slice that starts with N zero elements). Making a bare `[N]T` a
value everywhere would change existing programs' meaning, so it is left to an edition and is not
part of this design.

### 1.7 Phases

- **A.** Value structs whose fields are numbers, `bool`, other value structs and inline arrays of
  those (no references). A1 (built): everything below but inline arrays, with the
  representation described after 1.3. A2: inline arrays (built: a `K_VARRAY` type that counts
  as a value struct for storage, `Ty.key` holding N), results through a hidden destination
  (built, after 1.3), values up to 16 bytes in registers (not yet). Inline in fields, slices, frames; copy semantics; zero values and
  `make`; `==`; map keys; printing; `argo`; `keep` as a copy; generics; both back ends and the
  ABI of section 1.3. This is what `Point`, `complex`, `RGB`, matrix cells and `UUID` need, and
  it meets #631's acceptance (one million `Point` in 16 MB plus the header).
- **B.** Reference fields (section 1.4), `dyn` of a value struct, value-struct map values wider
  than a word.
- **C.** #633 uses the same frame areas for non-escaping *reference* structs.

## 2. Optional numbers (#632)

### Decision: `?T` over numbers and `bool` is a two-word tagged value

`?i64`, `?f64`, `?u8`, `?bool` and the other number optionals become **16 bytes: a tag word and a
payload word**, nil being tag 0. They are values: in registers, frame slots, fields and slice
elements, never allocated. `?T` over reference types stays one word (the pointer, or 0).

- **Why two words**: every bit pattern of an `i64` is a valid value, so no payload can mean nil;
  NaN-boxing would work for `f64` only. Two words is the width `dyn` values already have, so the
  back ends' two-word paths (registers, frame slots, fields, elements, `CALLMULTI` lanes) carry it
  without new ABI.
- **Operations**: `x != nil` and `x == nil` test the tag; narrowing reads the payload; `if let`,
  `??` (#561) and `match` likewise; `==` between two optional numbers is "both nil, or both set
  with equal payloads" under the number's own `==`; assigning a number sets tag 1 and the payload;
  `nil` is the zero pair.
- **`keep`** of an optional number is a copy; a global `?i64` needs no `keep`. `keep(5)` still
  compiles (a no-op), so no existing program breaks; the primer stops recommending it.
- **Printing** is unchanged (`<nil>` or the number); **`argo`** is unchanged (`null` or the number).
- **Region and reference counts**: an optional number holds no pointer, so it has no region bits
  and is not counted (today's box is counted).
- **`?ValueStruct`** (phase B of section 1) is the same scheme with the struct's width as the
  payload: `[tag, value...]`.

### 2.1 Migration

The representation changes but the meaning does not, so no edition is needed. Only
compiler-generated code makes or reads the box: `box_value` and the `Sym.unbox` narrowing in
`check.tin`, the printers in `lower.tin` (`say_optnum_slice`, struct fields), the generated
`argo` code, `==` and `keep`. No program or package sees it, and those sites are what this
replaces.

## 3. Order of work

1. **#632** (section 2), first: it reuses the existing two-word paths and is the smaller change.
   It turns the `is_dyn_value` tests in the back ends into a "two-word value" test that covers
   both, which phase A then extends to wider values.
2. **#631 phase A** (sections 1.1 to 1.3, 1.6), with a `bench/v2` case comparing an
   array-of-structs loop with Go on Linux.
3. **#631 phase B** (section 1.4, `dyn`, `?ValueStruct`).
4. **#633** on the frame areas of phase A.

Each step: both back ends, the strict suite, the `make bootstrap` fixed point, Linux numbers from
bench-linux for the performance claims (toolchain/docs/PERFORMANCE.md), and LANGUAGE.md §3 and §9,
AGENT_PRIMER.md and RUNTIME.md §1 updated with the representation.

## 4. Open questions for review

- The spelling `value struct`: alternatives are an attribute (`@value type Point struct`) or a
  different noun (`record`). `value struct` reads as what it is and adds no keyword.
- Wider-than-16-byte arguments by hidden pointer to a caller copy (section 1.3) versus splitting
  into more registers: the copy is simpler and the same on both back ends; Go's register ABI
  splits structs of up to a few words into registers, which could come later behind the same
  front end.
- `m[k].x = v` on a map of value structs: rejected (as Go does) or a write-through that inserts
  the zero value for a missing key. Rejecting is the smaller rule and can be relaxed later
  without breaking code.
