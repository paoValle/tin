package main

import "fmt"

// Array of structs: a million particles stored inline, moved 50 times.
type Vec struct {
	x float64
	y float64
}

type Particle struct {
	pos Vec
	vel Vec
}

func main() {
	n := 1000000
	ps := make([]Particle, n)
	for i := 0; i < n; i++ {
		ps[i] = Particle{pos: Vec{x: float64(i), y: 0.0}, vel: Vec{x: 1.0, y: float64(i % 7)}}
	}
	for step := 0; step < 50; step++ {
		for i := 0; i < n; i++ {
			ps[i].pos.x += ps[i].vel.x
			ps[i].pos.y += ps[i].vel.y
		}
	}
	sx, sy := 0.0, 0.0
	for _, p := range ps {
		sx += p.pos.x
		sy += p.pos.y
	}
	fmt.Println(sx, sy)
}
