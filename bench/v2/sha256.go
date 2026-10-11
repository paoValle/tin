package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// SHA-256 of 100 MB.
func main() {
	b := make([]byte, 100_000_000)
	for i := range b {
		b[i] = byte(i * 31)
	}
	s := sha256.Sum256(b)
	fmt.Println(hex.EncodeToString(s[:]))
}
