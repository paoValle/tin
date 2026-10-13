package main

// Go twin of toolchain/tests/v2/quarry_file.tin: the same operations with os.File and the same
// syscalls, printing the same lines. Run with `go run ./bench/ref/quarry_file`.

import (
	"fmt"
	"io"
	"os"
	"runtime"
	"strings"
	"syscall"
	"unsafe"
)

// golden is how the lines name this run's directory.
const golden = "/tmp/tin-test-quarry-file"

var (
	d    string
	path string
)

func named(err error) string {
	return strings.ReplaceAll(err.Error(), d, golden)
}

func wprint(f *os.File, label, s string, off int64) {
	n, err := f.WriteAt([]byte(s), off)
	if err != nil {
		fmt.Println(label, named(err))
		return
	}
	fmt.Println(label, n)
}

func rprint(f *os.File, label string, n int64, off int64) {
	buf := make([]byte, n)
	k, err := f.ReadAt(buf, off)
	if err != nil && err != io.EOF {
		fmt.Println(label, named(err))
		return
	}
	fmt.Println(label, k, string(buf))
}

func call(label string, err error) {
	if err != nil {
		fmt.Println(label, named(err))
		return
	}
	fmt.Println(label, "ok")
}

// fallocate reserves space without changing the size: fallocate(2) on Linux (mode 0), fcntl
// F_PREALLOCATE with F_ALLOCATEALL|F_PEOFPOSMODE on macOS.
func fallocate(fd int, off, n int64) error {
	if runtime.GOOS == "linux" {
		nr := uintptr(285)
		if runtime.GOARCH == "arm64" {
			nr = 47
		}
		_, _, e := syscall.Syscall6(nr, uintptr(fd), 0, uintptr(off), uintptr(n), 0, 0)
		if e != 0 {
			return e
		}
		return nil
	}
	type fstore struct {
		Flags      uint32
		Posmode    int32
		Offset     int64
		Length     int64
		Bytesalloc int64
	}
	fs := fstore{Flags: 4, Posmode: 3, Offset: off, Length: n}
	_, _, e := syscall.Syscall(syscall.SYS_FCNTL, uintptr(fd), 42, uintptr(unsafe.Pointer(&fs)))
	if e != 0 {
		return e
	}
	return nil
}

func readahead(fd int, off, n int64) error {
	if runtime.GOOS == "linux" {
		nr := uintptr(187)
		if runtime.GOARCH == "arm64" {
			nr = 213
		}
		_, _, e := syscall.Syscall(nr, uintptr(fd), uintptr(off), uintptr(n))
		if e != 0 {
			return e
		}
		return nil
	}
	type radvisory struct {
		Offset int64
		Count  int32
		_      int32
	}
	ra := radvisory{Offset: off, Count: int32(n)}
	_, _, e := syscall.Syscall(syscall.SYS_FCNTL, uintptr(fd), 44, uintptr(unsafe.Pointer(&ra)))
	if e != 0 {
		return e
	}
	return nil
}

func advise(fd int, off, n int64, a int) {
	if runtime.GOOS != "linux" {
		return
	}
	nr := uintptr(221)
	if runtime.GOARCH == "arm64" {
		nr = 223
	}
	syscall.Syscall6(nr, uintptr(fd), uintptr(off), uintptr(n), uintptr(a), 0, 0)
}

func syncRange(f *os.File, off, n int64, flags int) error {
	if runtime.GOOS == "linux" {
		nr := uintptr(277)
		if runtime.GOARCH == "arm64" {
			nr = 84
		}
		_, _, e := syscall.Syscall6(nr, f.Fd(), uintptr(off), uintptr(n), uintptr(flags), 0, 0)
		if e != 0 {
			return e
		}
		return nil
	}
	return f.Sync()
}

func setNoCache(fd int, on bool) error {
	if runtime.GOOS == "linux" {
		flags, _, e := syscall.Syscall(syscall.SYS_FCNTL, uintptr(fd), 3, 0)
		if e != 0 {
			return e
		}
		direct := uintptr(0x4000)
		if runtime.GOARCH == "arm64" {
			direct = 0x10000
		}
		want := flags &^ direct
		if on {
			want = flags | direct
		}
		_, _, e = syscall.Syscall(syscall.SYS_FCNTL, uintptr(fd), 4, want)
		if e != 0 {
			return e
		}
		return nil
	}
	v := uintptr(0)
	if on {
		v = 1
	}
	_, _, e := syscall.Syscall(syscall.SYS_FCNTL, uintptr(fd), 48, v)
	if e != 0 {
		return e
	}
	return nil
}

func dataSync(f *os.File) error {
	if runtime.GOOS == "linux" {
		nr := uintptr(75)
		if runtime.GOARCH == "arm64" {
			nr = 83
		}
		_, _, e := syscall.Syscall(nr, f.Fd(), 0, 0)
		if e != 0 {
			return e
		}
		return nil
	}
	return f.Sync()
}

func syncDir(p string) error {
	dir, err := os.Open(p)
	if err != nil {
		return err
	}
	defer dir.Close()
	return dir.Sync()
}

