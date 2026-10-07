package main

import "fmt"

// find returns the index of v in xs and whether it was found.
func find(xs []int64, v int64) (int64, bool) {
	for i := int64(0); i < int64(len(xs)); i++ {
		if xs[i] == v {
			return i, true
		}
	}
	return 0, false
}

// opt is an optional int64 stored inline, as Tin's ?i64 is.
type opt struct {
	v  int64
	ok bool
}

func main() {
	xs := make([]int64, 64)
	for i := int64(0); i < int64(len(xs)); i++ {
		xs[i] = (i * 37) % 101
	}
	total := int64(0)
	for round := int64(0); round < 2000000; round++ {
		if r, ok := find(xs, round%101); ok {
			total += r
		} else {
			total -= 1
		}
	}
	opts := make([]opt, 0, 1000000)
	for i := int64(0); i < 1000000; i++ {
		if i%3 == 0 {
			opts = append(opts, opt{})
		} else {
			opts = append(opts, opt{v: i, ok: true})
		}
	}
	sum := int64(0)
	for rep := int64(0); rep < 20; rep++ {
		for _, o := range opts {
			if o.ok {
				sum += o.v
			} else {
				sum += rep
			}
		}
	}
	fmt.Println(total, sum)
}
