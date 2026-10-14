package main

// Go twin of toolchain/tests/v2/mmap.tin: the same mappings and advice with syscall.Mmap, printing
// the same lines. Run with `go run ./bench/ref/mmap`.

import (
	"fmt"
	"os"
	"runtime"
	"strings"
	"syscall"
	"unsafe"
)

const golden = "/tmp/tin-test-mmap"

var d string

func named(err error) string {
	return strings.ReplaceAll(err.Error(), d, golden)
}

func madvise(b []byte, advice int) error {
	if len(b) == 0 {
		return nil
	}
	addr := uintptr(unsafe.Pointer(&b[0]))
	if runtime.GOOS == "linux" {
		nr := uintptr(28)
		if runtime.GOARCH == "arm64" {
			nr = 233
		}
		_, _, e := syscall.Syscall(nr, addr, uintptr(len(b)), uintptr(advice))
		if e != 0 {
			return e
		}
		return nil
	}
	_, _, e := syscall.Syscall(syscall.SYS_MADVISE, addr, uintptr(len(b)), uintptr(advice))
	if e != 0 {
		return e
	}
	return nil
}

func msync(b []byte, flags int) error {
	if len(b) == 0 {
		return nil
	}
	addr := uintptr(unsafe.Pointer(&b[0]))
	if runtime.GOOS == "linux" {
		nr := uintptr(26)
		if runtime.GOARCH == "arm64" {
			nr = 227
		}
		_, _, e := syscall.Syscall(nr, addr, uintptr(len(b)), uintptr(flags))
		if e != 0 {
			return e
		}
		return nil
	}
	_, _, e := syscall.Syscall(syscall.SYS_MSYNC, addr, uintptr(len(b)), uintptr(flags))
	if e != 0 {
		return e
	}
	return nil
}

func mprotect(b []byte, prot int) error {
	if len(b) == 0 {
		return nil
	}
	return syscall.Mprotect(b, prot)
}

func mapAnon(n, prot int, populate bool) ([]byte, error) {
	flags := syscall.MAP_PRIVATE | syscall.MAP_ANON
	if populate && runtime.GOOS == "linux" {
		flags |= 0x8000 // MAP_POPULATE
	}
	return syscall.Mmap(-1, 0, n, prot, flags)
}

func main() {
	d = fmt.Sprintf("/tmp/tin-test-mmap-%d", os.Getpid())
	os.RemoveAll(d)
	if err := os.MkdirAll(d, 0o755); err != nil {
		fmt.Println("mkdir:", named(err))
		return
	}
	page := os.Getpagesize()
	fmt.Println("page size is a power of two:", page > 0 && page&(page-1) == 0)

	r, err := mapAnon(4*page, syscall.PROT_READ|syscall.PROT_WRITE, false)
	if err != nil {
		fmt.Println("map anon:", named(err))
		return
	}
	fmt.Println("anon len is 4 pages:", len(r) == 4*page)
	fmt.Println("anon is page aligned:", uintptr(unsafe.Pointer(&r[0]))%uintptr(page) == 0)
	fmt.Println("bytes length matches:", len(r) == 4*page)
	r[0] = 65
	r[len(r)-1] = 90
	fmt.Println("write and read back:", r[0] == 65 && r[len(r)-1] == 90)

	// append on a mapping with cap == len copies into a new array.
	grown := append(r, 7)
	fmt.Println("append copies into the pool:", len(grown) == 4*page+1 && len(r) == 4*page)
	fmt.Println("mapping untouched by append:", r[0] == 65 && r[len(r)-1] == 90)

	rp, err := mapAnon(page, syscall.PROT_READ|syscall.PROT_WRITE, true)
	if err != nil {
		fmt.Println("map anon populate:", named(err))
		return
	}
	fmt.Println("populate len is a page:", len(rp) == page)
	rp[0] = 1
	fmt.Println("populate read:", rp[0])

	for _, a := range []int{3, 2, 1, 0, 4} {
		if e := madvise(r, a); e != nil {
			fmt.Println("advise:", named(e))
		}
	}
	fmt.Println("advise: ok")
	if runtime.GOOS == "linux" {
		if e := madvise(r, 14); e != nil {
			fmt.Println("hugepage:", named(e))
		}
	}
	fmt.Println("hugepage: ok")

	if e := mprotect(r, syscall.PROT_READ); e != nil {
		fmt.Println("protect:", named(e))
	}
	if e := mprotect(r, syscall.PROT_READ|syscall.PROT_WRITE); e != nil {
		fmt.Println("protect:", named(e))
	}
	r[0] = 9
	fmt.Println("protect: ok, write after restoring:", r[0])

	path := d + "/map"
	if err := os.WriteFile(path, []byte("0123456789abcdef"), 0o644); err != nil {
		fmt.Println("write file:", named(err))
		return
	}
	f, err := os.OpenFile(path, os.O_RDWR, 0)
	if err != nil {
		fmt.Println("open:", named(err))
		return
	}
	m, err := syscall.Mmap(int(f.Fd()), 0, page, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_SHARED)
	if err != nil {
		fmt.Println("map file:", named(err))
		return
	}
	fmt.Println("file mapping first bytes:", string(m[0:4]))
	m[0] = 88
	buf := make([]byte, 4)
	f.ReadAt(buf, 0)
	fmt.Println("file sees the mapping write:", string(buf))
	f.WriteAt([]byte("YZ"), 1)
	fmt.Println("mapping sees the file write:", string(m[0:4]))
	if e := msync(m, syscall.MS_SYNC); e != nil {
		fmt.Println("msync:", named(e))
	}
	if e := msync(m, syscall.MS_ASYNC); e != nil {
		fmt.Println("msync async:", named(e))
	}
	fmt.Println("msync: ok")

	p, err := syscall.Mmap(int(f.Fd()), 0, page, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_PRIVATE)
	if err != nil {
		fmt.Println("map file private:", named(err))
		return
	}
	p[0] = 81
	f.ReadAt(buf, 0)
	fmt.Println("private write not in file:", string(buf))

	syscall.Munmap(p)
	syscall.Munmap(m)
	syscall.Munmap(r)
	syscall.Munmap(rp)
	f.Close()
	fmt.Println("unmap: ok")
	os.RemoveAll(d)
}
