package main

import (
	"fmt"
	"regexp"
)

// The regular-expression benchmark, Go side: bench/v2/regex.tin does the same work and must
// print the same line.

func line(i int64) string {
	ip := fmt.Sprintf("10.%d.%d.%d", i%256, i*7%256, i*13%256)
	path := fmt.Sprintf("/a/%d/b.html", i%50)
	return fmt.Sprintf("%s - - [10/Oct/2024:13:55:%02d +0000] \"GET %s HTTP/1.1\" %d %d", ip, i%60, path, 200+i%5, 100+i*37%9000)
}

func main() {
	full := regexp.MustCompile(`^(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>[^\]]+)\] "(?P<method>[A-Z]+) (?P<path>[^ ]+) HTTP/(?P<ver>\d\.\d)" (?P<status>\d{3}) (?P<size>\d+)$`)
	ipre := regexp.MustCompile(`\d+\.\d+\.\d+\.\d+`)
	req := regexp.MustCompile(`"([A-Z]+) ([^ ]+) HTTP/\d\.\d" (\d{3}) (\d+)`)
	word := regexp.MustCompile(`[a-z]+`)
	var h, fields int64
	for i := int64(0); i < 1000; i++ {
		s := line(i)
		for _, p := range full.FindStringSubmatch(s) {
			fields++
			for k := 0; k < len(p); k++ {
				h = h*1000003 + int64(p[k])
			}
		}
		for _, m := range ipre.FindAllStringIndex(s, -1) {
			h = h*1000003 + int64(m[1]-m[0])
		}
		for _, p := range req.FindStringSubmatch(s) {
			h = h*1000003 + int64(len(p))
		}
		for _, m := range word.FindAllStringIndex(s, -1) {
			h = h*1000003 + int64(m[0])
		}
	}
	fmt.Println("fields", fields, "hash", h)
}
