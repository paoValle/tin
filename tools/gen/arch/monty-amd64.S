// Montgomery multiplication leaves for seal (#488), x86-64, and their CPUID checks.
// tools/gen/gen_aes_hw.py turns them into toolchain/compiler/aes_hw.tin. Relocation-free; they
// use rax rcx rdx rsi rdi r8-r11 and the callee-saved rbx rbp r12-r14 (pushed and popped here),
// and never touch r15 (the core context). Constant-time: every loop runs for a count that is a
// function of n alone, and no branch or address depends on the operands.
.intel_syntax noprefix
.text

// bmi2_cpu() -> 1 when the CPU has BMI2 (MULX), else 0 (CPUID leaf 7 EBX bit 8).
.global bmi2_cpu
.type bmi2_cpu, @function
bmi2_cpu:
	push rbx
	xor eax, eax
	cpuid
	cmp eax, 7
	jb 8f
	mov eax, 7
	xor ecx, ecx
	cpuid
	bt ebx, 8
	jnc 8f
	mov eax, 1
	pop rbx
	ret
8:	xor eax, eax
	pop rbx
	ret
.size bmi2_cpu, .-bmi2_cpu

// bmi2_adx_cpu() -> 1 when the CPU has both BMI2 and ADX (ADCX, ADOX), else 0 (CPUID leaf 7
// EBX bits 8 and 19).
.global bmi2_adx_cpu
.type bmi2_adx_cpu, @function
bmi2_adx_cpu:
	push rbx
	xor eax, eax
	cpuid
	cmp eax, 7
	jb 8f
	mov eax, 7
	xor ecx, ecx
	cpuid
	and ebx, 0x00080100
	cmp ebx, 0x00080100
	jne 8f
	mov eax, 1
	pop rbx
	ret
8:	xor eax, eax
	pop rbx
	ret
.size bmi2_adx_cpu, .-bmi2_adx_cpu

// BLOCK adx, src, off, first: 4 limbs of t += src * rdx at index r10 (src is rsi, x, or rcx, m),
// with the carry word in r8 in and out; the sums go to t[j+off/8] (off is 0, or -8 for the
// shifted-down pass B). first omits the store of the first limb, whose sum is 0 mod 2^64.
// Unrolled limbs 0..3: the plain version has the product chain then the t chain; the ADX one
// runs both at once, ADCX (CF) for the product plus the previous high word and ADOX (OF) for t.
.macro BLOCK adx, src, off, first
.if \adx
	xor ebx, ebx
	mulx rbp, rax, [\src+r10]
	adcx rax, r8
	adox rax, [r9+r10]
.if !\first
	mov [r9+r10+(\off)], rax
.endif
	mulx r8, r12, [\src+r10+8]
	adcx r12, rbp
	adox r12, [r9+r10+8]
	mov [r9+r10+8+(\off)], r12
	mulx rbp, rax, [\src+r10+16]
	adcx rax, r8
	adox rax, [r9+r10+16]
	mov [r9+r10+16+(\off)], rax
	mulx r8, r12, [\src+r10+24]
	adcx r12, rbp
	adox r12, [r9+r10+24]
	mov [r9+r10+24+(\off)], r12
	adcx r8, rbx
	adox r8, rbx
.else
	mulx rbx, rax, [\src+r10]
	mulx r12, rbp, [\src+r10+8]
	add rax, r8
	mulx r14, r13, [\src+r10+16]
	mulx r8, rdi, [\src+r10+24]
	adc rbp, rbx
	adc r13, r12
	adc rdi, r14
	adc r8, 0
	add rax, [r9+r10]
	adc rbp, [r9+r10+8]
	adc r13, [r9+r10+16]
	adc rdi, [r9+r10+24]
	adc r8, 0
.if !\first
	mov [r9+r10+(\off)], rax
.endif
	mov [r9+r10+8+(\off)], rbp
	mov [r9+r10+16+(\off)], r13
	mov [r9+r10+24+(\off)], rdi
.endif
.endm

