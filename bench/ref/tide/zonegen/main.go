// Command zonegen writes the IANA zone corpus (zones.in) and the Go expectations (expected.txt)
// for tide's zone work (#573): sampled instants, every transition from 1970 to 2040 with its
// neighbours, and wall times around each transition for DateIn. tools/ci/helpers_check.py runs
// it next to tools/ci/fixtures/tide_zones.tin and compares the two outputs.
package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sort"
	"time"
)

var zoneNames = []string{
	"UTC",
	"America/New_York",
	"Europe/London",
	"Europe/Paris",
	"Asia/Kolkata",
	"Asia/Kathmandu",
	"Australia/Lord_Howe",
	"Pacific/Chatham",
	"America/Sao_Paulo",
	"Africa/Casablanca",
	"Etc/GMT+5",
}

const (
	startSec = 0
	endSec   = 2240611200 // 2041-01-01
)

// findTransition returns the first second at or after lo where the offset differs from the one
// at lo-1 (lo..hi bracketed by the caller).
func findTransition(loc *time.Location, lo, hi int64) int64 {
	_, want := time.Unix(lo-1, 0).In(loc).Zone()
	for lo < hi {
		mid := (lo + hi) / 2
		_, off := time.Unix(mid, 0).In(loc).Zone()
		if off == want {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func transitions(loc *time.Location) []int64 {
	var out []int64
	prev := int64(1) << 62
	day := int64(0)
	for sec := int64(startSec); sec <= endSec; sec += 86400 {
		_, offw := time.Unix(sec, 0).In(loc).Zone()
		off := int64(offw)
		if off != prev {
			if prev != int64(1)<<62 && day > 0 {
				t := findTransition(loc, day*86400-86400, day*86400)
				out = append(out, t)
			}
			prev = off
		}
		day++
	}
	return out
}

var exp *os.File

// expF writes one expected line.
func expF(format string, args ...any) {
	fmt.Fprintf(exp, format, args...)
}

func main() {
	if len(os.Args) != 2 {
		log.Fatal("usage: tide DIR (writes DIR/zones.in and DIR/expected.txt)")
	}
	var err error
	in, err := os.Create(filepath.Join(os.Args[1], "zones.in"))
	if err != nil {
		log.Fatal(err)
	}
	defer in.Close()
	exp, err = os.Create(filepath.Join(os.Args[1], "expected.txt"))
	if err != nil {
		log.Fatal(err)
	}
	defer exp.Close()
	for _, name := range zoneNames {
		loc, err := time.LoadLocation(name)
		if err != nil {
			fmt.Fprintf(in, "ZONE %s\n", name)
			expF("zone %s fault\n", name)
			continue
		}
		fmt.Fprintf(in, "ZONE %s\n", name)
		expF("zone %s\n", name)
		seen := map[int64]bool{}
		var instants []int64
		add := func(sec int64) {
			if sec < startSec || sec >= endSec || seen[sec] {
				return
			}
			seen[sec] = true
			instants = append(instants, sec)
		}
		for sec := int64(startSec); sec < endSec; sec += 3 * 86400 {
			add(sec)
		}
		trs := transitions(loc)
		for _, t := range trs {
			for _, d := range []int64{-7200, -3600, -1800, -1, 0, 1, 1800, 3600, 7200} {
				add(t + d)
			}
		}
		sort.Slice(instants, func(i, j int) bool { return instants[i] < instants[j] })
		for _, sec := range instants {
			fmt.Fprintf(in, "IN %d\n", sec)
			t := time.Unix(sec, 0).In(loc)
			abbr, off := t.Zone()
			expF("in %s %d %d %d %d %d %d %d %d %s\n", name, sec,
				t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second(), off, abbr)
			// The same wall time through Date, for DateIn.
			d := time.Date(t.Year(), t.Month(), t.Day(), t.Hour(), t.Minute(), t.Second(), t.Nanosecond(), loc)
			fmt.Fprintf(in, "DATE %d %d %d %d %d %d 0\n", t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second())
			expF("date %s %d %d %d %d %d %d 0 %d\n", name, t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second(), d.UnixNano())
		}
		for _, tr := range trs {
			for _, d := range []int64{-7200, -3600, -1800, -900, -1, 0, 1, 900, 1800, 3600, 7200} {
				t := time.Unix(tr+d, 0).In(loc)
				fmt.Fprintf(in, "DATE %d %d %d %d %d %d 0\n", t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second())
				d2 := time.Date(t.Year(), t.Month(), t.Day(), t.Hour(), t.Minute(), t.Second(), 0, loc)
				expF("date %s %d %d %d %d %d %d 0 %d\n", name, t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second(), d2.UnixNano())
			}
		}
	}
}
