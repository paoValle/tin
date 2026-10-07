// m4_mont for seal (#488), x86-64 with BMI2: mont_mul for four limbs (P-256's field and order,
// Ed25519's order), everything in registers. tools/gen/gen_aes_hw.py turns it into
// toolchain/compiler/aes_hw.tin. Relocation-free, never touches r15 (the core context); rbx, rbp
// and r12-r14 are saved. Constant-time: straight-line code, a conditional move at the end.
.intel_syntax noprefix
.text

// m4row: one row of the Montgomery product. t0-t4 hold t (t4 is 0 or 1 on entry, so adding a
// carry to it cannot wrap), h0-h3 (r8-r11) the high halves of four products, \l a low half.
// Part 1 adds x*y[i]: the low halves into words 0-3 (one carry chain), the high halves into
// words 1-4 (another); the last carry, t5, waits at [rsp+8]. Part 2 does the same with mm*m, mm =
// t0*minv, which clears word 0; the result is shifted down one word, its top word (t5 and the
// last carry) ends in \l, and the register that held t0 is free for the next row's \l.
.macro m4row yoff, l, t0, t1, t2, t3, t4
	mov	rdx, [rdi+\yoff]
	mulx	r8, \l, [rsi]
	add	\t0, \l
	mulx	r9, \l, [rsi+8]
	adc	\t1, \l
	mulx	r10, \l, [rsi+16]
	adc	\t2, \l
	mulx	r11, \l, [rsi+24]
	adc	\t3, \l
	adc	\t4, 0
	add	\t1, r8
	adc	\t2, r9
	adc	\t3, r10
	adc	\t4, r11
	mov	\l, 0
	adc	\l, 0
	mov	[rsp+8], \l
	mov	rdx, \t0
	imul	rdx, [rsp+16]
	mulx	r8, \l, [rcx]
	add	\t0, \l
	mulx	r9, \l, [rcx+8]
	adc	\t1, \l
	mulx	r10, \l, [rcx+16]
	adc	\t2, \l
	mulx	r11, \l, [rcx+24]
	adc	\t3, \l
	adc	\t4, 0
	add	\t1, r8
	adc	\t2, r9
	adc	\t3, r10
	adc	\t4, r11
	mov	\l, [rsp+8]
	adc	\l, 0
.endm

// m4_mont(z rdi, x rsi, y rdx, m rcx, minv r8): z = x*y/2^256 mod m. z may alias x or y.
.global m4_mont
.type m4_mont, @function
m4_mont:
	push	rbx
	push	rbp
	push	r12
	push	r13
	push	r14
	sub	rsp, 24
	mov	[rsp], rdi
	mov	[rsp+16], r8
	mov	rdi, rdx
	xor	ebx, ebx
	xor	ebp, ebp
	xor	r12d, r12d
	xor	r13d, r13d
	xor	r14d, r14d
	// rax is the first row's \l; the rows rotate the names: the new top word lands in \l.
	m4row	0, rax, rbx, rbp, r12, r13, r14
	m4row	8, rbx, rbp, r12, r13, r14, rax
	m4row	16, rbp, r12, r13, r14, rax, rbx
	m4row	24, r12, r13, r14, rax, rbx, rbp
	// t = r14, rax, rbx, rbp and top word r12. d = t - m; keep t when that borrows past the top word.
	mov	r8, r14
	sub	r8, [rcx]
	mov	r9, rax
	sbb	r9, [rcx+8]
	mov	r10, rbx
	sbb	r10, [rcx+16]
	mov	r11, rbp
	sbb	r11, [rcx+24]
	sbb	r12, 0
	cmovc	r8, r14
	cmovc	r9, rax
	cmovc	r10, rbx
	cmovc	r11, rbp
	mov	rdi, [rsp]
	mov	[rdi], r8
	mov	[rdi+8], r9
	mov	[rdi+16], r10
	mov	[rdi+24], r11
	add	rsp, 24
	pop	r14
	pop	r13
	pop	r12
	pop	rbp
	pop	rbx
	ret
.size m4_mont, .-m4_mont

