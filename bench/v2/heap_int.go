package main

import (
	"container/heap"
	"fmt"
)

// int64Heap is a min-heap of int64 values for container/heap.
type int64Heap struct {
	xs []int64
}

func (h int64Heap) Len() int           { return len(h.xs) }
func (h int64Heap) Less(i, j int) bool { return h.xs[i] < h.xs[j] }
func (h int64Heap) Swap(i, j int)      { h.xs[i], h.xs[j] = h.xs[j], h.xs[i] }
func (h *int64Heap) Push(x any)        { h.xs = append(h.xs, x.(int64)) }
func (h *int64Heap) Pop() any {
	n := len(h.xs)
	x := h.xs[n-1]
	h.xs = h.xs[:n-1]
	return x
}

func main() {
	const n = 2000000
	h := &int64Heap{xs: make([]int64, 0, n)}
	k := int64(12345)
	for i := 0; i < n; i++ {
		k = k*6364136223846793005 + 1442695040888963407
		heap.Push(h, k)
	}
	var sum, count int64
	for h.Len() > 0 {
		v := heap.Pop(h).(int64)
		sum = sum*1000003 + v
		count++
	}
	fmt.Println("popped", count, sum)
}
