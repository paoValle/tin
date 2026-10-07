// Command lasso reads pattern/input pairs on stdin (hex-encoded, one pair per line) and prints,
// for each, what Go's regexp says: whether it matches, the leftmost match, the submatch offsets
// and every match. tools/ci/fixtures/lasso.tin prints the same lines and
// tools/ci/lasso_check.py compares them (#571).
package main

import (
	"bufio"
	"encoding/hex"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(make([]byte, 1<<20), 1<<20)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for line := 1; in.Scan(); line++ {
		fields := strings.Split(in.Text(), "\t")
		if len(fields) != 2 && len(fields) != 3 {
			fmt.Fprintf(os.Stderr, "line %d: want pattern\\tinput[\\tn]\n", line)
			os.Exit(1)
		}
		n := -1
		if len(fields) == 3 {
			v, err := strconv.Atoi(fields[2])
			if err != nil {
				fmt.Fprintf(os.Stderr, "line %d: %v\n", line, err)
				os.Exit(1)
			}
			n = v
		}
		pattern, err := hex.DecodeString(fields[0])
		if err != nil {
			fmt.Fprintf(os.Stderr, "line %d: %v\n", line, err)
			os.Exit(1)
		}
		input, err := hex.DecodeString(fields[1])
		if err != nil {
			fmt.Fprintf(os.Stderr, "line %d: %v\n", line, err)
			os.Exit(1)
		}
		re, err := regexp.Compile(string(pattern))
		if err != nil {
			// The check compares the two sides' lines; the fault text is each side's own.
			fmt.Fprintln(out, "compile")
			continue
		}
		s := string(input)
		fmt.Fprintf(out, "match %t", re.MatchString(s))
		loc := re.FindStringIndex(s)
		if loc == nil {
			fmt.Fprintf(out, " find -1 -1")
		} else {
			fmt.Fprintf(out, " find %d %d", loc[0], loc[1])
		}
		sub := re.FindStringSubmatchIndex(s)
		fmt.Fprintf(out, " subs")
		for _, v := range sub {
			fmt.Fprintf(out, " %d", v)
		}
		fmt.Fprintf(out, " all")
		for _, m := range re.FindAllStringIndex(s, n) {
			fmt.Fprintf(out, " %d %d", m[0], m[1])
		}
		fmt.Fprintf(out, " allsubs")
		for _, m := range re.FindAllStringSubmatchIndex(s, n) {
			for _, v := range m {
				fmt.Fprintf(out, " %d", v)
			}
		}
		fmt.Fprintln(out)
	}
	if err := in.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "read:", err)
		os.Exit(1)
	}
}