// m4_add(z rdi, x rsi, y rdx, m rcx): z = x + y mod m for four limbs, x, y < m; z may alias x or y.
// The sum has a fifth word (rax); m is subtracted unless that borrows past it. The masked words
// of m are made first: AND would clear the carry the subtraction chain carries.
.global m4_add
.type m4_add, @function
m4_add:
	push	rbx
	push	rbp
	mov	r8, [rsi]
	mov	r9, [rsi+8]
	mov	r10, [rsi+16]
	mov	r11, [rsi+24]
	add	r8, [rdx]
	adc	r9, [rdx+8]
	adc	r10, [rdx+16]
	adc	r11, [rdx+24]
	mov	eax, 0
	adc	rax, 0
	mov	rsi, r8
	sub	rsi, [rcx]
	mov	rsi, r9
	sbb	rsi, [rcx+8]
	mov	rsi, r10
	sbb	rsi, [rcx+16]
	mov	rsi, r11
	sbb	rsi, [rcx+24]
	sbb	rax, 0
	sbb	rsi, rsi
	not	rsi
	mov	rax, [rcx]
	and	rax, rsi
	mov	rdx, [rcx+8]
	and	rdx, rsi
	mov	rbx, [rcx+16]
	and	rbx, rsi
	mov	rbp, [rcx+24]
	and	rbp, rsi
	sub	r8, rax
	sbb	r9, rdx
	sbb	r10, rbx
	sbb	r11, rbp
	mov	[rdi], r8
	mov	[rdi+8], r9
	mov	[rdi+16], r10
	mov	[rdi+24], r11
	pop	rbp
	pop	rbx
	ret
.size m4_add, .-m4_add

// m4_sub(z rdi, x rsi, y rdx, m rcx): z = x - y mod m for four limbs; m is added back, masked,
// when the subtraction borrows.
.global m4_sub
.type m4_sub, @function
m4_sub:
	push	rbx
	push	rbp
	mov	r8, [rsi]
	mov	r9, [rsi+8]
	mov	r10, [rsi+16]
	mov	r11, [rsi+24]
	sub	r8, [rdx]
	sbb	r9, [rdx+8]
	sbb	r10, [rdx+16]
	sbb	r11, [rdx+24]
	sbb	rax, rax
	mov	rsi, [rcx]
	and	rsi, rax
	mov	rdx, [rcx+8]
	and	rdx, rax
	mov	rbx, [rcx+16]
	and	rbx, rax
	mov	rbp, [rcx+24]
	and	rbp, rax
	add	r8, rsi
	adc	r9, rdx
	adc	r10, rbx
	adc	r11, rbp
	mov	[rdi], r8
	mov	[rdi+8], r9
	mov	[rdi+16], r10
	mov	[rdi+24], r11
	pop	rbp
	pop	rbx
	ret
.size m4_sub, .-m4_sub

// p256_pick(dst rdi, tbl rsi, w rdx): dst (12 words) = the 12-word entry w of tbl (entries 1 to
// 15, in order) when 1 <= w <= 15, else unchanged. Every entry is read (cmov on one comparison
// per entry), so neither a branch nor an address depends on w.
.global p256_pick
.type p256_pick, @function
p256_pick:
	mov	ecx, 1
	mov	r8d, 15
1:	cmp	rcx, rdx
	mov	rax, [rdi]
	cmove	rax, [rsi]
	mov	[rdi], rax
	mov	rax, [rdi+8]
	cmove	rax, [rsi+8]
	mov	[rdi+8], rax
	mov	rax, [rdi+16]
	cmove	rax, [rsi+16]
	mov	[rdi+16], rax
	mov	rax, [rdi+24]
	cmove	rax, [rsi+24]
	mov	[rdi+24], rax
	mov	rax, [rdi+32]
	cmove	rax, [rsi+32]
	mov	[rdi+32], rax
	mov	rax, [rdi+40]
	cmove	rax, [rsi+40]
	mov	[rdi+40], rax
	mov	rax, [rdi+48]
	cmove	rax, [rsi+48]
	mov	[rdi+48], rax
	mov	rax, [rdi+56]
	cmove	rax, [rsi+56]
	mov	[rdi+56], rax
	mov	rax, [rdi+64]
	cmove	rax, [rsi+64]
	mov	[rdi+64], rax
	mov	rax, [rdi+72]
	cmove	rax, [rsi+72]
	mov	[rdi+72], rax
	mov	rax, [rdi+80]
	cmove	rax, [rsi+80]
	mov	[rdi+80], rax
	mov	rax, [rdi+88]
	cmove	rax, [rsi+88]
	mov	[rdi+88], rax
	add	rsi, 96
	add	rcx, 1
	sub	r8, 1
	jnz	1b
	ret
.size p256_pick, .-p256_pick
