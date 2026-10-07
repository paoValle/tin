package main

// The abacus corpus, Go side: the same operands and operations as tools/ci/fixtures/abacus.tin,
// against math/big, printing a hash per operation (or every case with "dump"). Equal hashes mean
// equal results. ABACUS_N is the number of random operand pairs (default 100000).

import (
	"fmt"
	"math"
	"math/big"
	"os"
	"strconv"
)

type rng struct{ s uint64 }

func (r *rng) next() uint64 {
	r.s ^= r.s >> 12
	r.s ^= r.s << 25
	r.s ^= r.s >> 27
	return r.s * 2685821657736338717
}

// sizes are the bit lengths the operands take: the edges, the limb boundaries and the powers of
// two around them.
var sizes = []int{0, 1, 2, 63, 64, 65, 127, 128, 129, 255, 256, 257, 512, 1024, 2048, 4096}

// edge values as magnitudes with signs.
var edges = []struct {
	mag  uint64
	neg  bool
	bits int
}{
	{0, false, 0}, {1, false, 1}, {1, true, 1}, {2, false, 2}, {2, true, 2},
	{1 << 62, false, 63}, {1 << 62, true, 63}, {1<<63 - 1, false, 63}, {1<<63 - 1, true, 63},
	{1 << 63, false, 64}, {1 << 63, true, 64}, {1<<64 - 1, false, 64}, {1<<64 - 1, true, 64},
}

func randInt(r *rng, bits int) *big.Int {
	if bits == 0 {
		return new(big.Int)
	}
	nbytes := (bits + 7) / 8
	buf := make([]byte, nbytes)
	for i := range buf {
		buf[i] = byte(r.next() >> 24)
	}
	// Trim to exactly `bits` bits.
	extra := nbytes*8 - bits
	if extra > 0 {
		buf[0] &= 0xff >> extra
	}
	z := new(big.Int).SetBytes(buf)
	if r.next()&1 == 1 {
		z.Neg(z)
	}
	return z
}

func operand(r *rng, i int) *big.Int {
	if i < len(edges) {
		z := new(big.Int).SetUint64(edges[i].mag)
		if edges[i].neg {
			z.Neg(z)
		}
		return z
	}
	bits := sizes[int(r.next()%uint64(len(sizes)))]
	if r.next()&3 == 0 {
		bits = int(r.next() % 4097)
	}
	return randInt(r, bits)
}

func hexInt(z *big.Int) string {
	if z.Sign() == 0 {
		return "0"
	}
	if z.Sign() < 0 {
		return "-" + new(big.Int).Abs(z).Text(16)
	}
	return z.Text(16)
}

type hasher struct{ h uint64 }

func (h *hasher) add(s string) {
	for i := 0; i < len(s); i++ {
		h.h ^= uint64(s[i])
		h.h *= 1099511628211
	}
}

func main() {
	n := 100000
	if s := os.Getenv("ABACUS_N"); s != "" {
		if v, err := strconv.Atoi(s); err == nil && v > 0 {
			n = v
		}
	}
	dump := len(os.Args) > 1 && os.Args[1] == "dump"
	r := &rng{s: 88172645463325252}
	ops := []string{"add", "sub", "mul", "cmp", "text10", "text16", "text36", "bytes", "i64", "u64", "f64"}
	hash := make(map[string]*hasher, len(ops))
	for _, op := range ops {
		hash[op] = &hasher{h: 14695981039346656037}
	}
	for i := 0; i < n; i++ {
		a := operand(r, i)
		b := operand(r, i+7)
		if dump {
			fmt.Printf("operands %d %s %s\n", i, hexInt(a), hexInt(b))
		}
		results := map[string]string{
			"add":    hexInt(new(big.Int).Add(a, b)),
			"sub":    hexInt(new(big.Int).Sub(a, b)),
			"mul":    hexInt(new(big.Int).Mul(a, b)),
			"cmp":    strconv.Itoa(a.Cmp(b)),
			"text10": a.Text(10),
			"text16": a.Text(16),
			"text36": a.Text(36),
			"bytes":  hexInt(new(big.Int).SetBytes(a.Bytes())),
			"i64":    i64Text(a),
			"u64":    u64Text(a),
			"f64":    fmt.Sprintf("%016x", f64Bits(a)),
		}
		for _, op := range ops {
			s := results[op]
			if dump {
				fmt.Printf("%s %d %s\n", op, i, s)
			} else {
				hash[op].add(s)
			}
		}
	}
	if !dump {
		for _, op := range ops {
			fmt.Printf("%s %d %016x\n", op, n, hash[op].h)
		}
	}
}

func i64Text(a *big.Int) string {
	if a.IsInt64() {
		return strconv.FormatInt(a.Int64(), 10) + " true"
	}
	return "0 false"
}

func u64Text(a *big.Int) string {
	if a.IsUint64() {
		return strconv.FormatUint(a.Uint64(), 10) + " true"
	}
	return "0 false"
}

func f64Bits(a *big.Int) uint64 {
	f, _ := new(big.Float).SetInt(a).Float64()
	return math.Float64bits(f)
}
