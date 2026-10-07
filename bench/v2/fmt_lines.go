package main

import "fmt"

func main() {
	names := []string{"alpha", "be", "gamma!", "d"}
	n := 0
	for i := 0; i < 1000000; i++ {
		s := fmt.Sprintf("%d:%s:%.2f", i, names[i&3], float64(i)*0.5)
		n += len(s)
		t := fmt.Sprintf("row %d %s", i, names[i&3])
		n += len(t)
	}
	fmt.Println(n)
}
