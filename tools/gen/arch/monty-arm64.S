// Montgomery multiplication leaves for seal (#488), AArch64. tools/gen/gen_aes_hw.py turns them
// into toolchain/compiler/aes_hw.tin. Relocation-free; they use x0-x17 and the callee-saved
// x19-x24 (saved and restored here) and keep x28 (the core context). Constant-time: the loops
// run for n limbs, and no branch or address depends on the operands.
	.text

// mont_mul(z x0, x x1, y x2, m x3, ctx x4): z = x*y/2^(64n) mod m for n >= 2 limbs, the same
// arithmetic as seal's portable monty.mul (FIOS: per row, x*y[i] and mm*m are added to t in
// one pass with two carries, and the low limb, which the second product clears, is dropped).
// ctx points at three words: -m^-1 mod 2^64, n, and the address of n+1 words of scratch. z may
// alias x or y: it is written only after the last row.
	.globl mont_mul
	.type mont_mul, %function
mont_mul:
	stp	x19, x20, [sp, #-48]!
	stp	x21, x22, [sp, #16]
	stp	x23, x24, [sp, #32]
	ldp	x5, x6, [x4]
	ldr	x7, [x4, #16]
	mov	x8, x7
	add	x9, x6, #1
0:	str	xzr, [x8], #8
	subs	x9, x9, #1
	b.ne	0b
	mov	x19, x2
	mov	x20, x6
1:	ldr	x9, [x19], #8
	ldr	x10, [x1]
	ldr	x11, [x7]
	mul	x12, x10, x9
	umulh	x13, x10, x9
	adds	x12, x12, x11
	cinc	x13, x13, hs
	mul	x14, x12, x5
	ldr	x15, [x3]
	mul	x16, x14, x15
	umulh	x17, x14, x15
	cmn	x16, x12
	cinc	x17, x17, hs
	add	x21, x1, #8
	add	x22, x3, #8
	mov	x23, x7
	sub	x24, x6, #1
2:	ldr	x10, [x21], #8
	ldr	x15, [x22], #8
	ldr	x11, [x23, #8]
	mul	x12, x10, x9
	umulh	x2, x10, x9
	adds	x12, x12, x11
	cinc	x2, x2, hs
	adds	x12, x12, x13
	cinc	x13, x2, hs
	mul	x16, x15, x14
	umulh	x4, x15, x14
	adds	x16, x16, x12
	cinc	x4, x4, hs
	adds	x16, x16, x17
	cinc	x17, x4, hs
	str	x16, [x23], #8
	subs	x24, x24, #1
	b.ne	2b
	ldr	x11, [x23, #8]
	adds	x11, x11, x13
	cset	x8, hs
	adds	x11, x11, x17
	cinc	x8, x8, hs
	str	x11, [x23]
	str	x8, [x23, #8]
	subs	x20, x20, #1
	b.ne	1b
	// z = t - m, then z = t again when that borrowed and t has no top word.
	ldr	x8, [x7, x6, lsl #3]
	mov	x9, x7
	mov	x10, x3
	mov	x11, x0
	mov	x12, x6
	subs	xzr, xzr, xzr
3:	ldr	x13, [x9], #8
	ldr	x14, [x10], #8
	sbcs	x13, x13, x14
	str	x13, [x11], #8
	sub	x12, x12, #1
	cbnz	x12, 3b
	cset	x13, lo
	eor	x8, x8, #1
	and	x13, x13, x8
	neg	x13, x13
	mov	x9, x7
	mov	x11, x0
	mov	x12, x6
4:	ldr	x14, [x9], #8
	ldr	x15, [x11]
	and	x14, x14, x13
	bic	x15, x15, x13
	orr	x14, x14, x15
	str	x14, [x11], #8
	sub	x12, x12, #1
	cbnz	x12, 4b
	ldp	x23, x24, [sp, #32]
	ldp	x21, x22, [sp, #16]
	ldp	x19, x20, [sp], #48
	ret
	.size mont_mul, .-mont_mul

// m4_mont(z x0, x x1, y x2, m x3, minv x4): mont_mul for four limbs, everything in registers.
// A row adds x*y[i] to t (the products' low halves into words 0-3 and their high halves into
// words 1-4, two carry chains), then adds mm*m with mm = t0*minv, which clears word 0, and
// drops it: the register names rotate by one word per row. t < 2m afterwards; the last step
// subtracts m and keeps t instead when that borrowed with no top word (csel, no branch).
	.macro m4row yoff, t0, t1, t2, t3, t4
	ldr	x3, [x2, #\yoff]
	mul	x19, x5, x3
	mul	x20, x6, x3
	mul	x21, x7, x3
	mul	x22, x8, x3
	umulh	x23, x5, x3
	umulh	x24, x6, x3
	umulh	x25, x7, x3
	umulh	x26, x8, x3
	adds	\t0, \t0, x19
	adcs	\t1, \t1, x20
	adcs	\t2, \t2, x21
	adcs	\t3, \t3, x22
	cset	x27, hs
	adds	\t1, \t1, x23
	adcs	\t2, \t2, x24
	adcs	\t3, \t3, x25
	adcs	\t4, \t4, x26
	cset	x1, hs
	adds	\t4, \t4, x27
	cinc	x1, x1, hs
	mul	x3, \t0, x4
	mul	x19, x9, x3
	mul	x20, x10, x3
	mul	x21, x11, x3
	mul	x22, x12, x3
	umulh	x23, x9, x3
	umulh	x24, x10, x3
	umulh	x25, x11, x3
	umulh	x26, x12, x3
	cmn	\t0, x19
	adcs	\t1, \t1, x20
	adcs	\t2, \t2, x21
	adcs	\t3, \t3, x22
	cset	x27, hs
	adds	\t1, \t1, x23
	adcs	\t2, \t2, x24
	adcs	\t3, \t3, x25
	adcs	\t4, \t4, x26
	cset	x3, hs
	adds	\t4, \t4, x27
	cinc	x3, x3, hs
	add	\t0, x1, x3
	.endm

	.globl m4_mont
	.type m4_mont, %function
m4_mont:
	stp	x19, x20, [sp, #-80]!
	stp	x21, x22, [sp, #16]
	stp	x23, x24, [sp, #32]
	stp	x25, x26, [sp, #48]
	str	x27, [sp, #64]
	ldp	x5, x6, [x1]
	ldp	x7, x8, [x1, #16]
	ldp	x9, x10, [x3]
	ldp	x11, x12, [x3, #16]
	mov	x13, #0
	mov	x14, #0
	mov	x15, #0
	mov	x16, #0
	mov	x17, #0
	m4row	0, x13, x14, x15, x16, x17
	m4row	8, x14, x15, x16, x17, x13
	m4row	16, x15, x16, x17, x13, x14
	m4row	24, x16, x17, x13, x14, x15
	// t = x17, x13, x14, x15 and top word x16.
	subs	x19, x17, x9
	sbcs	x20, x13, x10
	sbcs	x21, x14, x11
	sbcs	x22, x15, x12
	sbcs	xzr, x16, xzr
	csel	x19, x17, x19, lo
	csel	x20, x13, x20, lo
	csel	x21, x14, x21, lo
	csel	x22, x15, x22, lo
	stp	x19, x20, [x0]
	stp	x21, x22, [x0, #16]
	ldr	x27, [sp, #64]
	ldp	x25, x26, [sp, #48]
	ldp	x23, x24, [sp, #32]
	ldp	x21, x22, [sp, #16]
	ldp	x19, x20, [sp], #80
	ret
	.size m4_mont, .-m4_mont

// m4_add(z x0, x x1, y x2, m x3): z = x + y mod m for four limbs, x, y < m; z may alias x or y.
// The sum has a fifth word (the carry); m is subtracted unless that borrows past it (csel).
	.globl m4_add
	.type m4_add, %function
m4_add:
	ldp	x4, x5, [x1]
	ldp	x6, x7, [x1, #16]
	ldp	x8, x9, [x2]
	ldp	x10, x11, [x2, #16]
	adds	x4, x4, x8
	adcs	x5, x5, x9
	adcs	x6, x6, x10
	adcs	x7, x7, x11
	cset	x12, hs
	ldp	x13, x14, [x3]
	ldp	x15, x16, [x3, #16]
	subs	x8, x4, x13
	sbcs	x9, x5, x14
	sbcs	x10, x6, x15
	sbcs	x11, x7, x16
	sbcs	xzr, x12, xzr
	csel	x4, x4, x8, lo
	csel	x5, x5, x9, lo
	csel	x6, x6, x10, lo
	csel	x7, x7, x11, lo
	stp	x4, x5, [x0]
	stp	x6, x7, [x0, #16]
	ret
	.size m4_add, .-m4_add

// m4_sub(z x0, x x1, y x2, m x3): z = x - y mod m for four limbs, x, y < m; m is added back
// (masked, no branch) when the subtraction borrows.
	.globl m4_sub
	.type m4_sub, %function
m4_sub:
	ldp	x4, x5, [x1]
	ldp	x6, x7, [x1, #16]
	ldp	x8, x9, [x2]
	ldp	x10, x11, [x2, #16]
	subs	x4, x4, x8
	sbcs	x5, x5, x9
	sbcs	x6, x6, x10
	sbcs	x7, x7, x11
	csetm	x12, lo
	ldp	x13, x14, [x3]
	ldp	x15, x16, [x3, #16]
	and	x13, x13, x12
	and	x14, x14, x12
	and	x15, x15, x12
	and	x16, x16, x12
	adds	x4, x4, x13
	adcs	x5, x5, x14
	adcs	x6, x6, x15
	adcs	x7, x7, x16
	stp	x4, x5, [x0]
	stp	x6, x7, [x0, #16]
	ret
	.size m4_sub, .-m4_sub

// p256_pick(dst x0, tbl x1, w x2): dst (12 words) = the 12-word entry w of tbl (entries 1 to 15,
// in order) when 1 <= w <= 15, else unchanged. Every entry is read (csel on one comparison per
// entry), so neither a branch nor an address depends on w.
	.globl p256_pick
	.type p256_pick, %function
p256_pick:
	mov	x3, #1
	mov	x4, #15
1:	cmp	x3, x2
	ldp	x5, x6, [x1]
	ldp	x7, x8, [x0]
	csel	x5, x5, x7, eq
	csel	x6, x6, x8, eq
	stp	x5, x6, [x0]
	ldp	x5, x6, [x1, #16]
	ldp	x7, x8, [x0, #16]
	csel	x5, x5, x7, eq
	csel	x6, x6, x8, eq
	stp	x5, x6, [x0, #16]
	ldp	x5, x6, [x1, #32]
	ldp	x7, x8, [x0, #32]
	csel	x5, x5, x7, eq
	csel	x6, x6, x8, eq
	stp	x5, x6, [x0, #32]
	ldp	x5, x6, [x1, #48]
	ldp	x7, x8, [x0, #48]
	csel	x5, x5, x7, eq
	csel	x6, x6, x8, eq
	stp	x5, x6, [x0, #48]
	ldp	x5, x6, [x1, #64]
	ldp	x7, x8, [x0, #64]
	csel	x5, x5, x7, eq
	csel	x6, x6, x8, eq
	stp	x5, x6, [x0, #64]
	ldp	x5, x6, [x1, #80]
	ldp	x7, x8, [x0, #80]
	csel	x5, x5, x7, eq
	csel	x6, x6, x8, eq
	stp	x5, x6, [x0, #80]
	add	x1, x1, #96
	add	x3, x3, #1
	subs	x4, x4, #1
	b.ne	1b
	ret
	.size p256_pick, .-p256_pick