// MONT_MUL name, adx: z = x*y/2^(64n) mod m for n >= 2 limbs, the same arithmetic as the arm64
// leaf and seal's portable monty.mul, as two-pass CIOS: for every limb y[i], pass A adds
// x*y[i] to t, then pass B adds mm*m, mm = t[0] * (-m^-1), and drops the zero low limb (t is
// shifted down one limb as it is written). t < 2m holds after every row, so it is n+1 limbs,
// and the final subtract-and-select (keep t when t-m borrows and t has no top limb) fully
// reduces it. Both passes walk the limbs 4 at a time with a negative byte index in r10 that
// ends at 0 (so the loop test is the ADD itself). The n mod 4 low limbs go first, one at a
// time (the index is then a multiple of 32, which is how the single-limb loop knows to stop),
// then the 4-limb blocks. In pass B the first block (n >= 4) is the block that drops limb 0, so
// n = 16 and n = 32 run no single-limb steps at all.
//
// MULX takes the high word first in Intel syntax: mulx hi, lo, src.
//
// Arguments: z rdi, x rsi, y rdx, m rcx, ctx r8. ctx points at three words: -m^-1 mod 2^64,
// n, and the address of n+1 words of scratch t, which the leaf zeroes. z may alias x or y: it is
// written only after the last row.
//
// Registers in the rows: rdx the MULX multiplier (y[i], then mm); rsi, rcx, r9 the ends of x,
// m and t; r10 the index; r11 the word above t[n] (0 or 1); r8 the running carry word; rax rbx
// rbp r12 r13 r14 rdi are scratch. The frame holds z, the y cursor, the rows left, -m^-1 and -8n.
//
// PLAIN (MULX, ADD, ADC), per block of 4 limbs: 4 MULX; a carry chain over the products with
// the previous carry word (add, adc, adc, adc, adc: 5); a second chain that adds t (add, adc,
// adc, adc, adc with memory operands: 5); 4 stores; and the index step: 20 instructions, 5 per
// limb, 1 MULX per limb. The two chains do not share carries: the first ends in the carry
// word, the second starts fresh, so they overlap in the out-of-order core.
// ADX, per block: XOR (zero, and clears CF and OF), then per limb MULX, ADCX (product plus the
// previous high word, chain on CF), ADOX (plus t, chain on OF) and a store, then ADCX/ADOX of
// the zero into the high word (folding both carries) and the index step: 21 instructions per
// block. The instruction count is no lower than PLAIN's; what ADX changes is that the two
// chains advance together, limb by limb, on separate flags, which only a measurement on real
// hardware can price.
.macro MONT_MUL name, adx
.global \name
.type \name, @function
\name:
	push rbx
	push rbp
	push r12
	push r13
	push r14
	sub rsp, 48
	mov [rsp], rdi
	mov rax, [r8]
	mov [rsp+24], rax
	mov [rsp+8], rdx
	mov rax, [r8+8]
	mov [rsp+16], rax
	mov r9, [r8+16]
	lea rsi, [rsi+rax*8]
	lea rcx, [rcx+rax*8]
	lea r9, [r9+rax*8]
	neg rax
	shl rax, 3
	mov [rsp+32], rax
	// t = 0, n+1 words.
	xor r11d, r11d
	mov [r9], r11
	mov r10, rax
1:	mov [r9+r10], r11
	add r10, 8
	jnz 1b
	// One row per limb of y.
2:	mov rdi, [rsp+8]
	mov rdx, [rdi]
	add rdi, 8
	mov [rsp+8], rdi
	// Pass A: t += x*y[i]; the carry word is in r8.
	mov r10, [rsp+32]
	xor r8d, r8d
	test r10, 24
	jz 4f
3:	mulx rbx, rax, [rsi+r10]
	add rax, r8
	adc rbx, 0
	add rax, [r9+r10]
	adc rbx, 0
	mov [r9+r10], rax
	mov r8, rbx
	add r10, 8
	test r10, 24
	jnz 3b
4:	test r10, r10
	jz 6f
5:	BLOCK \adx, rsi, 0, 0
	add r10, 32
	jnz 5b
	// (r11, t[n]) = t[n] + carry.
6:	xor r11d, r11d
	add [r9], r8
	adc r11, 0
	// Pass B: mm = t[0] * (-m^-1); t = (t + mm*m) / 2^64. Limb 0 sums to 0 mod 2^64, so it only
	// leaves a carry; for n >= 4 the first block does it with its first store left out, for n < 4
	// limb 0 is done alone (the high word, plus one unless t[0] is 0).
	mov r10, [rsp+32]
	mov rdx, [r9+r10]
	imul rdx, [rsp+24]
	cmp r10, -32
	jg 13f
	xor r8d, r8d
	BLOCK \adx, rcx, -8, 1
	add r10, 32
	jmp 14f
13:	mulx r8, rax, [rcx+r10]
	add rax, [r9+r10]
	adc r8, 0
	add r10, 8
14:	test r10, 24
	jz 8f
7:	mulx rbx, rax, [rcx+r10]
	add rax, r8
	adc rbx, 0
	add rax, [r9+r10]
	adc rbx, 0
	mov [r9+r10-8], rax
	mov r8, rbx
	add r10, 8
	test r10, 24
	jnz 7b
8:	test r10, r10
	jz 10f
9:	BLOCK \adx, rcx, -8, 0
	add r10, 32
	jnz 9b
	// t[n-1] = t[n] + carry; t[n] = r11 + the carry out of that.
10:	mov rax, [r9]
	add rax, r8
	mov [r9-8], rax
	adc r11, 0
	mov [r9], r11
	dec qword ptr [rsp+16]
	jnz 2b
	// z = t - m, then z = t again when that borrowed and t has no top word. INC keeps CF, so the
	// SBB chain runs through the loop; the index counts words from -n up to 0.
	mov rdi, [rsp]
	mov r10, [rsp+32]
	sar r10, 3
	mov rax, r10
	neg rax
	lea rdi, [rdi+rax*8]
	xor eax, eax
11:	mov rax, [r9+r10*8]
	sbb rax, [rcx+r10*8]
	mov [rdi+r10*8], rax
	inc r10
	jnz 11b
	sbb rax, rax
	mov rbx, [r9]
	dec rbx
	and rax, rbx
	mov r10, [rsp+32]
	sar r10, 3
12:	mov rbx, [r9+r10*8]
	mov rbp, [rdi+r10*8]
	xor rbx, rbp
	and rbx, rax
	xor rbx, rbp
	mov [rdi+r10*8], rbx
	inc r10
	jnz 12b
	add rsp, 48
	pop r14
	pop r13
	pop r12
	pop rbp
	pop rbx
	ret
.size \name, .-\name
.endm

MONT_MUL mont_mul, 0
MONT_MUL mont_mul_adx, 1