func main() {
	d = fmt.Sprintf("/tmp/tin-test-quarry-file-%d", os.Getpid())
	os.RemoveAll(d)
	if err := os.MkdirAll(d, 0o755); err != nil {
		fmt.Println("mkdir:", named(err))
		return
	}
	path = d + "/data"

	f, err := os.OpenFile(path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0o644)
	if err != nil {
		fmt.Println("open:", named(err))
		return
	}

	wprint(f, "write 12 at 0:", "hello, world", 0)
	rprint(f, "pread 5 at 7:", 5, 7)
	wprint(f, "write 2 at 5:", "XX", 5)
	rprint(f, "read 12 at 0:", 12, 0)
	past := make([]byte, 12)
	n4, err := f.ReadAt(past, 100)
	if err != nil && err != io.EOF {
		fmt.Println("pread past end:", named(err))
		return
	}
	fmt.Println("pread past end:", n4)

	wprint(f, "write 3 at 20:", "end", 20)
	fi, err := f.Stat()
	if err != nil {
		fmt.Println("size:", named(err))
		return
	}
	fmt.Println("size after hole:", fi.Size())
	hole := make([]byte, 23)
	f.ReadAt(hole, 0)
	zeros := true
	for i := 13; i < 20; i++ {
		if hole[i] != 0 {
			zeros = false
		}
	}
	fmt.Println("hole is zeros:", zeros)

	call("truncate 10:", f.Truncate(10))
	fi, _ = f.Stat()
	fmt.Println("size after truncate 10:", fi.Size())
	call("truncate 0:", f.Truncate(0))
	fi, _ = f.Stat()
	fmt.Println("size after truncate 0:", fi.Size())

	call("preallocate 8kb at 0:", fallocate(int(f.Fd()), 0, 8192))
	wprint(f, "write 4 at 8188:", "tail", 8188)
	rprint(f, "read 4 at 8188:", 4, 8188)
	fi, _ = f.Stat()
	fmt.Println("size after preallocate+write:", fi.Size())

	call("truncate 0:", f.Truncate(0))
	wprint(f, "vectored source:", "abcdefg", 0)
	// The Tin ReadAtV fills every buffer (a short preadv continues into the next), which is a
	// sequential read of the buffers.
	ab := make([]byte, 3)
	bb := make([]byte, 4)
	bufs := [][]byte{ab, bb}
	total := int64(0)
	for _, b := range bufs {
		k, e := f.ReadAt(b, total)
		if e != nil && e != io.EOF {
			fmt.Println("preadv:", named(e))
			return
		}
		total += int64(k)
	}
	fmt.Println("preadv:", total, string(bufs[0]), string(bufs[1]))
	call("truncate 0:", f.Truncate(0))
	pv := int64(0)
	for _, s := range []string{"12", "34", "56"} {
		n, e := f.WriteAt([]byte(s), pv)
		if e != nil {
			fmt.Println("pwritev:", named(e))
			return
		}
		pv += int64(n)
	}
	fmt.Println("pwritev:", pv)
	rprint(f, "read 6 at 0:", 6, 0)

	call("sync:", f.Sync())
	call("datasync:", dataSync(f))
	call("readahead:", readahead(int(f.Fd()), 0, 6))
	advise(int(f.Fd()), 0, 6, 2)
	advise(int(f.Fd()), 0, 6, 3)
	advise(int(f.Fd()), 0, 6, 4)
	advise(int(f.Fd()), 0, 6, 1)
	advise(int(f.Fd()), 0, 6, 0)
	fmt.Println("advise: ok")
	call("sync range:", syncRange(f, 0, 6, 0))
	call("no cache off:", setNoCache(int(f.Fd()), false))
	call("no cache on:", setNoCache(int(f.Fd()), true))
	call("no cache off again:", setNoCache(int(f.Fd()), false))

	err = syscall.Flock(int(f.Fd()), syscall.LOCK_EX|syscall.LOCK_NB)
	fmt.Println("flock first:", err == nil)
	g, err := os.Open(path)
	if err != nil {
		fmt.Println("open second:", named(err))
		return
	}
	err = syscall.Flock(int(g.Fd()), syscall.LOCK_EX|syscall.LOCK_NB)
	fmt.Println("flock while held:", err == nil)
	call("unlock:", syscall.Flock(int(f.Fd()), syscall.LOCK_UN))
	err = syscall.Flock(int(g.Fd()), syscall.LOCK_EX|syscall.LOCK_NB)
	fmt.Println("flock after unlock:", err == nil)
	g.Close()

	call("close:", f.Close())
	if f.Close() != nil {
		fmt.Println("close twice: close " + named2(path) + ": file is closed")
	} else {
		fmt.Println("close twice: ok")
	}
	if _, err := f.ReadAt(make([]byte, 4), 0); err != nil {
		fmt.Println("read after close: pread " + named2(path) + ": file is closed")
	} else {
		fmt.Println("read after close: ok")
	}

	call("sync dir:", syncDir(d))
	os.RemoveAll(d)
}

// named2 names path as the golden output does.
func named2(p string) string {
	return strings.ReplaceAll(p, d, golden)
}
