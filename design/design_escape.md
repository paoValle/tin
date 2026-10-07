# Design: frame allocation and loop arenas (#633)

Status: proposal, 2026-10-07. Decides how values that never outlive a function call or a loop
iteration stop costing pool memory until the request (or the program) ends, before any code
(AGENTS.md rule 5). Builds on design/design_layouts.md (value structs, #631, already put value
types in the frame) and on the region pass (`toolchain/compiler/region.tin`).

## 0. The problem, measured

Every allocation goes to the pool and lives until the pool is reset: at the end of a request,
or never in a plain program. On 5ef78b9 (from the issue): a plain loop that makes a 16-byte
struct and a short string per iteration reaches 1.49 GB at five million iterations;
binary-trees holds 917 MB against Go's 37 MB; a long request holds every temporary until it
answers, so `limit memory` trips on garbage. #629 made the plain-program case visible (the
pool warning) and pointed at `arena { }`; this design makes the common cases need no `arena`.

Two mechanisms, because the cases differ:

- **A value that never leaves its function** (a struct made, read and dropped; a small buffer
  filled and parsed) needs no heap at all: it goes in the frame. Section 2.
- **A loop iteration whose allocations never leave the iteration** (binary-trees' `check(
  bottomUp(d))`, a parse-one-record loop, the plain-program loop) needs its memory back at the
  end of each iteration, whatever made it, including callees and runtime calls (strings, slices,
  trees). That is an arena per iteration, inferred instead of written. Section 3.

Frame allocation is the cheaper of the two (no runtime call at all), so it is tried first;
an iteration arena then covers what is left.

## 1. What the region pass already knows

The pass gives every expression a set of origin bits (`RG_FRESH`: made from this request's
pool; `RG_INGOT`: long-lived; `RG_P0 << i`: reachable from parameter i; `RG_UNK`) and summarizes
each function: which parameters it stores into (`sum[0]`, `sum[10]`), what its containers hold
(`sum[1]`, type and origin pairs), and where its results come from (`sum[2 + j]`). The summaries
are iterated to a fixed point over the whole program, indirect calls joined into `rg_fnsum`.
The explicit `arena { }` check (#236) already runs this machinery with one more bit (`RG_OUT`:
made outside the arena) and rejects a value made inside escaping outside (E316 and friends).

From the summaries a callee's **parameter i escapes** when any of these holds: a result's bits
include `RG_P0 << i`; a held pair of `sum[1]` (what the callee's containers keep, visible to its
caller) carries `RG_P0 << i`; the callee stores parameter i into a container reachable from
another parameter (`sum[10]` records the store, and the stored value's bits carry the parameter);
or the callee captures it in a closure that is not frame-local. Indirect calls use the joined
summary, so an unknown callee lets every argument escape.

## 2. Frame allocation (phase 1)

A **candidate** is a fresh allocation of known size bound directly to a local: a struct literal
(`let p = Point{...}`, `mut b = Builder{...}`), and later `make([]T, n, k)` with constant k under
the frame budget, `[]T{...}` literals, and closures (design_foundations §1 plans the closure case
the same way). It is placed in the frame instead of the pool when its local is **contained**:

- every use of the local reads a field or element of it, writes one (the value written may
  escape; the object does not), compares it, prints or formats it, or passes it to a parameter
  that does not escape (section 1), including a method receiver;
- it is never assigned to another variable, stored into a field, element, map entry or global,
  appended to a slice, returned, captured by a closure, sent, converted to `dyn`, or passed to
  `keep` (which copies, so that one is allowed), and no address of it is taken;
- the local itself is not reassigned while the object may be in use (a `mut` local rebound in a
  loop gets one frame slot per binding site, reused each iteration, since the old object is
  dead once the name moves on).

The check is intraprocedural over the function's statements, using the callee summaries for
calls; it runs after the region fixed point, so the summaries are final. It is conservative:
anything it cannot prove keeps the pool.

**Layout and limits.** The object gets a frame area of its size (the multi-word slots value
structs use, `Sym.addr`/`words`), zeroed where the literal is built. The frame budget is the
E905 ceiling (#570) less a margin: an object over 4 KiB, or a function whose frame objects would
pass 64 KiB, keeps the pool for the rest (large frames cost a stack probe per page and wreck the
cache; 64 KiB is well under the 16 MiB arm64 limit and Tin's task stacks).

*As built (phase 1).* `frame_objects` runs after the region pass and the loop scan of §3. A
candidate is a `let` or `mut` bound to a reference struct literal. It is contained when every
use of the local:
- reads or writes a field;
- compares its address;
- is a `keep` or a generated printing, comparing or key helper;
- or is an argument of a direct call whose summary shows that parameter reaching no result and
  no held pair, with the new may-keep word (§3) clear.

A rebinding of the local, a capture, an indirect or `dyn` call, a conversion, a function literal,
and a statement the pass does not know (`fail`, `defer`, `select`) all keep the pool.

The literal's `rt_alloc` becomes a frame area typed as a value-struct twin of the struct (so both
back ends home and zero it as #631 does), and the object is that area's address. The limits are
tighter than above while the zeroing is unrolled: 128 bytes per object and 512 per function.
That keeps deep recursion within the 256 KiB task stacks.

**Slices.** A frame slice (phase 1b) starts with a frame buffer of its constant capacity; its
header's region word says "frame". `append` past the capacity copies into the pool, as appending
to a slice whose backing it does not own does today (`rt_own`), so a slice that grows stays
correct and only stops being free.

**Unwinding.** A panic or `fail` that unwinds through the frame needs nothing: no object in the
frame is reachable from outside it (that is the rule), so discarding the frame discards them.
`guard` and `arena` blocks see frame objects as values of the function that holds them.

## 3. Iteration arenas (phase 2)

A `for` loop whose body **allocates** (a literal, `make`, `append`, a concatenation or
interpolation, or a call whose summary says it may allocate fresh memory) and whose iterations
**contain** their allocations gives back each iteration's memory: a pool mark before the body,
released after it and on every `continue`, `break` and `return` leaving it (see Cost). An iteration
contains its allocations when, treating everything made inside the body as `RG_FRESH` and
everything made before it as `RG_OUT` (exactly the explicit arena check, #236):

- no value with fresh bits is assigned to a variable declared outside the body, stored into a
  container that may be outside it (a field, element or map entry of an `RG_OUT` object, a
  global), appended to an outside slice or inserted into an outside map (either may reallocate
  the outside container's storage in the arena), returned, sent, captured by a closure made
  outside the body, or passed to a parameter that escapes;
- the body does not grow an outside slice or map at all (even with outside values), since the
  growth would land in the arena;
- `detach`, `scope` spawns and `defer` in the body capture nothing made in it (`defer` in a loop
  is already E270).

When the check fails the loop is left as it is, with no diagnostic: the inference is an
optimization, and `arena { }` stays the way to ask for one and be told why it cannot be. The
check is a separate scan of the lowered body after the region fixed point, not the explicit
arena's closure (which turns captured variables into cells): it reads the summaries the pass
leaves (`rg_grows`, `rg_fstores`, `rg_pstores`, results and held pairs) for each call, and
treats any store of a pointer-holding value into a local declared outside the body, or into
a field, element or map entry of an object not made in the body, as an escape. A function
literal in the body makes the loop ineligible in this phase.

A call is judged by its callee's summary, which gets one more word: the function, or one it
calls, **may keep memory past the call** other than through its parameters and results. The
region pass sets it, and carries it to callers through the fixed point, for a store into
long-lived memory (`RG_INGOT` or `RG_UNK`, stored or not reported in trusted code), the growth
of a long-lived slice or map, an indirect or `dyn` call, a call of a function with no summary
(extern, generated, other than the printing, comparing, key and `keep` helpers), and a runtime
call outside a short list known to keep nothing (allocation, map reads, string building,
formatting, system calls). Spawns, scopes, `defer`, `select`, `use`, `within`, `guard`, `limit`
and arenas are all outside the list. A loop that makes such a call is left alone, and so is one
that calls a function resetting the pool.

**Cost.** The explicit arena's `rt_arena_open`/`rt_arena_close` are too heavy to run per
iteration (a boundary record, its own pool record, a memset of what it used). An iteration needs
less: nothing made in it survives, so it can allocate from the pool it is in and give the space
back. A **pool mark** (three context words read inline: the bump pointer, the head of the
extra-chunk list and `ctxShareGen`, below) is taken before the body; after it, when either of
the first two moved, `rt_pool_release` frees the chunks added since and puts the bump pointer
back, zeroing the bytes the iteration used (the pool hands out zeroed memory) and refunding
what `limit` budgets were charged for the freed chunks. That is a handful of words and a memset
proportional to what the iteration allocated, which the allocation already touched. A detached
task has a pool of its own, but a scope's children allocate from their parent's pool
(`rt_pool_words`), so a child could allocate between a parent iteration's mark and its release
(while the parent waits), or a sibling between a child's. The core counts the pool-sharing
children alive (`poolSharers`) and bumps `ctxShareGen` whenever one starts or ends; the release
does nothing while one is alive or when the word moved since the mark, as it does nothing
inside an arena (`arenaLive`). A loop whose body makes no call is never wrapped. Inner loops are considered before outer ones; a
loop already inside an iteration arena is wrapped only if its own iterations allocate enough to
matter (a body with a literal or call that allocates), to keep tight inner loops free of the
overhead. bench-linux decides: no benchmark may move by more than its noise.

**Memory accounting.** With iteration arenas, a request's `limit memory` sees what is live across
iterations, not every iteration's garbage (the issue's third point), and a plain program's pool
stays at its working set, so the #629 warning stops firing for these loops.

## 4. Phases and tests

1. Frame allocation of struct literals bound to locals (section 2), both back ends. A `-S` check
   that a contained literal in a loop produces no allocator call; a strict test that each
   escaping form (stored, returned, captured, passed to an escaping parameter, appended) keeps
   the pool and still behaves; `hearth.HeapStats`/`rt_pool_used` showing zero pool growth for a
   contained loop.
2. Iteration arenas (section 3): the issue's plain-program loop in constant memory without
   `arena`, binary-trees' resident size within 3x of Go's on Linux (each depth's trees are made
   and checked inside one iteration), and a `task_check.py`-style check that `limit memory` on a
   request that builds and drops temporaries counts live data only.
3. Frame slices and closures (sections 2's slices and design_foundations §1).

Every phase: no region `_bad.tin` test changes its diagnostics (the analysis reads the summaries,
it does not replace them), the strict suite and the cross suites, `make bootstrap`, and
bench-linux numbers for each claim.

## 5. Open questions

- Whether phase 2 should also wrap a function body (a call whose allocations do not escape the
  call), which would cover recursive builders; a loop iteration is the common case and is
  decided first.
- Whether a frame object may be passed to a `mut` parameter that does not escape (it may be
  written through, which is fine) — proposed yes.
