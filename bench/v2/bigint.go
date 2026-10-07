package main

import (
	"fmt"
	"math/big"
)

func main() {
	f := big.NewInt(1)
	for i := 1; i <= 5000; i++ {
		f.Mul(f, big.NewInt(int64(i)))
	}
	s := f.String()
	digitSum := 0
	for i := 0; i < len(s); i++ {
		digitSum += int(s[i] - '0')
	}
	fmt.Println("factorial", len(s), digitSum)

	m := new(big.Int).Exp(big.NewInt(2), big.NewInt(2048), nil)
	m.Sub(m, big.NewInt(1))
	var h int64
	for i := 0; i < 20; i++ {
		base := new(big.Int).Exp(big.NewInt(3), big.NewInt(int64(500+i)), nil)
		r := new(big.Int).Exp(base, big.NewInt(int64(65537+i)), m)
		t := r.Text(16)
		h = h*1000003 + int64(len(t))
		h = h*1000003 + int64(t[0])
		h = h*1000003 + int64(t[len(t)-1])
	}
	fmt.Println("modpow", h)
}
