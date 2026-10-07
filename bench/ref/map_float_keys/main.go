// Go twin of toolchain/tests/v2/map_float_keys.tin (#643): its output is that test's .out.
package main

import "fmt"

type P struct {
	x float64
	n int64
}

func main() {
	z := 0.0
	nz := -z
	fmt.Println(z == nz, nz)
	m := map[float64]string{}
	m[nz] = "neg"
	m[z] = "pos"
	fmt.Println(len(m), m[0.0], m[nz])
	nan := z / z
	m[nan] = "nan"
	fmt.Println(nan == nan, len(m), m[nan])
	m[nan] = "nan2"
	fmt.Println(len(m))
	v, ok := m[nan]
	fmt.Println(v == "", ok)
	delete(m, nan)
	delete(m, nz)
	fmt.Println(len(m))
	sm := map[P]int64{}
	sm[P{x: -z, n: 1}] = 1
	sm[P{x: 0.0, n: 1}] = 2
	sm[P{x: nan, n: 1}] = 3
	sm[P{x: nan, n: 1}] = 4
	w, found := sm[P{x: nan, n: 1}]
	fmt.Println(len(sm), sm[P{x: 0.0, n: 1}], w, found)
	cnt := int64(0)
	for _, val := range sm {
		cnt += val
	}
	fmt.Println(cnt)
	big := map[float64]int64{}
	for i := int64(0); i < 10000; i++ {
		big[float64(i)*-1.0] = i
	}
	fmt.Println(len(big), big[0.0], big[-z], big[-9999.0])
}
