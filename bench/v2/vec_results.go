package main

import "fmt"

// Small struct results: points of 16 bytes returned by value from the calls a loop makes.
type Pt struct {
	x int64
	y int64
}

func add(a Pt, b Pt) Pt {
	return Pt{x: (a.x + b.x) & 16777215, y: (a.y + b.y) & 16777215}
}

func half(a Pt) Pt {
	return Pt{x: a.x >> 1, y: a.y >> 1}
}

func mix(a Pt) Pt {
	return Pt{x: (a.x*3 + a.y + 1) & 16777215, y: ((a.y * 5) ^ a.x) & 16777215}
}

func main() {
	p := Pt{x: 0, y: 0}
	v := Pt{x: 1, y: 2}
	for i := 0; i < 100000000; i++ {
		p = add(p, half(v))
		v = mix(v)
	}
	fmt.Println(p.x, p.y)
}
