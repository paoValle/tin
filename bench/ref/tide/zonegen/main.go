// Command zonegen writes the IANA zone corpus (zones.in) and the Go expectations (expected.txt)
// for tide's zone work (#573): sampled instants, every transition from 1970 to 2040 with its
// neighbours, and wall times around each transition for DateIn. tools/ci/helpers_check.py runs
// it next to tools/ci/fixtures/tide_zones.tin and compares the two outputs.
package main

import (
	"encoding/hex"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"time"
)

// layoutNames exercise every reference-time chunk; both sides format with these.
var layoutNames = []string{
	"01/02 03:04:05PM '06 -0700",
	"Mon Jan _2 15:04:05 2006",
	"Mon Jan _2 15:04:05 MST 2006",
	"Mon Jan 02 15:04:05 -0700 2006",
	"02 Jan 06 15:04 MST",
	"02 Jan 06 15:04 -0700",
	"Monday, 02-Jan-06 15:04:05 MST",
	"Mon, 02 Jan 2006 15:04:05 MST",
	"Mon, 02 Jan 2006 15:04:05 -0700",
	"2006-01-02T15:04:05Z07:00",
	"2006-01-02T15:04:05.999999999Z07:00",
	"3:04PM",
	"Jan _2 15:04:05",
	"Jan _2 15:04:05.000",
	"Jan _2 15:04:05.000000",
	"Jan _2 15:04:05.000000000",
	"2006-01-02 15:04:05",
	"2006-01-02",
	"15:04:05",
	"__2 002 1 01 Apr April 3 03 PM pm 15 4 04 5 05 06 -07 -0700 -07:00 -070000 -07:00:00 Z07 Z0700 Z07:00 Z070000 Z07:00:00 MST",
	"2006-01-02T15:04:05,000000000Z07:00",
	"2006-01-02T15:04:05.000000000Z07:00",
	"2006-01-02T15:04:05.999999999,07:00",
	"Mon Jan _2 15:04:05.999 -070000 MST",
	"2006-01-02T15:04:05.999999999-07:00:00",
}

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

// parsed renders ParseInLocation's result as an instant or "err".
func parsed(layout, value string, loc *time.Location) string {
	t, err := time.ParseInLocation(layout, value, loc)
	if err != nil {
		return "err"
	}
	// Go wraps UnixNano outside its range; tide faults there, so the twin compares "out".
	sec := t.Unix()
	if sec > 9223372036 || sec < -9223372037 {
		return "out"
	}
	return strconv.FormatInt(t.UnixNano(), 10)
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
	for i, layout := range layoutNames {
		fmt.Fprintf(in, "LAYOUT %d %s\n", i, hex.EncodeToString([]byte(layout)))
	}
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
		formatAt := func(sec int64, nano int64) {
			t := time.Unix(sec, nano).In(loc)
			for i, layout := range layoutNames {
				s := t.Format(layout)
				fmt.Fprintf(in, "FMT %d %d %d\n", sec, nano, i)
				expF("fmt %s %d %d %d %s\n", name, sec, nano, i, s)
				fmt.Fprintf(in, "PARSE %d %d %d\n", sec, nano, i)
				expF("parse %s %d %d %d %s\n", name, sec, nano, i, parsed(layout, s, loc))
				variants := []string{s[:max(0, len(s)-1)], "!" + s, s + "!"}
				for v, bad := range variants {
					fmt.Fprintf(in, "PARSEBAD %d %d %d %d\n", sec, nano, i, v)
					expF("parsebad %s %d %d %d %d %s\n", name, sec, nano, i, v, parsed(layout, bad, loc))
				}
			}
		}
		for k, sec := range instants {
			if k%1000 == 0 {
				formatAt(sec, 0)
			}
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
		for _, sec := range []int64{0, 1735603200, 1740787200, 1743379200, 1745971200, 1751414400, 1759190400, 1762041600, 2222121600} {
			formatAt(sec, 0)
		}
		if len(trs) > 0 {
			bases := []int64{trs[0], trs[len(trs)/2], trs[len(trs)-1], 1759317725}
			for _, base := range bases {
				for _, nano := range []int64{1, 999999999, 123456789} {
					formatAt(base, nano)
				}
			}
		}
		arithBases := []int64{0, 1735603200, 1759190400, 2222121600}
		if len(trs) > 0 {
			arithBases = append(arithBases, trs[0], trs[len(trs)/2], trs[len(trs)-1])
		}
		for _, sec := range arithBases {
			t := time.Unix(sec, 0).In(loc)
			for _, y := range []int{0, 1, -1} {
				for _, mo := range []int{0, 1, -1, 13, -13} {
					for _, d := range []int{0, 1, -1, 28, -28, 31, -31} {
						fmt.Fprintf(in, "ADDDATE %d %d %d %d\n", sec, y, mo, d)
						expF("adddate %s %d %d %d %d %d\n", name, sec, y, mo, d, t.AddDate(y, mo, d).UnixNano())
					}
				}
			}
		}
		truncBases := []int64{0, 1735603200, 1759317725, 2222121600}
		durs := []int64{1, 3, 7, 500, 1000, 1000000, 1500000, 1000000000, 90000000000, 3600000000000, 86400000000000, 604800000000000, 1234567, -5}
		for _, sec := range truncBases {
			t := time.Unix(sec, 0).In(loc)
			for _, d := range durs {
				fmt.Fprintf(in, "TRUNC %d %d\n", sec, d)
				expF("trunc %s %d %d %d\n", name, sec, d, t.Truncate(time.Duration(d)).UnixNano())
				fmt.Fprintf(in, "ROUND %d %d\n", sec, d)
				expF("round %s %d %d %d\n", name, sec, d, t.Round(time.Duration(d)).UnixNano())
			}
		}
		for _, sec := range append(append([]int64{}, arithBases...), truncBases...) {
			t := time.Unix(sec, 0).In(loc)
			iy, iw := t.ISOWeek()
			fmt.Fprintf(in, "ISOWEEK %d\n", sec)
			expF("isoweek %s %d %d %d\n", name, sec, iy, iw)
		}
		for _, tr := range trs {
			formatAt(tr, 0)
			for _, d := range []int64{-7200, -3600, -1800, -900, -1, 0, 1, 900, 1800, 3600, 7200} {
				t := time.Unix(tr+d, 0).In(loc)
				fmt.Fprintf(in, "DATE %d %d %d %d %d %d 0\n", t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second())
				d2 := time.Date(t.Year(), t.Month(), t.Day(), t.Hour(), t.Minute(), t.Second(), 0, loc)
				expF("date %s %d %d %d %d %d %d 0 %d\n", name, t.Year(), int(t.Month()), t.Day(), t.Hour(), t.Minute(), t.Second(), d2.UnixNano())
			}
		}
	}
}
