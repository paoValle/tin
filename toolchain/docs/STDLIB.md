# Tin standard library

Generated from the comments in `toolchain/std/*/` and `packages/*/` by `tools/gen/gendoc.tin`.

| package | role (Go equivalent) |
|---|---|
| [say](#say) | formatting and printing (fmt) |
| [fault](#fault) | fault chains and standard sentinels (errors) |
| [argo](#argo) | JSON (encoding/json) |
| [io](#io) | streaming shapes (io) |
| [fs](#fs) | file system interfaces and helpers (io/fs) |
| [embed](#embed) | read-only file trees compiled into the image, from a // embed: directive (embed) |
| [anvil](#anvil) | HTTP/1.1 and HTTP/2 server, HTTPS with ServeTLS (net/http) |
| [hearth](#hearth) | cores and threads (runtime) |
| [relay](#relay) | messages between cores (channels) |
| [task](#task) | deadline and cancellation of the running code (context) |
| [wire](#wire) | TCP and HTTP/1.1 and HTTP/2 client (net, net/http) |
| [httptrace](#httptrace) | observable HTTP client phase hooks (net/http/httptrace) |
| [pprof](#pprof) | HTTP profiling route names and runtime profile availability (net/http/pprof) |
| [jar](#jar) | HTTP cookie jar for wire clients (net/http/cookiejar) |
| [dump](#dump) | HTTP request and response dumps (net/http/httputil) |
| [proxy](#proxy) | streaming HTTP reverse proxy (net/http/httputil) |
| [cgi](#cgi) | CGI handler adapter over an anvil handler (net/http/cgi) |
| [cgi/fcgi](#cgi/fcgi) | FastCGI responder over an anvil handler (net/http/fcgi) |
| [assay](#assay) | HTTP test requests, recorders and local test servers (net/http/httptest) |
| [tls](#tls) | TLS 1.3 client and server (crypto/tls) |
| [hpack](#hpack) | HTTP/2 header compression (golang.org/x/net/http2/hpack) |
| [twine](#twine) | strings (strings) |
| [glyph](#glyph) | UTF-8, UTF-16 and Unicode (unicode/utf8, unicode/utf16, unicode) |
| [mint](#mint) | number and string conversion (strconv) |
| [gauge](#gauge) | math (math) |
| [cmplx](#cmplx) | complex numbers and the functions of math/cmplx |
| [bits](#bits) | bit counting and manipulation (math/bits) |
| [link](#link) | URLs and their escaping (net/url) |
| [netip](#netip) | IP addresses, address/port pairs and prefixes as value types (net/netip) |
| [ore](#ore) | byte slices (bytes) |
| [jsontext](#jsontext) | JSON tokens and values, token by token (encoding/json/jsontext) |
| [jsonv2](#jsonv2) | JSON Marshal and Unmarshal with options (encoding/json/v2) |
| [flume](#flume) | buffered I/O (bufio) |
| [quarry](#quarry) | files, environment, process (os) |
| [debug](#debug) | binary formats of the executables Tin writes (debug/elf, debug/macho, debug/buildinfo) |
| [debug/elf](#debug/elf) | ELF executable headers, sections, symbols and dynamic tables (debug/elf) |
| [debug/macho](#debug/macho) | Mach-O executable headers, load commands, sections and symbols (debug/macho) |
| [debug/buildinfo](#debug/buildinfo) | Tin's build metadata in Mach-O executables: the LC_UUID and LC_BUILD_VERSION commands (debug/buildinfo) |
| [debug](#debug) | binary formats of the executables Tin writes (debug/elf, debug/macho, debug/buildinfo) |
| [debug/dwarf](#debug/dwarf) | DWARF compilation units, DIEs and source line tables (debug/dwarf) |
| [user](#user) | users and groups (os/user) |
| [spawn](#spawn) | starting child processes (os/exec) |
| [sandbox](#sandbox) | running a program fenced by Linux: namespaces, cgroup v2 limits, seccomp, a timeout (Linux only) |
| [signal](#signal) | operating-system signals (os/signal) |
| [trail](#trail) | paths (path, path/filepath on Unix) |
| [lever](#lever) | command-line flags (flag) |
| [tty](#tty) | terminals: size, raw mode, colour (golang.org/x/term) |
| [tide](#tide) | time (time) |
| [dice](#dice) | random numbers (math/rand) |
| [sift](#sift) | sorting, searching and the generic slice functions (sort, slices, cmp) |
| [atlas](#atlas) | functions on maps (maps) |
| [cairn](#cairn) | containers (container/heap, sets, LRU) |
| [stamp](#stamp) | hashes and checksums (hash/*) |
| [squash](#squash) | compression: DEFLATE, gzip, zlib, Snappy, LZ4, Zstandard, LZW, bzip2 (compress/flate, compress/gzip, compress/zlib, compress/lzw, compress/bzip2) |
| [squash](#squash) | compression: DEFLATE, gzip, zlib, Snappy, LZ4, Zstandard, LZW, bzip2 (compress/flate, compress/gzip, compress/zlib, compress/lzw, compress/bzip2) |
| [zip](#zip) | ZIP archives (archive/zip) |
| [ledger](#ledger) | CSV reading and writing (encoding/csv) |
| [abacus](#abacus) | arbitrary-precision integers (math/big) |
| [seal](#seal) | crypto and encodings (crypto/sha256, hmac, encoding/hex, base64, base32, ascii85) |
| [nist](#nist) | NIST curves P-224 to P-521, DSA signature verification and FIPS 140-3 status (crypto/elliptic, crypto/dsa, crypto/fips140) |
| [herald](#herald) | logging (log/slog) |
| [expvar](#expvar) | published variables and their JSON handler (expvar) |
| [rpc](#rpc) | Go's net/rpc: registered methods, a server and a client over a codec (net/rpc, net/rpc/jsonrpc) |
| [syslog](#syslog) | system log and collectors: Unix, TCP and UDP connections, priorities and facilities (log/syslog) |
| [crucible](#crucible) | testing helpers (testing) |
| [crucible/iotest](#crucible/iotest) | readers and writers that fail or cut short (testing/iotest) |
| [crucible/quick](#crucible/quick) | properties checked over generated values (testing/quick) |
| [crucible/fstest](#crucible/fstest) | an in-memory file system and its consistency check (testing/fstest) |
| [crucible/slogtest](#crucible/slogtest) | herald's log lines checked against their layout (log/slog/slogtest) |
| [crucible/cryptotest](#crucible/cryptotest) | buffers for constant-time comparisons (testing/cryptotest, crypto/subtle) |
| [constraints](#constraints) | named generic constraint shapes |
| [policy](#policy) | with policies and slots (context values, retry/cache/trace middleware) |
| [redis](#redis) | Redis client (go-redis) |
| [mysql](#mysql) | MySQL client (database/sql with go-sql-driver/mysql) |
| [postgres](#postgres) | PostgreSQL client (database/sql with pgx) |
| [database](#database) | generic SQL drivers, pooling and queries (database/sql) |
| [kafka](#kafka) | Kafka client (franz-go, sarama) |
| [websocket](#websocket) | WebSocket server and client (gorilla/websocket) |
| [s3](#s3) | S3-compatible object storage client with Signature Version 4 (aws-sdk-go-v2 s3) |
| [atomic](#atomic) | counters and flags every core may change (sync/atomic) |
| [lane](#lane) | a bounded queue between the tasks of one core (buffered channels) |
| [replay](#replay) | recording and reading request capsules for tin replay |
| [stencil](#stencil) | text templates loaded at run time (text/template) |
| [htmltpl](#htmltpl) | HTML templates with contextual escaping (html/template) |
| [column](#column) | aligned text columns (text/tabwriter) |
| [scroll](#scroll) | XML tokenizer and writer (encoding/xml) |
| [html](#html) | HTML tokenizer and escaping (html, golang.org/x/net/html) |
| [lasso](#lasso) | regular expressions with linear-time matching (regexp) |
| [pack](#pack) | numbers as bytes: byte order and varints (encoding/binary) |
| [asn1](#asn1) | ASN.1 DER: tags, lengths, object identifiers, bit strings and times (encoding/asn1) |
| [gob](#gob) | Go's gob streams: type descriptions, values and the encoder and decoder over a schema (encoding/gob) |
| [mime](#mime) | media types, RFC 2047 words, quoted-printable and multipart (mime, mime/quotedprintable, mime/multipart) |
| [mail](#mail) | RFC 5322 message and address parsing (net/mail) |
| [textproto](#textproto) | line-oriented and dot-framed protocol I/O (net/textproto) |
| [smtp](#smtp) | SMTP client and message delivery (net/smtp) |
| [suffixarray](#suffixarray) | byte substring indexing with suffix arrays (index/suffixarray) |
| [scan](#scan) | a scanner and tokenizer for UTF-8 text (text/scanner) |
| [image](#image) | images, colors, drawing and PNG encoding (image, image/color, image/draw, image/png) |
| [image](#image) | images, colors, drawing and PNG encoding (image, image/color, image/draw, image/png) |
| [image](#image) | images, colors, drawing and PNG encoding (image, image/color, image/draw, image/png) |
| [tar](#tar) | bounded ustar archive reading and writing (archive/tar) |
| [appkit](#appkit) | macOS frameworks for the Tinland editor (Cocoa, WebKit) |
| [metal](#metal) | Metal: a GPU scene of rectangles and text with a glyph atlas, for the Tinland editor |
| [gpuwin](#gpuwin) | a window AppKit calls into (Objective-C classes defined in Tin), drawn on the GPU |
| [textedit](#textedit) | the editing model behind Tinland (buffer, cursor, undo, highlighting) |
| [tinjson](#tinjson) | a JSON reader and writer for the developer tools |
| [tinsym](#tinsym) | the compiler's declarations and errors, name resolution and completion (tin lsp, Tinland) |
| [tinfmt](#tinfmt) | the whitespace formatter (tin fmt, Tinland) |

## say

Built into the compiler (formatting by static type, no reflection): `say.Line(a, b...)`, `say.Text(...)`, `say.Out(format, ...)`, `say.Fmt(format, ...) str`, `say.Str(x) str`, `say.Fault(format, ...) fault`, `say.To(fd, ...)`, `say.LineTo(fd, ...)`. See toolchain/docs/LANGUAGE.md.

## fault

Package fault is fault chains and the standard sentinels, like Go's errors package: Wrap adds context and keeps the cause, Is walks the chain comparing identity, Join keeps several faults reachable. The runtime's sentinels are the variables Canceled, DeadlineExceeded, LimitExceeded, Overloaded, Draining and Panic; a package declares its own as `let ErrX = fault("msg")`. A function that makes a fault is declared ! here: its fault is the value (fail it, keep it in a variable, or test it). Layout and identities: design/interface_faults.md.

- `Wrap(err fault, msg str) !`: Wrap is err with msg in front ("msg: cause"), err reachable as its cause; nil when err is nil.
- `Is(err fault, target fault) bool`: Is reports whether err or a fault in its chain (causes and joined faults) is target: the same sentinel, or the same fault.
- `Cause(err fault) !`: Cause is the fault err wraps; nil when it wraps none (and for nil and a Join).
- `Join(errs []fault) !`: Join is one fault holding every non-nil fault of errs, each reachable by Is, the messages on separate lines; nil when all are nil.
- `Message(err fault) str`: Message is the full message of err ("outer: inner" for a wrapped fault), "" for nil.
- `Backtrace(err fault) str`: Backtrace is the backtrace text of the panic in err's chain (a fault.Panic), "" for none.

## argo

Package argo writes JSON. argo.Put(b, v) appends v to the []u8 buffer b; the compiler generates a dedicated encoder for v's type (fields in declaration order, no reflection, no allocation). The w* writers below are what those encoders call. argo.Get(s, v) fills v from the JSON text s with a decoder generated the same way; it returns a fault for arrays and objects nested more than 512 deep, as each level takes stack, and leaves v unchanged on any fault. argo.GetStrict(s, v) also rejects unknown and duplicate members.

- `Put(b mut []u8, v i64)`: Put appends v as JSON to b. The compiler replaces every call with a typed encoder.
- `PutV2(b mut []u8, v i64)`: PutV2 uses the encoding/json/v2 nil slice and map defaults. The compiler replaces every call with a typed encoder; v1 callers continue to use Put.
- `Str(b mut []u8, s str)`: Str appends s as a JSON string.
- `Raw(b mut []u8, s str)`: Raw appends already-encoded JSON text.
- `type Parser struct`

## io

Package io declares the streaming shapes: a type satisfies Reader, Writer, Closer or Seeker by having the methods, with no declaration, and compositions like ReadWriteCloser by satisfying every listed shape. The helpers read and write over any reader or writer: ReadAll, ReadFull, ReadAtLeast, Copy, CopyN, CopyBuffer, LimitReader, TeeReader, MultiReader, MultiWriter, WriteString and Discard. A stream ends when Read returns 0 (flume's and ledger's readers do), not with a sentinel fault; ReadByte and ReadRune say the same with ok false and size 0.

Pipe connects a writer and a reader on different tasks or cores: it waits through the scheduler, never blocking a core, and holds back a writer while it is full. The byte, rune and string shapes (ByteReader, ByteScanner, RuneReader, RuneScanner, ByteWriter, StringWriter) and ReaderFrom and WriterTo are declared for code that wants them; a generic helper cannot ask a value which shapes it has, so Copy always copies through its buffer and a caller with a WriterTo calls WriteTo itself. The file system interface (Go's io/fs) is package fs. Reading, writing, closing and seeking change the stream, so those methods are mut (#644): a type's method may take its receiver mut, and a call through a dyn value needs a mut one (w mut dyn io.Writer).

- `shape Reader { mut Read(buf mut []u8) !i64 }`: Reader is anything with Read: it fills buf and returns how many bytes it wrote.
- `shape Writer { mut Write(data []u8) !i64 }`: Writer is anything with Write: it takes data and returns how many bytes it took.
- `shape Closer { mut Close() !i64 }`: Closer is anything with Close.
- `shape Seeker { mut Seek(offset i64, whence i64) !i64 }`: Seeker is anything with Seek: offset is relative to whence (0 start, 1 current, 2 end).
- `shape ReaderAt { ReadAt(buf mut []u8, off i64) !i64 }`: ReaderAt is a reader that does not move a position: it reads at off.
- `shape WriterAt { mut WriteAt(data []u8, off i64) !i64 }`: WriterAt is a writer that does not move a position: it writes at off.
- `shape ReadWriter`: ReadWriter reads and writes.
- `shape ReadCloser`: ReadCloser reads and closes.
- `shape WriteCloser`: WriteCloser writes and closes.
- `shape WriteSeeker`: WriteSeeker writes and seeks.
- `shape ReadSeekCloser`: ReadSeekCloser reads, seeks and closes.
- `shape ReadWriteCloser`: ReadWriteCloser reads, writes and closes.
- `shape ReadSeeker`: ReadSeeker reads and seeks.
- `shape ReadWriteSeeker`: ReadWriteSeeker reads, writes and seeks.
- `shape ByteReader { mut ReadByte() !(u8, bool) }`: ByteReader reads one byte at a time: ok is false at the end of the stream.
- `shape ByteScanner`: ByteScanner is a ByteReader that can step back: UnreadByte makes the next ReadByte return the byte the last one returned.
- `shape ByteWriter { mut WriteByte(c u8) ! }`: ByteWriter writes one byte.
- `shape RuneReader { mut ReadRune() !(i32, i64) }`: RuneReader reads one UTF-8 encoded rune: its value and its size in bytes, size 0 at the end of the stream (an invalid encoding is U+FFFD of size 1, as Go's readers give).
- `shape RuneScanner`: RuneScanner is a RuneReader that can step back: UnreadRune makes the next ReadRune return the rune the last one returned.
- `shape StringWriter { mut WriteString(s str) !i64 }`: StringWriter writes a str without making a []u8 of it, and returns how many bytes it took.
- `shape ReaderFrom { mut ReadFrom(src mut dyn Reader) !i64 }`: ReaderFrom reads src until its end into itself and returns how many bytes it took.
- `shape WriterTo { mut WriteTo(dst mut dyn Writer) !i64 }`: WriterTo writes its data to dst until it has none left and returns how many bytes it wrote.
- `ReadAll[R Reader](src R) !str`: ReadAll reads until the stream ends and returns what it read.
- `ReadFull[R Reader](src R, buf mut []u8) !i64`: ReadFull reads exactly len(buf) bytes; a stream that ends first fails with "unexpected end of stream". A zero-length buffer reads nothing.
- `ReadAtLeast[R Reader](src R, buf mut []u8, min i64) !i64`: ReadAtLeast reads at least min bytes (or until the stream ends) into buf; fewer than min bytes is the "unexpected end of stream" fault.
- `Copy[W Writer, R Reader](dst W, src R) !i64`: Copy reads from src and writes every chunk to dst until the stream ends, and returns how many bytes it copied. The scratch buffer is 32 KiB, as Go's is, taken from this core's pool of them and given back when Copy returns, so a loop of copies allocates nothing; a Reader must not keep the buffer it is given (Go's rule too).
- `CopyBuffer[W Writer, R Reader](dst W, src R, buf mut []u8) !i64`: CopyBuffer is Copy with the caller's scratch buffer, which must not be empty.
- `CopyN[W Writer, R Reader](dst W, src R, n i64) !i64`: CopyN copies exactly n bytes; fewer means the stream ended first, which is the "unexpected end of stream" fault.
- `WriteString[W Writer](dst W, s str) !i64`: WriteString writes s to dst.
- `type LimitedReader[R Reader] struct`: LimitedReader reads at most n bytes from r; it is what LimitReader returns.
- `LimitReader[R Reader](src R, n i64) LimitedReader[R]`: LimitReader returns a reader that yields at most n bytes of src and then ends.
- `(l LimitedReader[R]) Left() i64`: Left returns how many bytes the limit has left.
- `(l mut LimitedReader[R]) Read(buf mut []u8) !i64`: Read reads at most what the limit has left; it returns 0 once the limit is reached.
- `type TeeReader[R Reader, W Writer] struct`: TeeReader reads from r and writes what it read to w, like Go's TeeReader.
- `NewTeeReader[R Reader, W Writer](src R, dst W) TeeReader[R, W]`: NewTeeReader returns a reader that writes everything it reads from src to dst.
- `(t mut TeeReader[R, W]) Read(buf mut []u8) !i64`: Read reads from the underlying reader and writes the same bytes to the tee.
- `type MultiReader struct`: MultiReader reads several readers in turn, as one stream; it is what NewMultiReader returns and takes dyn values, so the readers may have different types.
- `NewMultiReader(rs []dyn Reader) MultiReader`: NewMultiReader reads the readers in order.
- `(m mut MultiReader) Read(buf mut []u8) !i64`: Read reads from the current reader; when one ends, the next is used, and the last one's end is the stream's end.
- `type MultiWriter struct`: MultiWriter writes to every writer in turn; it is what NewMultiWriter returns and takes dyn values, so the writers may have different types.
- `NewMultiWriter(ws []dyn Writer) MultiWriter`: NewMultiWriter writes each chunk to every writer, and fails when one takes less than all of it.
- `(m mut MultiWriter) Write(data []u8) !i64`: Write writes data to every writer.
- `type DiscardWriter struct{}`: DiscardWriter is a writer that throws everything away, like Go's io.Discard.
- `Discard() DiscardWriter`: Discard returns the writer that throws everything away.
- `(d mut DiscardWriter) Write(data []u8) !i64`: Write takes data and reports all of it written.
- `type PipeReader struct`: PipeReader is the read end of a Pipe: an io.Reader whose stream ends when the writer closes.
- `type PipeWriter struct`: PipeWriter is the write end of a Pipe: an io.Writer that waits while the pipe is full.
- `Pipe() !(PipeReader, PipeWriter)`: Pipe makes a pipe: what is written to the PipeWriter is read from the PipeReader, in order. Unlike Go's, which hands each Write to a Read, the pipe holds what the system's pipe buffer holds (64 KiB on Linux): a Write returns once its bytes are in the pipe, and waits while it is full, so a writer is held back by a slow reader. Close the writer to end the reader's stream; close both ends to give back the descriptors. Making a pipe ignores SIGPIPE in the process (as Go's runtime does for every descriptor but the standard ones), so a write to a pipe whose reader closed fails instead of ending the program.
- `(p PipeReader) Read(buf mut []u8) !i64`: Read reads what the writer wrote into buf, waiting until some is there, and returns how many bytes came: 0 once the writer closed and everything was read. A writer's CloseWithError makes the end of the stream that fault (its text) instead; a Read after this end's Close fails with ErrClosedPipe.
- `(p mut PipeReader) Close() !`: Close closes the read end: the writer's next Write fails with ErrClosedPipe. A second Close does nothing.
- `(p mut PipeReader) CloseWithError(err fault) !`: CloseWithError closes the read end; the writer's next Write fails with err's text (ErrClosedPipe for nil). Only the first close of an end counts.
- `(p PipeWriter) Write(data []u8) !i64`: Write writes all of data to the pipe, waiting while it is full, and returns len(data). Once the reader has closed it fails with ErrClosedPipe (or the reader's CloseWithError text) and the count of bytes that went in is lost with the fault, as a short write is; after this end's own Close it fails with ErrClosedPipe.
- `(p PipeWriter) WriteString(s str) !i64`: WriteString writes s to the pipe, as Write does.
- `(p mut PipeWriter) Close() !`: Close closes the write end: the reader reads what is left and then its stream ends (Read returns 0). A second Close does nothing.
- `(p mut PipeWriter) CloseWithError(err fault) !`: CloseWithError closes the write end; once the reader has read what is left, its Read fails with err's text instead of returning 0 (nil: the plain end). Only the first close counts.

## fs

Package fs is the file system interface, like Go's io/fs: a file system is anything with Open (the FS shape), and ReadDirFS, StatFS and SubFS add what WalkDir, Glob and Sub use. Names are slash-separated and unrooted ("a/b.txt", "." for the root; ValidPath says which are). ReadFile, ReadDir, Stat, Sub, Glob and WalkDir work over any file system with the shape they need; Dir is the operating system's file tree under a directory (Go's os.DirFS), read through quarry.

Where Go asks an interface at run time (fs.ReadDir tries ReadDirFS, then a file's ReadDir), a helper here names the shape it needs at compile time: WalkDir and Glob take a TreeFS (ReadDir and Stat). A File has Stat and ReadDir itself (ReadDir fails on a file that is not a directory). Faults are Go's PathError text ("open a/b: no such file or directory") and match ErrNotExist, ErrPermission, ErrExist and ErrInvalid with fault.Is as Go's errors.Is does. A directory listing ends with an empty slice, not a sentinel fault, as a Read ends with 0.

- `const ModeDir = 1 << 31`: ModeDir is the mode bit of a directory (Go's fs.ModeDir); modes are i64 values of Go's FileMode bits.
- `const ModeAppend = 1 << 30`: ModeAppend is the append-only bit.
- `const ModeExclusive = 1 << 29`: ModeExclusive is the exclusive-use bit.
- `const ModeTemporary = 1 << 28`: ModeTemporary is the temporary-file bit.
- `const ModeSymlink = 1 << 27`: ModeSymlink is the mode bit of a symbolic link.
- `const ModeDevice = 1 << 26`: ModeDevice is the mode bit of a device file.
- `const ModeNamedPipe = 1 << 25`: ModeNamedPipe is the mode bit of a FIFO.
- `const ModeSocket = 1 << 24`: ModeSocket is the mode bit of a Unix domain socket.
- `const ModeSetuid = 1 << 23`: ModeSetuid is the setuid bit.
- `const ModeSetgid = 1 << 22`: ModeSetgid is the setgid bit.
- `const ModeCharDevice = 1 << 21`: ModeCharDevice is the bit of a character device (set with ModeDevice).
- `const ModeSticky = 1 << 20`: ModeSticky is the sticky bit.
- `const ModeIrregular = 1 << 19`: ModeIrregular is the bit of a file of no other known type.
- `const ModeType = ModeDir | ModeSymlink | ModeNamedPipe | ModeSocket | ModeDevice | ModeCharDevice | ModeIrregular`: ModeType is the type bits: a mode with none of them is a regular file.
- `const ModePerm = 0o777`: ModePerm is the Unix permission bits.
- `type FileInfo struct`: FileInfo describes a file, as Stat reports it (Go's fs.FileInfo).
- `(i FileInfo) IsDir() bool`: IsDir reports whether the file is a directory.
- `(i FileInfo) Type() i64`: Type is the file's type bits (Mode & ModeType).
- `type DirEntry struct`: DirEntry is a name in a directory with its type bits (Go's fs.DirEntry); fs.Stat gives the rest.
- `(d DirEntry) IsDir() bool`: IsDir reports whether the entry is a directory.
- `FileInfoToDirEntry(info FileInfo) DirEntry`: FileInfoToDirEntry is the DirEntry of a file described by info.
- `shape File`: File is an open file: Read until it returns 0, Stat, ReadDir for a directory, and Close. ReadDir(n) with n > 0 gives at most n entries and an empty slice at the end; n <= 0 gives all that are left.
- `type FileReader struct`: FileReader is an open File as an io.Reader, what Reader returns: a dyn File satisfies only its own shape (dyn-to-dyn widening, E514, is not built), so io.Copy and io.ReadAll take this.
- `Reader(f dyn File) FileReader`: Reader is f as an io.Reader: its Read is f's.
- `(r mut FileReader) Read(buf mut []u8) !i64`: Read reads from the file.
- `shape FS`: FS is a file system: Open opens a file by a name ValidPath accepts.
- `shape ReadDirFS`: ReadDirFS is a file system that lists a directory by name, sorted by name.
- `shape StatFS`: StatFS is a file system that describes a file by name.
- `shape ReadFileFS`: ReadFileFS is a file system that reads a whole file by name.
- `shape TreeFS`: TreeFS lists directories and describes files: what WalkDir and Glob need.
- `shape SubFS[S constraints.Any]`: SubFS is a file system whose Sub gives the file system of one of its directories, of type S.
- `ValidPath(name str) bool`: ValidPath reports whether name is a valid file system name: UTF-8, slash-separated elements that are not empty, "." or "..", no leading or trailing slash; "." alone names the root.
- `PathError(op str, path str, err fault) !`: PathError is err with the operation and the name in front ("op path: err"), as Go's fs.PathError prints; err stays reachable with fault.Is.
- `ReadFile[F FS](fsys F, name str) !str`: ReadFile reads the named file to its end: Open, Read until 0, Close.
- `ReadDir[F ReadDirFS](fsys F, name str) ![]DirEntry`: ReadDir lists the named directory, sorted by name.
- `Stat[F StatFS](fsys F, name str) !FileInfo`: Stat describes the named file.
- `Glob[F TreeFS](fsys F, pattern str) ![]str`: Glob lists the names that match pattern (trail.Match's syntax, per element), in lexical order within each directory, like Go's fs.Glob: a directory that cannot be read is skipped, a pattern with no special bytes gives itself when Stat finds it, and only a malformed pattern is a fault (ErrBadPattern).
- `WalkDir[F TreeFS](fsys F, root str, f fn(str, ?DirEntry, fault) !) !`: WalkDir calls f for root and every file and directory below it, in lexical order, like Go's fs.WalkDir: f gets the path (root joined with the names), the entry (nil when root cannot be described) and nil, or a fault: Stat's for root, or ReadDir's in a second call for a directory that cannot be listed. f's fault ends the walk and is WalkDir's, except SkipDir (skip this directory, or the rest of the one a file is in) and SkipAll (stop, with no fault). Symbolic links inside the tree are not followed; a root that is one is.
- `ModeString(m i64) str`: ModeString is a mode as Go's FileMode.String prints it: the type and special letters ("dalTLDpSugct?") or "-", then rwxrwxrwx with "-" for a missing permission.
- `type DirFS struct`: DirFS is the file tree under a directory of the operating system, read through quarry (Go's os.DirFS): it is a TreeFS, a ReadFileFS and a SubFS[DirFS]. Names are joined to the root with a slash; a name ValidPath refuses fails with ErrInvalid, and the faults name the name, not the joined path, as Go's do.
- `Dir(root str) DirFS`: Dir is the file tree under root.
- `(d DirFS) Root() str`: Root is the directory the file system was made with.
- `(d DirFS) Open(name str) !dyn File`: Open opens the named file or directory for reading.
- `(d DirFS) Stat(name str) !FileInfo`: Stat describes the named file, following a symbolic link.
- `(d DirFS) Lstat(name str) !FileInfo`: Lstat describes the named file; a symbolic link is described itself.
- `(d DirFS) ReadDir(name str) ![]DirEntry`: ReadDir lists the named directory, sorted by name, with each entry's type (not following links).
- `(d DirFS) ReadFile(name str) !str`: ReadFile reads the whole named file with quarry.ReadFile (its 64 MiB bound and its waits in a task).
- `(d DirFS) Sub(dir str) !DirFS`: Sub is the file tree under the directory dir of this one.
- `(f mut osFile) Read(buf mut []u8) !i64`: Read reads the next bytes of the file into buf: 0 at the end. A directory cannot be read.
- `(f osFile) Stat() !FileInfo`: Stat describes the file as it was when it was opened.
- `(f mut osFile) ReadDir(n i64) ![]DirEntry`: ReadDir gives the directory's next n entries (all that are left for n <= 0), sorted by name; an empty slice at the end.
- `(f mut osFile) Close() !`: Close closes the file; a second Close fails with ErrClosed.

## embed

Package embed is the file tree the compiler puts into a program's image (#928), read-only, as Go's embed.FS is. A line "// embed: PATTERN" at column 1, directly above a top-level "let NAME str", makes NAME the blob of the files PATTERN names, relative to the directory of the source file (globs with * and ?; directories are walked, hidden names left out). Parse reads that blob as a file system: Open, ReadDir, Stat and ReadFile satisfy the fs package's shapes, so fs.ReadFile, fs.WalkDir and fs.Glob work on it. Nothing is read from disk at run time, and the bytes stay in the image.

The blob has one record per file: its slash-separated name, a newline, its size in decimal, a newline and its bytes. The compiler writes each directory's records in name order, and Parse checks that order, so a blob that is not a tree from the compiler fails with ErrFormat rather than giving unsorted listings.

- `type FS struct`: FS is an embedded file tree, read-only: a value from Parse (the zero value has no files and no maps).
- `Parse(blob str) !FS`: Parse reads blob, the bytes of a tree the compiler embedded, as a file system; a blob that is not one fails with ErrFormat.
- `(f FS) Open(name str) !dyn fs.File`: Open opens the named file or directory for reading.
- `(f FS) ReadFile(name str) !str`: ReadFile reads the named file whole.
- `(f FS) ReadDir(name str) ![]fs.DirEntry`: ReadDir lists the named directory, sorted by name, with each entry's type.
- `(f FS) Stat(name str) !fs.FileInfo`: Stat describes the named file or directory: files are read-only (0444), directories 0555.
- `(f mut embedFile) Read(buf mut []u8) !i64`: Read reads the next bytes of the file into buf: 0 at the end.
- `(f embedFile) Stat() !fs.FileInfo`: Stat describes the file.
- `(f mut embedFile) ReadDir(n i64) ![]fs.DirEntry`: ReadDir fails: a file has no entries.
- `(f mut embedFile) Close() !`: Close closes the file; a second Close fails with fs.ErrClosed.
- `(f mut embedDir) Read(buf mut []u8) !i64`: Read fails: a directory cannot be read as a file (Go names it with a trailing slash too).
- `(f embedDir) Stat() !fs.FileInfo`: Stat describes the directory.
- `(f mut embedDir) ReadDir(n i64) ![]fs.DirEntry`: ReadDir gives the next n entries (all that are left for n <= 0), sorted by name; an empty slice at the end.
- `(f mut embedDir) Close() !`: Close closes the directory; a second Close fails with fs.ErrClosed.

## anvil

Package anvil is an HTTP/1.1 and HTTP/2 server: one event loop per core (epoll, kqueue), share-nothing. HTTP/2 without TLS (h2c) is served on the same port, by prior knowledge or after Upgrade: h2c, and over TLS (ServeTLS) to a client whose ALPN offers h2; handlers are the same for both, each request (or stream) in a task of its own.

Core 0 accepts connections and deals them round-robin to every core through a pipe; from then on a connection belongs to one core for its whole life. Each core reads into one scratch buffer, parses requests in place, runs the handler, writes every response of the batch with one write, and wipes its request pool. Idle connections hold no buffers, only a 96-byte record.

```tin
type Msg struct {
	message str
}

fn handle(q anvil.Req, w mut anvil.Out) {
	w.Type("application/json")
	argo.Put(mut w.Body, Msg{message: "hi"})
}

fn main() {
	anvil.Serve(":8080", handle) catch err {
		say.Line("server:", err)
	}
}
```

A Router picks the handler by method and path pattern, and runs middleware around it. Patterns match whole segments: "users" itself, {id} any one non-empty segment, and a last {path...} or * the rest of the path. Static segments win over {name}, and {name} over the rest, segment by segment, whatever the order of registration. A path whose routes take other methods gets 405 with Allow, any other miss 404; HEAD falls back to GET. A trailing slash is part of the path: /users/ and /users are different routes. Write patterns with {...} as raw strings: in "..." the braces would interpolate.

```tin
fn user(q anvil.Req, w mut anvil.Out) {
	let id = q.PathParam("id")
	w.Text("user {id}")
}

fn logged(q anvil.Req, w mut anvil.Out, next fn(anvil.Req, mut anvil.Out)) {
	next(q, mut w)
	herald.Log(herald.LInfo, "request", []str{
		"method", q.Method, "route", q.Pattern(), "status", say.Str(w.Code()), "client", q.ClientIP(),
	})
}

fn main() {
	let r = anvil.NewRouter()
	r.Use(logged)
	r.Get(`/users/{id}`, user)
	r.Route("/admin", fn(g mut anvil.Router) {
		g.Use(logged)
		g.Delete(`/users/{id}`, user)
	})
	r.Serve(":8080") catch err {
		say.Line("server:", err)
	}
}
```

The middleware writes one herald line per request, with the client's address as client:

```text
2026-10-05T09:00:00.000Z INFO core=0 request method=GET route=/users/{id} status=200 client=203.0.113.7
```

q.ClientIP() is the connection's peer unless the peer is one of the TrustedProxies: behind a proxy of yours, call TrustedProxies first, or every line carries the proxy's address.

ServeTLS (and Router.ServeTLS) serve HTTPS: TLS 1.3 with a PEM certificate chain and key, each handshake in a task of its own, then the same event loop with records decrypted before parsing and sealed before writing (toolchain/docs/RUNTIME.md). examples/https_server.tin.

- `TrustedProxies(cidrs []str) !`: TrustedProxies sets the proxies whose X-Forwarded-For and Forwarded headers ClientIP believes, as networks ("10.0.0.0/8", "fd00::/8") or single addresses. Call it before Serve. With none (the default) ClientIP is the connection's peer: the headers are written by the client and prove nothing unless a proxy you run replaced them.
- `(q Req) RemoteAddr() str`: RemoteAddr is the address the request's connection comes from, "ip:port" ("[ip]:port" for IPv6, and an IPv4 client of an IPv6 listener as IPv4), or "" for a request made in the process. It is read once per connection. A request replayed from a capsule (#242) gets the address it was recorded with, "" when the capsule is older than that (schema 1).
- `(q Req) ClientIP() str`: ClientIP is the client's IP address: the connection's peer, or, when the peer is one of the TrustedProxies, the rightmost address of X-Forwarded-For (else Forwarded's for=) that is not a trusted proxy. A malformed entry ends the walk at the peer. "" for a request made in the process.
- `type Req struct`: Req is the request being served. Its strings live in the request pool: keep() them to store them anywhere long-lived.
- `type Out struct`: Out is the response being built. Body is the response body; the status defaults to 200 and the content type to text/plain.
- `Serve(addr str, h fn(Req, mut Out)) !`: Serve listens on addr (":8080", "127.0.0.1:8080") and serves h on every core. It returns only if the server cannot start. TIN_CORES overrides the number of cores (1 to 1024; another value is named on stderr and the CPU count is used).
- `ServeN(addr str, n i64, h fn(Req, mut Out)) !`: ServeN is Serve on exactly n cores.
- `Drain(grace i64)`: Drain starts the graceful shutdown from code, as SIGTERM does (#238): listeners close, the requests in flight finish, and after grace nanoseconds what is left is cancelled with fault.Draining; then the cores stop, Serve returns and the stop events run. Any core may call it; it does nothing outside a server or once a shutdown started.
- `Timeouts(header i64, read i64, idle i64, write i64)`: Timeouts sets the connection timeouts in milliseconds; 0 turns one off. header: a request's line and headers must arrive within it (slowloris); read: the whole request, body included; idle: a keep-alive connection with no request in progress; write: a response the client stops reading (no progress for this long). A connection is closed when one passes; a request whose handler is running is governed by Deadline instead. Defaults 10000, 60000, 60000 and 30000; TIN_HEADER_TIMEOUT_MS, TIN_READ_TIMEOUT_MS, TIN_IDLE_TIMEOUT_MS and TIN_WRITE_TIMEOUT_MS override them. Call before Serve.
- `type Load struct`: Load is what an admission policy sees of the core a new request arrived on: its waiting request tasks, live connections, bytes buffered for requests still arriving, how many requests were refused so far, the request-pool bytes its requests hold beyond each one's first chunk (what TIN_REQUEST_MEMORY counts), and the bytes its long-lived (ingot) heap holds (design_semantics §11).
- `Admit(p fn(Load) bool)`: Admit sets the admission policy (call before Serve): after the built-in limits, p decides each new request before its handler runs; false answers 503 with Retry-After: 1 without running the handler. Every core calls p with its own Load.
- `Limits(maxBody i64, maxBuffered i64, maxConns i64)`: Limits sets the largest request body in bytes (413 past it), the bytes of requests still arriving that one core may buffer (a new partial request past it gets 503 and close), and the connections per core (0: no limit). Past maxConns a core still accepts up to 64 more connections and answers each request on them 503 with Retry-After and Connection: close, so a load balancer reads an answer instead of a reset; only past that margin is a new connection closed at accept. Defaults 64 MiB, 256 MiB and 16384; TIN_MAX_BODY, TIN_MAX_BUFFERED and TIN_MAX_CONNS override them. Call before Serve.
- `Deadline(ms i64)`: Deadline makes every request's waits (tide.Wait, client calls) fail with "deadline exceeded" once ms have passed since the request started (0: no deadline; call before Serve). TIN_DEADLINE_MS sets it too; the default is 30000.
- `(q Req) Header(name str) str`: Header returns the value of the request header name (any case), or "". A chunked request's trailer fields are read after the header block's, whether or not a Trailer field announced them: a field of the header block wins, and the framing fields (Host, Content-Length, Transfer-Encoding) are never taken from trailers. Go keeps trailers apart, in Request.Trailer. For an absolute-form target ("GET http://host/path", as proxies send), "host" is the target's authority, which replaces the Host field (RFC 9112 3.2.2, #749).
- `(q Req) Fields() []str`: Fields returns every field of the request's header block as "Name: value", in the order they came, the name as sent and the value without the blanks around it: for dumps and proxies (#739). Trailer fields are not among them.
- `(q Req) Proto() str`: Proto is the protocol the request came in: "HTTP/2.0" (h2c, or h2 over TLS), "HTTP/1.1" or "HTTP/1.0". A request made with Router.Run is "HTTP/1.1".
- `(q Req) Hijack() !i64`: Hijack takes the request's connection out of HTTP for a protocol of its own (the websocket package uses it): the responses before this request are written, the core stops reading the connection and the request's deadline no longer applies. It returns the non-blocking descriptor, for the caller's I/O until the handler returns; then anvil closes it. The handler's Out is not sent. An HTTP/2 stream cannot be hijacked: Hijack fails there.
- `(w mut Out) Stream() !`: Stream switches the response to streaming. The status, content type and headers set so far are sent with the first Write or Flush (set them before). The body is then written with Write and Flush, in chunks (Transfer-Encoding: chunked), or as a plain body of the size Length gave; an HTTP/1.0 client, which cannot read chunks, gets the body up to the end of the connection. Each write waits for a slow client within the write timeout (TIN_WRITE_TIMEOUT_MS), and the request deadline (TIN_DEADLINE_MS) counts from the last write, so a stream lives as long as it keeps writing. Calling Stream again does nothing. On HTTP/2 the body goes in DATA frames within the client's flow-control windows, and Length sets content-length.
- `(w mut Out) Length(n i64) !`: Length sets the size of the streamed body in bytes: the response then has a Content-Length header instead of chunks, and the handler must write exactly n bytes. Call it after Stream and before the first Write or Flush.
- `(w mut Out) Write(b []u8) !`: Write sends b as part of the body, after the head if that is not out yet. It waits while the client does not read, and fails when the client has closed the connection, stopped reading for the write timeout, or the request was cancelled: the handler should stop then. Text appended to the body with Text or argo.Put(mut w.Body, v) is sent by the next Write or Flush.
- `(w mut Out) WriteString(s str) !`: WriteString is Write for a str.
- `(w mut Out) Flush() !`: Flush sends the head if it is not out yet and what Text or argo.Put put in the body so far, as one chunk: with it a handler makes a client see an event now.
- `(w mut Out) Abort()`: Abort ends a stream the handler cannot finish (its data source failed halfway): the connection closes without the last chunk, so the client sees an incomplete response instead of a short one that looks complete. Before the head is sent, the response is an ordinary one again.
- `(w Out) Closed() bool`: Closed reports whether the client has closed the connection (a stream's handler asks between events: a write only fails once the client's reset arrives).
- `(w mut Out) SendFile(path str, off i64, n i64) !`: SendFile sends n bytes of the file at path, from byte off, as the body (n < 0: to the end of the file). As the whole body of a response that is not streaming yet it starts the stream with a Content-Length of n, so a download is `w.SendFile(path, 0, -1)`; in a stream already begun, the bytes go out as chunks or as part of the Content-Length body. The file goes to the socket with sendfile(2) in pieces of 1 MiB on a helper thread, so it is never read into the request pool and a slow disk does not stop the core; each piece waits for a slow client within the write timeout. The file is opened and its size read as quarry.OpenRegular does, through the core's io_uring or on a helper thread within the request's deadline, never on the core thread (#744); a directory or anything else that is not a regular file fails before the head is sent, so the handler can still answer.
- `(q Req) Body() str`: Body returns the request body (a chunked one decoded).
- `(q Req) BodyBound(n i64) !str`: BodyBound returns the request body when it is at most n bytes, and otherwise fails with fault.LimitExceeded before copying any of it: the compiler calls it for q.Body() into a bounded type (try bound(q.Body()), #240).
- `(q Req) Param(name str) str`: Param returns query parameter name, %-decoded, or "".
- `(q Req) PathParam(name str) str`: PathParam returns path parameter name of the Router route that matched ({name}, {name...}, or "*" for a last *), %-decoded, or "".
- `(q Req) Pattern() str`: Pattern returns the pattern of the Router route serving the request ("/users/{id}"), or "" (no Router, or a 404 or 405 answer).
- `(w mut Out) Status(code i64)`: Status sets the response status code.
- `(w mut Out) Type(t str)`: Type sets the Content-Type header. Control bytes in t (CR, LF, NUL and the others but HTAB, and DEL) become spaces, so a value taken from the request cannot add header lines.
- `(w mut Out) Head(k str, v str)`: Head adds a response header. A name that is not an HTTP token is ignored, and so are Content-Length, Transfer-Encoding and Connection: anvil writes the framing itself. Control bytes in the value (CR, LF, NUL and the others but HTAB, and DEL) become spaces, so a value taken from the request cannot add header lines or a body (response splitting), as Go's net/http does, nor hand a client a value RFC 9110 5.5 forbids (#748).
- `(w mut Out) Trailer(k str, v str)`: Trailer adds a trailer field, sent after the body: on HTTP/2 in a HEADERS frame that ends the stream (gRPC's grpc-status and grpc-message), on HTTP/1.1 after the last chunk of a chunked stream (w.Stream() without Length). A response with a Content-Length cannot carry trailers in HTTP/1.1: they are dropped there. Like Head, a name that is not a token and the framing fields are ignored, and control bytes in the value become spaces.
- `(w mut Out) Text(s str)`: Text appends s to the body.
- `(w mut Out) Json()`: Json sets the JSON content type; the body is then written with argo.Put(mut w.Body, v).
- `(w Out) Code() i64`: Code returns the response status set so far (200 unless Status changed it).
- `(w Out) Header(k str) str`: Header returns response header k as set so far (Type sets Content-Type, Head the rest), or "".
- `(w Out) Fields() []str`: Fields returns every header field Head (and SetCookie) added so far as "Name: value", in order: Content-Type, which Type sets, is read with Header (#739).
- `(w Out) HeadersAll() []str`: HeadersAll returns the response's headers as flat name, value pairs: Content-Type when set, then the Head and SetCookie fields in order.
- `(w mut Out) SetValue(key str, value str)`: SetValue stores value under key for the rest of the request: middleware hand data (a user id, a request id) to the handlers after them this way. Value reads it back.
- `(w Out) Value(key str) str`: Value returns what SetValue stored under key in this request, or "".
- `OnRelay(h fn(i64, str))`: OnRelay makes every core run h(from, msg) for each relay message it receives (call before Serve). Handlers run between requests, with their own request pool.
- `OnTick(ms i64, h fn(i64))`: OnTick makes every core run h(core) every ms milliseconds (call before Serve).
- `type Router struct`: Router sends each request to the handler routed for its method and path pattern, through the middleware added with Use. Build it in main (or in a function a global's initializer calls), then Serve it, or try requests on it with Run.
- `NewRouter() Router`: NewRouter makes an empty router: every request gets 404 until routes are added.
- `(r mut Router) Get(pattern str, h fn(Req, mut Out))`: Get routes GET requests for pattern to h, and HEAD requests unless Head routes them.
- `(r mut Router) Post(pattern str, h fn(Req, mut Out))`: Post routes POST requests for pattern to h.
- `(r mut Router) Put(pattern str, h fn(Req, mut Out))`: Put routes PUT requests for pattern to h.
- `(r mut Router) Patch(pattern str, h fn(Req, mut Out))`: Patch routes PATCH requests for pattern to h.
- `(r mut Router) Delete(pattern str, h fn(Req, mut Out))`: Delete routes DELETE requests for pattern to h.
- `(r mut Router) Head(pattern str, h fn(Req, mut Out))`: Head routes HEAD requests for pattern to h (without it, they go to the GET route).
- `(r mut Router) Options(pattern str, h fn(Req, mut Out))`: Options routes OPTIONS requests for pattern to h.
- `(r mut Router) Handle(method str, pattern str, h fn(Req, mut Out))`: Handle routes requests with method (any HTTP method name, like "PROPFIND") for pattern to h.
- `(r mut Router) Stream(method str, pattern str, h fn(Req, mut Out))`: Stream routes method requests for pattern to h, which runs as soon as the request's headers are in and reads the body as it arrives with q.BodyStream() (#481): large uploads in bounded memory, gRPC client and bidirectional streams. TIN_MAX_BODY does not bound such a body.
- `(r mut Router) Any(pattern str, h fn(Req, mut Out))`: Any routes requests for pattern with every method to h; a route for the request's own method on the same pattern wins over it.
- `(r mut Router) Use(mw fn(Req, mut Out, fn(Req, mut Out)))`: Use adds middleware mw to r. Middleware run in the order added, around every route of r and of the routers mounted in it, and around their 404 and 405 answers. Each gets next, the rest of the chain, and decides whether and when to call it.
- `(r mut Router) Route(prefix str, build fn(mut Router))`: Route groups routes under prefix ("/api"): build adds them to a new router mounted there.
- `(r mut Router) Mount(prefix str, sub Router)`: Mount serves sub's routes under prefix: "/api" and "/users" make "/api/users", and "/api" and "" make "/api". r's middleware run before sub's, and sub's 404 and 405 answers (with its middleware) cover the paths under prefix.
- `(r mut Router) NotFound(h fn(Req, mut Out))`: NotFound sets the handler for the paths no route matches (under r's prefix when r is mounted); the status starts as 404.
- `(r mut Router) MethodNotAllowed(h fn(Req, mut Out))`: MethodNotAllowed sets the handler for the paths whose routes take other methods; the status starts as 405 and the Allow header lists those methods.
- `(r Router) Check() !`: Check fails with r's first bad pattern, conflicting route or misplaced mount, the error Serve would fail with before listening.
- `(r Router) Serve(addr str) !`: Serve listens on addr and serves r on every core, like anvil.Serve. The routes are checked and compiled once, into a table every core reads; Serve fails with r's error, if any (see Check).
- `(r Router) ServeN(addr str, n i64) !`: ServeN is Serve on exactly n cores.
- `(r Router) Run(method str, target str, body str) Out`: Run sends one request through r on this thread, as Serve would (middleware, 404, 405), and returns the response: for tests. target is the path and query ("/users/7?full=1"), the request has no headers, and a HEAD response keeps its body. Run panics if r has an error (see Check).
- `(r Router) RunWith(method str, target str, headers []str, body str) Out`: RunWith is Run with request header fields, each written "Name: value" (Cookie, Content-Type ...): for tests of handlers that read headers, cookies or forms.
- `NewRequest(method str, target str, headers []str, body str) Req`: NewRequest builds an in-process request for test helpers; headers are "Name: value" lines and body is the decoded body.
- `(r Router) Match(method str, path str) str`: Match returns the pattern of the route that would serve method and path ("/users/{id}"), or "" when the request would get 404 or 405. Like Run, it panics if r has an error (see Check).
- `type Cookie struct`: Cookie is a Set-Cookie: the name, the value and the attributes. Expires is in Unix seconds and left out when 0; MaxAge in seconds is left out when 0 and, when negative, is written as Max-Age=0 (delete the cookie). SameSite is "", "Lax", "Strict" or "None".
- `(q Req) Cookie(name str) str`: Cookie returns the value of the request's cookie name, or "" when there is none (or it is not well formed): see Cookies.
- `(q Req) Cookies() map[str]str`: Cookies returns the request's cookies by name, as Go's Request.Cookies does: every Cookie header field is read (HTTP/2 joins its cookie fields with "; "), a pair splits at its first "=", a value may be wrapped in double quotes, and a pair with a bad name or value is skipped. When a name occurs twice, the first value wins.
- `(w mut Out) SetCookie(c Cookie)`: SetCookie adds a Set-Cookie header for c. A cookie whose name is not a token is dropped, a Domain that is not a valid domain name or IPv4 address is left out, and bytes that cannot be in the value or the path are removed, as Go's http.SetCookie does. Each call adds a header field of its own, so several cookies can be set in one response (HTTP/1.1 and HTTP/2).
- `(c Cookie) String() str`: String is the Set-Cookie header value for c, or "" when its name is not a valid cookie name.
- `(w Out) Headers(k str) []str`: Headers returns the values of every response header field called k as set so far (Head adds one per call), in order: all the Set-Cookie fields of a response, for tests.
- `(w mut Out) ServeFile(q Req, path str) !`: ServeFile sends the file at path as the response to request q. It sets Content-Type (from the extension, unless the handler set Type), Accept-Ranges, Last-Modified (the file's modification time) and ETag (the handler's own, if it set one, else a strong tag made of the time and the size), then decides as http.ServeContent does:  - If-Match that matches no tag, or If-Unmodified-Since before the file's time: 412 Precondition Failed; - If-None-Match that matches (a weak comparison), or, without it, If-Modified-Since at or after the file's time: 304 Not Modified for GET and HEAD (412 for other methods), with no body; - Range: bytes=a-b, a- or -n (when If-Range, if given, matches the tag or the time): 206 Partial Content with Content-Range, or 416 Range Not Satisfiable (with Content-Range: bytes */size) when the range starts past the end or is malformed. Several ranges in one request are answered with the whole file, which RFC 9110 allows; - otherwise 200 with the file.  The file is opened as SendFile does, never on the core thread; a missing file, a directory or anything but a regular file fails before anything is sent, so the handler can answer 404.
- `(q Req) PostForm() !link.Values`: PostForm returns the fields of an application/x-www-form-urlencoded request body of a POST, PUT or PATCH request, and nothing for any other request. A body over 10 MiB fails with fault.LimitExceeded, and a malformed field (a bad escape, a semicolon) fails with the first error. Use Multipart for multipart/form-data.
- `(q Req) Form() !link.Values`: Form returns the form fields of the request: those of a urlencoded body first (see PostForm), then those of the URL query, as Go's Request.Form does.
- `(q Req) FormValue(key str) str`: FormValue returns the first value of form field key (see Form), or "" when there is none or the form is malformed.
- `(w mut Out) Redirect(url_in str, code i64)`: Redirect answers with status code (301, 302, 303, 307 or 308) and a Location header, as Go's http.Redirect does: a url without a scheme and host is made absolute against the request's path (relative ones are resolved here, "." and ".." removed, the query kept), bytes outside ASCII are percent-encoded, a GET gets a small HTML body with a link, and a HEAD or a POST none.
- `StuckCores() i64`: StuckCores is how many cores have not turned their event loop for 1.5 seconds: each is running something that does not wait (a handler stuck in a loop, say). 0 while no server runs.
- `StuckFor() i64`: StuckFor is how long, in milliseconds, the most stuck core's event loop has not turned (0: every core turns). A service can export it and alert before a stuck core is an outage.
- `type MultipartReader struct`: MultipartReader reads the parts of a multipart body in order.
- `type Part struct`: Part is one part of a multipart body: its header fields and its content, which Read gives.
- `(q Req) Multipart() !MultipartReader`: Multipart returns a reader for the request's multipart/form-data body. It fails when the Content-Type is not multipart/form-data or has no boundary parameter.
- `NewMultipartReader(body str, boundary str) MultipartReader`: NewMultipartReader reads the multipart body in memory (for example a stored message) with the given boundary, as q.Multipart does a request's.
- `(m mut MultipartReader) SetBufferSize(n i64)`: SetBufferSize sets the size of the reader's read-ahead buffer (at least 128 bytes; the default is 64 KiB): a small buffer makes the body cross buffer boundaries often, which the tests use.
- `(m mut MultipartReader) SetLimit(n i64)`: SetLimit makes reading more than n body bytes fail with fault.LimitExceeded (the headers and the preamble count).
- `(m mut MultipartReader) NextPart() !?Part`: NextPart returns the next part, or nil when the body has no more. What is left of the previous part is skipped.
- `(p Part) Header(name str) str`: Header returns the value of the part's header field name (any case), the first when there are several, or "".
- `(p Part) Headers() []str`: Headers returns every header field of the part as "Name: value".
- `(p Part) FormName() str`: FormName returns the name parameter of the part's Content-Disposition when it is form-data, and "" otherwise.
- `(p Part) FileName() str`: FileName returns the filename parameter of the part's Content-Disposition without its directory (what follows the last "/"), or "".
- `(p mut Part) Read(buf mut []u8) !i64`: Read reads the part's content into buf and returns how many bytes it wrote, 0 at the end of the part. It fails when the body ends inside the part, when reading the body fails and when the reader's limit is passed.
- `(p mut Part) Bytes(max i64) !str`: Bytes reads the whole content of the part, failing with fault.LimitExceeded when it is longer than max bytes.
- `type FormFile struct`: FormFile is one uploaded file of a MultipartForm: the form field, the file's name as sent (without directories), its Content-Type and its bytes.
- `type MultipartForm struct`: MultipartForm is a whole multipart form read into memory.
- `(q Req) MultipartForm(max i64) !MultipartForm`: MultipartForm reads the whole multipart/form-data body into memory: the parts with a filename become Files, the others Values. It fails with fault.LimitExceeded when the body is longer than max bytes.
- `ServeTLS(addr str, certPEM str, keyPEM str, h fn(Req, mut Out)) !`: ServeTLS is Serve over TLS 1.3 (HTTPS): certPEM is the certificate chain (leaf first) and keyPEM the leaf's private key (RSA, or ECDSA P-256 or P-384), as PEM text. The pair is checked before listening. ALPN offers "h2" (HTTP/2) and then "http/1.1"; a client without ALPN gets HTTP/1.1. Each handshake runs in a task, so slow clients never hold a core; it must finish within TIN_HANDSHAKE_TIMEOUT_MS (default: the header timeout, 10 s). Clients without TLS 1.3 are refused with a protocol_version alert, and those whose ALPN offers neither protocol with no_application_protocol.
- `(r Router) ServeTLS(addr str, certPEM str, keyPEM str) !`: ServeTLS is Serve over TLS 1.3, as anvil.ServeTLS: the routes are checked first, then the certificate and key.
- `type TLSConfig struct`: TLSConfig configures ServeTLSConfig: the certificate chain and private key, as ServeTLS takes them, more certificates chosen by the client's server name (#476), and client certificates (mutual TLS, #475).
- `type TLSCert struct`: TLSCert is one certificate chain (leaf first) and its private key: PEM text, or the paths of PEM files, which the server reads again when they change (#476).
- `ReloadCertificates(certs []TLSCert) !`: ReloadCertificates replaces the server's certificates, from any core while it serves: the first is the default, the others are chosen by the client's server name. Every pair is checked first, and a bad one fails the call and changes nothing. Each core switches at its next handshake; connections already up keep their own. Pairs given as files are read now, and when the whole set was given as files, core 0 reads them again every TIN_TLS_RELOAD_S seconds (default 60) and reloads when they changed, so a renewal written to disk needs no call.
- `ServeTLSConfig(addr str, cfg TLSConfig, h fn(Req, mut Out)) !`: ServeTLSConfig is ServeTLS with a TLSConfig. With ClientAuth set, every full handshake asks for a client certificate: RequireClientCert refuses a client without one (certificate_required), and both refuse one that does not chain to ClientCAs for client authentication. A handler finds the verified chain in q.TLSConn().PeerCertificates().
- `(r Router) ServeTLSConfig(addr str, cfg TLSConfig) !`: ServeTLSConfig is Serve over TLS with a TLSConfig, as anvil.ServeTLSConfig.
- `(q Req) TLSConn() ?tls.Conn`: TLSConn is the TLS connection the request arrived on, or nil over plain TCP: for its ALPN(), CipherSuite() and Group(). After Hijack every byte must go through it (Read, Write, Close), since the descriptor carries records.
- `type BodyReader struct`: BodyReader reads a request body: Read fills buf with the next bytes. It is q.BodyStream().
- `(q Req) BodyStream() BodyReader`: BodyStream is the request body as a stream: on a route registered with Router.Stream it arrives as the handler reads it; elsewhere it has arrived whole (and Body has it too). Read the body either with Body or with BodyStream, not with both.
- `(r BodyReader) Read(buf mut []u8) !i64`: Read fills buf with the body's next bytes, waiting for them, and returns how many it wrote: 0 at the end of the body. It fails when the client ends the connection or resets the stream before the end of the body, when no byte comes within the read timeout, and at the request's deadline.

## hearth

Package hearth runs a program on every core: one thread per core, each with its own globals, request pool and ingot heap. Cores share nothing; relay carries messages.

- `Cores() i64`: Cores is the number of CPUs this program may use: the CPUs online, capped on Linux by the affinity mask (cpuset) and the cgroup CPU quota (ceil of cpu.max quota/period); never 0. It is how many cores to start (hearth.Run(hearth.Cores(), entry)), not how many run: relay.Cores() is the number started, and only those read their relay inbox.
- `MemLimit() i64`: MemLimit is the memory limit in bytes the container (cgroup) imposes: 0 when there is none.
- `ID() i64`: ID is the current core's number: 0 for the main core.
- `Run(n i64, entry fn(i64))`: Run starts entry(i) on cores 1..n-1, runs entry(0) here, then waits for every core. Before starting it sizes the request pools to the memory limit and decides whether cores pin themselves to CPUs (only when they map one-to-one onto the allowed CPUs, or TIN_PIN=1). A program starts its cores once: a second Run that would start cores again panics (#858); run every step under one Run, core 0 handing the others work over relay.
- `PoolChunk() i64`: PoolChunk is the request pool chunk size in bytes each core uses (after pool_tune).
- `PoolCapacity() i64`: PoolCapacity is the usable size in bytes of this core's current base pool chunk (0 before its first request allocation).
- `Reset()`: Reset ends the current request: the core's pool is emptied for the next one.
- `HeapStats() (i64, i64, i64)`: HeapStats reports what this core's long-lived heap has from the system (#345): the bytes of its slabs (blocks up to 256 KiB), the bytes of the mappings of its larger blocks (those in use and those kept for reuse) and the number of mappings in all.
- `Quiet(wait fn())`: Quiet runs wait (a tide.Wait, a receive from a channel) with the calling task taken out of the runtime's reclamation epochs (#358). A task that lives for hours, such as a detach loop, holds back the release of every long-lived value dropped on its core while it lives, and past a million waiting blocks the core stops releasing them (RcStats shows the limbo). A task that waits inside Quiet holds back nothing, on the condition that it holds no value it borrowed from long-lived memory across the call: `let u = cache[k]` before Quiet is not safe to use after it, so read it again. websocket.Conn's reads work this way.
- `RcStats() (i64, i64, i64)`: RcStats reports what long-lived memory this core still counts (#176): the number of counted blocks, their bytes and how many dropped blocks wait in the limbo.

## relay

Package relay carries messages between cores, which share no memory. A message is a str copied into the receiving core's inbox (a lock-free multi-producer queue); the receiver gets its own copy in its request pool. Encode structs with argo.Put/argo.Get. Send only to cores below relay.Cores(), the cores the program started: hearth.Cores() is the CPUs it may use, and a message to a core that was never started waits forever.

```tin body
relay.Send(2, "hello")              // from any core
let (from, msg) = relay.Recv()      // on core 2: blocks until a message arrives
let (src, text) = try relay.Next()  // the same, but fails on a deadline or cancel
```

- `Send(to i64, msg str)`: Send copies msg into core to's inbox; it never blocks. A core that was never started (to >= Cores()) never reads it.
- `Broadcast(msg str)`: Broadcast sends msg to every other running core.
- `Cores() i64`: Cores is the number of cores the program started (1 before hearth.Run), the cores whose inboxes are read. hearth.Cores() is a different number: the CPUs the program may use.
- `TryRecv() (i64, str, bool)`: TryRecv returns the next message for this core, if there is one.
- `Recv() (i64, str)`: Recv blocks until a message for this core arrives and returns its sender and text. It blocks the whole core and ignores deadlines and cancels; use Next in tasks and within blocks.
- `Next() !(i64, str)`: Next waits until a message for this core arrives and returns its sender and text. Unlike Recv it waits through rt_task_wait: inside a task the core serves other tasks meanwhile, and a deadline (within, the request's) or a cancel ends the wait with that fault. Under anvil.OnRelay the event loop takes every message, so do not call Next there.
- `WakeFD() i64`: WakeFD is this core's wake-up descriptor, for event loops: after it turns readable, call Drain. Arm must be called before the loop blocks.
- `Arm()`: Arm asks senders to wake this core through WakeFD (call just before blocking).
- `Drain(h fn(i64, str))`: Drain runs h on every waiting message (event loops call it after WakeFD fires).
- `Received() i64`: Received is how many messages this core has taken from its inbox.
- `Me() i64`: Me is this core's number.

## task

Package task reads the deadline and cancellation of the running code, which belong to its innermost boundary (the request, a `within` or `limit` block, a scope's child; Go's context.Context Deadline and Err, without passing a context). Waits already fail when either stops the code: these are for code that does not wait, or that wants to stop at a point of its own choosing.

- `Deadline() i64`: Deadline is the effective deadline of the running code in tide.Now() nanoseconds (the earliest of its request's and every enclosing within block's), or 0 when it has none.
- `Canceled() !`: Canceled is nil while the running code may go on, else the fault its next wait would fail with: fault.DeadlineExceeded once the deadline has passed, fault.LimitExceeded past a budget, or fault.Canceled wrapping the reason of a cancel or drain.

## wire

Package wire is TCP networking and an HTTP client: HTTP/1.1, and HTTP/2 to servers that choose it by ALPN or with Options.H2C (#480). Calls inside a request wait without blocking the core; every connection can carry a read/write timeout.

```tin body
let c = try wire.Dial("127.0.0.1:6379")
try c.Write("PING\r\n")
let r = try wire.Get("http://127.0.0.1:8080/json")
```

- `type Stream struct`: Stream is a response whose body is read as it arrives: an io.Reader. Close it when done with it before its end (Read to the end closes it).
- `type NoBody struct{}`: NoBody is the body of a request that has none, for DoStream.
- `(b mut NoBody) Read(buf mut []u8) !i64`: Read gives nothing: the body has ended.
- `DoStream[R io.Reader](method str, url str, headers []str, body R, opt Options) !Stream`: DoStream sends one request with its body read from body, and returns the response once its headers are in; see the section comment above.
- `type Copied struct`: decimal is a Content-Length header's value. Copied is what DoStreamTo gives back: the response's status and how many body bytes it copied.
- `DoStreamTo[R io.Reader, W io.Writer](method str, url str, headers []str, body R, opt Options, w mut W) !Copied`: DoStreamTo is DoStream with the response's body copied to w as it arrives, a buffer at a time, whatever its status (an error answer's body too).
- `type Head struct`: Head is a response's status and header fields, as DoStreamToHead gives them before the body.
- `(h Head) Header(name str) str`: Header returns the response header name (any case), or "".
- `shape HeadWriter`: HeadWriter is an io.Writer that is told the response's head before its body: a client that must know the status before it keeps a body (an object store's error answer is no object).
- `DoStreamToHead[R io.Reader, W HeadWriter](method str, url str, headers []str, body R, opt Options, w mut W) !Copied`: DoStreamToHead is DoStreamTo with w.Begin called once with the response's status and fields before any body byte is written to w; a fault from Begin ends the call, closing the connection.
- `(s mut Stream) Read(buf mut []u8) !i64`: Read fills buf with the next bytes of the body and returns how many; 0 at its end, after which the connection is back in the pool or closed. A connection that fails or ends early is closed and Read fails: it never gives a truncated body as complete.
- `(s mut Stream) Close()`: Close ends the response: a body not read to its end closes the connection.
- `(s Stream) Header(name str) str`: Header returns the response header name (any case), or "".
- `(s Stream) Length() i64`: Length is the body's length when the response gave it (Content-Length), else -1.
- `type Conn struct`: Conn is a TCP connection.
- `type Listener struct`: Listener accepts TCP connections.
- `type Resp struct`: Resp is an HTTP response.
- `IsEOF(err fault) bool`: EOF is the fault Read returns at the end of the stream.
- `Dial(addr str) !Conn`: Dial connects to "host:port".
- `DialTimeout(addr str, timeout i64) !Conn`: DialTimeout connects to "host:port", giving up after timeout nanoseconds (0: no limit).
- `(c Conn) Fd() i64`: Fd is the connection's descriptor, for clients that do their own I/O on it (it stays non-blocking; Close still closes it).
- `(c mut Conn) SetTimeout(ns i64)`: SetTimeout limits every later read and write to ns nanoseconds (0: no limit).
- `(c Conn) SetNoDelay(on bool)`: SetNoDelay turns Nagle's algorithm off (true) or on.
- `(c Conn) Write(s str) !`: Write sends all of s.
- `(c Conn) WriteBytes(b []u8) !`: WriteBytes sends all of b.
- `(c Conn) Read(buf mut []u8, max i64) !i64`: Read appends up to max bytes to buf and returns how many; at the end it returns 0 and EOF.
- `(c Conn) ReadFull(n i64) !str`: ReadFull reads exactly n bytes.
- `(c mut Conn) Close()`: Close closes the connection.
- `Listen(addr str) !Listener`: Listen opens a TCP listener on "host:port" (":0" picks a free port: see Port).
- `(l Listener) Port() i64`: Port is the port the listener is bound to.
- `(c Conn) LocalPort() i64`: LocalPort is the port this end of the connection uses (what the peer sees as the source port).
- `(c Conn) CloseWrite()`: CloseWrite half-closes the connection: the peer reads the end of the stream after what was written, and this end still reads what the peer sends.
- `(l Listener) Accept() !Conn`: Accept waits for the next connection.
- `(l Listener) AcceptTimeout(timeout i64) !Conn`: AcceptTimeout waits at most timeout ns for the next connection (0: no limit), failing with a fault that says "timed out" when none came. A negative timeout is refused.
- `(l mut Listener) Close()`: Close stops listening.
- `type Options struct`: Options configure one client call (DoWith); the zero value is what Do uses.
- `const DefaultMaxIdle = 8`: DefaultMaxIdle is how many idle connections per host (and core) DoWith keeps when Options.MaxIdle is 0.
- `const DefaultMaxBody = 67108864`: DefaultMaxBody is the largest response body Do accepts (64 MiB, anvil's request limit): a larger one is a fault rather than memory a broken or hostile server can fill.
- `Get(url str) !Resp`: Get fetches url.
- `Post(url str, ctype str, body str) !Resp`: Post sends body with content type ctype to url.
- `Do(method str, url str, headers []str, body str) !Resp`: Do sends one request: headers is a list of name, value pairs. The method and header names must be tokens, and the URL and header values must not hold CR, LF, NUL or other control bytes (the URL no spaces either), or Do fails instead of sending a request an input could have split. Response bodies over DefaultMaxBody fail; DoWith sets a timeout and the limit.  Connections are kept alive: after a response that ends cleanly (HTTP/1.1, framed by a length or chunks, no "Connection: close") the connection waits in a per-core pool, by scheme, host and port (and TLS settings), and the next call to that host uses it instead of dialing and, for https, doing a TLS handshake. A kept connection is checked before it is used, dropped after 30 s idle, and at most Options.MaxIdle are kept per host. One the server closed meanwhile is replaced by a new connection without the caller seeing it, for a GET, HEAD, PUT, DELETE, OPTIONS or TRACE; any other method (a POST) fails instead of being sent twice.  Do does not follow redirects: a 3xx is returned as the response, with its Location header (Go follows up to 10). Response lines must end in CRLF; a response with bare LF line ends fails (Go accepts it).
- `DoWith(method str, url str, headers []str, body str, opt Options) !Resp`: DoWith is Do with options: an overall timeout and a response size limit.
- `(r Resp) Header(name str) str`: Header returns the response header name (any case), or "".
- `(r Resp) Trailer(name str) str`: Trailer returns the response trailer name (any case), or "": HTTP/2 responses carry trailers (gRPC's grpc-status, for one; #480).
- `(r Resp) Fields() []str`: Fields returns every header field of the response as "Name: value", in the order they came, the name as sent and the value without the blanks around it: all the Set-Cookie fields, for a cookie jar, and the whole head, for a dump (#739).
- `(r Resp) Proto() str`: Proto is the protocol of the response: "HTTP/1.1" or "HTTP/1.0" as its status line says, "HTTP/2.0" for HTTP/2.
- `(r Resp) Reason() str`: Reason is the reason phrase of the status line ("OK" in "HTTP/1.1 200 OK"), "" when there is none (HTTP/2 has none).

## httptrace

Package httptrace provides the HTTP client hooks wire can observe on HTTP/1.1 and TLS. DNS and connect hooks are unavailable because wire's platform resolver combines those phases. HTTP/2 requests currently use a separate path and report only GetConn and TLS handshake hooks.

- `type ClientTrace struct`: ClientTrace contains callbacks for observable HTTP client phases.

## pprof

Package pprof exposes Go-compatible profiling route names for anvil and reports which profiles the Tin runtime cannot provide.

- `Register(r mut anvil.Router)`: Register adds the standard pprof route paths to r. Tin currently has no runtime profile source, so profile requests return 501.

## jar

Package jar is a cookie jar for HTTP clients, as Go's net/http/cookiejar is (#739): it keeps the cookies servers set (RFC 6265 parsing, domain and path matching, Secure, expiry by Max-Age and Expires, HttpOnly) and gives each request the ones it should carry. Do sends a wire request with the jar's cookies and keeps the cookies of its response.

```tin body
mut j = jar.New()
let r = try j.Do("GET", "http://127.0.0.1:8080/login", []str{}, "")
let r2 = try j.Do("GET", "http://127.0.0.1:8080/account", []str{}, "") // sends the session cookie
```

Public suffixes: like Go's cookiejar.New(nil), New has no public suffix list, so a host may set a cookie for its parent domain whatever it is (a server at a.co.uk may set Domain=co.uk). The list is not in the standard library (Go keeps it in golang.org/x/net/publicsuffix); a program that talks to hosts it does not trust passes one to WithSuffixes, a function that returns a domain's public suffix as Go's PublicSuffixList.PublicSuffix does.

Cookies are anvil.Cookie values, the type anvil's SetCookie writes: Expires is in Unix seconds and 0 means none, so an Expires at the Unix epoch itself is read as -1 (also in the past). Host names must be ASCII (Go turns others into punycode first: here they get no cookies). The jar is not written to a file, as Go's is not.

- `type Jar struct`: Jar holds cookies. The zero value is not usable: make one with New or WithSuffixes.
- `New() Jar`: New returns an empty jar with no public suffix list.
- `WithSuffixes(suffix fn(str) str) Jar`: WithSuffixes returns an empty jar that asks suffix for a domain's public suffix ("co.uk" for "a.b.co.uk", "" when it has none), as Go's cookiejar.Options.PublicSuffixList: a cookie's Domain may not be a public suffix but for the host itself.
- `(j mut Jar) SetClock(now fn() i64)`: SetClock makes the jar read the time from now (Unix nanoseconds) instead of the wall clock: for tests of expiry.
- `(j Jar) Len() i64`: Len is the number of cookies held, expired ones that no request has looked at yet included.
- `ParseSetCookie(line str) !anvil.Cookie`: ParseSetCookie parses a Set-Cookie field value as Go's http.ParseSetCookie does: the name and value (a value in double quotes is unquoted and marked Quoted), then the attributes Path, Domain, Expires (RFC 1123, or with dashes in the date), Max-Age (0 or less becomes -1: delete), Secure, HttpOnly, SameSite and Partitioned, in any case. An attribute with a bad value or an unknown one is ignored. It fails on an empty line, a missing "=", a bad name or a bad value.
- `ParseSetCookies(fields []str) []anvil.Cookie`: ParseSetCookies parses every Set-Cookie field of a response (header field lines "Name: value", as wire.Resp.Fields gives them) and returns the cookies that parse, in order.
- `(j mut Jar) SetCookies(url str, cookies []anvil.Cookie)`: SetCookies keeps the cookies a response from url set, as Go's Jar.SetCookies: a cookie without a Path gets the URL's directory, one without a Domain is a host-only cookie, a Domain the host is not in (or, with a list, a public suffix) is refused, and a Max-Age of 0 or less or an Expires in the past deletes the cookie of that name, domain and path. url must be http:// or https://; another URL sets nothing.
- `(j mut Jar) Cookies(url str) []anvil.Cookie`: Cookies returns the cookies to send in a request to url, as Go's Jar.Cookies: those whose domain and path match it and that have not expired (a Secure cookie only over https://), longest path first, then the oldest first. Each has only its Name, Value and Quoted set. Expired cookies are dropped from the jar on the way.
- `(j mut Jar) Header(url str) str`: Header is the Cookie field value a request to url carries ("a=1; b=2", as Go's Request.AddCookie writes each cookie), or "" when the jar has none for it.
- `(j mut Jar) Do(method str, url str, headers []str, body str) !wire.Resp`: Do sends a request with wire.Do, carrying the jar's cookies for url (added to a Cookie field in headers, if there is one, as Go's client does), and keeps the cookies the response sets. headers is a list of name, value pairs.
- `(j mut Jar) DoWith(method str, url str, headers []str, body str, opt wire.Options) !wire.Resp`: DoWith is Do with wire's options.

## dump

Package dump writes HTTP requests and responses out as text, byte for byte as Go's httputil.DumpRequest and httputil.DumpResponse do (#739): for logs, for debugging a client or a handler, and for tests that compare what went over the wire.

```tin
fn handle(q anvil.Req, w mut anvil.Out) {
	herald.Info(dump.Request(q, false))
}
```

Dumping the response a client got:

```tin body
let r = try wire.Get("http://127.0.0.1:8080/")
say.Text(dump.Response(r, true))
```

Request takes the request a handler serves (Go's server-side Request); Response takes the response a wire call returned. The header fields are written as Go writes them: names in canonical form ("content-type" becomes "Content-Type"), sorted by name, the values of one name in the order they came. Bodies are written as they were framed: a chunked body as one chunk and the last chunk, any other as it is. tools/ci/dump_check.tin compares both with Go's over a corpus.

Not reproduced: an absolute-form request target ("GET http://host/x") is written as its path with a Host field (Go keeps the URL and writes no Host); a status line without a reason phrase ("HTTP/1.1 200") is written "HTTP/1.1 200 " (Go writes "HTTP/1.1 200 200"); the trailers of an HTTP/1.1 chunked response, which wire does not keep.

- `Request(q anvil.Req, body bool) str`: Request returns the request q as text, as Go's httputil.DumpRequest(req, body): the request line, the Host field, a Transfer-Encoding: chunked field for a chunked request, the other fields (Cache-Control: no-cache added after a Pragma: no-cache, as Go's server does), an empty line and, when body is true, the body (chunked again when it came chunked). A request on a Router.Stream route has no body here: its body is read with BodyStream.
- `Response(r wire.Resp, body bool) str`: Response returns the response r as text, as Go's httputil.DumpResponse(resp, body): the status line, a Connection: close field when the connection ends after it (HTTP/1.0 without keep-alive, a body read to the end of the connection), the framing (Content-Length, or Transfer-Encoding: chunked), the other fields, an empty line and, when body is true, the body.

## proxy

Package proxy forwards HTTP requests to an upstream server with bounded memory, like Go's net/http/httputil.ReverseProxy.

A basic proxy:

```tin body
let p = proxy.New("http://127.0.0.1:8081")
let r = anvil.NewRouter()
r.Stream("POST", `/{path...}`, p.ServeHTTP)
r.Get(`/{path...}`, p.ServeHTTP)
r.Serve(":8080") catch err { say.Line(err) }
```

Set Director to rewrite a request to a complete upstream URL. ModifyResponse can edit the upstream status and fields and fail or reject them before they are written; ErrorHandler replaces the default 502 response. The proxy removes hop-by-hop fields and appends the caller's address to X-Forwarded-For. Register request-body routes with Router.Stream.

Once the response head is sent its status cannot change, so a failure in the upstream body is not handed to ErrorHandler. The proxy logs it once with herald and aborts the response: the client sees the response end early instead of a body that looks complete, as Go's ReverseProxy aborts the handler.

- `type Response struct`: Response is the upstream status and headers before they are copied to the client.
- `type Proxy struct`: Proxy is an HTTP reverse proxy. Target is an http:// URL. Director, when set, returns the complete upstream URL for each request, or an empty string to use Target. Use New to get default hooks.
- `New(target str) Proxy`: New returns a proxy with default hook functions. Set hooks before registering ServeHTTP.
- `DefaultErrorHandler(q anvil.Req, w mut anvil.Out, err fault)`: DefaultErrorHandler writes Go ReverseProxy's default 502: the status with no body (anvil adds its text/plain content type).
- `(p Proxy) ServeHTTP(q anvil.Req, w mut anvil.Out)`: ServeHTTP handles a request and can be registered with anvil.Router.Stream. Requests and responses reuse one 32 KiB buffer in each direction; neither body is accumulated.

## cgi

Package cgi runs an anvil handler, or a Router, as a CGI program (RFC 3875) the way Go's net/http/cgi does. Serve reads the request from the environment and standard input and writes the response to standard output. Call and Format are the same steps on values, for cgi/fcgi and tests. The request goes through anvil's in-process path (Router.RunWith), so RemoteAddr and TLS are empty.

- `Serve(r anvil.Router) !`: Serve runs r as a CGI program: the request comes from the environment and standard input, the response goes to standard output.
- `ServeFunc(h fn(anvil.Req, mut anvil.Out)) !`: ServeFunc is Serve for one handler h on every path and method.
- `Call(r anvil.Router, env map[str]str, body str) !anvil.Out`: Call answers the request the CGI variables env describe, with body as its body, through r: Go's cgi.RequestFromMap, then the handler.
- `Format(code i64, headers []str, body str, fastcgi bool) str`: Format is the response bytes for a status code, its header fields (name and value pairs) and its body: the Status line, the fields sorted by canonical name, a blank line, then the body. fastcgi gives Go's fcgi child instead: a Date, and no Content-Type on 304.

## cgi/fcgi

Package fcgi runs an anvil handler, or a Router, as a FastCGI responder: the record protocol of Go's net/http/fcgi (responder role). Serve answers the connections one after another, and each connection's requests in order, each when its stdin ends (Go answers them concurrently, which a sequential client cannot tell apart). The response is the bytes cgi.Format gives, cut into STDOUT records, with Go's Date header and its error for a request whose variables are malformed (a 500 and the message on STDERR).

- `Serve(l wire.Listener, r anvil.Router) !`: Serve answers FastCGI requests that arrive on l with r, one connection after another, until l fails. A task spawned per connection would not run while this loop waits in Accept (see packages/rpc).
- `ServeFunc(l wire.Listener, h fn(anvil.Req, mut anvil.Out)) !`: ServeFunc is Serve for one handler h on every path and method.

## assay

Package assay provides small HTTP test helpers for anvil handlers, like net/http/httptest (#739).

- `type Server value struct`: Server is a local HTTP/1.1 test server. Close stops its listener and waits for the accept loop.
- `NewRecorder() anvil.Out`: NewRecorder returns an empty anvil response recorder.
- `NewRequest(method str, target str, headers []str, body str) anvil.Req`: NewRequest builds a request for a handler test; headers are "Name: value" lines.
- `NewServer(router anvil.Router) !Server`: NewServer starts an HTTP/1.1 server for router on a random loopback port.
- `(s Server) Close()`: Close stops accepting requests and waits for the accept loop. A request already accepted may finish before Close returns.

## tls

Package tls is TLS 1.3 (RFC 8446) and TLS 1.2 (RFC 5246). Clients: tls.Dial connects and handshakes, and Conn reads and writes like wire.Conn; the server's certificate is verified by default against the system's roots (plus Config.RootCAs). A server's NewSessionTicket is kept (per core, for the same name and settings) and offered on the next connection to it, which then resumes without the certificate messages (Conn.Resumed). Servers: anvil.ServeTLS serves HTTPS with this package; LoadServerConfig reads a certificate chain and its key (RSA, ECDSA P-256 or P-384), and Server runs the server side over an accepted wire.Conn. Cipher suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384 and TLS_CHACHA20_POLY1305_SHA256; key exchange X25519MLKEM768 (post-quantum hybrid, ML-KEM-768 with X25519) or X25519, or P-256 by HelloRetryRequest. TLS 1.2, for peers that stop there, has the six ECDHE suites with AES-GCM or ChaCha20-Poly1305 and the extended master secret; 1.3 is preferred, and Config.MinVersion (ServerConfig.MinVersion) VersionTLS13 turns 1.2 off. No 0-RTT, no renegotiation, no 1.2 session resumption and nothing older than 1.2. Every wait lets the core serve other tasks and honours Config.Timeout during the handshake, SetTimeout afterwards and a request's deadline.

```tin body
let c = try tls.Dial("example.com:443", tls.Config{ALPN: []str{"http/1.1"}})
try c.Write("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
```

- `const NoClientCert = 0`: NoClientCert, RequestClientCert and RequireClientCert are ServerConfig.ClientAuth: ask for no client certificate; ask for one and verify it when the client sends one; require a verified one.
- `const RequestClientCert = 1`
- `const RequireClientCert = 2`
- `CheckServerConfig(cfg ServerConfig) !`: CheckServerConfig checks the client-certificate settings of cfg before a server starts: a known ClientAuth, and ClientCAs that hold certificates when it asks for any.
- `type Conn struct`: Conn is a TLS 1.3 connection over a wire.Conn. After the handshake its memory only changes in place (record buffers made once, keys rewritten by seal.AEAD.Rekey), so a Conn stays valid wherever it lives: a request's pool, or keep()'s long-lived heap for a client that holds connections across requests.
- `(c Conn) Taken() Conn`: Taken is c as a Conn of the running request: the same connection in the same state, in a struct of its own. A pool that keeps Conns in long-lived memory (wire's) gives a request the one it takes off the pool this way, so the request's reads and writes, which may store request memory into the Conn, never store it into long-lived memory; the pool keeps a copy again when the Conn comes back (#1036). It copies every field: a field added to Conn is added here as well.
- `const TLS_AES_128_GCM_SHA256 = 0x1301`: TLS_AES_128_GCM_SHA256 is cipher suite 0x1301 (Conn.CipherSuite).
- `const TLS_AES_256_GCM_SHA384 = 0x1302`: TLS_AES_256_GCM_SHA384 is cipher suite 0x1302.
- `const TLS_CHACHA20_POLY1305_SHA256 = 0x1303`: TLS_CHACHA20_POLY1305_SHA256 is cipher suite 0x1303.
- `type ServerConfig struct`: ServerConfig configures a TLS server: its certificate chain and private key, and the application protocols it speaks.
- `LoadServerConfig(certPEM str, keyPEM str) !ServerConfig`: LoadServerConfig reads a PEM certificate chain (leaf first) and the leaf's PEM private key and checks that they belong together.
- `Server(conn wire.Conn, cfg ServerConfig) !Conn`: Server runs the server side of the handshake over an accepted connection. The Conn owns conn from then on: its Close closes conn. Every wait lets the core serve other tasks.
- `ServerOnFd(fd i64, cfg ServerConfig) !Conn`: ServerOnFd runs the server handshake on a socket another package owns (anvil): the Conn never closes fd. Used with ReadRaw and SealRaw.
- `(c mut Conn) ReadRaw(p i64, cap i64) (i64, []u8)`: ReadRaw reads what the socket has without waiting, decrypts whole records and copies up to cap bytes of application data to the raw buffer at p. It returns the bytes copied (more than 0; -1 when nothing is available yet; 0 once the peer closed with close_notify or end of input; -2 when the connection is broken) and ciphertext the caller must send next: a KeyUpdate answer, or for -2 the alert to send before closing. It never waits.
- `(c mut Conn) ClosedRaw() (bool, []u8)`: ClosedRaw reports, without waiting, whether the peer has ended the connection: its close_notify or another alert arrived, the socket reached end of input, or it failed. It decrypts what the socket has, record by record, and stops at the first one of application data, which stays buffered for ReadRaw; a KeyUpdate answer (or the alert to send) is returned for the caller to send. For a stream that asks whether its client went away: a peek at the socket sees only ciphertext.
- `SealRawSize(n i64) i64`: SealRawSize is the most bytes SealRawTo writes for n bytes of application data.
- `(c mut Conn) SealRaw(p i64, n i64) ![]u8`: SealRaw encrypts n bytes of application data at the raw address p into records (16 KiB each, a KeyUpdate first when the write key is worn out) for the caller to send.
- `(c mut Conn) SealRawTo(p i64, n i64, dst i64) !i64`: SealRawTo is SealRaw into raw memory at dst, which holds SealRawSize(n) bytes; it returns the bytes written. Each record is built and sealed in place there, so nothing it allocates grows with n: an event loop seals into a buffer it reuses.
- `(c mut Conn) CloseNotifyRaw() []u8`: CloseNotifyRaw is the close_notify alert record to send before closing.
- `(c Conn) PendingRaw() bool`: PendingRaw reports whether the Conn holds input ReadRaw has not returned yet: decrypted data, or bytes of a record read from the socket. An event loop that stopped reading (its output was blocked) calls ReadRaw again when this is true, since the socket will not report that input.
- `(c mut Conn) ReleaseRaw()`: ReleaseRaw ends a Conn kept in long-lived memory before its owner drops it: it marks it closed and resets the failure text, which a failed Read or Write made in a request's pool, so releasing the Conn never follows a pointer into a pool that is gone. Nothing is sent.
- `SetTicketSecret(key secret []u8) !`: SetTicketSecret sets the 32-byte secret the server's session-ticket keys are derived from. Servers that share it (several processes behind one load balancer) resume each other's sessions. Call it before the server starts; the default is a random secret per process, or the 64 hex digits of TIN_TLS_TICKET_SECRET.
- `type Credential struct`: Credential is a certificate chain (DER, leaf first), its private key, and the names its leaf covers (its DNS names and IP addresses, lower case), for ServerConfig.Others.
- `LoadCredential(certPEM str, keyPEM str) !Credential`: LoadCredential reads a PEM certificate chain (leaf first) and the leaf's PEM private key and checks that they belong together.
- `type Config struct`: Config configures a client connection; the zero value verifies the server against the system's roots for the name in the address.
- `Dial(addr str, cfg Config) !Conn`: Dial connects to "host:port" and runs the handshake. ServerName defaults to host.
- `Client(conn wire.Conn, cfg Config) !Conn`: Client runs the handshake over an established connection, for protocols that switch to TLS mid-stream (MySQL, PostgreSQL). cfg.ServerName is required unless InsecureSkipVerify is set. The Conn owns conn from then on: its Close closes conn.
- `(c mut Conn) SetTimeout(ns i64)`: SetTimeout limits every later read and write to ns nanoseconds (0: no limit).
- `(c mut Conn) SetDeadline(at i64)`: SetDeadline makes every later wait fail once the monotonic clock (tide.Now) passes at (0: no deadline), whatever the per-call timeout: wire uses it for a whole HTTP call.
- `(c Conn) ALPN() str`: ALPN is the application protocol the server chose ("" when none).
- `(c Conn) CipherSuite() i64`: CipherSuite is the negotiated cipher suite (TLS_AES_128_GCM_SHA256 and so on).
- `(c Conn) Group() str`: Group is the key exchange: "X25519MLKEM768" (post-quantum hybrid, #479), "X25519", or "P-256" when the server asked for it.
- `const VersionTLS13 = 0x0304`: VersionTLS13 is TLS 1.3's protocol version (Conn.Version).
- `(c Conn) Version() i64`: Version is the negotiated protocol version: VersionTLS13 or VersionTLS12.
- `(c Conn) Resumed() bool`: Resumed reports whether the handshake resumed an earlier session with a ticket: the server's certificate was checked on that session, and PeerCertificates is empty.
- `(c Conn) PeerCertificates() [][]u8`: PeerCertificates is the peer's certificate chain as sent (DER, leaf first): on a client the server's, on a server the client's when it sent one (mutual TLS, #475).
- `(c Conn) Fd() i64`: Fd is the connection's descriptor (for waiting on it; never read or write it directly).
- `(c Conn) Buffered() i64`: Buffered is how many decrypted bytes a Read returns without waiting.
- `(c mut Conn) Read(buf mut []u8, max i64) !i64`: Read appends up to max bytes of application data to buf and returns how many; after the server's close_notify it fails with EOF (wire.IsEOF), and a connection the server drops without close_notify is a fault, not EOF (a truncation would otherwise look complete).
- `(c mut Conn) ReadNow(buf mut []u8, max i64) !i64`: ReadNow is Read without waiting: it returns 0 when no application data can be had without waiting for the socket (then wait until Fd is readable and call it again). For clients that run their own non-blocking loop; data TLS has already buffered is always returned first.
- `(c mut Conn) ReadNowTo(p i64, max i64) !i64`: ReadNowTo is ReadNow into the raw buffer at p, at most max bytes: for trusted code that keeps its own buffers (the kafka client reads frames of many megabytes this way, with no copy per record).
- `(c mut Conn) ReadFull(n i64) !str`: ReadFull reads exactly n bytes.
- `(c mut Conn) WriteBytes(b []u8) !`: WriteBytes sends all of b.
- `(c mut Conn) Write(s str) !`: Write sends all of s.
- `(c mut Conn) Close()`: Close sends close_notify and closes the connection; closing twice does nothing.
- `const VersionTLS12 = 0x0303`: VersionTLS12 is TLS 1.2's protocol version (Conn.Version, Config.MinVersion).
- `const TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = 0xc02b`: The TLS 1.2 cipher suites (all ECDHE with an AEAD).
- `const TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 = 0xc02c`
- `const TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = 0xc02f`
- `const TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 = 0xc030`
- `const TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 = 0xcca8`
- `const TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 = 0xcca9`

## hpack

Package hpack is HPACK (RFC 7541), HTTP/2's header compression, for HTTP/2 clients (wire, #480): a Decoder that keeps one connection's dynamic table and decodes Huffman-coded strings, and Encode, which writes a header list with static-table names and plain literals that are never indexed, so it keeps no state and adds nothing to the peer's table. anvil's server has its own decoder, which hands fields over without copying them.

```tin body
mut block = make([]u8, 0, 64)
hpack.Encode(mut block, []hpack.Field{hpack.Field{Name: ":status", Value: "200"}})
let d = hpack.NewDecoder(4096, 65536)
let fields = try d.Decode(block)
```

- `type Field struct`: Field is one header field.
- `type Decoder struct`: Decoder decodes the header blocks one peer sends on a connection, in order: its dynamic table carries from block to block. The table is in malloc'd memory, so a decoder kept with a connection outlives the requests that used it; Free releases it.
- `NewDecoder(tableSize i64, listMax i64) Decoder`: NewDecoder is a decoder for a peer allowed a table of tableSize bytes (4096 unless the connection's settings say otherwise, at most 8192) whose header lists stay within listMax bytes.
- `(d Decoder) Free()`: Free releases the decoder's table; the decoder must not be used again.
- `(d Decoder) Decode(block []u8) ![]Field`: Decode decodes one header block (the fragments of a HEADERS frame and its CONTINUATIONs, joined). An error is a COMPRESSION_ERROR: the connection must end, since the table is no longer the peer's.
- `Encode(b mut []u8, fields []Field)`: Encode appends the header block of fields to b: a static entry where one matches name and value exactly, else a literal without indexing (with a static name where there is one). Names must be lowercase, as HTTP/2 requires.

## twine

Package twine manipulates UTF-8 strings (like Go's strings), with Unicode case mapping, folding and white space from glyph's tables.

- `Clone(s str) str`: Clone returns a copy of s that shares no memory with it.
- `CutPrefix(s str, prefix str) (str, bool)`: CutPrefix returns s without the leading prefix and true, or s and false when it does not start with prefix.
- `CutSuffix(s str, suffix str) (str, bool)`: CutSuffix returns s without the trailing suffix and true, or s and false when it does not end with suffix.
- `SplitAfter(s str, sep str) []str`: SplitAfter slices s after every sep (into runes when sep is empty) and returns the pieces, each ending with sep.
- `SplitAfterN(s str, sep str, n i64) []str`: SplitAfterN is SplitAfter returning at most n pieces (all when n < 0, none when n == 0).
- `LastIndexAny(s str, chars str) i64`: LastIndexAny returns the byte offset of the last rune of s that is in chars, or -1.
- `ToValidUTF8(s str, replacement str) str`: ToValidUTF8 returns s with each run of invalid UTF-8 bytes replaced by replacement.
- `Lines(s str) []str`: Lines returns the lines of s, each ending with its newline ("\n", and a final line may lack one).
- `type Replacer struct`: Replacer replaces a list of strings with replacements, in one pass over the text.
- `NewReplacer(oldnew []str) Replacer`: NewReplacer returns a Replacer from a list of old, new string pairs. Replacements are made in the order they appear in the text, without overlapping matches; at one position the old strings are tried in argument order. An empty old string matches at the start and after every byte. It panics when the list has an odd length.
- `(r Replacer) Replace(s str) str`: Replace returns s with all replacements performed.
- `IndexByte(s str, c u8) i64`: IndexByte returns the byte offset of the first c in s, or -1.
- `IndexByteFrom(s str, from i64, c u8) i64`: IndexByteFrom returns the byte offset of the first c in s at or after from, or -1 (also when from is past the end): IndexByte of s[from:] without copying that slice.
- `LastIndexByte(s str, c u8) i64`: LastIndexByte returns the byte offset of the last c in s, or -1.
- `Index(s str, sub str) i64`: Index returns the byte offset of the first sub in s, or -1 (0 for an empty sub).
- `LastIndex(s str, sub str) i64`: LastIndex returns the byte offset of the last sub in s, or -1 (len(s) for an empty sub).
- `Contains(s str, sub str) bool`: Contains reports whether sub occurs in s.
- `ContainsByte(s str, c u8) bool`: ContainsByte reports whether byte c occurs in s.
- `HasPrefix(s str, prefix str) bool`: HasPrefix reports whether s starts with prefix.
- `HasSuffix(s str, suffix str) bool`: HasSuffix reports whether s ends with suffix.
- `Split(s str, sep str) []str`: Split slices s around every sep (into runes when sep is empty) and returns the pieces.
- `SplitN(s str, sep str, n i64) []str`: SplitN is Split returning at most n pieces (all when n < 0, none when n == 0).
- `Join(elems []str, sep str) str`: Join concatenates elems with sep between them.
- `Repeat(s str, count i64) str`: Repeat returns s concatenated count times (empty when count <= 0; panics when the length overflows).
- `Count(s str, sub str) i64`: Count returns the number of non-overlapping sub in s (RuneCount+1 when sub is empty).
- `Replace(s str, old str, repl str, n i64) str`: Replace returns s with the first n non-overlapping old replaced by repl (all when n < 0; empty old matches at every rune boundary).
- `ReplaceAll(s str, old str, repl str) str`: ReplaceAll returns s with every non-overlapping old replaced by repl.
- `TrimLeft(s str, cutset str) str`: TrimLeft returns s without its leading runes that are in cutset.
- `TrimRight(s str, cutset str) str`: TrimRight returns s without its trailing runes that are in cutset.
- `Trim(s str, cutset str) str`: Trim returns s without leading and trailing runes that are in cutset.
- `TrimSpace(s str) str`: TrimSpace returns s without leading and trailing white space (ASCII, U+0085, U+00A0).
- `TrimPrefix(s str, prefix str) str`: TrimPrefix returns s without the leading prefix, or s unchanged.
- `TrimSuffix(s str, suffix str) str`: TrimSuffix returns s without the trailing suffix, or s unchanged.
- `Compare(a str, b str) i64`: Compare returns -1, 0 or 1 ordering a and b bytewise.
- `IndexRune(s str, r i32) i64`: IndexRune returns the byte offset of the first r in s, or -1.
- `ContainsRune(s str, r i32) bool`: ContainsRune reports whether rune r occurs in s.
- `IndexAny(s str, chars str) i64`: IndexAny returns the byte offset of the first rune of s that is in chars, or -1.
- `ContainsAny(s str, chars str) bool`: ContainsAny reports whether any rune of chars occurs in s.
- `Cut(s str, sep str) (str, str, bool)`: Cut splits s around the first sep, returning (before, after, true), or (s, "", false) when absent.
- `type Builder struct`: Builder accumulates bytes; the zero Builder{} is ready to use, NewBuilder preallocates.
- `NewBuilder(n i64) Builder`: NewBuilder returns an empty Builder with room for n bytes.
- `(b mut Builder) Str(s str)`: Str appends s.
- `(b mut Builder) Byte(c u8)`: Byte appends one byte.
- `(b mut Builder) Rune(r i32)`: Rune appends the UTF-8 encoding of r.
- `(b mut Builder) Int(v i64)`: Int appends v in decimal.
- `(b Builder) Len() i64`: Len returns the number of bytes accumulated.
- `(b Builder) String() str`: String returns a copy of the accumulated bytes as a str.
- `(b Builder) Bytes() []u8`: Bytes returns the accumulated bytes without copying (aliases the Builder).
- `(b Builder) Cap() i64`: Cap returns the number of bytes the Builder can hold without growing.
- `(b mut Builder) Grow(n i64)`: Grow makes room for n more bytes.
- `(b mut Builder) Write(p []u8)`: Write appends p.
- `(b mut Builder) Reset()`: Reset empties the Builder but keeps its capacity.
- `Map(mapping fn(i32) i32, s str) str`: Map returns s with every rune replaced by mapping(rune); a rune mapped to a negative value is dropped. Invalid UTF-8 bytes reach mapping as U+FFFD, and a rune mapped to it is written as U+FFFD.
- `ToUpper(s str) str`: ToUpper returns s with every letter mapped to upper case.
- `ToLower(s str) str`: ToLower returns s with every letter mapped to lower case.
- `ToTitle(s str) str`: ToTitle returns s with every letter mapped to title case.
- `Title(s str) str`: Title returns s with the first letter of each word mapped to title case. It cannot tell where words start in every script (the apostrophe in "they're" starts one): it is Go's deprecated strings.Title.
- `EqualFold(s str, t str) bool`: EqualFold reports whether s and t are equal under Unicode simple case folding.
- `Fields(s str) []str`: Fields splits s around runs of white space (Unicode's) and returns the non-empty pieces.
- `FieldsFunc(s str, f fn(i32) bool) []str`: FieldsFunc splits s around runs of runes for which f is true and returns the non-empty pieces.
- `IndexFunc(s str, f fn(i32) bool) i64`: IndexFunc returns the byte offset of the first rune for which f is true, or -1.
- `LastIndexFunc(s str, f fn(i32) bool) i64`: LastIndexFunc returns the byte offset of the last rune for which f is true, or -1.
- `ContainsFunc(s str, f fn(i32) bool) bool`: ContainsFunc reports whether f is true for any rune of s.
- `TrimLeftFunc(s str, f fn(i32) bool) str`: TrimLeftFunc returns s without the leading runes for which f is true.
- `TrimRightFunc(s str, f fn(i32) bool) str`: TrimRightFunc returns s without the trailing runes for which f is true.
- `TrimFunc(s str, f fn(i32) bool) str`: TrimFunc returns s without the leading and trailing runes for which f is true.

## glyph

Package glyph is UTF-8 (like Go's unicode/utf8) and Unicode: general categories, scripts, properties and case mapping, from the same tables as Go's unicode package (see UnicodeVersion).

- `const RuneError = 0xfffd`: RuneError is the replacement character returned for invalid UTF-8.
- `const MaxRune = 0x10ffff`: MaxRune is the largest valid Unicode code point.
- `const UTFMax = 4`: UTFMax is the maximum number of bytes one encoded rune occupies.
- `ValidRune(r i32) bool`: ValidRune reports whether r can be legally encoded as UTF-8.
- `RuneLen(r i32) i64`: RuneLen returns the number of bytes needed to encode r, or -1 if r is not a valid rune.
- `EncodeRune(b mut []u8, r i32) i64`: EncodeRune appends the UTF-8 encoding of r to b (RuneError if invalid) and returns the byte count.
- `RuneStr(r i32) str`: RuneStr returns r encoded as a one-rune string (RuneError if invalid).
- `DecodeRune(s str, i i64) (i32, i64)`: DecodeRune decodes the rune starting at byte i of s, returning (RuneError, 1) for bad bytes and (RuneError, 0) at the end.
- `DecodeLastRune(s str, end i64) (i32, i64)`: DecodeLastRune decodes the last rune of s[0:end], returning its rune and size ((RuneError, 0) when end <= 0).
- `RuneStart(b u8) bool`: RuneStart reports whether byte b could be the first byte of an encoded rune (not a continuation byte).
- `FullRune(s str, i i64) bool`: FullRune reports whether s[i:] begins with a complete encoded rune (invalid bytes count as complete).
- `RuneCount(s str) i64`: RuneCount returns the number of runes in s, counting each invalid byte as one rune.
- `Valid(s str) bool`: Valid reports whether s is entirely valid UTF-8.
- `const UnicodeVersion = "17.0.0"`: UnicodeVersion is the version of the Unicode Character Database the tables come from.
- `type Table enum`: Table names a set of code points by Unicode's own name: a general category (Lu, Nd, P), a script (Latin, Han, Arabic) or a property (White_Space, Dash). Use it with Is.
- `TableOf(name str) ?Table`: TableOf returns the table with a Unicode name: a general category (Lu, Nd, P), a script (Latin, Han, Arabic) or a property (White_Space, Dash). It returns nil for a name with no table, so a pattern like \p{Greek} can be refused.
- `TableRanges(t Table) []i64`: TableRanges returns the table's code points as low, high pairs, with strides expanded, for a caller that builds its own classes (lasso's \p{...}).
- `Is(t Table, r i32) bool`: Is reports whether r is in the set t.
- `IsOneOf(sets []Table, r i32) bool`: IsOneOf reports whether r is in any of the sets.
- `IsLetter(r i32) bool`: IsLetter reports whether r is a letter (category L).
- `IsDigit(r i32) bool`: IsDigit reports whether r is a decimal digit (category Nd).
- `IsNumber(r i32) bool`: IsNumber reports whether r is a number (category N).
- `IsSpace(r i32) bool`: IsSpace reports whether r is white space as Unicode defines it (property White_Space): tab, line feed, vertical tab, form feed, carriage return, space, U+0085, U+00A0 and the Unicode space separators.
- `IsUpper(r i32) bool`: IsUpper reports whether r is an upper-case letter (category Lu).
- `IsLower(r i32) bool`: IsLower reports whether r is a lower-case letter (category Ll).
- `IsTitle(r i32) bool`: IsTitle reports whether r is a title-case letter (category Lt).
- `IsMark(r i32) bool`: IsMark reports whether r is a mark (category M).
- `IsPunct(r i32) bool`: IsPunct reports whether r is punctuation (category P).
- `IsSymbol(r i32) bool`: IsSymbol reports whether r is a symbol (category S).
- `IsControl(r i32) bool`: IsControl reports whether r is a control character: U+0000 to U+001F and U+007F to U+009F.
- `IsGraphic(r i32) bool`: IsGraphic reports whether r is a letter, mark, number, punctuation, symbol or space separator.
- `IsPrint(r i32) bool`: IsPrint reports whether r is printable: a letter, mark, number, punctuation or symbol, or the ASCII space (no other space is).
- `const UpperCase = 0`: The case a rune is mapped to by To.
- `const LowerCase = 1`
- `const TitleCase = 2`
- `To(which i64, r i32) i32`: To maps r to the given case (UpperCase, LowerCase or TitleCase); a rune without a mapping is returned unchanged.
- `ToUpper(r i32) i32`: ToUpper maps r to upper case.
- `ToLower(r i32) i32`: ToLower maps r to lower case.
- `ToTitle(r i32) i32`: ToTitle maps r to title case.
- `SimpleFold(r i32) i32`: SimpleFold iterates over the code points that are equivalent under simple case folding: it returns the smallest rune greater than r in r's orbit, or the smallest one when there is none ('K' gives 'k', 'k' gives U+212A, U+212A gives 'K').
- `Utf16IsSurrogate(r i32) bool`: Utf16IsSurrogate reports whether r is a surrogate code point, which no string may contain.
- `Utf16DecodeRune(r1 i32, r2 i32) i32`: Utf16DecodeRune joins a surrogate pair into one rune, or returns RuneError when r1 and r2 are not a valid pair (as Go's utf16.DecodeRune).
- `Utf16EncodeRune(r i32) (i32, i32)`: Utf16EncodeRune splits r into a surrogate pair. A rune that is not above 0xFFFF (which needs no pair) or not a valid code point gives RuneError twice, as Go's utf16.EncodeRune.
- `Utf16RuneLen(r i32) i64`: Utf16RuneLen returns the number of UTF-16 code units r needs, or -1 when r is not a valid rune (a surrogate or above MaxRune), as Go's utf16.RuneLen.
- `Utf16AppendRune(a mut []u16, r i32) []u16`: Utf16AppendRune appends the UTF-16 code units of r to a: one for a rune up to 0xFFFF that is not a surrogate, two for one above, and RuneError for anything else, as Go's utf16.AppendRune.
- `Utf16Encode(s str) []u16`: Utf16Encode returns the UTF-16 code units of s: one or two per rune, as Go's utf16.Encode over the string's runes. Invalid UTF-8 decodes to RuneError, as in Go.
- `Utf16Decode(u []u16) str`: Utf16Decode returns the string of the code units, as Go's utf16.Decode: a high surrogate followed by a low one is one rune, and a lone surrogate is RuneError.

## mint

Package mint converts numbers and quoted strings to and from text (like Go's strconv), with Go's error texts under mint's own names: mint.Atoi: parsing "x": invalid syntax. A parse fault's cause is the sentinel ErrSyntax or ErrRange (fault.Is(err, mint.ErrRange)); like every fault it comes with 0.

- `const MaxI64 = 9223372036854775807`: MaxI64 is the largest i64.
- `const MinI64 = -9223372036854775807 - 1`: MinI64 is the smallest i64.
- `Itoa(v i64) str`: Itoa returns v in decimal.
- `FormatInt(v i64, base i64) str`: FormatInt returns v in base 2..36 with lower-case digits (panics on any other base).
- `FormatUint(v u64, base i64) str`: FormatUint returns v in base 2..36 with lower-case digits (panics on any other base).
- `AppendInt(b mut []u8, v i64) []u8`: AppendInt appends v in decimal to b and returns b (use it as b = AppendInt(b, v)).
- `Atoi(s str) !i64`: Atoi parses a decimal i64 like Go's Atoi; out of range is a fault caused by ErrRange (with 0, where Go returns the clamped value).
- `ParseInt(s str, base i64) !i64`: ParseInt parses a signed integer in base 2..36, or base 0 for 0x/0o/0b prefixes and underscores.
- `ParseUint(s str, base i64) !u64`: ParseUint parses an unsigned integer in base 2..36, or base 0 for 0x/0o/0b prefixes and underscores.
- `ParseBool(s str) !bool`: ParseBool parses 1 t T TRUE true True and 0 f F FALSE false False.
- `ParseFloat(s str) !f64`: ParseFloat parses a Go float literal (decimal or 0x hex with p exponent, underscores, inf/infinity/nan) with exact nearest-even rounding; a finite literal beyond the largest f64 is a fault caused by ErrRange (with 0, where Go returns ±Inf).
- `F64frombits(b u64) f64`: F64frombits returns the f64 with bit pattern b.
- `FormatFloat(f f64, fmt u8, prec i64) str`: FormatFloat formats f as 'f' (ddd.ddd), 'e' (d.ddde±dd), 'g' (shortest of the two), 'b' (ddddp±ddd, a binary exponent) or 'x' (0x1.hhhhp±dd, hex mantissa); 'E', 'G' and 'X' are the upper-case forms, and any other byte gives "%" and the byte, as in Go. prec -1 is the shortest text that reads back exactly ('b' ignores it).
- `Quote(s str) str`: Quote returns s as a Go double-quoted literal with \n-style, \x, \u and \U escapes.
- `AppendQuote(b mut []u8, s str) []u8`: AppendQuote appends Quote(s) to b and returns b.
- `QuoteRune(r i32) str`: QuoteRune returns r as a Go single-quoted rune literal (invalid runes become U+FFFD).
- `Unquote(s str) !str`: Unquote interprets s as a Go string literal ("..." with escapes, '...' one rune, `...` raw) and returns its value.

## gauge

Package gauge is floating-point math and a few integer helpers (like Go's math); bit operations are in package bits. The transcendental functions are written in Tin (ported from Go's math package); only the functions the CPU has an instruction for (sqrt, floor, ceil, trunc, round, rint) go through the system.

- `Atan(x f64) f64`: Atan returns the arctangent of x, in [-Pi/2, Pi/2]. Atan(±0) = ±0, Atan(±Inf) = ±Pi/2.
- `Atan2(y f64, x f64) f64`: Atan2 returns the arctangent of y/x using the signs of both to pick the quadrant, in [-Pi, Pi].
- `Asin(x f64) f64`: Asin returns the arcsine of x, in [-Pi/2, Pi/2]. NaN for |x| > 1.
- `Acos(x f64) f64`: Acos returns the arccosine of x, in [0, Pi]. NaN for |x| > 1.
- `Cbrt(x f64) f64`: Cbrt returns the cube root of x. Cbrt(±0) = ±0, Cbrt(±Inf) = ±Inf, Cbrt(NaN) = NaN.
- `Erf(x f64) f64`: Erf returns the error function of x. Erf(±Inf) = ±1, Erf(NaN) = NaN.
- `Erfc(x f64) f64`: Erfc returns the complementary error function of x, 1 - Erf(x) without cancellation for large x. Erfc(+Inf) = 0, Erfc(-Inf) = 2, Erfc(NaN) = NaN.
- `Erfinv(x f64) f64`: Erfinv returns the inverse error function of x. Erfinv(1) = +Inf, Erfinv(-1) = -Inf, Erfinv(x) = NaN outside [-1, 1] and for NaN.
- `Erfcinv(x f64) f64`: Erfcinv returns the inverse of Erfc: Erfcinv(0) = +Inf, Erfcinv(2) = -Inf, Erfcinv(x) = NaN outside [0, 2] and for NaN.
- `Exp(x f64) f64`: Exp returns e**x. Exp(+Inf) = +Inf, Exp(-Inf) = 0, Exp(NaN) = NaN; it overflows above 709.78.
- `const Exp2Overflow = 1.0239999999999999e+03`
- `const Exp2Underflow = -1.0740e+03`
- `Exp2(x f64) f64`: Exp2 returns 2**x. Exp2(+Inf) = +Inf, Exp2(-Inf) = 0, Exp2(NaN) = NaN.
- `Expm1(x f64) f64`: Expm1 returns e**x - 1, more accurate than Exp(x) - 1 near zero (FreeBSD's s_expm1.c through Go's expm1.go). Expm1(-Inf) = -1, Expm1(+Inf) = +Inf, Expm1(NaN) = NaN.
- `F64bits(f f64) u64`: F64bits returns the IEEE 754 bit pattern of f.
- `F64frombits(b u64) f64`: F64frombits returns the f64 with bit pattern b.
- `Abs(x f64) f64`: Abs returns |x| (NaN stays NaN, -0 becomes +0).
- `Signbit(x f64) bool`: Signbit reports whether x is negative or negative zero.
- `Copysign(f f64, sign f64) f64`: Copysign returns a value with the magnitude of f and the sign of sign.
- `Inf(sign i64) f64`: Inf returns +Inf when sign >= 0, else -Inf.
- `NaN() f64`: NaN returns a quiet not-a-number.
- `IsNaN(f f64) bool`: IsNaN reports whether f is not-a-number.
- `IsInf(f f64, sign i64) bool`: IsInf reports whether f is +Inf (sign > 0), -Inf (sign < 0) or either (sign == 0).
- `Min(x f64, y f64) f64`: Min returns the smaller of x and y; any NaN gives NaN and -0 is smaller than +0 (like Go).
- `Max(x f64, y f64) f64`: Max returns the larger of x and y; any NaN gives NaN and +0 is larger than -0 (like Go).
- `Clamp(x f64, lo f64, hi f64) f64`: Clamp returns x limited to [lo, hi] (NaN passes through).
- `Pow10(n i64) f64`: Pow10 returns 10**n: +Inf above 308, 0 below -323, exactly as Go's math.Pow10.
- `F32bits(f f32) u32`: F32bits returns the IEEE 754 bit pattern of f. Tin holds an f32 as an f64 rounded to f32, so the 32-bit pattern is re-encoded; a NaN payload is canonical, as conversions do.
- `F32frombits(b u32) f32`: F32frombits returns the f32 with bit pattern b. Subnormals and infinities are exact; a NaN is a quiet NaN with the payload's high bits, since the f32 lives as an f64.
- `Nextafter(x f64, y f64) f64`: Nextafter returns the next representable f64 after x towards y, like Go's math.Nextafter; NaN when either is NaN.
- `Nextafter32(x f32, y f32) f32`: Nextafter32 is Nextafter for f32 values.
- `Dim(x f64, y f64) f64`: Dim returns the maximum of x-y or 0, like Go's math.Dim: Dim(+Inf, +Inf) = Dim(-Inf, -Inf) = NaN, and any NaN gives NaN.
- `FMA(x f64, y f64, z f64) f64`
- `Frexp(f f64) (f64, i64)`: Frexp breaks f into a fraction in [0.5, 1) and a power of two: f = frac * 2**exp. Frexp(0), Frexp(±Inf) and Frexp(NaN) return f and 0.
- `Ldexp(frac f64, exp i64) f64`: Ldexp returns frac * 2**exp, the inverse of Frexp.
- `Modf(f f64) (f64, f64)`: Modf returns the integer and fractional parts of f, both with the sign of f.
- `Gamma(x f64) f64`: Gamma returns the gamma function of x. Gamma(±Inf) = +Inf, Gamma(0) = ±Inf by sign, Gamma(NaN) = Gamma(negative integer) = NaN.
- `const Pi = 3.141592653589793`: Pi is the ratio of a circle's circumference to its diameter.
- `const E = 2.718281828459045`: E is the base of natural logarithms.
- `const Sqrt2 = 1.4142135623730951`: Sqrt2 is the square root of 2.
- `const Ln2 = 0.6931471805599453`: Ln2 is the natural logarithm of 2.
- `const MaxI64 = 9223372036854775807`: MaxI64 is the largest i64.
- `const MinI64 = -9223372036854775807 - 1`: MinI64 is the smallest i64.
- `const MaxU64 u64 = 18446744073709551615`: MaxU64 is the largest u64 (typed, because an untyped constant this large folds to -1 in the frozen compiler).
- `const MaxF64 = 1.7976931348623157e308`: MaxF64 is the largest finite f64.
- `const SmallestNonzeroF64 = 4.9406564584124654e-324`: SmallestNonzeroF64 is the smallest positive denormal f64.
- `const MaxF32 = 3.4028234663852886e+38`: MaxF32 is the largest finite f32.
- `const Ln10 = 2.302585092994046`: Ln10 is the natural logarithm of 10.
- `const Log2E = 1.4426950408889634`: Log2E is the base-2 logarithm of e.
- `const Log10E = 0.4342944819032518`: Log10E is the base-10 logarithm of e.
- `const Phi = 1.618033988749895`: Phi is the golden ratio.
- `const SqrtE = 1.6487212707001282`: SqrtE is the square root of e.
- `const SqrtPi = 1.772453850905516`: SqrtPi is the square root of Pi.
- `const SqrtPhi = 1.272019649514069`: SqrtPhi is the square root of Phi.
- `Sqrt(x f64) f64`: Sqrt returns the square root of x.
- `Floor(x f64) f64`: Floor returns the largest integer value <= x.
- `Ceil(x f64) f64`: Ceil returns the smallest integer value >= x.
- `Trunc(x f64) f64`: Trunc returns the integer part of x (rounding toward zero).
- `Round(x f64) f64`: Round returns x rounded to the nearest integer, halves away from zero.
- `RoundToEven(x f64) f64`: RoundToEven returns x rounded to the nearest integer, halves to the even neighbour.
- `Sinh(x f64) f64`: Sinh returns the hyperbolic sine of x. It uses Exp above 0.5 and a rational approximation below.
- `Cosh(x f64) f64`: Cosh returns the hyperbolic cosine of x.
- `Tanh(x f64) f64`: Tanh returns the hyperbolic tangent of x, in [-1, 1].
- `Asinh(x f64) f64`: Asinh returns the inverse hyperbolic sine of x (FreeBSD's s_asinh.c through Go's asinh.go).
- `Acosh(x f64) f64`: Acosh returns the inverse hyperbolic cosine of x (FreeBSD's e_acosh.c through Go's acosh.go); it is NaN below 1.
- `Atanh(x f64) f64`: Atanh returns the inverse hyperbolic tangent of x (FreeBSD's e_atanh.c through Go's atanh.go); it is +Inf at 1, -Inf at -1 and NaN outside [-1, 1].
- `Hypot(p f64, q f64) f64`: Hypot returns sqrt(p*p + q*q), overflowing only if the result does.
- `MinI(a i64, b i64) i64`: MinI returns the smaller of a and b.
- `MaxI(a i64, b i64) i64`: MaxI returns the larger of a and b.
- `AbsI(x i64) i64`: AbsI returns |x| (MinI64 wraps to itself).
- `ClampI(x i64, lo i64, hi i64) i64`: ClampI returns x limited to [lo, hi].
- `Gcd(a i64, b i64) i64`: Gcd returns the greatest common divisor of |a| and |b| (0 when both are 0).
- `Lcm(a i64, b i64) i64`: Lcm returns the least common multiple of |a| and |b| (0 when either is 0; wraps on overflow).
- `Lgamma(x f64) (f64, i64)`: Lgamma returns the natural logarithm of the absolute value of Gamma(x) and its sign (+1 or -1), like Go's math.Lgamma. Lgamma(±Inf) = +Inf, Lgamma(0) = +Inf, Lgamma(NaN) = NaN.
- `Log(x f64) f64`: Log returns the natural logarithm of x: Log(+Inf) = +Inf, Log(0) = -Inf, Log(x < 0) = NaN; bit for bit Go's math.Log (#942).
- `Log2(x f64) f64`: Log2 returns the binary logarithm of x, exact for powers of two.
- `Log10(x f64) f64`: Log10 returns the decimal logarithm of x.
- `Log1p(x f64) f64`: Log1p returns log(1 + x), accurate even when x is close to zero.
- `Logb(x f64) f64`: Logb returns the binary exponent of x as an f64 (Go's math.Logb): +Inf for infinities, -Inf for zero, NaN for NaN.
- `Ilogb(x f64) i64`: Ilogb returns the binary exponent of x as an i64, like Go's math.Ilogb: MaxI32 for infinities and NaN, MinI32 for zero.
- `Mod(x f64, y f64) f64`: Mod returns the remainder of x/y with the sign of x, exactly. NaN for y == 0, infinite x or either NaN.
- `Remainder(x f64, y f64) f64`: Remainder returns the IEEE 754 remainder of x/y: x - n*y where n is x/y rounded to the nearest integer, ties to even (FreeBSD's e_remainder.c through Go's remainder.go). Unlike Mod its sign follows x and it is NaN for y = 0 or an infinite x.
- `Pow(x f64, y f64) f64`: Pow returns x**y, with the special cases of C99 and Go: Pow(x, ±0) = 1, Pow(1, y) = 1, Pow(NaN, y) = NaN, Pow(x < 0, non-integer y) = NaN, and the usual infinities and signed zeros. It is exact for small integer powers of exactly representable bases and within an ulp or two otherwise (it is not correctly rounded).
- `Sin(x f64) f64`: Sin returns the sine of x (radians). Sin(±0) = ±0, Sin(±Inf) = Sin(NaN) = NaN.
- `Cos(x f64) f64`: Cos returns the cosine of x (radians). Cos(±Inf) = Cos(NaN) = NaN.
- `Tan(x f64) f64`: Tan returns the tangent of x (radians). Tan(±0) = ±0, Tan(±Inf) = Tan(NaN) = NaN.
- `Sincos(x f64) (f64, f64)`: Sincos returns Sin(x), Cos(x) with one argument reduction, like Go's math.Sincos.

## cmplx

Package cmplx is complex arithmetic: the functions of Go's math/cmplx on Complex (a value struct of two f64 parts) and Complex64 (two f32 parts). The real functions come from package gauge; the branches, poles, signed zeros and infinities are Go's, and the expressions keep Go's shape so that arm64 fuses the same products (see the note on mul).

- `type Complex value struct`: Complex is a complex number: Re is the real part and Im the imaginary part (Go's complex128).
- `type Complex64 value struct`: Complex64 is a complex number with float32 parts (Go's complex64); From64 rounds each part to float32.
- `New(re f64, im f64) Complex`: New returns the complex number re + im*i (Go's complex(re, im)).
- `From64(z Complex) Complex64`: From64 rounds each part of z to float32, as Go's complex64(z) does.
- `(c Complex64) To128() Complex`: To128 widens each part of c to float64 (exact).
- `Inf() Complex`: Inf returns the complex infinity (+Inf, +Inf).
- `NaN() Complex`: NaN returns the complex NaN (NaN, NaN).
- `IsInf(z Complex) bool`: IsInf reports whether either part of z is an infinity.
- `IsNaN(z Complex) bool`: IsNaN reports whether z is NaN: a part is NaN and neither part is an infinity.
- `Abs(z Complex) f64`: Abs returns the absolute value (modulus) of z, computed with Hypot so it does not overflow.
- `Phase(z Complex) f64`: Phase returns the phase (argument) of z, in [-Pi, Pi].
- `Polar(z Complex) (f64, f64)`: Polar returns the absolute value and the phase of z (Abs and Phase).
- `Rect(r f64, theta f64) Complex`: Rect returns the complex number with modulus r and phase theta.
- `Conj(z Complex) Complex`: Conj returns the complex conjugate of z.
- `Sqrt(z Complex) Complex`: Sqrt returns the principal square root of z, with the sign of the imaginary part chosen as Go does.
- `Exp(z Complex) Complex`: Exp returns e**z, the complex exponential of z.
- `Log(z Complex) Complex`: Log returns the natural logarithm of z: ln|z| + i*Phase(z), the principal branch (cut along the negative real axis).
- `Log10(z Complex) Complex`: Log10 returns the base-10 logarithm of z.
- `Pow(x Complex, y Complex) Complex`: Pow returns x**y for complex x and y, as exp(y*log(x)) with Go's special cases (x == 0 gives 0, 1, Inf or NaN by y). Go's version panics ("not reached") for x == 0 with a NaN real part and an infinite imaginary part of y; this returns NaN.
- `Sin(z Complex) Complex`: Sin returns the sine of z.
- `Sinh(z Complex) Complex`: Sinh returns the hyperbolic sine of z.
- `Cos(z Complex) Complex`: Cos returns the cosine of z.
- `Cosh(z Complex) Complex`: Cosh returns the hyperbolic cosine of z.
- `Tan(z Complex) Complex`: Tan returns the tangent of z.
- `Tanh(z Complex) Complex`: Tanh returns the hyperbolic tangent of z.
- `Cot(z Complex) Complex`: Cot returns the cotangent of z.
- `Asin(z Complex) Complex`: Asin returns the arcsine of z, on the principal branch (cuts on the real axis beyond ±1).
- `Acos(z Complex) Complex`: Acos returns the arccosine of z.
- `Asinh(z Complex) Complex`: Asinh returns the inverse hyperbolic sine of z.
- `Acosh(z Complex) Complex`: Acosh returns the inverse hyperbolic cosine of z, with a real part that is never negative.
- `Atan(z Complex) Complex`: Atan returns the arctangent of z, on the principal branch (cuts on the imaginary axis beyond ±i).
- `Atanh(z Complex) Complex`: Atanh returns the inverse hyperbolic tangent of z.

## bits

Package bits counts, rotates and reverses the bits of fixed-width unsigned integers, and does 64-bit and 32-bit arithmetic with carries (like Go's math/bits). Every name carries its width; PopCount is Go's OnesCount; there is no uint-wide form because Tin has no uint.

- `Len64(x u64) i64`: Len64 returns the minimum number of bits needed to represent x; Len64(0) is 0.
- `Len32(x u32) i64`: Len32 is Len64 for a u32.
- `Len16(x u16) i64`: Len16 is Len64 for a u16.
- `Len8(x u8) i64`: Len8 is Len64 for a u8.
- `LeadingZeros64(x u64) i64`: LeadingZeros64 returns the number of leading zero bits in x; it is 64 for 0.
- `LeadingZeros32(x u32) i64`: LeadingZeros32 returns the number of leading zero bits in x; it is 32 for 0.
- `LeadingZeros16(x u16) i64`: LeadingZeros16 returns the number of leading zero bits in x; it is 16 for 0.
- `LeadingZeros8(x u8) i64`: LeadingZeros8 returns the number of leading zero bits in x; it is 8 for 0.
- `TrailingZeros64(x u64) i64`: TrailingZeros64 returns the number of trailing zero bits in x; it is 64 for 0.
- `TrailingZeros32(x u32) i64`: TrailingZeros32 returns the number of trailing zero bits in x; it is 32 for 0.
- `TrailingZeros16(x u16) i64`: TrailingZeros16 returns the number of trailing zero bits in x; it is 16 for 0.
- `TrailingZeros8(x u8) i64`: TrailingZeros8 returns the number of trailing zero bits in x; it is 8 for 0.
- `PopCount64(x u64) i64`: PopCount64 returns the number of one bits in x.
- `PopCount32(x u32) i64`: PopCount32 returns the number of one bits in x.
- `PopCount16(x u16) i64`: PopCount16 returns the number of one bits in x.
- `PopCount8(x u8) i64`: PopCount8 returns the number of one bits in x.
- `RotateLeft64(x u64, k i64) u64`: RotateLeft64 returns x rotated left by k bits; a negative k rotates right.
- `RotateLeft32(x u32, k i64) u32`: RotateLeft32 returns x rotated left by k bits; a negative k rotates right.
- `RotateLeft16(x u16, k i64) u16`: RotateLeft16 returns x rotated left by k bits; a negative k rotates right.
- `RotateLeft8(x u8, k i64) u8`: RotateLeft8 returns x rotated left by k bits; a negative k rotates right.
- `ReverseBytes64(x u64) u64`: ReverseBytes64 returns x with its bytes in reversed order.
- `ReverseBytes32(x u32) u32`: ReverseBytes32 returns x with its bytes in reversed order.
- `ReverseBytes16(x u16) u16`: ReverseBytes16 returns x with its bytes in reversed order.
- `Reverse64(x u64) u64`: Reverse64 returns x with its bits in reversed order.
- `Reverse32(x u32) u32`: Reverse32 returns x with its bits in reversed order.
- `Reverse16(x u16) u16`: Reverse16 returns x with its bits in reversed order.
- `Reverse8(x u8) u8`: Reverse8 returns x with its bits in reversed order.
- `Add64(x u64, y u64, carry u64) (u64, u64)`: Add64 returns the sum x + y + carry and the carry out. carry must be 0 or 1, otherwise the behavior is undefined.
- `Add32(x u32, y u32, carry u32) (u32, u32)`: Add32 returns the sum x + y + carry and the carry out (0 or 1).
- `Sub64(x u64, y u64, borrow u64) (u64, u64)`: Sub64 returns the difference x - y - borrow and the borrow out. borrow must be 0 or 1, otherwise the behavior is undefined.
- `Sub32(x u32, y u32, borrow u32) (u32, u32)`: Sub32 returns the difference x - y - borrow and the borrow out (0 or 1).
- `Mul64(x u64, y u64) (u64, u64)`: Mul64 returns the 128-bit product of x and y as (high word, low word): two instructions, umulh and mul on arm64, one mul on x86-64 (#474).
- `Mul32(x u32, y u32) (u32, u32)`: Mul32 returns the 64-bit product of x and y as (high word, low word).
- `const Div64Mask32 = two32 - 1`
- `Div64(hi u64, lo u64, y u64) (u64, u64)`: Div64 returns the quotient and remainder of (hi, lo) divided by y. It panics for y == 0 (division by zero) and for y <= hi (the quotient does not fit in 64 bits).
- `Div32(hi u32, lo u32, y u32) (u32, u32)`: Div32 returns the quotient and remainder of (hi, lo) divided by y. It panics for y == 0 and for y <= hi (the quotient does not fit in 32 bits).
- `Rem64(hi u64, lo u64, y u64) u64`: Rem64 returns the remainder of (hi, lo) divided by y, for any hi (no overflow panic). It panics for y == 0.
- `Rem32(hi u32, lo u32, y u32) u32`: Rem32 returns the remainder of (hi, lo) divided by y. It panics for y == 0.

## link

Package link parses, builds and resolves URLs, and escapes and unescapes their parts (like Go's net/url). A URL is a struct; its User is an optional (nil when the URL has no userinfo); query parameters are a Values, a small wrapper over map[str][]str whose keys keep insertion order and whose Encode sorts them. Faults carry Go's messages: parse "x": invalid URL escape "%zz".

- `QueryUnescape(s str) !str`: QueryUnescape converts each %AB in s to the byte 0xAB and each + to a space; a % not followed by two hex digits is a fault.
- `PathUnescape(s str) !str`: PathUnescape is QueryUnescape for a path segment: + stays a plus sign.
- `QueryEscape(s str) str`: QueryEscape escapes s for use as a query key or value: a space becomes +.
- `PathEscape(s str) str`: PathEscape escapes s for use as one path segment: / and ? are escaped too.
- `type Userinfo struct`: Userinfo is the username and optional password of a URL.
- `User(username str) Userinfo`: User returns a Userinfo with a username and no password.
- `UserPassword(username str, password str) Userinfo`: UserPassword returns a Userinfo with a username and a password (only for legacy services: RFC 2396 warns against passwords in URLs).
- `(u Userinfo) Username() str`: Username returns the username.
- `(u Userinfo) Password() (str, bool)`: Password returns the password and whether one is set.
- `(u Userinfo) String() str`: String returns the escaped userinfo, username[:password].
- `type URL struct`: URL is a parsed URL, in the general form [scheme:][//[userinfo@]host][/]path[?query][#fragment]. A URL whose rest after the scheme does not start with a slash is opaque: scheme:opaque[?query][#fragment]. Path and Fragment are stored decoded; RawPath and RawFragment hold the original encoding when it differs from the default one (EscapedPath and EscapedFragment use them).
- `(u URL) Clone() URL`: Clone returns a copy of u (a plain assignment of a struct shares it).
- `Parse(rawURL str) !URL`: Parse parses a URL, absolute or relative; a hostname and path without a scheme is invalid but may not be rejected, because of parsing ambiguities.
- `ParseRequestURI(rawURL str) !URL`: ParseRequestURI parses a URL received in an HTTP request: an absolute URI or an absolute path, without a #fragment.
- `(u URL) EscapedPath() str`: EscapedPath returns u.RawPath when it is a valid encoding of u.Path, else the default escaping.
- `(u URL) EscapedFragment() str`: EscapedFragment returns u.RawFragment when it is a valid encoding of u.Fragment, else the default.
- `(u URL) Username() str`: Username returns the username of u's userinfo, or "".
- `(u URL) Password() (str, bool)`: Password returns the password of u's userinfo and whether one is set.
- `(u URL) String() str`: String reassembles u into a URL string: [scheme:][//[userinfo@]host][/]path[?query][#fragment].
- `(u URL) Redacted() str`: Redacted is String with the password, if any, replaced by xxxxx.
- `(u URL) IsAbs() bool`: IsAbs reports whether u has a scheme.
- `(u URL) Hostname() str`: Hostname returns u.Host without its port, and without the brackets of an IPv6 literal.
- `(u URL) Port() str`: Port returns the port of u.Host, or "" when there is none.
- `(u URL) RequestURI() str`: RequestURI returns what goes in an HTTP request line: the escaped path (or / when empty) and query, or the opaque part.
- `(u URL) Query() Values`: Query parses u.RawQuery, keeping every well-formed parameter and skipping malformed ones.
- `(u URL) Parse(ref str) !URL`: Parse parses ref (which may be relative) in the context of u: Parse then ResolveReference.
- `(u URL) ResolveReference(ref URL) URL`: ResolveReference resolves a URI reference against u as an absolute URI (RFC 3986 section 5.2): ref may be relative or absolute, and u is typically an absolute URL.
- `(u URL) JoinPath(elems []str) URL`: JoinPath returns a copy of u with the elements joined onto its path (cleaned, with a trailing slash kept if the last element had one).
- `JoinPath(base str, elems []str) !str`: JoinPath parses base and joins the elements onto its path, returning the URL as a string.
- `type Values struct`: Values maps a query key to its values, in the order they were added; Encode sorts the keys.
- `NewValues() Values`: NewValues returns an empty Values.
- `(v Values) Get(key str) str`: Get returns the first value of key, or "" when there is none.
- `(v Values) All(key str) []str`: All returns every value of key (empty when there is none).
- `(v mut Values) Set(key str, value str)`: Set makes value the only value of key.
- `(v mut Values) Add(key str, value str)`: Add appends value to the values of key.
- `(v mut Values) Del(key str)`: Del removes key and its values.
- `(v Values) Has(key str) bool`: Has reports whether key is present.
- `(v Values) Keys() []str`: Keys returns the keys in the order they were first added.
- `(v Values) Len() i64`: Len returns the number of keys.
- `ParseQuery(query str) !Values`: ParseQuery parses a URL query ("a=1&b=2&a=3") into Values. It faults on the first malformed parameter (a bad escape, or a semicolon separator); URL.Query keeps the good ones instead.
- `(v Values) Encode() str`: Encode returns the values URL-encoded ("a=1&a=3&b=2"), sorted by key.

## netip

Package netip holds IP addresses, address/port pairs and prefixes as small value types, like Go's net/netip. An Addr is a value struct of 16 bytes, a zone and a kind byte: it is copied by every store, compares with == and is a map key by value. Comparing, classifying, Contains, Overlaps and AppendTo allocate nothing.

```tin body
let a = try netip.ParseAddr("192.168.1.10")
let p = try netip.ParsePrefix("192.168.0.0/16")
p.Contains(a)                                   // true
a.IsPrivate()                                   // true
let ap = try netip.ParseAddrPort("[fe80::1%eth0]:8080")
ap.Port()                                       // 8080
ap.Addr().Zone()                                // "eth0"
```

Parsing, formatting, the fault messages and every classification follow net/netip exactly: an IPv4 address is stored as its IPv4-mapped IPv6 form with the IPv4 kind, IPv4 fields with leading zeros are refused, an IPv6 address may end in an embedded IPv4 address and carry a zone after %, and the zero Addr is invalid.

- `type Addr value struct`: Addr is an IPv4 or IPv6 address, with an IPv6 zone or none; the zero Addr is not a valid address.
- `type AddrPort value struct`: AddrPort is an IP address and a port number.
- `type Prefix value struct`: Prefix is an IP network: an address and the number of leading bits that name the network.
- `AddrFrom4(b []u8) Addr`: AddrFrom4 is the IPv4 address of the four bytes b (it panics unless len(b) is 4).
- `AddrFrom16(b []u8) Addr`: AddrFrom16 is the IPv6 address of the sixteen bytes b (it panics unless len(b) is 16); a mapped IPv4 address stays IPv6.
- `AddrFromSlice(b []u8) (Addr, bool)`: AddrFromSlice is the IPv4 address of 4 bytes or the IPv6 address of 16, and false for any other length.
- `IPv4Unspecified() Addr`: IPv4Unspecified is 0.0.0.0.
- `IPv6Unspecified() Addr`: IPv6Unspecified is ::.
- `IPv6Loopback() Addr`: IPv6Loopback is ::1.
- `IPv6LinkLocalAllNodes() Addr`: IPv6LinkLocalAllNodes is ff02::1.
- `IPv6LinkLocalAllRouters() Addr`: IPv6LinkLocalAllRouters is ff02::2.
- `ParseAddr(s str) !Addr`: ParseAddr parses an IPv4 address ("192.0.2.1"), an IPv6 address ("2001:db8::68") or one with a zone ("fe80::1%eth0").
- `MustParseAddr(s str) Addr`: MustParseAddr is ParseAddr that panics with the fault's message.
- `(a Addr) IsValid() bool`: IsValid reports whether a is an address, not the zero Addr (0.0.0.0 and :: are valid).
- `(a Addr) BitLen() i64`: BitLen is 32 for IPv4, 128 for IPv6 (mapped IPv4 included) and 0 for the zero Addr.
- `(a Addr) Zone() str`: Zone is a's IPv6 zone, or "".
- `(a Addr) Is4() bool`: Is4 reports whether a is an IPv4 address (not an IPv4-mapped IPv6 one).
- `(a Addr) Is6() bool`: Is6 reports whether a is an IPv6 address, IPv4-mapped ones included.
- `(a Addr) Is4In6() bool`: Is4In6 reports whether a is an IPv4-mapped IPv6 address (in ::ffff:0:0/96).
- `(a Addr) Unmap() Addr`: Unmap is a without its IPv4-mapped prefix: the IPv4 address of ::ffff:a.b.c.d, else a unchanged.
- `(a Addr) WithZone(zone str) Addr`: WithZone is a with the given IPv6 zone ("" removes it); an IPv4 or zero Addr is returned unchanged.
- `(a Addr) IsLoopback() bool`: IsLoopback reports whether a is a loopback address: 127.0.0.0/8 or ::1.
- `(a Addr) IsMulticast() bool`: IsMulticast reports whether a is a multicast address: 224.0.0.0/4 or ff00::/8.
- `(a Addr) IsInterfaceLocalMulticast() bool`: IsInterfaceLocalMulticast reports whether a is an IPv6 interface-local multicast address (ff01::/16 and its flags).
- `(a Addr) IsLinkLocalMulticast() bool`: IsLinkLocalMulticast reports whether a is a link-local multicast address: 224.0.0.0/24 or ff02::/16 and its flags.
- `(a Addr) IsLinkLocalUnicast() bool`: IsLinkLocalUnicast reports whether a is a link-local unicast address: 169.254.0.0/16 or fe80::/10.
- `(a Addr) IsGlobalUnicast() bool`: IsGlobalUnicast reports whether a is a global unicast address, as Go's net.IP.IsGlobalUnicast (private ranges included).
- `(a Addr) IsPrivate() bool`: IsPrivate reports whether a is in 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 or fc00::/7 (RFC 1918, RFC 4193).
- `(a Addr) IsUnspecified() bool`: IsUnspecified reports whether a is 0.0.0.0 or :: (with no zone).
- `(a Addr) Compare(b Addr) i64`: Compare is -1, 0 or +1 as a sorts before, with or after b: by bit length, then address, then zone.
- `(a Addr) Less(b Addr) bool`: Less reports whether a sorts before b: by bit length, then address, then zone (a zone sorts after none).
- `(a Addr) As16() []u8`: As16 is a's 16 bytes (an IPv4 address in its IPv4-mapped IPv6 form).
- `(a Addr) As4() []u8`: As4 is the 4 bytes of an IPv4 or IPv4-mapped address; it panics for another IPv6 address or the zero Addr.
- `(a Addr) AsSlice() []u8`: AsSlice is a's 4 bytes (IPv4) or 16 bytes (IPv6), or an empty slice for the zero Addr.
- `(a Addr) Next() Addr`: Next is the address after a (same zone), or the zero Addr past the last address of its family.
- `(a Addr) Prev() Addr`: Prev is the address before a (same zone), or the zero Addr before the first address of its family.
- `(a Addr) Prefix(bits i64) !Prefix`: Prefix is the network of a's first bits bits, the rest cleared and the zone dropped; the zero Addr gives the zero Prefix.
- `(a Addr) AppendTo(b mut []u8) []u8`: AppendTo appends a's text form (String) to b, nothing for the zero Addr, and returns b.
- `(a Addr) String() str`: String is a's text form: dotted IPv4, ::ffff:a.b.c.d, RFC 5952 IPv6 with %zone, or "invalid IP".
- `(a Addr) StringExpanded() str`: StringExpanded is String with every IPv6 group written as four hex digits and no :: shortening.
- `(a Addr) MarshalText() []u8`: MarshalText is a's text form as bytes, empty for the zero Addr.
- `(a mut Addr) UnmarshalText(text []u8) !`: UnmarshalText sets a from its text form; empty text gives the zero Addr.
- `(a Addr) MarshalBinary() []u8`: MarshalBinary is 4 bytes for IPv4, 16 bytes and the zone for IPv6, and none for the zero Addr.
- `(a mut Addr) UnmarshalBinary(b []u8) !`: UnmarshalBinary sets a from MarshalBinary's bytes: 0 (zero Addr), 4, 16, or more than 16 (the rest is the zone).
- `AddrPortFrom(ip Addr, port u16) AddrPort`: AddrPortFrom is the pair of an address and a port.
- `(p AddrPort) Addr() Addr`: Addr is p's address.
- `(p AddrPort) Port() u16`: Port is p's port.
- `(p AddrPort) IsValid() bool`: IsValid reports whether p's address is valid.
- `ParseAddrPort(s str) !AddrPort`: ParseAddrPort parses "1.2.3.4:80" or "[2001:db8::1%eth0]:80"; an IPv6 address must be bracketed and an IPv4 one must not.
- `MustParseAddrPort(s str) AddrPort`: MustParseAddrPort is ParseAddrPort that panics with the fault's message.
- `(p AddrPort) Compare(q AddrPort) i64`: Compare is -1, 0 or +1 as p sorts before, with or after q: by address, then port.
- `(p AddrPort) AppendTo(b mut []u8) []u8`: AppendTo appends p's text form (String) to b, nothing when p's address is the zero Addr, and returns b.
- `(p AddrPort) String() str`: String is "1.2.3.4:80", "[2001:db8::1]:80" or "invalid AddrPort".
- `(p AddrPort) MarshalText() []u8`: MarshalText is p's text form as bytes, empty when p's address is the zero Addr.
- `(p mut AddrPort) UnmarshalText(text []u8) !`: UnmarshalText sets p from its text form; empty text gives the zero AddrPort.
- `PrefixFrom(ip Addr, bits i64) Prefix`: PrefixFrom is the prefix of ip's first bits bits, with ip's zone dropped and its other bits kept (see Masked); bits out of range for ip, or the zero Addr, give an invalid Prefix.
- `ParsePrefix(s str) !Prefix`: ParsePrefix parses "192.168.0.0/16" or "2001:db8::/32"; the address bits after the prefix are kept (see Masked).
- `MustParsePrefix(s str) Prefix`: MustParsePrefix is ParsePrefix that panics with the fault's message.
- `(p Prefix) Addr() Addr`: Addr is p's address, with the bits after the prefix as given (see Masked).
- `(p Prefix) Bits() i64`: Bits is p's prefix length, or -1 for an invalid Prefix.
- `(p Prefix) IsValid() bool`: IsValid reports whether p has a valid address and a length in range for it.
- `(p Prefix) IsSingleIP() bool`: IsSingleIP reports whether p holds exactly one address (/32 for IPv4, /128 for IPv6).
- `(p Prefix) Masked() Prefix`: Masked is p in canonical form: the address bits after the prefix cleared; an invalid p gives the zero Prefix.
- `(p Prefix) Contains(ip Addr) bool`: Contains reports whether ip is in p; an address with a zone, or of another family, never is.
- `(p Prefix) Overlaps(o Prefix) bool`: Overlaps reports whether p and o share an address; prefixes of different families never do.
- `(p Prefix) Compare(o Prefix) i64`: Compare is -1, 0 or +1 as p sorts before, with or after o: by masked address, then length, then address.
- `(p Prefix) AppendTo(b mut []u8) []u8`: AppendTo appends p's text form (String) to b, nothing for the zero Prefix, and returns b.
- `(p Prefix) String() str`: String is "192.168.0.0/16", "2001:db8::/32", "::ffff:1.2.3.0/120" or "invalid Prefix".
- `(p Prefix) MarshalText() []u8`: MarshalText is p's text form as bytes, empty for the zero Prefix.
- `(p mut Prefix) UnmarshalText(text []u8) !`: UnmarshalText sets p from its text form; empty text gives the zero Prefix.

## ore

Package ore works on byte slices ([]u8), like Go's bytes. Functions that append take the slice as mut and grow it in place.

- `Equal(a []u8, b []u8) bool`: Equal reports whether a and b hold the same bytes.
- `Compare(a []u8, b []u8) i64`: Compare returns -1, 0 or 1 by byte-wise order.
- `IndexByte(b []u8, c u8) i64`: IndexByte returns the index of the first c in b, or -1.
- `LastIndexByte(b []u8, c u8) i64`: LastIndexByte returns the index of the last c in b, or -1.
- `Index(b []u8, sep []u8) i64`: Index returns the index of the first occurrence of sep in b, or -1.
- `Contains(b []u8, sep []u8) bool`: Contains reports whether sep occurs in b.
- `HasPrefix(b []u8, p []u8) bool`: HasPrefix reports whether b starts with p.
- `HasSuffix(b []u8, p []u8) bool`: HasSuffix reports whether b ends with p.
- `Clone(b []u8) []u8`: Clone returns a fresh copy of b.
- `AppendStr(b mut []u8, s str) []u8`: AppendStr appends the bytes of s.
- `AppendByte(b mut []u8, c u8) []u8`: AppendByte appends c.
- `AppendInt(b mut []u8, v i64) []u8`: AppendInt appends v in decimal.
- `AppendUint(b mut []u8, v u64) []u8`: AppendUint appends v in decimal.
- `AppendHex(b mut []u8, v u64) []u8`: AppendHex appends v in lower-case hexadecimal (no prefix).
- `Reset(b mut []u8)`: Reset empties b, keeping its capacity.
- `Truncate(b mut []u8, n i64)`: Truncate keeps the first n bytes of b.
- `ToStr(b []u8) str`: ToStr returns b's bytes as a str.
- `TrimSpace(b []u8) []u8`: TrimSpace returns b without leading and trailing ASCII white space (a sub-slice).
- `Split(b []u8, sep u8) []str`: Split cuts b around every sep byte and returns the pieces as strs.
- `Fields(b []u8) []str`: Fields splits b around runs of ASCII white space.
- `ToLower(b []u8) []u8`: ToLower returns a copy with ASCII letters lowered.
- `ToUpper(b []u8) []u8`: ToUpper returns a copy with ASCII letters raised.
- `Repeat(b []u8, n i64) []u8`: Repeat returns n copies of b (panics when the length overflows).

## jsontext

Package jsontext reads and writes JSON token by token, as Go's encoding/json/jsontext does: a Decoder yields Tokens and whole Values, an Encoder takes them back and formats them with Options. Strings are unescaped in Token.String; numbers, literals and delimiters keep their text. Errors carry Go's messages (#931).

- `type Token struct`: Token is one JSON token: its kind byte and its text (the unescaped string of a string token, the literal of any other).
- `Bool(b bool) Token`: Bool returns the true or false token.
- `String(s str) Token`: String returns the string token for s (unescaped text; it is escaped when written).
- `Int(n i64) Token`: Int returns the number token for n.
- `Uint(n u64) Token`: Uint returns the number token for n.
- `Float(n f64) Token`: Float returns the number token for n, in the shortest form that reads back (NaN and infinities are not numbers: their token is the text "NaN" or "Inf", which Encoder refuses).
- `(t Token) Kind() u8`: Kind returns the token's kind byte: '"', '0', 't', 'f', 'n', '{', '}', '[' or ']'.
- `(t Token) String() str`: String returns the unescaped text of a string token and the literal of any other token.
- `(t Token) Bool() bool`: Bool reports whether the token is true.
- `(t Token) Int() i64`: Int returns the token's number as an integer (0 when it is not one or does not fit).
- `(t Token) Float() f64`: Float returns the token's number as a float64 (0 when it is not one).
- `type Options struct`: Options are the jsontext options this package implements (Go's jsontext.Options). Multiline or a non-empty Indent puts each member and element on its own line; each line starts with IndentPrefix and then Indent once per nesting level.
- `type Decoder struct`: Decoder reads the tokens and values of a JSON text. Top-level values follow one another without separators, as in Go.
- `NewDecoder(s str, opts Options) Decoder`: NewDecoder returns a Decoder that reads the JSON text s.
- `type Encoder struct`: Encoder writes tokens and values as JSON text, formatted with its Options. Each complete top-level value ends with a newline.
- `NewEncoder(opts Options) Encoder`: NewEncoder returns an Encoder that formats with opts.
- `(e Encoder) Bytes() str`: Bytes returns the JSON text written so far.
- `(d mut Decoder) ReadToken() !Token`: ReadToken returns the next token. At the end of the input it returns EOF; inside an open object or array, the end of the input is an unexpected EOF.
- `(d mut Decoder) ReadValue() !str`: ReadValue returns the raw text of the next whole value, from its first byte to its last (the white space between its tokens is kept), or EOF at the end of the input. Go reads a value in one pass, so a comma before a close is reported at the close.
- `(e mut Encoder) WriteToken(t Token) !`: WriteToken writes the next token: a name where the innermost object expects one, a value otherwise, and the closing delimiter of the innermost container. A complete top-level value ends with a newline.
- `(e mut Encoder) WriteValue(v str) !`: WriteValue writes the JSON value v (validated, and formatted with the encoder's options).

## jsonv2

Package jsonv2 is encoding/json/v2's surface over argo and jsontext: Marshal and Unmarshal with options (#931). argo does the typed work (its encoders and decoders are generated per type); jsontext rewrites the encoded text with the options and checks text for the v2 rules argo does not apply (malformed text and duplicate member names are refused). The differences from v2 are in README.md.

- `type Options struct`: Options are the v2 options this package implements: the formatting of Marshal's output (jsontext's options), whether Unmarshal accepts duplicate member names, and whether it refuses members that match no field.
- `Marshal[T constraints.Any](v T, opts Options) !str`: Marshal returns the JSON encoding of v, formatted with opts. It has no newline at the end, as Go's Marshal has none. Strings are not HTML-escaped unless opts asks for it.
- `Unmarshal[T constraints.Any](s str, v mut T, opts Options) !`: Unmarshal parses the JSON text s into v, a struct, slice or map. Malformed text and duplicate member names are faults (unless AllowDuplicateNames); a member that matches no field is a fault with RejectUnknownMembers. A fault leaves v unchanged.

## flume

Package flume reads and writes file descriptors through 64 KiB buffers: lines, whole files and buffered output with one write per flush.

- `type Reader struct`: Reader buffers reads from a file descriptor. Inside a task it waits on a pipe, socket or terminal through rt_task_wait, so a deadline or cancel fails the read (the next read retries).
- `type Writer struct`: Writer buffers writes to a file descriptor.
- `New(fd i64) Reader`: New reads from fd.
- `Open(path str) !Reader`: Open reads the file at path.
- `(r mut Reader) Close()`: Close closes the reader's descriptor.
- `(r mut Reader) Line() !(str, bool)`: Line returns the next line without its "\n" (or "\r\n"); ok is false at the end.
- `(r mut Reader) Byte() (u8, bool)`: Byte returns the next byte; ok is false at the end.
- `(r mut Reader) Read(buf mut []u8) !i64`: Read fills buf with the next buffered bytes, waiting for them, and returns how many it wrote: 0 at the end. It is what makes a flume.Reader an io.Reader (ledger.NewStream).
- `(r mut Reader) ReadByte() !(u8, bool)`: ReadByte returns the next byte; ok is false at the end. It makes a flume.Reader an io.ByteReader.
- `(r mut Reader) ReadRune() !(i32, i64)`: ReadRune returns the next UTF-8 encoded rune and its size in bytes: size 0 at the end, and U+FFFD of size 1 for an invalid encoding, as Go's bufio.Reader does. It makes a flume.Reader an io.RuneReader.
- `(r mut Reader) ReadAll() !str`: ReadAll returns everything left.
- `ReadFile(path str) !str`: ReadFile returns the contents of the file at path.
- `NewWriter(fd i64) Writer`: NewWriter writes to fd.
- `Stdout() Writer`: Stdout writes to standard output (flush it before mixing with say output).
- `Create(path str) !Writer`: Create truncates or creates the file at path for writing.
- `CreateExcl(path str) !Writer`: CreateExcl creates the file at path for writing (mode 0644) only if nothing exists there yet; two processes that race for one path never both succeed, which makes it the basis of lock files.
- `(w mut Writer) Sync() !`: Sync flushes the writer and waits until the file is on stable storage (fsync; on macOS F_FULLFSYNC).
- `(w mut Writer) Str(s str)`: Str appends s.
- `(w mut Writer) Byte(c u8)`: Byte appends c.
- `(w mut Writer) Write(data []u8) !i64`: Write appends data, flushing first when the buffer would pass 64 KiB, and returns len(data); it fails with the writer's fault (a failed flush, or a closed writer). It makes a flume.Writer an io.Writer.
- `(w mut Writer) WriteString(s str) !i64`: WriteString is Write for a str (an io.StringWriter).
- `(w mut Writer) WriteByte(c u8) !`: WriteByte is Write for one byte (an io.ByteWriter).
- `(w mut Writer) Int(v i64)`: Int appends v in decimal.
- `(w mut Writer) Line(s str)`: Line appends s and a newline.
- `(w mut Writer) Flush() !`: Flush writes everything buffered (with as few writes as the descriptor allows).
- `(w mut Writer) Close() !`: Close flushes and closes the writer's descriptor once; closing again (or a writer that never opened) is a fault.

## quarry

Package quarry is the operating system interface (like Go's os): arguments, environment, files and directories.

- `type FileType enum`: FileType is what a path is.
- `type FileInfo struct`: FileInfo is what stat and lstat report about a path. Times are unix nanoseconds.
- `type DirEntry struct`: DirEntry is a name in a directory with its type.
- `Stat(path str) !FileInfo`: Stat describes the file at path, following symlinks.
- `Lstat(path str) !FileInfo`: Lstat describes the file at path; a symlink is described itself, not followed.
- `Chmod(path str, perm i64) !`: Chmod sets the permission bits (the low 12 bits of perm) of the file at path, following symlinks.
- `Symlink(target str, link str) !`: Symlink makes link a symlink to target.
- `Readlink(path str) !str`: Readlink is the target of the symlink at path.
- `Sync(path str) !`: Sync waits until the file or directory at path is on stable storage (fsync; on macOS F_FULLFSYNC, which also flushes the drive's cache). Sync a directory after creating or renaming in it.
- `ReadDirEntries(path str) ![]DirEntry`: ReadDirEntries lists the directory at path, sorted by name, with each entry's type. The type comes from the directory itself where the file system records it, and from lstat where it does not.
- `Alive(pid i64) bool`: Alive reports whether a process with this id exists on this machine (kill with signal 0; a process this one may not signal still exists).
- `Args() []str`: Args returns the command line, program name first.
- `Getenv(key str) str`: Getenv returns the value of environment variable key, or "" when it is unset.
- `LookupEnv(key str) (str, bool)`: LookupEnv returns the value of key and whether it is set (an empty value is still set).
- `Setenv(key str, value str) !`: Setenv sets environment variable key to value; an empty key or one holding '=' or NUL is a fault.
- `Unsetenv(key str) !`: Unsetenv removes environment variable key.
- `ReadAt(path str, off i64, n i64) !str`: ReadAt returns up to n bytes of the file at path from offset off: fewer at the file's end, "" past it. Only those bytes are read (pread), so one record of a large file costs its own size, inside a request task too (a local file's pages come from the page cache; a whole file read for a few bytes cost a request its size in memory). Inside a task on a file system that may wait for a daemon or a server (FUSE, 9p, CIFS: see useRing), or without the core's io_uring (macOS, a container that refuses it), the same pread runs on a helper thread: reading the whole file there made a push, which reads each object of a pack, quadratic in the pack's size (#1105). Recording or replaying a tape, it reads the file through ReadFileBound and gives the same bytes.
- `ReadFile(path str) !str`: ReadFile returns the whole content of the file at path. A file larger than 64 MiB (anvil's request limit) fails with fault.LimitExceeded before it is read, and so does a device or pipe past it, read by read (#745); ReadFileBound sets another bound.
- `ReadFileBound(path str, n i64) !str`: ReadFileBound returns the whole content of the file at path when it is at most n bytes, and otherwise fails with fault.LimitExceeded: a regular file by its size, before anything is read, a device or pipe as soon as more than n bytes have come (#745).
- `OpenRegular(path str) !(i64, i64)`: OpenRegular opens the regular file at path for reading and returns its descriptor and size; the caller closes the descriptor. Inside a request task it opens the file as ReadFile does: through the core's io_uring (Linux), or on a helper thread, always there under a slow mount, so an open that waits (a FIFO with no writer, a hung network mount) waits within the task's deadline and the core serves others meanwhile (#744). A directory ("is a directory"), a FIFO, a device or a socket ("not a regular file") is refused after the open: it has no size to send. It is for code that hands the file to the system, as anvil's SendFile does.
- `OpenRegularStat(path str) !(i64, i64, i64)`: OpenRegularStat is OpenRegular and the file's modification time too, in seconds since the Unix epoch: the descriptor, the size and the time, from one open and one fstat, never on the core thread.
- `ReadStdin() !str`: ReadStdin reads standard input to its end. Inside a task, from a pipe, socket or terminal, it waits through rt_task_wait: the core serves others, and a deadline or cancel fails it.
- `WriteFile(path str, data str) !`: WriteFile writes data to the file at path, creating it (mode 0644) or truncating it.
- `AppendFile(path str, data str) !`: AppendFile appends data to the file at path, creating it (mode 0644) when needed.
- `Exists(path str) bool`: Exists reports whether path names an existing file or directory (symlinks are followed).
- `IsDir(path str) bool`: IsDir reports whether path names a directory.
- `Size(path str) !i64`: Size returns the size in bytes of the file at path.
- `ModTime(path str) !i64`: ModTime returns the modification time of path in seconds since the Unix epoch.
- `Remove(path str) !`: Remove deletes the file or empty directory at path.
- `RemoveAll(path str) !`: RemoveAll deletes path and everything below it; a missing path is not a fault.
- `Rename(oldpath str, newpath str) !`: Rename moves oldpath to newpath, replacing a file there; like Go it never replaces a directory.
- `Mkdir(path str) !`: Mkdir creates the directory path (mode 0755); its parent must exist.
- `MkdirAll(path str) !`: MkdirAll creates path and any missing parents (mode 0755); an existing directory is fine.
- `SortStrs(a mut []str)`: SortStrs sorts a bytewise in place.
- `ReadDir(path str) ![]str`: ReadDir returns the names in directory path, sorted bytewise, without "." and "..".
- `Getwd() !str`: Getwd returns the current working directory ($PWD when it still names it, like Go).
- `Chdir(path str) !`: Chdir changes the current working directory to path.
- `TempDir() str`: TempDir returns the directory for temporary files: $TMPDIR, or /tmp.
- `Hostname() !str`: Hostname returns the machine's host name.
- `Pid() i64`: Pid returns the process id.
- `Exit(code i64)`: Exit flushes stdout and ends the program with status code.
- `Eprint(s str)`: Eprint writes s to stderr.
- `Eprintln(s str)`: Eprintln writes s and a newline to stderr in one write.

## debug/elf

Package elf reads bounded ELF64 little-endian binaries for Linux arm64 and amd64.

- `type Header struct`: Header is the ELF identification and file header fields used by this reader.
- `type Segment struct`: Segment describes one ELF program header.
- `type Section struct`: Section describes one ELF section header; its data is read on demand.
- `type Symbol struct`: Symbol is one ELF symbol table entry.
- `type DynamicEntry struct`: DynamicEntry is one ELF dynamic table key and value.
- `type File struct`: File is a validated ELF image backed by a path; section bytes are not retained.
- `Open(path str) !File`: Open validates the ELF64 little-endian header and tables for arm64 or amd64.
- `(f File) ReadSection(index i64) !str`: ReadSection reads one section's file-backed bytes, capped at 64 MiB.
- `(f File) Symbols() ![]Symbol`: Symbols reads static and dynamic ELF symbol tables with their linked strings.
- `(f File) Dynamic() ![]DynamicEntry`: Dynamic reads entries from SHT_DYNAMIC sections until DT_NULL.

## debug/macho

Package macho reads bounded 64-bit little-endian Mach-O executables for arm64 and x86-64, the files the compiler writes for macOS.

- `type Header struct`: Header is the Mach-O file header fields this reader keeps.
- `type Command struct`: Command is one load command's type and size, and where it sits in the file.
- `type Segment struct`: Segment describes one LC_SEGMENT_64 command.
- `type Section struct`: Section describes one section header; its data is read on demand.
- `type Symbol struct`: Symbol is one entry of the static symbol table.
- `type BuildVersion struct`: BuildVersion is the LC_BUILD_VERSION command: the platform and the OS versions a file was built for.
- `type File struct`: File is a validated Mach-O image backed by a path; section bytes and symbols are read on demand.
- `Open(path str) !File`: Open validates the Mach-O header and load commands of a 64-bit arm64 or x86-64 file; symbols and sections are read later.
- `(f File) ReadSection(index i64) !str`: ReadSection reads one section's file-backed bytes, capped at 64 MiB; zero-fill sections have no file bytes and read as "".
- `(f File) Symbols() ![]Symbol`: Symbols reads the static symbol table (LC_SYMTAB) and its strings, each capped at 64 MiB.

## debug/buildinfo

Package buildinfo reads the build metadata Tin's own Mach-O executables carry: the LC_UUID and LC_BUILD_VERSION load commands.

Contract: the compiler does not write Go's buildinfo blob (the "\xff Go buildinf:" record that debug/buildinfo of Go reads), and ELF executables carry no build metadata today. A Tin Mach-O executable carries an LC_UUID, a hash of its code, so identical builds have the same UUID (toolchain/docs/COMPILER.md, section 9), and an LC_BUILD_VERSION naming macOS and the minimum and SDK versions the compiler targets. Nothing else is written, so this package reads only those two commands.

- `type Info struct`: Info is the build metadata of one Mach-O executable.
- `Read(path str) !Info`: Read returns the build metadata of a Mach-O executable: ErrNoBuildInfo for an ELF file or one without Tin's commands.

## debug/dwarf

Package dwarf reads the DWARF 4 sections written by Tin's compiler with -g. It reads ELF files lazily through debug/elf; Go's debug/dwarf is the model.

- `type Sections struct`: Sections contains the DWARF sections in an ELF file. Open caps the combined section data at 64 MiB before retaining it.
- `Open(path str) !Sections`: Open reads the DWARF sections of an ELF executable. A binary without -g returns ErrNoDebugInfo, matching Go's debug/dwarf.New on missing sections.
- `(s Sections) Get(name str) (str, bool)`: Get is the bytes of a section and whether there is one.
- `type Row struct`: Row is a row of the line table.
- `type Lines struct`: Lines is the files and rows of a DWARF 4 line program.
- `(l Lines) LineForPC(pc i64) (Row, bool)`: LineForPC returns the row whose address range contains pc. End-sequence markers close a range and are never returned as source locations.
- `LineRows(sec str) !Lines`
- `type Die struct`: Die is a debugging information entry: its tag, parent (an offset, -1 at the top), and the attribute values it holds as numbers (Nums) and as text or bytes (Strs).
- `(d Die) Num(attr i64) (i64, bool)`
- `(d Die) Str(attr i64) (str, bool)`
- `type Abbrev struct`: Abbrev is an abbreviation: tag, whether it has children and its (attribute, form) pairs.
- `Dies(info str, abbrev str) ![]Die`: Dies decodes the entries of the one compilation unit in order.
- `Find(dies []Die, at i64) !Die`: Find is the entry at an offset.
- `TypeText(dies []Die, at i64) !str`: TypeText is a short text for the type entry at an offset: a base type's name, a pointer as *target, a struct's name.

## user

- `type User struct`: User is an account from the system user database.
- `type Group struct`: Group is an account from the system group database.
- `Current() !User`: Current returns the user identified by the process's real user ID.
- `LookupId(uid str) !User`: LookupId looks up a user by numeric user ID.
- `Lookup(username str) !User`: Lookup looks up a user by login name.
- `LookupGroup(name str) !Group`: LookupGroup looks up a group by name.
- `(u User) GroupIds() ![]str`: GroupIds returns the IDs of the groups to which u belongs, including its primary group.

## spawn

Package spawn starts child processes, like Go's os/exec: Run a program and collect its output, or Start it, talk to it through pipes, signal it or kill it. A program is never run through a shell: write []str{"sh", "-c", script} for one. On Linux the child is a clone that execs and waits block on a pidfd; on macOS it is posix_spawn with file actions (POSIX_SPAWN_CLOEXEC_DEFAULT keeps the runtime's descriptors out of it) and the wait sleeps through the scheduler, which carries the task's deadline on both (#576).

- `type Stdio enum`: Stdio says where a child's standard descriptor points.
- `type Env enum`: Env says which environment a child gets. A Tin slice has no nil, so where Go's exec.Cmd says "nil inherits and an empty list is empty", this package says so with a variant.
- `type Cmd struct`: Cmd describes a program to start. Argv[0] is the program: a name without a slash is looked up in PATH.
- `type Process struct`: Process is a running child. Wait reaps it; a Process that is never waited for leaves a zombie.
- `type Result struct`: Result is a finished Run.
- `const SIGKILL = 9`: SIGKILL and SIGTERM are the signals Signal and Kill send.
- `const SIGTERM = 15`
- `const DefaultMaxOutput = 64 * 1024 * 1024`: DefaultMaxOutput is Run's cap on the stdout and stderr it collects: 64 MiB.
- `Start(c Cmd) !Process`: Start starts c and returns the running child. A start error names the program, like Go's exec.Error.
- `Run(c Cmd) !Result`: Run starts c, collects its output and waits for it. A non-empty Input is written to the child's standard input (which becomes a pipe) while the output is collected, so a child that answers while it reads does not deadlock; the pipe is closed after the last byte. Stdout and Stderr are captured unless they are File or Null; more than MaxOutput (DefaultMaxOutput when 0) bytes of the two together fail with fault.LimitExceeded and the child is killed. A non-zero exit is not a fault, and a task deadline (within) kills the child, reaps it and fails with fault.DeadlineExceeded.
- `(p mut Process) Wait() !i64`: Wait waits for the child, reaps it and returns its exit code, or -1 when a signal killed it. A task deadline (within) interrupts the wait, kills the child and reaps it.
- `(p Process) Pid() i64`: Pid is the child's process number.
- `(p Process) Signal(sig i64) !`: Signal sends sig to the child.
- `(p Process) Kill() !`: Kill sends SIGKILL to the child.
- `(p mut Process) Write(data str) !i64`: Write writes data to the child's standard input (Stdio.Pipe on Cmd.Stdin) and returns how many bytes went out. It never blocks the core: what the pipe cannot take yet waits for it to drain, so another task can read the child's output meanwhile. A task deadline interrupts the write with fault.DeadlineExceeded.
- `(p mut Process) CloseStdin() !`: CloseStdin closes the child's standard input, so a reader sees EOF.
- `(p Process) Read(buf mut []u8) !i64`: Read reads the child's standard output (Stdio.Pipe on Cmd.Stdout) into buf, up to its length, and returns how many bytes came; 0 is end of file.
- `(p Process) ReadStderr(buf mut []u8) !i64`: ReadStderr is Read for the child's standard error.
- `LookPath(name str) !str`: LookPath finds name like Go's exec.LookPath: a name with a slash is used as it is, otherwise each PATH entry is tried in order and the first executable file wins.

## sandbox

Package sandbox runs a program fenced by Linux (#1002): its own cgroup v2 (memory.max with no swap, cpu.max, pids.max, cpu.weight), new user, mount, PID, network, IPC, UTS and cgroup namespaces, a root built from read-only bind mounts of the system directories and the given inputs plus one writable scratch directory (pivot_root, a fresh /proc, no other host file visible), no network (a down loopback only), a seccomp allow-list, a hard timeout that kills the whole process tree, and its stdout and stderr captured up to a cap. It is meant for code from your own repositories (builds, tests, generated programs); code from anyone else belongs in a microVM, not here. Linux only: on macOS Run fails. The caller needs unprivileged user namespaces (or root) and, for the cgroup limits, a delegated cgroup v2 directory (Spec.Cgroup) that holds no processes of its own; see the package README for the exact requirements and how CI runs the escape tests.

- `type Bind struct`: Bind is a host file or directory mounted read-only inside the sandbox.
- `type Spec struct`: Spec describes one sandboxed run. Zero values mean: no cgroup limit for Memory, CPU, Pids and Weight (they need Cgroup), DefaultTimeout, DefaultMaxOutput, DefaultSystem, ScratchPath "/scratch", and Dir the scratch path (or "/" without one).
- `type Result struct`: Result is how a sandboxed run ended and what it printed.
- `const DefaultTimeout = 60 * 1000 * 1000 * 1000`: DefaultTimeout is Run's timeout when Spec.Timeout is 0: one minute.
- `const DefaultMaxOutput = 1024 * 1024`: DefaultMaxOutput is Run's cap on each of stdout and stderr when Spec.MaxOutput is 0: 1 MiB.
- `DefaultSystem() []str`: DefaultSystem is the host directories mounted read-only when Spec.System is empty; a missing one is skipped and a symlink (a merged /usr's /bin) is recreated as the same symlink.
- `Run(spec Spec) !Result`: Run runs spec.Argv in a new sandbox and waits for it: the output is read while it runs, the wait goes through the scheduler (other tasks keep running), and a task deadline (within) kills the tree like the timeout but fails with fault.DeadlineExceeded. A program that exits non-zero, dies of a signal, times out or is killed for memory is a Result, not a fault; a sandbox that cannot be built (no user namespaces, a missing input, a cgroup that is not delegated) or a program that cannot be executed is a fault that names the step.

## signal

Package signal lets a program handle operating-system signals, like Go's os/signal: Notify sends the chosen signals to a Chan, and a task takes them with Recv (#737). The handler the runtime installs only marks the signal and wakes the Chan (a byte on the Chan's pipe); the signal is taken by the task waiting in Recv, on that task's core, never in the handler. A signal no Chan listens for keeps its default action: Stop and Reset give a signal its first disposition back (usually the default, so the exit status shows the signal) and Ignore discards it. SIGSEGV and SIGBUS stay the runtime's, and SIGKILL and SIGSTOP cannot be caught.

In an anvil server, SIGTERM and SIGINT start the graceful drain as before; a Chan that listens for them gets them as well (anvil hands them on from its event loop), so an application can log or flush while the drain runs. Ignoring them there stops the drain too.

- `type Signal i64`: Signal is an operating-system signal number (Go's os.Signal / syscall.Signal).
- `const Interrupt Signal = 2`: Interrupt is SIGINT (Go's os.Interrupt), the same on every platform.
- `const Kill Signal = 9`: Kill is SIGKILL (Go's os.Kill): it cannot be caught or ignored.
- `type Chan struct`: Chan receives the signals Notify sends it (Go's chan os.Signal); a task takes them with Recv. Its signals wait in a pipe, so none is lost while no task waits (up to the pipe's 64 KiB).
- `New() !Chan`: New makes a Chan that listens for nothing yet; Notify adds signals. It fails when the process has no descriptor left, or 64 Chans are open at once.
- `Notify(c Chan, sigs ...Signal) !`: Notify sends sigs to c from now on (Go's signal.Notify); with no sigs, every signal it can catch. Any core may call it. It fails for SIGKILL, SIGSTOP, the fault signals the runtime owns or must not return into (SIGSEGV, SIGBUS, SIGILL, SIGFPE, SIGTRAP), a number out of range or a closed Chan.
- `Stop(c Chan)`: Stop ends every Notify of c (Go's signal.Stop): once it returns, no further signal reaches c. A signal no other Chan listens for gets its first disposition back. Signals already in c stay.
- `Reset(sigs ...Signal) !`: Reset undoes every Notify and Ignore of sigs (Go's signal.Reset), giving each the disposition it had when the program started (usually the default action); with no sigs, every signal.
- `Ignore(sigs ...Signal) !`: Ignore makes sigs ignored (Go's signal.Ignore): no Chan gets them and they do nothing; with no sigs, every signal Notify could catch. Reset or a later Notify undoes it.
- `Ignored(sig Signal) bool`: Ignored reports whether sig is ignored now (Go's signal.Ignored): by Ignore, or inherited ignored from the parent (nohup ignores SIGHUP).
- `Notified(sig Signal) bool`: Notified reports whether some Chan listens for sig now.
- `Raise(sig Signal) !`: Raise sends sig to this process (kill(getpid(), sig)): a handled signal reaches the Chans listening for it, an unhandled one takes its default action, which may end the process (its buffered output is lost then: flush first).
- `(c Chan) Recv() !Signal`: Recv waits for the next signal sent to c and returns it. The wait takes the task's deadline and cancellation like any other (inside `within 5s` it fails with fault.DeadlineExceeded); the core runs its other tasks meanwhile, and in main (outside a task) it blocks.
- `(c Chan) TryRecv() (Signal, bool)`: TryRecv takes a signal waiting in c without waiting; ok is false when there is none.
- `(c mut Chan) Close()`: Close stops c and frees its descriptors and slot; signals still in it are dropped. Using c afterwards fails (Notify, Recv) or does nothing (Stop, TryRecv).
- `(s Signal) String() str`: String is the signal's description, as Go's syscall.Signal prints it ("interrupt", "terminated"), or "signal N" for a number without one.

## trail

Package trail manipulates slash-separated file paths (like Go's path/filepath on Unix).

- `const Separator = '/'`: Separator is the path separator byte.
- `Clean(path str) str`: Clean returns the shortest path equivalent to path by Go's rules: no "." or ".." elements where avoidable, no repeated or trailing slashes, "." for an empty path.
- `IsAbs(path str) bool`: IsAbs reports whether path starts with a slash.
- `Base(path str) str`: Base returns the last element of path after dropping trailing slashes: "." for an empty path, "/" for all slashes.
- `Dir(path str) str`: Dir returns Clean of everything but the last element of path: "." when there is no slash.
- `Ext(path str) str`: Ext returns the suffix of path's last element from its final dot, or "".
- `Split(path str) (str, str)`: Split splits path right after its last slash into (dir, file); dir keeps the slash.
- `JoinAll(parts []str) str`: JoinAll joins the non-empty parts with slashes and Cleans the result; "" when every part is empty.
- `Join2(a str, b str) str`: Join2 joins two path elements like Go's filepath.Join(a, b).
- `Join3(a str, b str, c str) str`: Join3 joins three path elements like Go's filepath.Join(a, b, c).
- `Rel(base str, targ str) !str`: Rel returns a relative path that is lexically equivalent to targ when joined to base, or a fault when one is absolute and the other is not or base holds "..".
- `Match(pattern str, name str) !bool`: Match reports whether name matches the shell pattern: '*' (no slash), '?', '[a-z]', '[^x]' and '\' escapes, like Go's path.Match: a malformed pattern is a fault even when the name stops matching before it (Go's filepath.Match returns false there).

## lever

Package lever parses command-line flags (like Go's flag): register handles, Parse the arguments, then read .Val().

- `type Flag struct`: Flag is one registered flag; the typed handles below wrap it.
- `type StrFlag struct`: StrFlag is the handle of a string flag.
- `type IntFlag struct`: IntFlag is the handle of an integer flag.
- `type BoolFlag struct`: BoolFlag is the handle of a boolean flag.
- `type F64Flag struct`: F64Flag is the handle of a floating-point flag.
- `Str(name str, def str, help str) StrFlag`: Str registers a string flag with its default and help text.
- `Int(name str, def i64, help str) IntFlag`: Int registers an integer flag with its default and help text.
- `Bool(name str, def bool, help str) BoolFlag`: Bool registers a boolean flag with its default and help text.
- `F64(name str, def f64, help str) F64Flag`: F64 registers a floating-point flag with its default and help text.
- `(h StrFlag) Val() str`: Val returns the flag's value (its default until Parse sets it).
- `(h IntFlag) Val() i64`: Val returns the flag's value (its default until Parse sets it).
- `(h BoolFlag) Val() bool`: Val returns the flag's value (its default until Parse sets it).
- `(h F64Flag) Val() f64`: Val returns the flag's value (its default until Parse sets it).
- `(h StrFlag) Given() bool`: Given reports whether the flag appeared on the command line.
- `(h IntFlag) Given() bool`: Given reports whether the flag appeared on the command line.
- `(h BoolFlag) Given() bool`: Given reports whether the flag appeared on the command line.
- `(h F64Flag) Given() bool`: Given reports whether the flag appeared on the command line.
- `Reset()`: Reset forgets every registered flag and parse result (for programs that parse several times).
- `Rest() []str`: Rest returns the arguments left after the flags (empty before Parse).
- `Parsed() bool`: Parsed reports whether Parse has run.
- `Set(name str, value str) !`: Set assigns value to the flag named name as if it were given on the command line.
- `Parse(args []str) !`: Parse reads flags from args (without the program name) until the first non-flag or "--"; the rest is kept for Rest().
- `Usage() str`: Usage returns the flags sorted by name, each with its value type, help and non-zero default, formatted exactly like Go's PrintDefaults.

## tty

Package tty is the terminal for command line programs: whether a descriptor is a terminal, its size, raw mode with a State that restores it, a pseudo-terminal pair for tests, and colour that turns itself off when the output is not a terminal, when NO_COLOR is set or when TERM is dumb.

- `type State struct`: State is a terminal's mode before Raw changed it; Close (or Restore) puts it back, so `use st = tty.Raw(0)` restores the terminal on every way out of the function.
- `IsTerminal(fd i64) bool`: IsTerminal reports whether fd is a terminal.
- `Size(fd i64) !(i64, i64)`: Size is the terminal's width and height in characters.
- `Raw(fd i64) !State`: Raw puts the terminal into raw mode (no echo, no line editing, no signals from keys, bytes as typed) and returns the state to restore.
- `Restore(st State) !`: Restore puts the terminal back as it was before Raw.
- `(st State) Close() !`: Close restores the terminal (for `use`).
- `IsRaw(fd i64) bool`: IsRaw reports whether the terminal at fd has echo and line editing off.
- `OpenPty() !(i64, i64)`: OpenPty opens a pseudo-terminal pair: the controlling side and the terminal side, as descriptors.
- `CloseFd(fd i64)`: CloseFd closes a descriptor OpenPty gave.
- `Colors(fd i64) bool`: Colors reports whether colour should be written to fd: it is a terminal, NO_COLOR is unset and TERM is not dumb.
- `Paint(on bool, code str, s str) str`: Paint wraps s in the SGR code (such as "1" bold, "31" red, "32" green, "2" dim) when on is true, else returns s.

## tide

Package tide is clocks, durations, civil (calendar) time and time zones, like Go's time package. A Zone comes from the IANA database (TZif, RFC 8536): $ZONEINFO, the system directories, or the nested package tide/tzdata, which embeds the whole database for images with no /usr/share/zoneinfo (import it for its side effect).

- `Truncate(ns i64, d i64) i64`: Truncate returns ns rounded down to a multiple of d since the zero time (0001-01-01), like Go's Time.Truncate; d <= 0 returns ns unchanged. A result outside Unix nanoseconds panics.
- `Round(ns i64, d i64) i64`: Round returns ns rounded to the nearest multiple of d since the zero time, with halfway values rounding up, like Go's Time.Round; d <= 0 returns ns unchanged. A result outside Unix nanoseconds panics.
- `AddDate(ns i64, z Zone, years i64, months i64, days i64) i64`: AddDate returns the instant years, months and days after ns in zone z, keeping the wall-clock fields like Go's Time.AddDate: January 31 plus one month lands in early March. Out-of-range fields carry the way DateIn does.
- `ISOWeek(c Civil) (i64, i64)`: ISOWeek returns the ISO 8601 year and week (1 to 53) of the civil date, like Go's Time.ISOWeek: week 1 is the week holding the first Thursday of the year.
- `const Layout = "01/02 03:04:05PM '06 -0700"`: The standard layouts, as Go's time package names them.
- `const ANSIC = "Mon Jan _2 15:04:05 2006"`
- `const UnixDate = "Mon Jan _2 15:04:05 MST 2006"`
- `const RubyDate = "Mon Jan 02 15:04:05 -0700 2006"`
- `const RFC822 = "02 Jan 06 15:04 MST"`
- `const RFC822Z = "02 Jan 06 15:04 -0700"`
- `const RFC850 = "Monday, 02-Jan-06 15:04:05 MST"`
- `const RFC1123 = "Mon, 02 Jan 2006 15:04:05 MST"`
- `const RFC1123Z = "Mon, 02 Jan 2006 15:04:05 -0700"`
- `const RFC3339 = "2006-01-02T15:04:05Z07:00"`
- `const RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"`
- `const Kitchen = "3:04PM"`
- `const Stamp = "Jan _2 15:04:05"`
- `const StampMilli = "Jan _2 15:04:05.000"`
- `const StampMicro = "Jan _2 15:04:05.000000"`
- `const StampNano = "Jan _2 15:04:05.000000000"`
- `const DateTime = "2006-01-02 15:04:05"`
- `const DateOnly = "2006-01-02"`
- `const TimeOnly = "15:04:05"`
- `Format(ns i64, z Zone, layout str) str`: Format renders the instant ns in zone z with a reference-time layout, like Go's Time.Format.
- `Parse(layout str, value str, z Zone) !i64`: Parse parses value with a reference-time layout, like Go's time.ParseInLocation: a wall time with no zone in the value is read in z, while a zone offset or abbreviation is that instant (matched against z when it names one of z's zones). It returns Unix nanoseconds; malformed or out-of-range values fail with a parse fault (tide's message carries the layout and text).
- `const Nanosecond = 1`: Durations are i64 nanoseconds; these constants are the units, like Go's time.Duration.
- `const Microsecond = 1000`
- `const Millisecond = 1000000`
- `const Second = 1000000000`
- `const Minute = 60000000000`
- `const Hour = 3600000000000`
- `const Sunday = 0`: Weekdays as returned in Civil.Weekday, Sunday first like Go.
- `const Monday = 1`
- `const Tuesday = 2`
- `const Wednesday = 3`
- `const Thursday = 4`
- `const Friday = 5`
- `const Saturday = 6`
- `Now() i64`: Now returns monotonic nanoseconds since boot (CLOCK_UPTIME_RAW): use it to measure intervals.
- `Wall() i64`: Wall returns the wall clock as nanoseconds since the Unix epoch, 1970-01-01T00:00:00Z.
- `Since(t i64) i64`: Since returns the nanoseconds elapsed since the Now() reading t.
- `Sleep(ns i64)`: Sleep pauses the running code for ns nanoseconds (nothing happens when ns <= 0); in a task, the core serves others meanwhile. A deadline or cancellation that comes first ends the sleep and leaves the way a safepoint does: the `within`, `limit` or `guard` block that owns it fails with its fault (fault.DeadlineExceeded), and a request past its deadline gets 504 (#527).
- `Wait(ns i64) !`: Wait pauses for ns like Sleep, but inside a request with a deadline it fails with "deadline exceeded" once the deadline comes first. On a server core, other requests run while one waits.
- `Seconds(d i64) f64`: Seconds returns d as floating-point seconds, like Go's Duration.Seconds.
- `Minutes(d i64) f64`: Minutes returns d as floating-point minutes.
- `Hours(d i64) f64`: Hours returns d as floating-point hours.
- `Milliseconds(d i64) i64`: Milliseconds returns d as whole milliseconds, truncated toward zero.
- `Microseconds(d i64) i64`: Microseconds returns d as whole microseconds, truncated toward zero.
- `FormatDuration(d i64) str`: FormatDuration renders d exactly like Go's Duration.String: "1.5s", "250ms", "1h2m3s", "0s", "-1.5µs".
- `ParseDuration(s str) !i64`: ParseDuration parses "300ms", "-1.5h" or "2h45m" (units ns us µs ms s m h) exactly like Go's time.ParseDuration.
- `type Civil struct`: Civil is a broken-down instant: Month 1..12, Day 1..31, Weekday 0 (Sunday)..6, YearDay 1..366, and, from In, the zone's Offset in seconds east of UTC and its abbreviation in Zone.
- `IsLeap(year i64) bool`: IsLeap reports whether year is a leap year in the proleptic Gregorian calendar.
- `DaysIn(year i64, month i64) i64`: DaysIn returns the number of days in month (1..12) of year, or 0 for a month out of range.
- `DaysFromCivil(y i64, m i64, d i64) i64`: DaysFromCivil returns the days from 1970-01-01 to the date y-m-d (m 1..12; d may be out of range and carries).
- `CivilFromDays(z i64) (i64, i64, i64)`: CivilFromDays returns the (year, month, day) that is z days after 1970-01-01.
- `UTCSec(sec i64) Civil`: UTCSec breaks Unix seconds into UTC calendar fields (Nano is 0); it covers every i64 second.
- `UTC(ns i64) Civil`: UTC breaks the Unix-nanosecond instant ns into its UTC calendar fields.
- `Date(year i64, month i64, day i64, hour i64, min i64, sec i64, nano i64) i64`: Date returns the Unix nanoseconds of the UTC civil time; out-of-range fields carry like Go's time.Date (month 13 is January of the next year), and a time outside the years 1677..2262 that i64 nanoseconds hold panics (integer overflow).
- `Unix(c Civil) i64`: Unix returns the Unix nanoseconds of c (the inverse of UTC; Weekday and YearDay are ignored, other fields carry).
- `UnixSec(c Civil) i64`: UnixSec returns the Unix seconds of c, rounded toward negative infinity.
- `WeekdayName(d i64) str`: WeekdayName returns the English name of weekday d (0 = Sunday), or "%!Weekday(d)" with d unsigned like Go.
- `MonthName(m i64) str`: MonthName returns the English name of month m (1 = January), or "%!Month(m)" with m unsigned like Go.
- `FormatRFC3339(ns i64) str`: FormatRFC3339 renders the Unix-nanosecond instant ns as "2026-10-01T11:22:05Z" (whole seconds, UTC).
- `FormatRFC3339Nano(ns i64) str`: FormatRFC3339Nano is FormatRFC3339 with the fractional seconds, trailing zeros removed: "2026-10-01T11:22:05.5Z".
- `ParseRFC3339(s str) !i64`: ParseRFC3339 parses "2026-10-01T11:22:05Z", optional fraction ".123" and offsets "+02:00", accepting what Go's time.Parse(RFC3339) accepts, into Unix nanoseconds.
- `FormatHTTP(unixSec i64) str`: FormatHTTP renders Unix seconds in the HTTP date format "Thu, 01 Oct 2026 11:22:05 GMT".
- `type Zone struct`: Zone is a time zone: the transitions of the IANA database with the local time in effect after each, plus the TZ string that extends the zone past its last transition. A Zone is a handle that can be stored in a global; LoadZone caches one per core.
- `RegisterEmbedded(packed str) bool`: RegisterEmbedded installs the packed IANA database of tide/tzdata on this core: it inflates the DEFLATE stream (RFC 1951) into the container of u32 count; per zone, u32 name length, u32 data length, the name and the TZif bytes (RFC 8536), and keeps each zone's bytes. The package tide/tzdata calls it from its globals' initializer, on every core, before main; it reports whether the stream was well formed. LoadZone reads the database after $ZONEINFO and the system directories miss.
- `(z Zone) Name() str`: Name returns the zone's name, like "Europe/Paris".
- `UTCZone() Zone`: UTCZone returns the UTC zone.
- `FixedZone(name str, offset i64) Zone`: FixedZone returns a zone that is always offset seconds east of UTC, shown as name.
- `LoadZoneData(name str, data str) !Zone`: LoadZoneData parses the bytes of a TZif file (RFC 8536) as the zone called name, like Go's time.LoadLocationFromTZData.
- `LoadZone(name str) !Zone`: LoadZone returns the zone with an IANA name ("Europe/Paris", "Asia/Kathmandu", "UTC") from $ZONEINFO, the system directories and the database embedded by tide/tzdata, reading each name once per core. Unknown names fail with ErrUnknownZone (fault.Is). Loading reads files, and so needs the files capability.
- `Local() Zone`: Local returns the local zone: $TZ ("" is UTC, a path after ':' or a leading '/' is a file, "UTC" and names are looked up like LoadZone) or /etc/localtime when $TZ is unset, falling back to UTC, as Go's time.Local does.
- `In(ns i64, z Zone) Civil`: In returns the civil time of the instant ns in zone z, with Offset (seconds east of UTC) and Zone (the abbreviation, like "CET") set.
- `DateIn(year0 i64, month0 i64, day0 i64, hour0 i64, min0 i64, sec0 i64, nano0 i64, z Zone) i64`: DateIn returns the Unix nanoseconds of the civil time in zone z. Fields out of range carry like Date. A wall time in a gap (the clocks going forward) or an overlap (going back) picks the instant Go's time.Date picks: the one whose zone offset is valid there.

## dice

Package dice is fast pseudo-random numbers: xoshiro256** generators with a lazily seeded per-core one, and math/rand/v2's PCG-DXSM and ChaCha8 behind RandV2 (V2 names where a legacy name exists).

- `type Rand struct`: Rand is a xoshiro256** generator; make one with New or FromState, or call the package functions for this core's generator.
- `(r mut Rand) Seed(s u64)`: Seed resets r to the sequence for seed s (expanded with splitmix64, so every seed gives a good state).
- `New(s u64) Rand`: New returns a generator seeded with s; equal seeds give equal sequences.
- `FromState(s0 u64, s1 u64, s2 u64, s3 u64) Rand`: FromState returns a generator holding the exact xoshiro256** state words, which must not all be zero.
- `(r Rand) State() (u64, u64, u64, u64)`: State returns the four state words, so the sequence can be resumed later with FromState.
- `(r mut Rand) U64() u64`: U64 returns the next uniformly distributed 64-bit value.
- `(r mut Rand) U32() u32`: U32 returns the next uniformly distributed 32-bit value (the high half of U64).
- `(r mut Rand) U64n(n u64) u64`: U64n returns a uniform value in [0, n) without bias (Lemire's method); n == 0 means the full 64-bit range.
- `(r mut Rand) I64n(n i64) i64`: I64n returns a uniform value in [0, n); it panics when n <= 0.
- `(r mut Rand) Intn(n i64) i64`: Intn is I64n under Go's name (Tin's int is i64).
- `(r mut Rand) Range(lo i64, hi i64) i64`: Range returns a uniform value in [lo, hi); it panics when hi <= lo.
- `(r mut Rand) F64() f64`: F64 returns a uniform float in [0, 1) built from 53 random bits.
- `(r mut Rand) NormF64() f64`: NormF64 returns a normally distributed float (mean 0, standard deviation 1) by Marsaglia's polar method.
- `(r mut Rand) Shuffle(xs mut []i64)`: Shuffle permutes xs uniformly in place (Fisher-Yates).
- `(r mut Rand) ShuffleStr(xs mut []str)`: ShuffleStr permutes the strings xs uniformly in place.
- `(r mut Rand) Perm(n i64) []i64`: Perm returns a uniformly random permutation of 0..n-1 (empty when n <= 0).
- `(r mut Rand) Fill(b mut []u8)`: Fill overwrites every byte of b with random bytes, eight at a time.
- `(r mut Rand) Bytes(n i64) []u8`: Bytes returns n random bytes (empty when n <= 0).
- `(r mut Rand) Str(n i64, alphabet str) str`: Str returns n characters drawn uniformly from alphabet (its bytes when ASCII, its runes otherwise); "" when n <= 0 or alphabet is empty.
- `Seed(s u64)`: Seed seeds this core's generator so that the package functions become deterministic on this core.
- `U64() u64`: U64 returns the next 64-bit value from this core's generator.
- `U32() u32`: U32 returns the next 32-bit value from this core's generator.
- `U64n(n u64) u64`: U64n returns a uniform value in [0, n) from this core's generator (n == 0 means the full range).
- `I64n(n i64) i64`: I64n returns a uniform value in [0, n) from this core's generator; it panics when n <= 0.
- `Intn(n i64) i64`: Intn is I64n under Go's name.
- `Range(lo i64, hi i64) i64`: Range returns a uniform value in [lo, hi) from this core's generator; it panics when hi <= lo.
- `F64() f64`: F64 returns a uniform float in [0, 1) from this core's generator.
- `NormF64() f64`: NormF64 returns a standard normal float from this core's generator.
- `Shuffle(xs mut []i64)`: Shuffle permutes xs uniformly in place with this core's generator.
- `ShuffleStr(xs mut []str)`: ShuffleStr permutes the strings xs uniformly in place with this core's generator.
- `Perm(n i64) []i64`: Perm returns a random permutation of 0..n-1 from this core's generator.
- `Fill(b mut []u8)`: Fill overwrites b with random bytes from this core's generator.
- `Bytes(n i64) []u8`: Bytes returns n random bytes from this core's generator.
- `Str(n i64, alphabet str) str`: Str returns n random characters of alphabet from this core's generator.
- `shape SourceV2`: SourceV2 is the 64-bit stream a RandV2 draws from: a PCG, a ChaCha8, or a Rand.
- `type PCG struct`: PCG is Go math/rand/v2's 128-bit PCG-DXSM generator.
- `NewPCG(d1 u64, d2 u64) PCG`: NewPCG returns a PCG stream initialized with the two seed words (Go's NewPCG).
- `(p mut PCG) Uint64() u64`: Uint64 returns the next Go-compatible PCG-DXSM value.
- `(r mut Rand) Uint64() u64`: Uint64 returns the next value of the legacy generator, so a Rand is a v2 source too.
- `type ChaCha8 struct`: ChaCha8 is Go math/rand/v2's ChaCha8 stream: four interleaved blocks per generation, reseeded from the last four words.
- `NewChaCha8(seed [32]u8) ChaCha8`: NewChaCha8 returns a ChaCha8 stream seeded with the 32 bytes of seed (Go's NewChaCha8).
- `(c mut ChaCha8) Uint64() u64`: Uint64 returns the next word of the stream (Go's ChaCha8.Uint64).
- `type RandV2 struct`: RandV2 draws Go math/rand/v2-style values from a 64-bit source (Go's Rand).
- `NewV2(source dyn SourceV2) RandV2`: NewV2 returns a RandV2 that draws from source, a PCG, a ChaCha8 or a Rand (Go's New).
- `(r mut RandV2) Uint64() u64`: Uint64 returns the next value of the source.
- `(r mut RandV2) Int64() i64`: Int64 returns a non-negative 63-bit value (Go's Int64).
- `(r mut RandV2) Int() i64`: Int returns a non-negative 63-bit value (Tin's int is i64; Go's Int).
- `(r mut RandV2) Uint() u64`: Uint returns a uniform 64-bit unsigned value (Go's Uint).
- `(r mut RandV2) Int32N(n i32) i32`: Int32N returns a uniform value in [0, n); it panics when n <= 0.
- `(r mut RandV2) Int64N(n i64) i64`: Int64N returns a uniform value in [0, n); it panics when n <= 0.
- `(r mut RandV2) Float64() f64`: Float64 returns a uniform value in [0, 1) from the low 53 bits of a source word (Go's Float64).
- `(r mut RandV2) NormFloat64() f64`: NormFloat64 returns a standard normal value by Marsaglia and Tsang's ziggurat, as Go's NormFloat64.
- `(r mut RandV2) ExpFloat64() f64`: ExpFloat64 returns an exponential value with rate 1 by Marsaglia and Tsang's ziggurat, as Go's ExpFloat64.
- `(r mut RandV2) Shuffle(n i64, swap fn(i64, i64))`: Shuffle calls swap(i, j) for the pairs of Go's Fisher-Yates shuffle of n elements; it panics when n < 0.
- `(r mut RandV2) Perm(n i64) []i64`: Perm returns a uniform permutation of 0 through n-1 (Go's Perm); it panics when n < 0.
- `Int32N(n i32) i32`: Int32N returns a uniform value in [0, n) from this core's v2 stream; it panics when n <= 0.
- `Int64N(n i64) i64`: Int64N returns a uniform value in [0, n) from this core's v2 stream; it panics when n <= 0.
- `N(n i64) i64`: N returns a uniform value in [0, n) from this core's v2 stream; it panics when n <= 0 (i64 only: Tin has no generic conversion).
- `Int64() i64`: Int64 returns a non-negative 63-bit value from this core's v2 stream.
- `Int() i64`: Int returns a non-negative 63-bit value from this core's v2 stream.
- `Uint() u64`: Uint returns a uniform 64-bit unsigned value from this core's v2 stream.
- `Float64() f64`: Float64 returns a uniform value in [0, 1) from this core's v2 stream.
- `NormFloat64() f64`: NormFloat64 returns a standard normal value from this core's v2 stream.
- `ExpFloat64() f64`: ExpFloat64 returns an exponential value with rate 1 from this core's v2 stream.
- `ShuffleV2(n i64, swap fn(i64, i64))`: ShuffleV2 calls swap for the pairs of a Fisher-Yates shuffle of n elements from this core's v2 stream.
- `PermV2(n i64) []i64`: PermV2 returns a uniform permutation of 0 through n-1 from this core's v2 stream; it panics when n < 0.

## sift

Package sift sorts and searches slices and has the generic functions on them (like Go's sort, slices and cmp). Sort, SortFunc, IsSorted and the rest work on any element type; the type-specific functions (Ints, Strs, SortBy ...) are the faster, older forms.

- `Ints(xs mut []i64)`: Ints sorts xs in increasing order with pattern-defeating quicksort (not stable, O(n log n) worst case).
- `IntsDesc(xs mut []i64)`: IntsDesc sorts xs in decreasing order.
- `U64s(xs mut []u64)`: U64s sorts xs in increasing unsigned order.
- `F64s(xs mut []f64)`: F64s sorts xs in increasing order with NaNs first, like Go's slices.Sort (-0 sorts before 0).
- `Strs(xs mut []str)`: Strs sorts xs in increasing bytewise order.
- `SortBy(xs mut []i64, less fn(i64, i64) bool)`: SortBy sorts xs so that less(xs[i+1], xs[i]) is never true (less must be a strict weak order).
- `HeapInts(xs mut []i64)`: HeapInts sorts xs in increasing order with heapsort (slower than Ints, no recursion, no extra memory).
- `StableInts(xs mut []i64)`: StableInts sorts xs in increasing order with a merge sort that keeps equal elements in their original order.
- `IsSortedInts(xs []i64) bool`: IsSortedInts reports whether xs is in increasing order.
- `IsSortedStrs(xs []str) bool`: IsSortedStrs reports whether xs is in increasing bytewise order.
- `SearchInts(xs []i64, x i64) i64`: SearchInts returns the first index of sorted xs holding a value >= x (len(xs) when there is none).
- `SearchStrs(xs []str, x str) i64`: SearchStrs returns the first index of sorted xs holding a str >= x bytewise (len(xs) when there is none).
- `ReverseInts(xs mut []i64)`: ReverseInts reverses xs in place.
- `ReverseStrs(xs mut []str)`: ReverseStrs reverses xs in place.
- `UniqInts(xs mut []i64) i64`: UniqInts compacts runs of equal values in sorted xs to one element and returns the new length (xs[0:k] is the result).
- `MinInts(xs []i64) !i64`: MinInts returns the smallest element of xs, or a fault when xs is empty.
- `MaxInts(xs []i64) !i64`: MaxInts returns the largest element of xs, or a fault when xs is empty.
- `SumInts(xs []i64) i64`: SumInts returns the sum of xs (0 for an empty slice); it panics when the sum overflows i64.
- `IndexInts(xs []i64, x i64) i64`: IndexInts returns the index of the first x in xs, or -1.
- `ContainsStr(xs []str, x str) bool`: ContainsStr reports whether x occurs in xs.
- `EqualInts(a []i64, b []i64) bool`: EqualInts reports whether a and b have the same length and elements.
- `Map[T constraints.Any, U constraints.Any](xs []T, f fn(T) U) []U`: Map returns f applied to each element of xs.
- `Filter[T constraints.Any](xs []T, keep_ fn(T) bool) []T`: Filter returns the elements of xs for which keep returns true, in order.
- `Reduce[T constraints.Any, A constraints.Any](xs []T, start A, f fn(A, T) A) A`: Reduce folds xs into one value: f(f(f(start, x0), x1), ...).
- `shape Ordered = i64 | i32 | i16 | i8 | u64 | u32 | u16 | u8 | f64 | f32 | str`: Ordered is the set of built-in types with a total ordering operator.
- `Sort[E Ordered](xs mut []E)`: Sort sorts xs in ascending order, in place. Floating-point NaNs sort first. It is not stable, and the order of equal elements is the same as Go's slices.Sort.
- `SortFunc[E constraints.Any](xs mut []E, cmp fn(E, E) i64)`: SortFunc sorts xs in place by cmp, which returns a negative number when a sorts before b, zero when they are equal and a positive number after. It is not stable.
- `SortStableFunc[E constraints.Any](xs mut []E, cmp fn(E, E) i64)`: SortStableFunc is SortFunc, keeping the original order of elements that compare equal.
- `IsSorted[E Ordered](xs []E) bool`: IsSorted reports whether xs is in ascending order.
- `IsSortedFunc[E constraints.Any](xs []E, cmp fn(E, E) i64) bool`: IsSortedFunc reports whether xs is sorted by cmp.
- `Less[E Ordered](x E, y E) bool`: Less is cmp.Less: x < y, with NaN smaller than every other value (and so before them in Sort).
- `Cmp[E Ordered](x E, y E) i64`: Cmp is cmp.Compare: -1 if x sorts before y, 0 if they are equal, +1 after. NaNs are equal to each other and sort before every other value.
- `BinarySearch[E Ordered](xs []E, target E) (i64, bool)`: BinarySearch searches the sorted xs for target and returns the position where it is, or would be inserted, and whether it is there.
- `BinarySearchFunc[E constraints.Any, T constraints.Any](xs []E, target T, cmp fn(E, T) i64) (i64, bool)`: BinarySearchFunc is BinarySearch for a target of another type, ordered by cmp(element, target).
- `Min[E Ordered](xs []E) E`: Min returns the smallest element of xs; a NaN anywhere gives NaN. It panics if xs is empty. (-0 and +0 compare equal here, so a mix of them returns whichever comes first.)
- `Max[E Ordered](xs []E) E`: Max returns the largest element of xs; a NaN anywhere gives NaN. It panics if xs is empty.
- `MinFunc[E constraints.Any](xs []E, cmp fn(E, E) i64) E`: MinFunc returns the first smallest element of xs by cmp. It panics if xs is empty.
- `MaxFunc[E constraints.Any](xs []E, cmp fn(E, E) i64) E`: MaxFunc returns the first largest element of xs by cmp. It panics if xs is empty.
- `Index[E constraints.Comparable](xs []E, v E) i64`: Index returns the position of the first element equal to v, or -1.
- `IndexFunc[E constraints.Any](xs []E, f fn(E) bool) i64`: IndexFunc returns the position of the first element for which f is true, or -1.
- `Contains[E constraints.Comparable](xs []E, v E) bool`: Contains reports whether v is in xs.
- `ContainsFunc[E constraints.Any](xs []E, f fn(E) bool) bool`: ContainsFunc reports whether f is true for some element of xs.
- `Equal[E constraints.Comparable](a []E, b []E) bool`: Equal reports whether a and b have the same length and equal elements.
- `EqualFunc[A constraints.Any, B constraints.Any](a []A, b []B, eq fn(A, B) bool) bool`: EqualFunc is Equal for two element types, with eq deciding.
- `Compare[E Ordered](a []E, b []E) i64`: Compare compares a and b element by element with Cmp, then by length: -1, 0 or +1.
- `CompareFunc[A constraints.Any, B constraints.Any](a []A, b []B, cmp fn(A, B) i64) i64`: CompareFunc is Compare for two element types, with cmp comparing elements.
- `Reverse[E constraints.Any](xs mut []E)`: Reverse reverses xs in place.
- `Clone[E constraints.Any](xs []E) []E`: Clone returns a copy of xs that shares nothing with it.
- `Grow[E constraints.Any](xs []E, n i64) []E`: Grow returns a copy of xs with room for n more elements before it has to grow again.
- `Concat[E constraints.Any](a []E, b []E) []E`: Concat returns a new slice holding a followed by b.
- `ConcatAll[E constraints.Any](parts [][]E) []E`: ConcatAll returns a new slice holding every slice of parts, in order.
- `Repeat[E constraints.Any](xs []E, count i64) []E`: Repeat returns a new slice that repeats xs count times.
- `Insert[E constraints.Any](xs mut []E, i i64, v E) []E`: Insert inserts v at position i (0 to len(xs)) and returns the longer slice. Like append, it grows xs in place, so every other reference to the same slice sees the new length.
- `InsertAll[E constraints.Any](xs mut []E, i i64, vs []E) []E`: InsertAll inserts all of vs at position i and returns the longer slice (grown in place, as Insert).
- `Delete[E constraints.Any](xs mut []E, i i64, j i64) []E`: Delete removes xs[i:j] and returns the shorter slice; the elements after j move down in place.
- `DeleteFunc[E constraints.Any](xs mut []E, del fn(E) bool) []E`: DeleteFunc removes the elements for which del is true, in place, and returns the shorter slice.
- `Replace[E constraints.Any](xs mut []E, i i64, j i64, vs []E) []E`: Replace replaces xs[i:j] with vs and returns the resulting slice (grown or shrunk in place).
- `Compact[E constraints.Comparable](xs mut []E) []E`: Compact removes runs of equal consecutive elements, keeping the first of each run, in place, and returns the shorter slice.
- `CompactFunc[E constraints.Any](xs mut []E, eq fn(E, E) bool) []E`: CompactFunc is Compact with eq deciding which neighbours are equal.
- `Each[E constraints.Any](xs []E, f fn(E))`: Each calls f for every element of xs in ascending index order.

## atlas

Package atlas is the functions on maps (like Go's maps): keys, values, copies and comparisons.

- `Keys[K constraints.Comparable, V constraints.Any](m map[K]V) []K`: Keys returns m's keys in insertion order.
- `Values[K constraints.Comparable, V constraints.Any](m map[K]V) []V`: Values returns m's values in insertion order.
- `SortedKeys[K sift.Ordered, V constraints.Any](m map[K]V) []K`: SortedKeys returns m's keys in ascending order (NaN first), whatever order they were added in.
- `Clone[K constraints.Comparable, V constraints.Any](m map[K]V) map[K]V`: Clone returns a new map with the same entries, in the same order.
- `Copy[K constraints.Comparable, V constraints.Any](dst mut map[K]V, src map[K]V)`: Copy adds every entry of src to dst, replacing the values of keys dst already has.
- `Equal[K constraints.Comparable, V constraints.Comparable](a map[K]V, b map[K]V) bool`: Equal reports whether a and b have the same keys with equal values.
- `EqualFunc[K constraints.Comparable, V1 constraints.Any, V2 constraints.Any](a map[K]V1, b map[K]V2, eq fn(V1, V2) bool) bool`: EqualFunc is Equal with eq comparing the values, which may have different types.
- `DeleteFunc[K constraints.Comparable, V constraints.Any](m mut map[K]V, del fn(K, V) bool)`: DeleteFunc removes the entries for which del is true.

## cairn

Package cairn is a set of containers: heaps, deques, a queue, sets, a bitset and an LRU cache for i64 and str values, and the generic Heap, Deque, Set and Cache over any element types, with Go's container/list (List, Element) and container/ring (Ring) over any element types too.

- `type IntHeap struct`: IntHeap is a binary min-heap of i64 values; IntHeap{} is ready to use.
- `NewIntHeap(n i64) IntHeap`: NewIntHeap returns an empty min-heap with room for n values.
- `(h mut IntHeap) Push(v i64)`: Push adds v to the heap.
- `(h mut IntHeap) Pop() (i64, bool)`: Pop removes and returns the smallest value, or (0, false) when the heap is empty.
- `(h IntHeap) Peek() (i64, bool)`: Peek returns the smallest value without removing it, or (0, false) when the heap is empty.
- `(h IntHeap) Len() i64`: Len returns the number of values in the heap.
- `type IntMaxHeap struct`: IntMaxHeap is a binary max-heap of i64 values; IntMaxHeap{} is ready to use.
- `NewIntMaxHeap(n i64) IntMaxHeap`: NewIntMaxHeap returns an empty max-heap with room for n values.
- `(h mut IntMaxHeap) Push(v i64)`: Push adds v to the heap.
- `(h mut IntMaxHeap) Pop() (i64, bool)`: Pop removes and returns the largest value, or (0, false) when the heap is empty.
- `(h IntMaxHeap) Peek() (i64, bool)`: Peek returns the largest value without removing it, or (0, false) when the heap is empty.
- `(h IntMaxHeap) Len() i64`: Len returns the number of values in the heap.
- `type IntDeque struct`: IntDeque is a double-ended queue of i64 values in a growing ring buffer; IntDeque{} is ready to use.
- `NewIntDeque(n i64) IntDeque`: NewIntDeque returns an empty deque with room for n values.
- `(d mut IntDeque) PushBack(v i64)`: PushBack appends v at the back.
- `(d mut IntDeque) PushFront(v i64)`: PushFront prepends v at the front.
- `(d mut IntDeque) PopFront() (i64, bool)`: PopFront removes and returns the front value, or (0, false) when the deque is empty.
- `(d mut IntDeque) PopBack() (i64, bool)`: PopBack removes and returns the back value, or (0, false) when the deque is empty.
- `(d IntDeque) Front() (i64, bool)`: Front returns the front value, or (0, false) when the deque is empty.
- `(d IntDeque) Back() (i64, bool)`: Back returns the back value, or (0, false) when the deque is empty.
- `(d IntDeque) At(i i64) i64`: At returns the i-th value from the front, panicking when i is out of range.
- `(d IntDeque) Len() i64`: Len returns the number of values in the deque.
- `type IntQueue struct`: IntQueue is a first-in first-out queue of i64 values in a growing ring buffer; IntQueue{} is ready to use.
- `NewIntQueue(n i64) IntQueue`: NewIntQueue returns an empty queue with room for n values.
- `(q mut IntQueue) Push(v i64)`: Push appends v at the back of the queue.
- `(q mut IntQueue) Pop() (i64, bool)`: Pop removes and returns the front value, or (0, false) when the queue is empty.
- `(q IntQueue) Peek() (i64, bool)`: Peek returns the front value without removing it, or (0, false) when the queue is empty.
- `(q IntQueue) Len() i64`: Len returns the number of values in the queue.
- `type IntSet struct`: IntSet is a hash set of i64 values with open addressing and linear probing; IntSet{} is ready to use.
- `NewIntSet(n i64) IntSet`: NewIntSet returns an empty set sized for about n values.
- `(s mut IntSet) Add(k i64) bool`: Add puts k in the set and reports whether it was absent.
- `(s IntSet) Has(k i64) bool`: Has reports whether k is in the set.
- `(s mut IntSet) Del(k i64) bool`: Del removes k and reports whether it was present.
- `(s IntSet) Len() i64`: Len returns the number of values in the set.
- `(s IntSet) Keys() []i64`: Keys returns the values in table order (unsorted).
- `type StrSet struct`: StrSet is a set of strs backed by a map; make one with NewStrSet.
- `NewStrSet() StrSet`: NewStrSet returns an empty set.
- `(s mut StrSet) Add(k str) bool`: Add puts k in the set and reports whether it was absent.
- `(s StrSet) Has(k str) bool`: Has reports whether k is in the set.
- `(s mut StrSet) Del(k str) bool`: Del removes k and reports whether it was present.
- `(s StrSet) Len() i64`: Len returns the number of strs in the set.
- `(s StrSet) Keys() []str`: Keys returns the strs in map order (unsorted).
- `type Bitset struct`: Bitset is a growing set of bit indexes stored in []u64 words; Bitset{} is ready to use.
- `NewBitset(n i64) Bitset`: NewBitset returns a bitset with room for n bits (Set grows it further as needed).
- `(b mut Bitset) Set(i i64)`: Set turns bit i on, growing the bitset when i is past its end.
- `(b mut Bitset) Clear(i i64)`: Clear turns bit i off (bits past the end are already off).
- `(b Bitset) Has(i i64) bool`: Has reports whether bit i is on (false past the end or for a negative i).
- `(b Bitset) Count() i64`: Count returns the number of bits that are on.
- `(b Bitset) Next(i i64) i64`: Next returns the lowest bit index >= i that is on, or -1.
- `(b Bitset) Len() i64`: Len returns the number of bits the bitset currently holds words for.
- `(b Bitset) Words() []u64`: Words returns the underlying words without copying.
- `type LRU struct`: LRU is a least-recently-used cache from str to str with a fixed capacity; use NewLRU.
- `NewLRU(capacity i64) LRU`: NewLRU returns an empty cache holding at most capacity entries (at least 1).
- `(c mut LRU) Get(k str) (str, bool)`: Get returns the value for k and marks it most recently used, or ("", false).
- `(c LRU) Peek(k str) (str, bool)`: Peek returns the value for k without touching its recency, or ("", false).
- `(c LRU) Has(k str) bool`: Has reports whether k is cached, without touching its recency.
- `(c mut LRU) Put(k str, v str)`: Put stores v under k as most recently used, evicting the least recently used entry when full.
- `(c mut LRU) Del(k str) bool`: Del removes k and reports whether it was cached.
- `(c LRU) Len() i64`: Len returns the number of cached entries.
- `(c LRU) Cap() i64`: Cap returns the capacity.
- `(c LRU) Keys() []str`: Keys returns the cached keys from most to least recently used.
- `type Heap[T constraints.Any] struct`: Heap is a binary heap ordered by its less function; use NewHeap. less(a, b) = a < b makes a min-heap, a > b a max-heap, and any other order gives the corresponding priority queue.
- `NewHeap[T constraints.Any](less fn(T, T) bool) Heap[T]`: NewHeap returns an empty heap ordered by less, with room for eight values.
- `(h mut Heap[T]) Push(v T)`: Push adds v to the heap.
- `(h mut Heap[T]) Pop() ?T`: Pop removes and returns the first value in less's order, or nil when the heap is empty.
- `(h Heap[T]) Peek() ?T`: Peek returns the first value without removing it, or nil when the heap is empty.
- `(h Heap[T]) Len() i64`: Len returns the number of values in the heap.
- `(h mut Heap[T]) Clear()`: Clear removes every value.
- `type Deque[T constraints.Any] struct`: Deque is a double-ended queue in a growing ring buffer; use NewDeque. Every push and pop is O(1) amortized at either end.
- `NewDeque[T constraints.Any]() Deque[T]`: NewDeque returns an empty deque.
- `(d Deque[T]) Len() i64`: Len returns the number of values in the deque.
- `(d mut Deque[T]) PushBack(v T)`: PushBack appends v at the back.
- `(d mut Deque[T]) PushFront(v T)`: PushFront prepends v at the front.
- `(d mut Deque[T]) PopFront() ?T`: PopFront removes and returns the front value, or nil when the deque is empty.
- `(d mut Deque[T]) PopBack() ?T`: PopBack removes and returns the back value, or nil when the deque is empty.
- `(d Deque[T]) Front() ?T`: Front returns the front value, or nil when the deque is empty.
- `(d Deque[T]) Back() ?T`: Back returns the back value, or nil when the deque is empty.
- `(d Deque[T]) At(i i64) T`: At returns the i-th value from the front, panicking when i is out of range.
- `type Set[K constraints.Comparable] struct`: Set is a set of comparable keys in insertion order; use NewSet.
- `NewSet[K constraints.Comparable]() Set[K]`: NewSet returns an empty set.
- `(s mut Set[K]) Add(k K) bool`: Add puts k in the set and reports whether it was absent.
- `(s Set[K]) Has(k K) bool`: Has reports whether k is in the set.
- `(s mut Set[K]) Remove(k K) bool`: Remove takes k out and reports whether it was present.
- `(s Set[K]) Len() i64`: Len returns the number of keys.
- `(s Set[K]) Items() []K`: Items returns the keys in insertion order.
- `(s Set[K]) Union(o Set[K]) Set[K]`: Union returns a new set of the keys of s and o: s's keys in their order, then o's new ones.
- `(s Set[K]) Intersect(o Set[K]) Set[K]`: Intersect returns a new set of the keys in both, in s's insertion order.
- `type Cache[K constraints.Comparable, V constraints.Any] struct`: Cache is a least-recently-used cache from comparable keys to any values with a fixed capacity; use NewCache. It is the generic form of LRU (the str to str one); an empty slot holds no key and no value, so ?K and ?V storage.
- `NewCache[K constraints.Comparable, V constraints.Any](capacity i64) Cache[K, V]`: NewCache returns an empty cache holding at most capacity entries (at least 1).
- `(c mut Cache[K, V]) Get(k K) ?V`: Get returns the value for k and marks it most recently used, or nil.
- `(c Cache[K, V]) Peek(k K) ?V`: Peek returns the value for k without touching its recency, or nil.
- `(c Cache[K, V]) Has(k K) bool`: Has reports whether k is cached, without touching its recency.
- `(c mut Cache[K, V]) Put(k K, v V)`: Put stores v under k as most recently used, evicting the least recently used entry when full.
- `(c mut Cache[K, V]) Remove(k K) bool`: Remove takes k out and reports whether it was cached.
- `(c Cache[K, V]) Len() i64`: Len returns the number of cached entries.
- `(c Cache[K, V]) Keys() []K`: Keys returns the keys from the most to the least recently used.
- `type Element[T constraints.Any] struct`: Element is a node of a List: Value is its value, and Next and Prev walk the list it is in.
- `type List[T constraints.Any] struct`: List is a doubly linked list of Elements; use NewList.
- `NewList[T constraints.Any]() List[T]`: NewList returns an empty list.
- `(l List[T]) Len() i64`: Len returns the number of elements in the list.
- `(l List[T]) Front() ?Element[T]`: Front returns the first element, or nil when the list is empty.
- `(l List[T]) Back() ?Element[T]`: Back returns the last element, or nil when the list is empty.
- `(e Element[T]) Next() ?Element[T]`: Next returns the element after e, or nil at the back of its list and after Remove.
- `(e Element[T]) Prev() ?Element[T]`: Prev returns the element before e, or nil at the front of its list and after Remove.
- `(l mut List[T]) PushFront(v T) Element[T]`: PushFront inserts v at the front and returns its element.
- `(l mut List[T]) PushBack(v T) Element[T]`: PushBack inserts v at the back and returns its element.
- `(l mut List[T]) InsertBefore(v T, mark mut Element[T]) ?Element[T]`: InsertBefore inserts v in front of mark and returns its element, or nil when mark is not in l.
- `(l mut List[T]) InsertAfter(v T, mark mut Element[T]) ?Element[T]`: InsertAfter inserts v after mark and returns its element, or nil when mark is not in l.
- `(l mut List[T]) Remove(e mut Element[T]) T`: Remove takes e out of l and returns its value; e is left alone when it is not in l.
- `(l mut List[T]) MoveToFront(e mut Element[T])`: MoveToFront moves e to the front of l; it does nothing when e is not in l or is already first.
- `(l mut List[T]) MoveToBack(e mut Element[T])`: MoveToBack moves e to the back of l; it does nothing when e is not in l or is already last.
- `(l mut List[T]) PushBackList(other List[T])`: PushBackList appends a copy of each value of other, in order, to the back of l; other is unchanged, and other may be l itself.
- `(l mut List[T]) PushFrontList(other List[T])`: PushFrontList prepends a copy of each value of other to the front of l, keeping their order; other is unchanged, and other may be l itself.
- `type Ring[T constraints.Any] struct`: Ring is an element of a circular list: Value is its value, and Next and Prev move around the ring. A ring always has at least one element; NewRing builds one.
- `NewRing[T constraints.Any](values []T) ?Ring[T]`: NewRing returns a ring with one element per value, in order, or nil when values is empty. (Go's ring.New gives nil values; a type parameter has no zero value, so the values come in a slice.)
- `(r Ring[T]) Next() Ring[T]`: Next returns the element after r in its ring.
- `(r Ring[T]) Prev() Ring[T]`: Prev returns the element before r in its ring.
- `(r Ring[T]) Len() i64`: Len returns the number of elements in r's ring.
- `(r Ring[T]) Move(n i64) Ring[T]`: Move returns the element n steps after r, or -n steps before it when n is negative.
- `(r Ring[T]) Do(f fn(T))`: Do calls f with each value of r's ring, starting at r and going forward.
- `(r mut Ring[T]) Link(s mut Ring[T]) Ring[T]`: Link makes s follow r: r.Next() becomes s and the rest of s's ring follows s, and it returns r's old next. Within one ring it splits the ring; between two rings it joins them.
- `(r mut Ring[T]) Unlink(n i64) ?Ring[T]`: Unlink removes the n elements after r from their ring and returns them as a ring, or nil when n <= 0.

## stamp

Package stamp computes non-cryptographic hashes and checksums: FNV-1a, CRC-32 (IEEE and Castagnoli, slicing-by-8), Adler-32, xxHash64, and Hash, a fast 64-bit hash for tables.

- `Crc32(s str) u32`: Crc32 is the IEEE CRC-32 of s (as in zip, gzip and PNG).
- `Crc32Update(crc u32, s str) u32`: Crc32Update continues an IEEE CRC-32 over more data.
- `Crc32UpdateBytes(crc u32, b []u8) u32`: Crc32UpdateBytes continues an IEEE CRC-32 over the bytes of b, read in place (no string is made).
- `Crc32C(s str) u32`: Crc32C is the Castagnoli CRC-32 of s (as in iSCSI, ext4 and many databases).
- `Fnv32a(s str) u32`: Fnv32a is the 32-bit FNV-1a hash of s.
- `Fnv64a(s str) u64`: Fnv64a is the 64-bit FNV-1a hash of s.
- `Adler32(s str) u32`: Adler32 is the Adler-32 checksum of s (as in zlib).
- `Xxh64(s str, seed u64) u64`: Xxh64 is the xxHash64 of s with seed.
- `Hash(s str) u64`: Hash is a fast, well-mixed 64-bit hash for hash tables (not stable across versions).
- `Crc64ECMA(s str) u64`: Crc64ECMA is the ECMA-182 CRC-64 of s (as in XZ and Go's crc64.ECMA).
- `Crc64ECMAUpdate(crc u64, s str) u64`: Crc64ECMAUpdate continues an ECMA-182 CRC-64 over more data.
- `Crc64ISO(s str) u64`: Crc64ISO is the ISO CRC-64 of s (Go's crc64.ISO).
- `Crc64ISOUpdate(crc u64, s str) u64`: Crc64ISOUpdate continues an ISO CRC-64 over more data.
- `MapHash(seed u64, s str) u64`: MapHash is a fast seeded 64-bit hash of s, for spreading keys of a table one builds oneself. It is not a cryptographic hash, and it is not Go's hash/maphash (whose algorithm is not specified and whose seed is random): two runs with the same seed and the same bytes agree, and different seeds give unrelated hashes.

## squash

Package squash compresses and decompresses: DEFLATE (RFC 1951) and its gzip (RFC 1952) and zlib (RFC 1950) wrappers like Go's compress/flate, compress/gzip and compress/zlib, plus Snappy, LZ4, Zstandard (RFC 8878), LZW (compress/lzw) and bzip2 decompression (compress/bzip2). Every decoder takes the most bytes it may produce and fails with fault.LimitExceeded past it, so a small input cannot make a huge output.

```tin body
let z = squash.Gzip("hello, hello, hello", squash.Default)
let back = try squash.Gunzip(z, 64mb)
```

- `Bunzip2(data str, max i64) !str`: Bunzip2 decompresses bzip2 data (one stream or several back to back, as Go's compress/bzip2 reads them), checking every block CRC and stream CRC and failing past max bytes of output.
- `Deflate(data str, level i64) str`: Deflate compresses data as raw DEFLATE at level (Store to Best).
- `const Store = 0`: Levels for Deflate, Gzip, Zlib and Zstd: Store writes the data uncompressed (in valid frames), Fastest and Best trade speed against size, Default is between.
- `const Fastest = 1`
- `const Default = 6`
- `const Best = 9`
- `Inflate(data str, max i64) !str`: Inflate decompresses raw DEFLATE data, producing at most max bytes.
- `Gzip(data str, level i64) str`: Gzip compresses data as one gzip member (no name, no time, OS unknown) at level.
- `Gunzip(data str, max i64) !str`: Gunzip decompresses gzip data (one member or several back to back), producing at most max bytes. It checks each member's CRC-32 and length, and the header's CRC-16 when there is one.
- `Zlib(data str, level i64) str`: Zlib compresses data in the zlib format (RFC 1950) at level.
- `Unzlib(data str, max i64) !str`: Unzlib decompresses zlib data, producing at most max bytes, and checks its Adler-32.
- `type InflateReader struct`: InflateReader reads the decompressed bytes of a raw DEFLATE stream (RFC 1951) in memory. Read returns 0 once the final block has been read; bytes after it are left alone (Used says where the stream ended).
- `NewInflateReader(data str, from i64, to i64) InflateReader`: NewInflateReader reads the DEFLATE stream in data[from:to]; to past the stream's end costs nothing, and a stream that needs more than data[from:to] fails with ErrUnexpectedEOF. The window and tables are made at the first Read.
- `(z InflateReader) Used() i64`: Used is how many bytes of the input the stream has taken so far: after the end, the stream's length.
- `(z mut InflateReader) Read(buf mut []u8) !i64`: Read fills buf with the next decompressed bytes and returns how many, 0 at the end of the stream. A damaged stream fails with ErrCorrupt or ErrUnexpectedEOF once the bytes before the damage have been read, and keeps failing.
- `Lz4(data str) str`: Lz4 compresses data as one LZ4 frame: independent 64 KiB blocks, a stored block where compression does not help, and a content checksum.
- `Lz4NoChecksum(data str) str`: Lz4NoChecksum is Lz4 without the content checksum (the frame Kafka's Java client writes).
- `Unlz4(data str, max i64) !str`: Unlz4 decompresses LZ4 frames (one or several, and skippable frames), producing at most max bytes.
- `Lz4BlockOf(data str) str`: Lz4BlockOf compresses data as one bare LZ4 block (no frame).
- `UnLz4Block(b str, max i64) !str`: UnLz4Block decompresses one bare LZ4 block, producing at most max bytes.
- `const MSB = 0`: The code orders: MSB packs the bits of a code most significant first (GIF), LSB least significant first (TIFF).
- `const LSB = 1`
- `Lzw(data str, order i64) str`: Lzw compresses data with LZW, literal width 8, as Go's lzw.Writer does: a clear code starts the stream, the dictionary grows to 4096 codes and then a clear code starts it again, and the stream ends with the end code.
- `LzwWidth(data str, order i64, litWidth i64) str`: LzwWidth compresses bytes with the given literal width (2 through 8), as GIF requires.
- `Unlzw(data str, order i64, max i64) !str`: Unlzw decompresses an LZW stream of the given order, failing past max bytes.
- `UnlzwWidth(data str, order i64, max i64, litWidth i64) !str`: UnlzwWidth decompresses an LZW stream with the given literal width (2 through 8).
- `Snappy(data str) str`: Snappy compresses data as one Snappy block.
- `Unsnappy(data str, max i64) !str`: Unsnappy decompresses one Snappy block whose length is at most max.
- `shape Writer`: Writer is what a streaming compressor writes to: io.Writer's method.
- `type DeflateWriter[W Writer] struct`: DeflateWriter compresses raw DEFLATE into another writer, a chunk of up to 256 KiB at a time; Close ends the stream. Each chunk is compressed on its own (matches do not reach into the chunk before), which costs a little ratio and bounds the memory.
- `NewDeflateWriter[W Writer](out W, level i64) DeflateWriter[W]`: NewDeflateWriter is a raw DEFLATE writer into out at level.
- `NewZlibWriter[W Writer](out W, level i64) !DeflateWriter[W]`: NewZlibWriter is a zlib (RFC 1950) writer into out at level; Close writes the Adler-32 trailer.
- `(z mut DeflateWriter[W]) Write(data []u8) !i64`: Write takes data, compressing and writing each full chunk.
- `(z mut DeflateWriter[W]) Close() !`: Close compresses what is buffered, ends the stream and writes the zlib trailer; it does not close the writer below.
- `InflatePrefix(data str, max i64) !(str, i64)`: InflatePrefix decompresses the raw DEFLATE stream at the start of data (at most max bytes out) and says how many bytes of data the stream took; what follows is left alone.
- `UnzlibPrefix(data str, max i64) !(str, i64)`: UnzlibPrefix decompresses the zlib stream at the start of data (at most max bytes out), checks its Adler-32 and says how many bytes of data the stream took, trailer included.
- `shape Reader`: Reader is what a streaming decompressor reads from: io.Reader's method.
- `type InflateStream[R Reader] struct`: InflateStream decompresses the DEFLATE stream (raw, or zlib when made by NewZlibReader) read from src. It reads from another reader as it goes; InflateReader (inflate_reader.tin) reads DEFLATE data already in memory.
- `NewInflateStream[R Reader](src R, max i64) InflateStream[R]`: NewInflateStream reads raw DEFLATE from src, making at most max bytes.
- `NewZlibReader[R Reader](src R, max i64) !InflateStream[R]`: NewZlibReader reads a zlib stream from src (its header now, its Adler-32 at the end), making at most max bytes.
- `(r mut InflateStream[R]) Read(buf mut []u8) !i64`: Read fills buf with the next bytes of the decompressed stream; 0 at its end (a zlib stream's checksum checked).
- `Unzstd(data str, max i64) !str`: Unzstd decompresses Zstandard data (any number of frames, and skippable frames), producing at most max bytes.
- `Zstd(data str, level i64) str`: Zstd compresses data as one Zstandard frame at level (Store to Best; Store writes raw blocks).

## squash

Package squash compresses and decompresses: DEFLATE (RFC 1951) and its gzip (RFC 1952) and zlib (RFC 1950) wrappers like Go's compress/flate, compress/gzip and compress/zlib, plus Snappy, LZ4, Zstandard (RFC 8878), LZW (compress/lzw) and bzip2 decompression (compress/bzip2). Every decoder takes the most bytes it may produce and fails with fault.LimitExceeded past it, so a small input cannot make a huge output.

```tin body
let z = squash.Gzip("hello, hello, hello", squash.Default)
let back = try squash.Gunzip(z, 64mb)
```

- `Bunzip2(data str, max i64) !str`: Bunzip2 decompresses bzip2 data (one stream or several back to back, as Go's compress/bzip2 reads them), checking every block CRC and stream CRC and failing past max bytes of output.
- `Deflate(data str, level i64) str`: Deflate compresses data as raw DEFLATE at level (Store to Best).
- `const Store = 0`: Levels for Deflate, Gzip, Zlib and Zstd: Store writes the data uncompressed (in valid frames), Fastest and Best trade speed against size, Default is between.
- `const Fastest = 1`
- `const Default = 6`
- `const Best = 9`
- `Inflate(data str, max i64) !str`: Inflate decompresses raw DEFLATE data, producing at most max bytes.
- `Gzip(data str, level i64) str`: Gzip compresses data as one gzip member (no name, no time, OS unknown) at level.
- `Gunzip(data str, max i64) !str`: Gunzip decompresses gzip data (one member or several back to back), producing at most max bytes. It checks each member's CRC-32 and length, and the header's CRC-16 when there is one.
- `Zlib(data str, level i64) str`: Zlib compresses data in the zlib format (RFC 1950) at level.
- `Unzlib(data str, max i64) !str`: Unzlib decompresses zlib data, producing at most max bytes, and checks its Adler-32.
- `type InflateReader struct`: InflateReader reads the decompressed bytes of a raw DEFLATE stream (RFC 1951) in memory. Read returns 0 once the final block has been read; bytes after it are left alone (Used says where the stream ended).
- `NewInflateReader(data str, from i64, to i64) InflateReader`: NewInflateReader reads the DEFLATE stream in data[from:to]; to past the stream's end costs nothing, and a stream that needs more than data[from:to] fails with ErrUnexpectedEOF. The window and tables are made at the first Read.
- `(z InflateReader) Used() i64`: Used is how many bytes of the input the stream has taken so far: after the end, the stream's length.
- `(z mut InflateReader) Read(buf mut []u8) !i64`: Read fills buf with the next decompressed bytes and returns how many, 0 at the end of the stream. A damaged stream fails with ErrCorrupt or ErrUnexpectedEOF once the bytes before the damage have been read, and keeps failing.
- `Lz4(data str) str`: Lz4 compresses data as one LZ4 frame: independent 64 KiB blocks, a stored block where compression does not help, and a content checksum.
- `Lz4NoChecksum(data str) str`: Lz4NoChecksum is Lz4 without the content checksum (the frame Kafka's Java client writes).
- `Unlz4(data str, max i64) !str`: Unlz4 decompresses LZ4 frames (one or several, and skippable frames), producing at most max bytes.
- `Lz4BlockOf(data str) str`: Lz4BlockOf compresses data as one bare LZ4 block (no frame).
- `UnLz4Block(b str, max i64) !str`: UnLz4Block decompresses one bare LZ4 block, producing at most max bytes.
- `const MSB = 0`: The code orders: MSB packs the bits of a code most significant first (GIF), LSB least significant first (TIFF).
- `const LSB = 1`
- `Lzw(data str, order i64) str`: Lzw compresses data with LZW, literal width 8, as Go's lzw.Writer does: a clear code starts the stream, the dictionary grows to 4096 codes and then a clear code starts it again, and the stream ends with the end code.
- `LzwWidth(data str, order i64, litWidth i64) str`: LzwWidth compresses bytes with the given literal width (2 through 8), as GIF requires.
- `Unlzw(data str, order i64, max i64) !str`: Unlzw decompresses an LZW stream of the given order, failing past max bytes.
- `UnlzwWidth(data str, order i64, max i64, litWidth i64) !str`: UnlzwWidth decompresses an LZW stream with the given literal width (2 through 8).
- `Snappy(data str) str`: Snappy compresses data as one Snappy block.
- `Unsnappy(data str, max i64) !str`: Unsnappy decompresses one Snappy block whose length is at most max.
- `shape Writer`: Writer is what a streaming compressor writes to: io.Writer's method.
- `type DeflateWriter[W Writer] struct`: DeflateWriter compresses raw DEFLATE into another writer, a chunk of up to 256 KiB at a time; Close ends the stream. Each chunk is compressed on its own (matches do not reach into the chunk before), which costs a little ratio and bounds the memory.
- `NewDeflateWriter[W Writer](out W, level i64) DeflateWriter[W]`: NewDeflateWriter is a raw DEFLATE writer into out at level.
- `NewZlibWriter[W Writer](out W, level i64) !DeflateWriter[W]`: NewZlibWriter is a zlib (RFC 1950) writer into out at level; Close writes the Adler-32 trailer.
- `(z mut DeflateWriter[W]) Write(data []u8) !i64`: Write takes data, compressing and writing each full chunk.
- `(z mut DeflateWriter[W]) Close() !`: Close compresses what is buffered, ends the stream and writes the zlib trailer; it does not close the writer below.
- `InflatePrefix(data str, max i64) !(str, i64)`: InflatePrefix decompresses the raw DEFLATE stream at the start of data (at most max bytes out) and says how many bytes of data the stream took; what follows is left alone.
- `UnzlibPrefix(data str, max i64) !(str, i64)`: UnzlibPrefix decompresses the zlib stream at the start of data (at most max bytes out), checks its Adler-32 and says how many bytes of data the stream took, trailer included.
- `shape Reader`: Reader is what a streaming decompressor reads from: io.Reader's method.
- `type InflateStream[R Reader] struct`: InflateStream decompresses the DEFLATE stream (raw, or zlib when made by NewZlibReader) read from src. It reads from another reader as it goes; InflateReader (inflate_reader.tin) reads DEFLATE data already in memory.
- `NewInflateStream[R Reader](src R, max i64) InflateStream[R]`: NewInflateStream reads raw DEFLATE from src, making at most max bytes.
- `NewZlibReader[R Reader](src R, max i64) !InflateStream[R]`: NewZlibReader reads a zlib stream from src (its header now, its Adler-32 at the end), making at most max bytes.
- `(r mut InflateStream[R]) Read(buf mut []u8) !i64`: Read fills buf with the next bytes of the decompressed stream; 0 at its end (a zlib stream's checksum checked).
- `Unzstd(data str, max i64) !str`: Unzstd decompresses Zstandard data (any number of frames, and skippable frames), producing at most max bytes.
- `Zstd(data str, level i64) str`: Zstd compresses data as one Zstandard frame at level (Store to Best; Store writes raw blocks).

## zip

Package zip reads and writes ZIP archives like Go's archive/zip: the central directory (not just the local headers), names and comments, MS-DOS and extended times, Unix and MS-DOS modes, the Store and Deflate methods with their CRC-32, data descriptors, and ZIP64 (sizes, offsets and entry counts past 32 and 16 bits).

```tin body
let r = try zip.OpenReader("site.zip")
for f in r.File {
	let text = try f.ReadAll(16mb)          // fault.LimitExceeded past 16 MiB
	say.Line(f.Header.Name, f.Header.Mode(), len(text))
}

let out = try flume.Create("out.zip")
mut w = zip.NewWriter(out)
try w.Create("hello.txt")
_ = try w.Write([]u8("hello, zip"))
try w.Close()
```

The reader works over the whole archive in memory (NewReader, or OpenReader for a file) and decompresses an entry as it is read (File.Open), so an entry of any size costs a 32 KiB window. An entry that inflates past its declared size fails with ErrFormat, a damaged one with ErrChecksum, a cut one with ErrUnexpectedEOF, as Go's reader does. Unlike Go, a header is a field of File (f.Header.Name) and the Writer itself takes the entry's bytes (w.Write after w.Create), since Tin has no embedding. Reading follows Go byte for byte; tools/ci/zip_check.tin compares the two.

- `type Reader struct`: Reader is an archive's entries, in the central directory's order, and its comment.
- `type File struct`: File is one entry: its header, and where its bytes are in the archive.
- `NewReader(data str) !Reader`: NewReader reads the archive in data (all of it, as Go's NewReader(r, size) reads one of size bytes).
- `OpenReader(path str) !Reader`: OpenReader reads the archive in the file at path (at most 64 MiB, as quarry.ReadFile; quarry.ReadFileBound and NewReader read a larger one).
- `(r Reader) CheckPaths() !`: CheckPaths fails with ErrInsecurePath if an entry's name is absolute, climbs out with "..", or has a backslash (Go's NewReader with GODEBUG=zipinsecurepath=0); empty names are allowed. Check before extracting to disk.
- `(f File) DataOffset() !i64`: DataOffset is where the entry's (possibly compressed) bytes start in the archive.
- `type FileReader struct`: FileReader reads an entry's bytes: Read, then 0 at the end, where the size and the CRC-32 (and the data descriptor's) are checked.
- `(f File) Open() !FileReader`: Open opens the entry's bytes for reading, decompressed as they are read. A directory reads nothing (or fails with ErrFormat when it claims a size); an unknown method fails with ErrAlgorithm.
- `(f File) OpenRaw() !FileReader`: OpenRaw opens the entry's bytes as they are stored, with no decompression and no checks.
- `(f File) ReadAll(most i64) !str`: ReadAll is the entry's whole content, at most most bytes: past that it fails with fault.LimitExceeded, having held no more than most bytes (an entry that inflates past its declared size fails sooner, with ErrFormat).
- `(r mut FileReader) Read(buf mut []u8) !i64`: Read fills buf with the entry's next bytes and returns how many, 0 at the end. More bytes than the header's size fail with ErrFormat, fewer with ErrUnexpectedEOF, a CRC-32 that does not match with ErrChecksum; a fault repeats on every later Read.
- `(r mut FileReader) Close() !i64`: Close ends reading; the archive stays in memory, so there is nothing to release.
- `(s mut sink[W]) Write(data []u8) !i64`
- `type Writer[W io.Writer] struct`: Writer writes a zip archive to out. Create or CreateHeader starts an entry, Write gives it its bytes, and Close writes the central directory (it does not close out).
- `NewWriter[W io.Writer](out W) Writer[W]`: NewWriter writes an archive to out.
- `(w mut Writer[W]) SetOffset(n i64)`: SetOffset says the archive starts n bytes into out (it follows other data, as in a self-extracting program); it must be called before anything is written.
- `(w mut Writer[W]) SetComment(comment str) !`: SetComment sets the archive's comment, at most 65535 bytes.
- `(w mut Writer[W]) Create(name str) !`: Create starts an entry named name, compressed with Deflate (a name ending in a slash is a directory).
- `(w mut Writer[W]) CreateHeader(fh FileHeader) !`: CreateHeader starts an entry described by fh (the writer works on a copy). It sets the UTF-8 flag for a name or comment that needs it, the versions, the data descriptor flag, the MS-DOS time and an extended timestamp from Modified when that is set; a directory gets Store and no sizes.
- `(w mut Writer[W]) CreateRaw(fh FileHeader) !`: CreateRaw starts an entry whose bytes Write takes as they are (already compressed, as fh's Method and sizes and CRC-32 say). Without the data descriptor flag in fh, the local header carries the sizes.
- `(w mut Writer[W]) Copy(f File) !`: Copy copies the entry f of a Reader into the archive as it is stored, with no decompression or checks.
- `(w mut Writer[W]) Write(data []u8) !i64`: Write gives the entry being written more bytes, compressing them as its method says (as they are for CreateRaw). A directory takes no bytes.
- `(w mut Writer[W]) WriteString(s str) !i64`: WriteString is Write of the bytes of s.
- `(w mut Writer[W]) Close() !`: Close ends the last entry and writes the central directory and the end records. It does not close out.
- `const Store = 0`: Compression methods: Store keeps the bytes as they are, Deflate compresses them (RFC 1951).
- `const Deflate = 8`
- `const ModeDir = 0x80000000`: File modes, Go's fs.FileMode bits: Mode returns them and SetMode takes them.
- `const ModeAppend = 0x40000000`
- `const ModeExclusive = 0x20000000`
- `const ModeTemporary = 0x10000000`
- `const ModeSymlink = 0x8000000`
- `const ModeDevice = 0x4000000`
- `const ModeNamedPipe = 0x2000000`
- `const ModeSocket = 0x1000000`
- `const ModeSetuid = 0x800000`
- `const ModeSetgid = 0x400000`
- `const ModeCharDevice = 0x200000`
- `const ModeSticky = 0x100000`
- `const ModeIrregular = 0x80000`
- `const ModeType = 0x8f280000`: ModeType is the type bits of a mode, ModePerm its permission bits.
- `const ModePerm = 0o777`
- `type FileHeader struct`: FileHeader describes an entry, with the fields of Go's zip.FileHeader. Modified is the modification time in Unix nanoseconds and ModifiedOffset the zone the MS-DOS fields are in (seconds east of UTC): reading, Go's estimate from the MS-DOS and extended times when both are there (else 0); writing, a Modified of 0 means "not set", and then the MS-DOS fields are written as they are, with no extended timestamp. The 32-bit sizes are 0xffffffff when either size needs ZIP64; the 64-bit ones are always right.
- `(h FileHeader) IsDir() bool`: IsDir reports whether the entry is a directory: its name ends in a slash.
- `(h FileHeader) Size() i64`: Size is the entry's uncompressed size (Go's FileInfo().Size()).
- `(h FileHeader) Mode() u32`: Mode returns the permission and type bits, from the Unix or MS-DOS attributes the creator wrote.
- `(h mut FileHeader) SetMode(mode u32)`: SetMode sets the permission and type bits, as Unix attributes and the matching MS-DOS ones.
- `(h FileHeader) ModTime() i64`: ModTime is the time of the MS-DOS fields, in Unix nanoseconds read as UTC (Go's deprecated ModTime).
- `(h mut FileHeader) SetModTime(ns i64)`: SetModTime sets Modified (in UTC) and the MS-DOS fields to the time ns.
- `FileInfoHeader(name str, fi quarry.FileInfo) FileHeader`: FileInfoHeader is a header for the file that fi describes, named name (add a slash for a directory): its size, modification time and mode. Set Method to Deflate to compress it.
- `IsLocal(name str) bool`: IsLocal is Go's filepath.IsLocal on Unix: name is not empty, not absolute, and does not climb out with "..".
- `FaultKind(err fault) str`: FaultKind lets a caller tell the faults apart without their text: "format", "algorithm", "checksum", "eof", "flate", "limit", "insecure" or "other".

## ledger

Package ledger reads and writes CSV records (RFC 4180), like Go's encoding/csv: quoting and escaping rules, \r\n normalization, comments, a fields-per-record check and parse faults with the record's line and column. The reader and writer port Go's encoding/csv (BSD licence: licenses/strconv.txt). Read faults carry the sentinels ErrBareQuote, ErrQuote, ErrFieldCount and ErrInvalidDelim (fault.Is), and Done at the end of the input.

A Reader over a stream holds a fixed window (64 KiB by default; NewStreamSize changes it) because Tin has no GC: the reader never grows or replaces its buffers, so a Read inside an arena frees its records with the arena, and streaming a huge file keeps a flat footprint. The window bounds a line: a longer one fails with fault.LimitExceeded. A Reader over an in-memory str has no window and no line limit. A comma or comment character is one byte (Go's encoding/csv accepts any rune); UTF-8 delimiters are a known gap.

- `type Reader struct`: Reader reads records from CSV text, like Go's csv.Reader. Set the exported fields before the first Read: Comma and Comment are single bytes.
- `NewReader(text str) Reader`: NewReader reads records from text.
- `NewStream[S io.Reader](src S) Reader`: NewStream reads records from a stream in a 64 KiB window (see NewStreamSize).
- `NewStreamSize[S io.Reader](src S, maxLine i64) Reader`: NewStreamSize is NewStream with a window of maxLine bytes (0 gives the default 64 KiB); a line longer than the window fails with fault.LimitExceeded.
- `(r mut Reader) ReadAll() ![][]str`: ReadAll returns the remaining records; a parse fault stops it instead, like Read.
- `(r Reader) Pos() (i64, i64)`: Pos returns the line and column where the record of the last successful Read started (1-based), or (0, 0) before any Read.
- `TrimBOM(s str) str`: TrimBOM returns s without a leading UTF-8 byte order mark; a BOM elsewhere (the Reader itself does not strip one, as Go's encoding/csv does not) is an ordinary field byte.
- `(r mut Reader) Read() ![]str`: Read returns the next record: the fields with their quotes removed and escapes decoded, or the fault Done at the end of the input. A parse fault carries one of ErrBareQuote, ErrQuote, ErrFieldCount or ErrInvalidDelim (fault.Is) and the record's position in its message. On a parse fault no partial record is returned, where Go's Read returns the fields read so far.
- `type Writer struct`: Writer writes records in CSV form into a buffer, like Go's csv.Writer. Set the exported fields before the first Write.
- `NewWriter() Writer`: NewWriter returns a Writer with Comma set to ','.
- `(w mut Writer) Write(fields []str) !`: Write appends one record, quoting fields that hold the delimiter, a quote, a newline or a leading space, and doubling quotes, as Go's encoding/csv does.
- `(w mut Writer) WriteAll(records [][]str) !`: WriteAll writes every record in order.
- `(w Writer) String() str`: String returns the bytes written so far as a str.

## abacus

Package abacus is arbitrary-precision integers, like Go's math/big.Int, with value semantics: every operation returns a new value and leaves its operands alone. A value is a sign and a little-endian magnitude of 64-bit limbs, normalized (no leading zero limbs; zero is an empty magnitude with a false sign).

It is not constant-time: use seal for cryptography. There is no formatting hook in say yet, so print an Int with x.Str() or x.Text(base) (see design/stdlib_verified.md).

- `type Int struct`: Int is an arbitrary-precision integer.
- `FromI64(v i64) Int`: FromI64 returns v as an Int.
- `(a Int) Sign() i64`: Sign returns -1, 0 or 1.
- `(a Int) IsZero() bool`: IsZero reports whether the value is zero.
- `(a Int) BitLen() i64`: BitLen returns the number of bits of the magnitude, 0 for zero.
- `(a Int) Neg() Int`: Neg returns -a.
- `(a Int) Abs() Int`: Abs returns |a|.
- `(a Int) Cmp(b Int) i64`: Cmp returns -1, 0 or 1 as a is less than, equal to or greater than b.
- `(a Int) Add(b Int) Int`: Add returns a + b.
- `(a Int) Sub(b Int) Int`: Sub returns a - b.
- `(a Int) Mul(b Int) Int`: Mul returns a * b.
- `(a Int) I64() (i64, bool)`: I64 returns the value as an i64 and whether it fits.
- `(a Int) U64() (u64, bool)`: U64 returns the value as a u64 and whether it fits (a negative value does not).
- `(a Int) F64() f64`: F64 returns the value as the nearest f64, ties to even, like Go's Int.Float64 (which is ±Inf when the value is too large).
- `(a Int) Bytes() []u8`: Bytes returns the magnitude as big-endian bytes, like Go's Int.Bytes (zero is empty).
- `FromBytes(b []u8) Int`: FromBytes returns the value of the big-endian magnitude b (the sign is always positive).
- `Parse(s str, base i64) !Int`: Parse returns the value of s, like Go's big.Int.SetString: base 2 to 36, or 0 to read a prefix (0x and 0X for 16, 0o and 0O for 8, 0b and 0B for 2, a leading 0 for 8, otherwise 10). The string may start with + or -. With base 0 an underscore may stand between the prefix and a digit or between two digits, as in Go.
- `(a Int) Str() str`: Str returns the decimal value.
- `(a Int) Text(base i64) str`: Text returns the value in the given base, 2 to 36.
- `(a Int) Not() Int`: Not returns ^a, which is -a-1.
- `(a Int) And(b Int) Int`: And returns a & b.
- `(a Int) Or(b Int) Int`: Or returns a | b.
- `(a Int) Xor(b Int) Int`: Xor returns a ^ b.
- `(a Int) Lsh(n i64) Int`: Lsh returns a << n, like Go's Int.Lsh; a negative shift panics.
- `(a Int) Rsh(n i64) Int`: Rsh returns a >> n, the arithmetic shift (floor division by 2^n), like Go's Int.Rsh; a negative shift panics.
- `(a Int) QuoRem(b Int) (Int, Int)`: QuoRem returns the truncated quotient and remainder of a/b, like Go's QuoRem: the quotient is rounded toward zero and r = a - q*b, so the remainder has a's sign. Division by zero panics.
- `(a Int) DivMod(b Int) (Int, Int)`: DivMod returns the Euclidean quotient and remainder, like Go's DivMod: q = a div b and r = a - q*b with 0 <= r < |b|. Division by zero panics.
- `(a Int) Mod(b Int) Int`: Mod returns the Euclidean remainder of a/b, like Go's Mod (0 <= r < |b|).
- `(a Int) Exp(e Int, m Int) Int`: Exp returns a**e, or a**e mod |m| when m is not zero, like Go's Exp: the sign of m is ignored, e <= 0 gives 1 for a plain power, and a negative exponent with a modulus uses the base's modular inverse (panicking when there is none, where Go returns nil).
- `(a Int) Sqrt() Int`: Sqrt returns the floor of the square root of a, like Go's Int.Sqrt; a negative value panics.
- `(a Int) Gcd(b Int) Int`: Gcd returns the greatest common divisor of a and b, always non-negative, like Go's Int.GCD; Gcd(0, 0) is 0.
- `(a Int) ModInverse(m Int) ?Int`: ModInverse returns the multiplicative inverse of a modulo m (m's sign is ignored), like Go's Int.ModInverse: the result x with a*x == 1 (mod m), or nil when a and m are not coprime. A modulus of 1 or less panics.

## seal

Package seal has cryptographic hashes (MD5, SHA-256, SHA-384, SHA-512, SHA-1, SHA3-256, SHA3-512, and SHAKE128 and SHAKE256), HMAC over any of the SHA-2 hashes, HKDF, PBKDF2-HMAC-SHA-256, AES and DES/3DES block ciphers, CBC, CTR, CFB and OFB modes, RC4, PKCS #7 padding, AES-GCM, ChaCha20-Poly1305, P-256 ECDH, ML-KEM-768 (FIPS 203), RSA signature verification (PKCS #1 v1.5 and PSS), X.509 certificates with chain and host name verification, constant-time comparison, secure random bytes, the hex, base64 and PEM encodings, and RSA-OAEP encryption with a public key. MD5, DES/3DES, RC4, CBC, CFB and OFB are for legacy interoperability only; prefer an authenticated cipher for new protocols.

- `type AEAD struct`: AEAD is an authenticated cipher with its key (AES-GCM or ChaCha20-Poly1305): Seal encrypts and appends a 16-byte tag, Open checks the tag in constant time and decrypts.
- `NewChaCha20Poly1305(key secret []u8) !AEAD`: NewChaCha20Poly1305 is the RFC 8439 AEAD with a 32-byte key.
- `(a AEAD) NonceSize() i64`: NonceSize is the nonce length in bytes (12).
- `(a AEAD) Overhead() i64`: Overhead is the tag length in bytes (16).
- `(a AEAD) Seal(nonce []u8, plaintext secret []u8, aad []u8) ![]u8`: Seal encrypts plaintext and authenticates it with aad under a 12-byte nonce, returning the ciphertext followed by the tag. A nonce must never be used twice with one key.
- `(a AEAD) SealTo(nonce []u8, src i64, n i64, aad []u8, dst i64) !`: SealTo is Seal into raw memory: it encrypts the n bytes at src into dst and writes the 16-byte tag after them (dst may be src, to seal in place). Nothing it allocates grows with n, so a connection that streams can seal into a buffer of its own instead of its request's pool; AES-GCM on the CPU's instructions allocates nothing at all.
- `(a AEAD) OpenTo(nonce []u8, src i64, n i64, aad []u8, dst i64) !`: OpenTo is Open into raw memory: it checks the 16-byte tag after the n bytes of ciphertext at src and decrypts them into dst (dst may be src, to open in place); it writes nothing when the tag does not match. Like SealTo, nothing it allocates grows with n, and AES-GCM on the CPU's instructions allocates nothing at all: a connection that streams opens records into a buffer of its own.
- `(a AEAD) Open(nonce []u8, sealed []u8, aad []u8) ![]u8`: Open checks the tag of sealed (ciphertext then tag) against aad and the nonce and returns the plaintext; it fails, revealing nothing else, when anything was changed.
- `(a mut AEAD) Rekey(key secret []u8) !`: Rekey replaces a's key with key, of the same algorithm and length, reusing a's memory: an AEAD kept in long-lived memory (a connection's state) can change keys without allocating there.
- `AESHardware() bool`: AESHardware reports whether AES-GCM runs on the CPU's AES instructions here (AES-NI and PCLMULQDQ, or ARMv8 AES and PMULL); without them it runs a slower constant-time software path and ChaCha20-Poly1305 is the faster choice.
- `NewAESGCM(key secret []u8) !AEAD`: NewAESGCM is AES-GCM (16-byte tags, 12-byte nonces) with a 16-, 24- or 32-byte key (AES-128, AES-192 or AES-256).
- `ArithDigest() str`: ArithDigest is the SHA-256 of the results of seal's multi-word arithmetic on a fixed set of operands (#488): the Montgomery multiplication and squaring for n = 2 to 48 limbs over random moduli and moduli of all-one limbs, with operands 0, 1, m-1, all-ones limbs and random values, z aliasing x and y; and the X25519 field multiplication and squaring on limbs of every size up to 2^52 - 1. Where the CPU's assembly (mont_mul, m4_mont, fe_mul_hw, fe_sq_hw) is in use the digest must equal the portable code's (run with TIN_SEAL_SOFT=1): the test pins the value.
- `shape Block`: Block is a block cipher with its key, as Go's cipher.Block; AES and DES satisfy it. Encrypt and Decrypt transform the first block of src into dst (dst may be src). EncryptBlocks and DecryptBlocks transform every whole block of src on its own: the batch form the modes call. On its own that is ECB, which shows which blocks are equal: never use it as a mode.
- `type AES struct`: AES is the AES block cipher with its key (AES-128, AES-192 or AES-256 by the key's length), as Go's aes.NewCipher; it satisfies Block. It keeps scratch space for its blocks, so it allocates nothing per call: use it on one core (not from a shared let).
- `NewAES(key secret []u8) !AES`: NewAES is AES with a 16-, 24- or 32-byte key; another length fails as Go's KeySizeError does.
- `(a AES) BlockSize() i64`: BlockSize is AES's block length, 16 bytes.
- `(a AES) Encrypt(dst mut []u8, src []u8)`: Encrypt encrypts the first 16 bytes of src into dst (dst may be src).
- `(a AES) Decrypt(dst mut []u8, src []u8)`: Decrypt decrypts the first 16 bytes of src into dst (dst may be src).
- `(a AES) EncryptBlocks(dst mut []u8, src []u8)`: EncryptBlocks encrypts every 16-byte block of src on its own into dst (the modes' batch form).
- `(a AES) DecryptBlocks(dst mut []u8, src []u8)`: DecryptBlocks decrypts every 16-byte block of src on its own into dst (the modes' batch form).
- `ChaCha20(key secret []u8, nonce []u8, counter u32, data []u8) ![]u8`: ChaCha20 XORs data with the ChaCha20 keystream (RFC 8439) for a 32-byte key, a 12-byte nonce and the initial block counter.
- `ParseRSAPublicKeyDER(der []u8) !RSAPublicKey`: ParseRSAPublicKeyDER reads a DER RSAPublicKey (PKCS #1) or SubjectPublicKeyInfo holding one.
- `type DES struct`: DES is the DES or triple-DES (EDE, three keys) block cipher with its key, as Go's des.NewCipher and des.NewTripleDESCipher; it satisfies Block. Broken or deprecated: legacy protocols only.
- `NewDES(key secret []u8) !DES`: NewDES is DES with an 8-byte key, as Go's des.NewCipher (the parity bits are ignored); another length fails as Go's KeySizeError does. DES is broken: legacy protocols only.
- `NewTripleDES(key secret []u8) !DES`: NewTripleDES is triple DES (encrypt with the first 8 key bytes, decrypt with the next 8, encrypt with the last 8) with a 24-byte key, as Go's des.NewTripleDESCipher; another length fails as Go's KeySizeError does. Two-key 3DES is a key whose last 8 bytes repeat the first. Deprecated.
- `(d DES) BlockSize() i64`: BlockSize is DES's block length, 8 bytes.
- `(d DES) Encrypt(dst mut []u8, src []u8)`: Encrypt encrypts the first 8 bytes of src into dst (dst may be src).
- `(d DES) Decrypt(dst mut []u8, src []u8)`: Decrypt decrypts the first 8 bytes of src into dst (dst may be src).
- `(d DES) EncryptBlocks(dst mut []u8, src []u8)`: EncryptBlocks encrypts every 8-byte block of src on its own into dst (the modes' batch form).
- `(d DES) DecryptBlocks(dst mut []u8, src []u8)`: DecryptBlocks decrypts every 8-byte block of src on its own into dst (the modes' batch form).
- `ParseDSAPublicKeyBytes(der []u8) !([]u8, []u8, []u8, []u8)`: ParseDSAPublicKeyBytes reads a DSA SubjectPublicKeyInfo as certificates carry it and returns the magnitudes of its parameters p, q and g and of the public value y.
- `ParseDSASignatureBytes(sig []u8) !([]u8, []u8)`: ParseDSASignatureBytes reads a DER SEQUENCE{r, s} DSA signature, the form certificates carry, and returns the magnitudes of r and s.
- `VerifyECDSA(curve str, pub []u8, digest []u8, sig []u8) !`: VerifyECDSA checks a DER-encoded ECDSA signature over digest (a hash of the message) by the public key pub, an uncompressed point on curve ("P-256" or "P-384"). A digest longer than the curve's order is truncated to its leftmost bytes, as FIPS 186-5 says.
- `SignECDSA(k ECPrivateKey, h Hash, digest []u8) ![]u8`: SignECDSA signs digest (a hash of the message, made with h) with k and returns a DER ECDSA-Sig-Value. The nonce is RFC 6979's, derived with HMAC over h, so equal inputs give equal signatures.
- `(k PrivateKey) SignTLS12(scheme i64, msg []u8) ![]u8`: SignTLS12 signs msg for TLS 1.2 (ServerKeyExchange, CertificateVerify; #473) with scheme: also RSA PKCS #1 v1.5 (0x0401, 0x0501, 0x0601) and ECDSA with the scheme's hash on either curve.
- `(k PrivateKey) SignTLS(scheme i64, msg []u8) ![]u8`: SignTLS signs msg (the bytes a TLS 1.3 CertificateVerify covers) with k under scheme: RSA-PSS 0x0804-0x0806 for RSA keys, 0x0403 for P-256 and 0x0503 for P-384.
- `VerifyEd25519(pub []u8, msg []u8, sig []u8) !`: VerifyEd25519 checks an Ed25519 signature (64 bytes) of msg by the public key pub (32 bytes).
- `type Ed25519PrivateKey struct`: Ed25519PrivateKey is an Ed25519 key: the 32-byte seed and the public key it gives.
- `Ed25519PublicKey(seed secret []u8) ![]u8`: Ed25519PublicKey is the 32-byte public key of a 32-byte Ed25519 seed.
- `SignEd25519(seed secret []u8, msg []u8) ![]u8`: SignEd25519 is the 64-byte Ed25519 signature of msg by the key with the 32-byte seed (pure Ed25519: msg is not hashed first).
- `type Hasher struct`: Hasher is an incremental SHA-256, SHA-1 or MD5; it satisfies io.Writer.
- `NewSha256() Hasher`: NewSha256 is an incremental SHA-256.
- `NewSha1() Hasher`: NewSha1 is an incremental SHA-1; use it only where a protocol requires SHA-1.
- `NewMd5() Hasher`: NewMd5 is an incremental MD5, as Go's md5.New; MD5 is broken, use it only where a protocol names it.
- `(x mut Hasher) Reset()`: Reset forgets everything written, as if the hasher were new.
- `(x Hasher) Size() i64`: Size is the length of the digest: 32 for SHA-256, 20 for SHA-1, 16 for MD5.
- `(x Hasher) Len() i64`: Len is the number of bytes written since the hasher was made or reset.
- `(x Hasher) BlockSize() i64`: BlockSize is the hash's block length in bytes (64 for all three).
- `(x mut Hasher) Write(data []u8) !i64`: Write adds data to the hash; it never fails, and returns len(data).
- `(x mut Hasher) WriteStr(s str)`: WriteStr adds the bytes of s to the hash.
- `(x Hasher) Sum() []u8`: Sum is the digest of everything written so far; the hasher can go on taking data.
- `type Hash enum { SHA256, SHA384, SHA512 }`: Hash names a SHA-2 function for Hmac and HKDF.
- `Sum(h Hash, s secret str) []u8`: Sum is the digest of s under h; s may be secret.
- `Size(h Hash) i64`: Size is the length in bytes of h's digest.
- `BlockSize(h Hash) i64`: BlockSize is the length in bytes of h's input block (the HMAC key block).
- `Hmac(h Hash, key secret str, msg str) []u8`: Hmac is the HMAC of msg under key with hash h (RFC 2104); key may be secret.
- `HkdfExtract(h Hash, salt str, ikm secret str) []u8`: HkdfExtract is HKDF-Extract(salt, ikm) (RFC 5869): a pseudorandom key of Size(h) bytes. An empty salt means Size(h) zero bytes. ikm may be secret.
- `HkdfExpand(h Hash, prk secret str, info str, n i64) ![]u8`: HkdfExpand is HKDF-Expand(prk, info, n) (RFC 5869): n bytes, at most 255*Size(h). prk may be secret.
- `HkdfExpandLabel(h Hash, key secret str, label str, context str, n i64) ![]u8`: HkdfExpandLabel is TLS 1.3's HKDF-Expand-Label(secret, label, context, n) (RFC 8446 section 7.1); label is given without the "tls13 " prefix. key may be secret.
- `type HPKEKEM enum { HPKEP256, HPKEX25519 }`: HPKEKEM selects the DHKEM curve used by the RFC 9180 base mode.
- `type HPKEAEAD enum { HPKEAES128GCM, HPKEAES256GCM, HPKEChaCha20Poly1305 }`: HPKEAEAD selects an authenticated encryption algorithm for HPKE.
- `HPKESeal(kem HPKEKEM, aead HPKEAEAD, recipientPublic []u8, info []u8, aad []u8, plaintext secret []u8) !([]u8, []u8)`: HPKESeal performs one RFC 9180 base-mode encryption with HKDF-SHA256. recipientPublic is the uncompressed 65-byte P-256 or 32-byte X25519 public key. It returns enc and ciphertext||tag.
- `HPKEOpen(kem HPKEKEM, aead HPKEAEAD, recipientPrivate []u8, enc []u8, info []u8, aad []u8, ciphertext []u8) ![]u8`: HPKEOpen opens one RFC 9180 base-mode ciphertext using the recipient's private key and enc. Authentication failures, invalid keys and malformed enc values return a fault.
- `type RSAPrivateKey struct`: RSAPrivateKey is an RSA key with its CRT values; the private parts can only be read by seal.
- `type ECPrivateKey struct`: ECPrivateKey is an ECDSA key on P-256 or P-384: the curve, the scalar and the uncompressed public point.
- `type PrivateKey struct`: PrivateKey is an RSA, ECDSA or Ed25519 private key, as ParsePrivateKeyPEM reads it.
- `ParsePrivateKeyDER(der []u8) !PrivateKey`: ParsePrivateKeyDER reads a PKCS #8 PrivateKeyInfo, a PKCS #1 RSAPrivateKey or a SEC 1 ECPrivateKey.
- `ParsePrivateKeyPEM(pem str) !PrivateKey`: ParsePrivateKeyPEM reads the first "PRIVATE KEY", "RSA PRIVATE KEY" or "EC PRIVATE KEY" block of pem.
- `(k PrivateKey) MatchesCertificate(c Certificate) bool`: MatchesCertificate reports whether k is the private key of c's public key.
- `Md5(s secret str) []u8`: Md5 is the MD5 digest of s (16 bytes), as Go's md5.Sum; s may be secret. MD5 is broken: use it only where a protocol names it (PostgreSQL's md5 login), never for new designs.
- `Md5Hex(s secret str) str`: Md5Hex is the MD5 digest of s in lower-case hex; s may be secret.
- `const MLKEM768EncapsulationKeySize = 1184`: MLKEM768EncapsulationKeySize, MLKEM768DecapsulationKeySize and MLKEM768CiphertextSize are ML-KEM-768's sizes in bytes; the shared key is 32 bytes.
- `const MLKEM768DecapsulationKeySize = 2400`
- `const MLKEM768CiphertextSize = 1088`
- `MLKEM768KeyFromSeed(seed secret []u8) !([]u8, []u8)`: MLKEM768KeyFromSeed is the key pair of a 64-byte seed d || z (FIPS 203's ML-KEM.KeyGen_internal, the seed form Go and BoringSSL keep): the decapsulation key (2400 bytes) and the encapsulation key (1184 bytes).
- `MLKEM768GenerateKey() ([]u8, []u8)`: MLKEM768GenerateKey makes a key pair from fresh randomness: the decapsulation key (2400 bytes) and the encapsulation key (1184 bytes).
- `MLKEM768Encapsulate(ek []u8) !([]u8, []u8)`: MLKEM768Encapsulate makes a shared key for the holder of encapsulation key ek: the shared key (32 bytes) and the ciphertext to send (1088 bytes). A key of the wrong size or with a value not below q is refused (FIPS 203's input check).
- `MLKEM768EncapsulateDerand(ek []u8, m secret []u8) !([]u8, []u8)`: MLKEM768EncapsulateDerand is MLKEM768Encapsulate with its 32 random bytes given (FIPS 203's ML-KEM.Encaps_internal): for known-answer tests only.
- `MLKEM768Decapsulate(dk secret []u8, c []u8) ![]u8`: MLKEM768Decapsulate is the shared key in ciphertext c for decapsulation key dk. A ciphertext that was not made for dk gives a key derived from dk's secret z and c (implicit rejection), in the same time; only wrong sizes fail.
- `shape BlockMode`: BlockMode is a block cipher mode that works on whole blocks, as Go's cipher.BlockMode; CBC satisfies it.
- `shape Stream`: Stream is a stream cipher, as Go's cipher.Stream: XORKeyStream XORs src with the keystream into dst, keeping its place between calls. BlockStream (CTR, CFB, OFB) and RC4 satisfy it.
- `type CBC struct`: CBC is cipher block chaining over a Block, encrypting or decrypting, with its current IV; it satisfies BlockMode. CBC needs padding (Pkcs7Pad) and a MAC over the ciphertext: CBC decryption that reports bad padding is a padding oracle.
- `NewCBCEncrypter(b dyn Block, iv []u8) !CBC`: NewCBCEncrypter is CBC encryption with b and a one-block IV, as Go's cipher.NewCBCEncrypter; an IV of another length is a fault. The IV must be unpredictable (RandomBytes) for each message.
- `NewCBCDecrypter(b dyn Block, iv []u8) !CBC`: NewCBCDecrypter is CBC decryption with b and a one-block IV, as Go's cipher.NewCBCDecrypter; an IV of another length is a fault.
- `(c CBC) BlockSize() i64`: BlockSize is the block length of the mode's cipher.
- `(c mut CBC) SetIV(iv []u8) !`: SetIV starts a new message with iv, as Go's CBC SetIV; an IV of another length is a fault.
- `(c mut CBC) CryptBlocks(dst mut []u8, src []u8) !`: CryptBlocks encrypts or decrypts src into dst (dst may be src), carrying the chain into the next call. It fails, writing nothing, when src is not whole blocks, dst is shorter than src, or dst overlaps src shifted (Go's panics, in the same order).
- `Pkcs7Pad(data []u8, bs i64) ![]u8`: Pkcs7Pad is data followed by PKCS #7 padding for blocks of bs bytes (1 to 255): n bytes of value n, 1 <= n <= bs, so the result is whole blocks. It is a helper for CBC, not part of the mode.
- `Pkcs7Unpad(data []u8, bs i64) ![]u8`: Pkcs7Unpad is data without its PKCS #7 padding for blocks of bs bytes (1 to 255), sharing data's memory. Empty data, data that is not whole blocks and wrong padding all fail with one fault, and the padding is read in time that depends only on bs. A CBC decryption that reports bad padding to an attacker who can send ciphertexts is a padding oracle: check a MAC first.
- `type BlockStream struct`: BlockStream is a Block run as a stream cipher (CTR, CFB or OFB), with its place in the keystream; it satisfies Stream. Never use one key and IV for two messages.
- `NewCTR(b dyn Block, iv []u8) !BlockStream`: NewCTR is counter mode with b and a one-block initial counter, as Go's cipher.NewCTR: the counter is the whole block, big-endian, wrapping to zero. An IV of another length is a fault.
- `NewCFBEncrypter(b dyn Block, iv []u8) !BlockStream`: NewCFBEncrypter is full-block cipher feedback encryption with b and a one-block IV, as Go's cipher.NewCFBEncrypter (deprecated there: use CTR or an AEAD). An IV of another length is a fault.
- `NewCFBDecrypter(b dyn Block, iv []u8) !BlockStream`: NewCFBDecrypter is full-block cipher feedback decryption with b and a one-block IV, as Go's cipher.NewCFBDecrypter (deprecated there: use CTR or an AEAD). An IV of another length is a fault.
- `NewOFB(b dyn Block, iv []u8) !BlockStream`: NewOFB is output feedback mode with b and a one-block IV, as Go's cipher.NewOFB (deprecated there: use CTR or an AEAD). An IV of another length is a fault.
- `(x mut BlockStream) XORKeyStream(dst mut []u8, src []u8) !`: XORKeyStream XORs src with the keystream into dst (dst may be src), going on from where the last call stopped. It fails, writing nothing, when dst is shorter than src or overlaps it shifted.
- `P256NewPrivateKey() []u8`: P256NewPrivateKey returns a random P-256 private key: 32 big-endian bytes in [1, n-1].
- `P256PublicKey(priv secret []u8) ![]u8`: P256PublicKey is the uncompressed public key (65 bytes) of a P-256 private key; it fails unless priv is 32 bytes in [1, n-1]. Constant-time in priv.
- `P256ECDH(priv secret []u8, peer []u8) ![]u8`: P256ECDH is the P-256 Diffie-Hellman shared secret (the 32-byte x coordinate of priv*peer). peer is an uncompressed or compressed public key; it fails for an invalid private key, a point not on the curve, or a result at infinity. Constant-time in priv.
- `type PrimeCurve struct`: PrimeCurve is a curve built by NewPrimeCurve.
- `NewPrimeCurve(name str, ph str, nh str, bh str, gxh str, gyh str) !PrimeCurve`: NewPrimeCurve builds the curve name from big-endian hex p, n, b, Gx and Gy, and fails on bad constants.
- `(p PrimeCurve) OnCurve(x []u8, y []u8) bool`: OnCurve reports whether (x, y) is a point of the curve, not the point at infinity.
- `(p PrimeCurve) Add(x1 []u8, y1 []u8, x2 []u8, y2 []u8) !([]u8, []u8)`: Add returns (x1, y1) + (x2, y2) as big-endian coordinates, and fails when either point is not on the curve.
- `(p PrimeCurve) Double(x []u8, y []u8) !([]u8, []u8)`: Double returns 2*(x, y) as big-endian coordinates, and fails when the point is not on the curve.
- `(p PrimeCurve) ScalarMult(x []u8, y []u8, k []u8) !([]u8, []u8)`: ScalarMult returns k*(x, y) for a big-endian scalar k of any length, and fails when the point is not on the curve.
- `(p PrimeCurve) ScalarBaseMult(k []u8) ([]u8, []u8)`: ScalarBaseMult returns k*G for the curve's generator G and a big-endian scalar k of any length.
- `type RC4 struct`: RC4 is an RC4 keystream with its state, as Go's rc4.Cipher; it satisfies Stream. Broken: legacy protocols only.
- `NewRC4(key secret []u8) !RC4`: NewRC4 is RC4 keyed with 1 to 256 bytes, as Go's rc4.NewCipher; another length fails as Go's KeySizeError does.
- `(c mut RC4) Reset()`: Reset zeroes the key state; the RC4 is unusable afterwards (Go's deprecated Reset).
- `(c mut RC4) XORKeyStream(dst mut []u8, src []u8) !`: XORKeyStream XORs src with the keystream into dst (dst may be src); it fails, writing nothing, when dst is shorter than src or overlaps it shifted.
- `RSAKeyBits(key RSAPublicKey) i64`: RSAKeyBits is the size of key's modulus in bits.
- `VerifyPKCS1v15(key RSAPublicKey, h Hash, digest []u8, sig []u8) !`: VerifyPKCS1v15 checks an RSASSA-PKCS1-v1_5 signature over digest, a hash made with h.
- `VerifyPSS(key RSAPublicKey, h Hash, digest []u8, sig []u8, saltLen i64) !`: VerifyPSS checks an RSASSA-PSS signature over digest, a hash made with h, with MGF1 over the same hash. saltLen is the exact salt length, or -1 to accept any.
- `SignPKCS1v15(k mut RSAPrivateKey, h Hash, digest []u8) ![]u8`: SignPKCS1v15 signs digest, a hash made with h, with RSASSA-PKCS1-v1_5 (deterministic).
- `SignPSS(k mut RSAPrivateKey, h Hash, digest []u8) ![]u8`: SignPSS signs digest, a hash made with h, with RSASSA-PSS: MGF1 over h and a random salt as long as the digest (what TLS 1.3 requires).
- `Sha256(s secret str) []u8`: Sha256 is the SHA-256 digest of s (32 bytes); s may be secret.
- `Sha256Soft(s str) []u8`: Sha256Soft is SHA-256 in portable code (the reference the hardware path is tested against).
- `Sha256Hex(s secret str) str`: Sha256Hex is the SHA-256 digest of s in lower-case hex; s may be secret.
- `Sha1(s str) []u8`: Sha1 is the SHA-1 digest of s (20 bytes); use it only where a protocol requires it.
- `HmacSha256(key secret str, msg str) []u8`: HmacSha256 is the HMAC-SHA256 of msg under key (32 bytes); key may be secret.
- `Pbkdf2Sha256(password secret str, salt str, iterations i64, length i64) ![]u8`: Pbkdf2Sha256 derives length bytes using PBKDF2-HMAC-SHA-256. Iterations must be positive; length must be between 0 and 1 MiB. Temporary storage is reused between rounds, so memory usage does not grow with iterations. Choose the work factor for your protocol or password policy (this function does not choose one). The password may be secret.
- `Pbkdf2Sha256Timeout(password secret str, salt str, iterations i64, length i64, timeout i64) ![]u8`: Pbkdf2Sha256Timeout derives bytes like Pbkdf2Sha256, with a timeout in nanoseconds (<= 0: no limit). Both forms honor request deadlines and let other tasks run between batches of rounds. Scratch storage is released before any timeout fault returns.
- `ConstantTimeEq(a secret []u8, b secret []u8) bool`: ConstantTimeEq compares a and b in time that depends only on their lengths; they may be secret.
- `Equal(a secret str, b secret str) bool`: Equal reports whether a and b hold the same bytes, in time that depends only on their lengths. It is how secrets are compared: == on a secret is a compile error.
- `RandomBytes(n i64) []u8`: RandomBytes returns n cryptographically secure random bytes.
- `Hex(b []u8) str`: Hex encodes b in lower-case hexadecimal.
- `HexDecode(s str) ![]u8`: HexDecode decodes hexadecimal text.
- `B64(b []u8) str`: B64 encodes b as standard padded base64.
- `B64Decode(s str) ![]u8`: B64Decode decodes standard padded base64 as Go's strict StdEncoding does: "\r" and "\n" are skipped and the unused low bits must be zero.
- `B64URL(b []u8) str`: B64URL encodes b as unpadded URL-safe base64 (as in JWTs).
- `B64URLDecode(s str) ![]u8`: B64URLDecode decodes unpadded URL-safe base64 as Go's strict RawURLEncoding does: "\r" and "\n" are skipped and the unused low bits must be zero.
- `Base32(b []u8) str`: Base32 encodes b as standard padded base32 (RFC 4648).
- `Base32Hex(b []u8) str`: Base32Hex encodes b as padded base32 with the extended-hex alphabet (RFC 4648).
- `Base32NoPad(b []u8) str`: Base32NoPad encodes b as standard base32 without the padding characters.
- `Base32Decode(s str) ![]u8`: Base32Decode decodes standard padded base32, as Go's StdEncoding does: "\r" and "\n" are skipped.
- `Base32HexDecode(s str) ![]u8`: Base32HexDecode decodes extended-hex base32.
- `Ascii85(b []u8) str`: Ascii85 encodes b with the ascii85 alphabet. The <~ and ~> delimiters are the caller's.
- `Ascii85MaxLen(n i64) i64`: Ascii85MaxLen is the most Ascii85 writes for n bytes.
- `Ascii85Decode(s str) ![]u8`: Ascii85Decode decodes ascii85, following Go's Decode function: any byte at or below a space is skipped, 'z' is a group of four zero bytes, a group that does not fit in 32 bits wraps (as Go's uint32 arithmetic does), and a final group of one byte is refused. The <~ and ~> markers are the caller's: Go's Decode does not know them (its streaming decoder does).
- `type RSAPublicKey struct`: RSAPublicKey is an RSA public key: modulus N and exponent E, as big-endian bytes.
- `ParseRSAPublicKeyPEM(pem str) !RSAPublicKey`: ParseRSAPublicKeyPEM reads a PEM "PUBLIC KEY" (SubjectPublicKeyInfo) or "RSA PUBLIC KEY" (PKCS #1) block.
- `EncryptOAEPSha1(key RSAPublicKey, msg []u8) ![]u8`: EncryptOAEPSha1 encrypts msg for key with RSA-OAEP (SHA-1, MGF1-SHA-1, empty label), as MySQL's caching_sha2_password and sha256_password expect.
- `Sha3_256(s secret str) []u8`: Sha3_256 is the SHA3-256 digest of s (32 bytes); s may be secret.
- `Sha3_512(s secret str) []u8`: Sha3_512 is the SHA3-512 digest of s (64 bytes); s may be secret.
- `Shake128(s secret str, n i64) []u8`: Shake128 is the first n bytes of SHAKE128 of s; s may be secret.
- `Shake256(s secret str, n i64) []u8`: Shake256 is the first n bytes of SHAKE256 of s; s may be secret.
- `Sha512(s secret str) []u8`: Sha512 is the SHA-512 digest of s (64 bytes); s may be secret.
- `Sha384(s secret str) []u8`: Sha384 is the SHA-384 digest of s (48 bytes); s may be secret.
- `X25519(scalar secret []u8, point []u8) ![]u8`: X25519 is the RFC 7748 function: the shared secret of a 32-byte private scalar and a peer's 32-byte public key. It fails for wrong lengths and when the result is all zeros (a low-order peer key), as TLS 1.3 requires. Constant-time in the scalar and the point.
- `X25519NewPrivateKey() []u8`: X25519NewPrivateKey returns 32 random bytes to use as an X25519 private key.
- `X25519PublicKey(priv secret []u8) ![]u8`: X25519PublicKey is the public key (32 bytes) of a 32-byte X25519 private key.
- `type PEMBlock struct`: PEMBlock is one "-----BEGIN TYPE-----" block: its type and decoded bytes.
- `DecodePEM(text str) ![]PEMBlock`: DecodePEM returns every PEM block in text, in order; text between blocks is ignored.
- `type SignatureAlgorithm enum`: SignatureAlgorithm is how a certificate is signed.
- `type PublicKeyAlgorithm enum`: PublicKeyAlgorithm is the kind of key a certificate holds.
- `const KeyUsageDigitalSignature = 1`: Key usage bits (KeyUsage), numbered as in RFC 5280 with bit 0 = digitalSignature.
- `const KeyUsageContentCommitment = 2`
- `const KeyUsageKeyEncipherment = 4`
- `const KeyUsageDataEncipherment = 8`
- `const KeyUsageKeyAgreement = 16`
- `const KeyUsageCertSign = 32`
- `const KeyUsageCRLSign = 64`
- `const KeyUsageEncipherOnly = 128`
- `const KeyUsageDecipherOnly = 256`
- `const ExtKeyUsageAny = "2.5.29.37.0"`: Extended key usage OIDs.
- `const ExtKeyUsageServerAuth = "1.3.6.1.5.5.7.3.1"`
- `const ExtKeyUsageClientAuth = "1.3.6.1.5.5.7.3.2"`
- `type Name struct`: Name is a distinguished name: the common attributes, and the DER bytes chains are matched on.
- `type Certificate struct`: Certificate is a parsed X.509 v1/v3 certificate. Times are Unix seconds.
- `(n Name) String() str`: String formats n like "CN=example.com,O=Example,C=US".
- `ParseCertificate(der []u8) !Certificate`: ParseCertificate parses one DER certificate. Slices in the result share der's memory.
- `ParseCertificatesPEM(pem str) ![]Certificate`: ParseCertificatesPEM parses every CERTIFICATE block in pem (other blocks are skipped).
- `(c Certificate) CheckSignature(alg SignatureAlgorithm, signed []u8, sig []u8) !`: CheckSignature checks that sig is c's key's signature of signed under alg. SHA-1 is refused.
- `(c Certificate) CheckSignatureFrom(parent Certificate) !`: CheckSignatureFrom checks that parent signed c. It does not check that parent may sign.
- `(c Certificate) CheckTLSSignature(scheme i64, signed []u8, sig []u8) !`: CheckTLSSignature checks a TLS 1.3 CertificateVerify signature by c's key: scheme is the SignatureScheme code and signed the bytes the peer signed (padding, context and transcript hash).
- `(c Certificate) CheckTLS12Signature(scheme i64, signed []u8, sig []u8) !`: CheckTLS12Signature verifies a TLS 1.2 signature (ServerKeyExchange, a client's CertificateVerify; #473) by c's key over signed. TLS 1.2 also allows RSA PKCS #1 v1.5 (0x0401, 0x0501, 0x0601), and its ECDSA schemes name only the hash, not the curve.
- `type CertPool struct`: CertPool is a set of certificates indexed by subject, used for roots and intermediates.
- `NewCertPool() CertPool`: NewCertPool returns an empty pool.
- `(p mut CertPool) Add(c Certificate)`: Add adds c to the pool unless it is already there.
- `(p mut CertPool) AddPEM(pem str) !i64`: AddPEM adds every certificate in pem that parses and returns how many were added; it fails only when none could be.
- `(p CertPool) Len() i64`: Len is the number of certificates in the pool.
- `(p CertPool) Certificates() []Certificate`: Certificates returns the pool's certificates in the order they were added.
- `SystemRoots() !CertPool`: SystemRoots loads the operating system's trusted roots (SSL_CERT_FILE overrides the location) once per core and returns them.
- `type VerifyOptions struct`: VerifyOptions controls Verify. Roots nil means the system roots; Now 0 means the clock; DNSName "" skips the host name check; KeyUsages empty means server authentication; MaxChain 0 means 8 certificates, leaf and root included.
- `(c Certificate) Verify(opts VerifyOptions) ![]Certificate`: Verify builds a chain from c through opts.Intermediates to a trusted root and checks it: validity periods, CA and key-usage rules, path lengths, name constraints, signatures (no SHA-1), the chain length and the host name. The chain is returned leaf first, root last.
- `ParseIP(s str) ?[]u8`: ParseIP parses dotted IPv4 (4 bytes) or IPv6 text (16 bytes), optionally in brackets; nil if invalid.
- `(c Certificate) VerifyHostname(host str) !`: VerifyHostname checks that c is valid for host: an IP address against the IP SANs, otherwise a DNS name against the DNS SANs (case-insensitive, one leftmost "*" label followed by at least two labels; a host containing "*" never matches). The common name is not used.

## nist

Package nist has the NIST curves P-224, P-256, P-384 and P-521 as Go's crypto/elliptic Curve (affine abacus points, with (0, 0) for the point at infinity), legacy DSA signature verification as Go's crypto/dsa does it (no DSA signer: Go deprecates DSA and FIPS 186-5 does not approve it for signing), and Tin's FIPS 140-3 status as Go's crypto/fips140 reports it. Tin is not a validated module, so FIPS mode is never enabled.

- `type DSAPublicKey struct`: DSAPublicKey is a DSA public key: the parameters p, q and g, and the public value y.
- `DSAVerify(pub DSAPublicKey, hash []u8, r abacus.Int, s abacus.Int) !`: DSAVerify checks the legacy DSA signature (r, s) over hash by pub, as Go's dsa.Verify does. Parameters no signature can verify under (P zero, Q at most 1 or not a whole number of bytes long) fail with ErrDSAParameters; a signature that does not verify fails with a plain fault.
- `DSAVerifyDER(pub DSAPublicKey, hash []u8, sig []u8) !`: DSAVerifyDER checks a DER SEQUENCE{r, s} DSA signature, the form X.509 certificates carry, over hash by pub.
- `ParseDSAPublicKeyDER(der []u8) !DSAPublicKey`: ParseDSAPublicKeyDER reads a DSA SubjectPublicKeyInfo as certificates carry it: the algorithm's parameters (p, q, g) and the public value y. Like Go's x509, it fails on a zero or negative value.
- `shape Curve`: Curve is the operations of Go's crypto/elliptic.Curve that crypto/ecdsa uses. A point (x, y) is affine, and (0, 0) is the point at infinity. Add, Double and ScalarMult fail where Go panics: on a point that is off the curve or has a coordinate out of range.
- `P224() dyn Curve`: P224 is the NIST curve P-224 as a Curve. Its constants are fixed, so building it cannot fail.
- `P256() dyn Curve`: P256 is the NIST curve P-256 as a Curve.
- `P384() dyn Curve`: P384 is the NIST curve P-384 as a Curve.
- `P521() dyn Curve`: P521 is the NIST curve P-521 as a Curve.
- `(e ellipticCurve) IsOnCurve(x abacus.Int, y abacus.Int) bool`: IsOnCurve reports whether (x, y) is a point of the curve, not the point at infinity (0, 0).
- `(e ellipticCurve) Add(x1 abacus.Int, y1 abacus.Int, x2 abacus.Int, y2 abacus.Int) !(abacus.Int, abacus.Int)`: Add returns (x1, y1) + (x2, y2), and fails when either point is not on the curve.
- `(e ellipticCurve) Double(x abacus.Int, y abacus.Int) !(abacus.Int, abacus.Int)`: Double returns 2*(x, y), and fails when the point is not on the curve.
- `(e ellipticCurve) ScalarMult(x abacus.Int, y abacus.Int, k []u8) !(abacus.Int, abacus.Int)`: ScalarMult returns k*(x, y) for a big-endian scalar k of any length, and fails when the point is not on the curve. The time depends on the lengths of k and the curve, not on its bits.
- `(e ellipticCurve) ScalarBaseMult(k []u8) (abacus.Int, abacus.Int)`: ScalarBaseMult returns k*G for the curve's generator G and a big-endian scalar k of any length.
- `FIPS140Enabled() bool`: FIPS140Enabled reports whether FIPS 140-3 mode is on. Tin's verdict is always false.
- `FIPS140Enforced() bool`: FIPS140Enforced reports whether FIPS 140-3 rules are enforced (Go's Enforced, the only-mode switch). Tin's verdict is always false.
- `FIPS140Version() str`: FIPS140Version is the version of a frozen FIPS 140-3 module: "" because Tin has none (Go reports "latest" for its unfrozen module).
- `FIPS140WithoutEnforcement(f fn())`: FIPS140WithoutEnforcement runs f. Tin never enforces FIPS 140-3 rules, so there is nothing to switch off.
- `type MLDSAParams struct`: MLDSAParams is one parameter set of FIPS 204 (Table 1): the matrix shape k x l, the secret bound eta, the challenge weight tau, the mask bound gamma1, the rounding gamma2, the hint weight omega, the challenge length ctilde (lambda / 4 bytes), the bits of a z coefficient and of a w1 coefficient.
- `(p MLDSAParams) String() str`: String is the parameter set's name, such as "ML-DSA-44".
- `(p MLDSAParams) PublicKeySize() i64`: PublicKeySize is the length of a public key in bytes (32 + 320 k).
- `(p MLDSAParams) SignatureSize() i64`: SignatureSize is the length of a signature in bytes (ctilde + 32 l zbits + omega + k).
- `(p MLDSAParams) ExpandedKeySize() i64`: ExpandedKeySize is the length of an expanded private key in bytes (2560, 4032 or 4896).
- `MLDSAGenerateKey(p MLDSAParams) ([]u8, []u8)`: MLDSAGenerateKey makes a key pair from fresh randomness: the 32-byte seed (the private key) and the public key.
- `MLDSAPublicKey(p MLDSAParams, seed secret []u8) ![]u8`: MLDSAPublicKey is the public key of the 32-byte seed (FIPS 204's KeyGen_internal, Go's PrivateKey.PublicKey).
- `MLDSAExpandedKey(p MLDSAParams, seed secret []u8) ![]u8`: MLDSAExpandedKey is the FIPS 204 expanded private key of the 32-byte seed (2560, 4032 or 4896 bytes).
- `MLDSASign(p MLDSAParams, seed secret []u8, msg []u8, ctx []u8) ![]u8`: MLDSASign signs msg with context ctx under the seed with a fresh nonce, as Go's PrivateKey.Sign does.
- `MLDSASignDeterministic(p MLDSAParams, seed secret []u8, msg []u8, ctx []u8) ![]u8`: MLDSASignDeterministic signs msg with context ctx under the seed with a zero nonce, as Go's SignDeterministic does.
- `MLDSASignMu(p MLDSAParams, seed secret []u8, mu []u8) ![]u8`: MLDSASignMu signs the message representative mu (64 bytes) under the seed with a fresh nonce (Go's SignExternalMu).
- `MLDSASignMuDeterministic(p MLDSAParams, seed secret []u8, mu []u8) ![]u8`: MLDSASignMuDeterministic signs mu under the seed with a zero nonce (Go's SignExternalMuDeterministic).
- `MLDSASignMuDerand(p MLDSAParams, seed secret []u8, mu []u8, rnd secret []u8) ![]u8`: MLDSASignMuDerand signs mu under the seed with the nonce rnd (32 bytes): for known-answer tests only.
- `MLDSASignExpandedMuDerand(p MLDSAParams, sk secret []u8, mu []u8, rnd secret []u8) ![]u8`: MLDSASignExpandedMuDerand signs mu under the expanded key sk with the nonce rnd: for known-answer tests only.
- `MLDSAVerify(p MLDSAParams, pk []u8, msg []u8, sig []u8, ctx []u8) !`: MLDSAVerify checks sig as a signature of msg with context ctx under pk; a signature that does not verify fails.
- `MLDSADecompose(p MLDSAParams, r i64) (i64, i64)`: MLDSADecompose is Decompose (FIPS 204 Algorithm 36) of r in [0, q) for the set: the high part and the centered low part.
- `MLDSAVerifyMu(p MLDSAParams, pk []u8, mu []u8, sig []u8) !`: MLDSAVerifyMu checks sig as a signature of the message representative mu under pk (the pre-hashed mode).

## herald

Package herald writes leveled log lines, one write(2) per line so cores never interleave:

```text
2026-10-01T11:22:05.123Z INFO core=2 listening addr=:8080
```

- `const LDebug = 0`
- `const LInfo = 1`
- `const LWarn = 2`
- `const LError = 3`
- `SetLevel(l i64)`: SetLevel drops lines below l (LDebug, LInfo, LWarn, LError) on this core.
- `SetOutput(fd i64)`: SetOutput sends this core's lines to file descriptor fd.
- `SetClock(f fn() i64)`: SetClock replaces the clock (unix milliseconds), for tests.
- `Line(l i64, msg str, kv []str) str`: Line formats a log line (without writing it): timestamp, level, core, message, pairs.
- `Log(l i64, msg str, kv []str)`: Log writes msg at level l with key/value pairs kv (k1, v1, k2, v2, ...).
- `Debug(msg str)`: Debug logs msg at debug level.
- `Info(msg str)`: Info logs msg at info level.
- `Warn(msg str)`: Warn logs msg at warning level.
- `Error(msg str)`: Error logs msg at error level.
- `Info2(msg str, k str, v str)`: Info2 logs msg with one key/value pair.
- `Info4(msg str, k1 str, v1 str, k2 str, v2 str)`: Info4 logs msg with two key/value pairs.
- `Error2(msg str, k str, v str)`: Error2 logs msg with one key/value pair at error level.

## expvar

Package expvar publishes named variables that a running program can read back, as Go's expvar does: integers, floats, strings, flags and maps of them, plus computed values (Func) and variables published under a second name (Publish). The registry is process-wide, so a variable made on one core is seen by every core. Integer and float updates are atomic; the lists and string values are changed under a short lock. Handler serves the registry as Go's JSON at /debug/vars.

```tin body
let requests = expvar.NewInt("requests")   // made before the cores start, or in a shared let
requests.Add(1)
let r = anvil.NewRouter()
r.Get("/debug/vars", expvar.Handler)
```

Nothing is freed while a handle may still use it (there is no collector): see README.md.

- `shape Var`: Var is a published variable: what Get returns and Map.Set takes. Only this package's types implement it.
- `type KeyValue struct`: KeyValue is one variable of the registry or of a map, as Do passes it.
- `type Int struct`: Int is an integer variable; the handle is a pointer to its node, so copies share it.
- `type Float struct`: Float is a float variable; the handle is a pointer to its node, so copies share it.
- `type String struct`: String is a string variable; the handle is a pointer to its node, so copies share it.
- `type Bool struct`: Bool is a flag variable; the handle is a pointer to its node, so copies share it. Go's expvar has no Bool (it publishes a flag with Func over a variable that is read, not shared); this package adds it because a flag that several cores set and read needs an atomic word.
- `type Map struct`: Map is a map of variables; the handle is a pointer to its node, so copies share it.
- `NewInt(name str) Int`: NewInt publishes a new integer variable named name, starting at 0. It panics if the name is taken, as Go's Publish does.
- `NewFloat(name str) Float`: NewFloat publishes a new float variable named name, starting at 0. It panics if the name is taken.
- `NewString(name str) String`: NewString publishes a new string variable named name, starting as "". It panics if the name is taken.
- `NewBool(name str) Bool`: NewBool publishes a new flag named name, starting as false. It panics if the name is taken.
- `NewMap(name str) Map`: NewMap publishes a new, empty map named name. It panics if the name is taken.
- `Publish(name str, v dyn Var)`: Publish publishes v under name, as Go's Publish does. v is shared, not copied: a variable published under two names is one variable, and a later change shows under both. It panics if the name is taken.
- `Func[T bool | i64 | f64 | str](f fn() T) dyn Var`: Func returns a variable whose value is f's result, computed and encoded as JSON at each read, as Go's expvar.Func does: f runs again whenever the variable is served or read. Go's any has no Tin equivalent, so T is bool, i64, f64 or str. A NaN or an infinity has no JSON form and reads as an empty value, as in Go. Publish the result, or Set it in a Map.
- `Get(name str) ?dyn Var`: Get returns the variable published as name, or nil when there is none.
- `Do(f fn(KeyValue))`: Do calls f for each published variable, in name order.
- `Handler(q anvil.Req, w mut anvil.Out)`: Handler serves every published variable as JSON in Go's format: one "name": value line per variable, in name order, with the application/json content type.
- `(v Int) Add(delta i64)`: Add adds delta to the integer variable, wrapping on overflow as Go's expvar does.
- `(v Int) Set(value i64)`: Set stores value in the integer variable.
- `(v Int) Value() i64`: Value returns the integer variable's value.
- `(v Int) String() str`: String returns the value in decimal, as Go's expvar writes it.
- `(v Float) Add(delta f64)`: Add adds delta to the float variable; concurrent adds are not lost.
- `(v Float) Set(value f64)`: Set stores value in the float variable.
- `(v Float) Value() f64`: Value returns the float variable's value.
- `(v Float) String() str`: String returns the value as Go's expvar writes it: the shortest form that reads back exactly.
- `(v String) Set(value str)`: Set stores value in the string variable. The value is copied, so the caller may change its own.
- `(v String) Value() str`: Value returns the string variable's value.
- `(v String) String() str`: String returns the value quoted the way Go's expvar writes it (JSON escapes).
- `(v Bool) Set(value bool)`: Set stores value in the flag.
- `(v Bool) Value() bool`: Value returns the flag.
- `(v Bool) String() str`: String returns "true" or "false".
- `(v funcVar) String() str`: String computes the value now and returns it as JSON.
- `(m Map) Add(key str, delta i64)`: Add adds delta to the integer under key, creating it at 0 when the key is new. A key that holds another kind of variable is left alone, as in Go.
- `(m Map) AddFloat(key str, delta f64)`: AddFloat adds delta to the float under key, creating it at 0 when the key is new. A key that holds another kind of variable is left alone, as in Go.
- `(m Map) Set(key str, av dyn Var)`: Set stores av under key, replacing whatever the key held. av is shared, not copied: later changes to it show in the map, as in Go.
- `(m Map) SetString(key str, value str)`: SetString stores a new string variable holding value under key. This package's helper: Go makes such a value with new(String), which has no handle here.
- `(m Map) SetBool(key str, value bool)`: SetBool stores a new flag holding value under key. This package's helper, as SetString.
- `(m Map) Get(key str) ?dyn Var`: Get returns the variable under key, or nil when there is none.
- `(m Map) Delete(key str)`: Delete removes key from m. The variable stays valid for any handle that holds it.
- `(m Map) Init() Map`: Init removes every key from m and returns m.
- `(m Map) Do(f fn(KeyValue))`: Do calls f for each variable of m, in key order.
- `(m Map) String() str`: String returns m as Go's expvar writes it on one line: {"a": 1, "b": "x"}.

## rpc

Package rpc is Go's net/rpc over a codec. A Server serves methods registered with RegisterMethod; a Client calls them with Call and Go. The codec owns the wire (rpc/jsonrpc is Go's net/rpc/jsonrpc); this package owns Go's request and response grammar and its error texts. Codecs move JSON text: the parameters of a call and its result.

- `type Request struct`: Request is the header of a call: the "Service.Method" name and the client's sequence number.
- `type Response struct`: Response is the header of an answer: the request's name and sequence number, and the error text ("" for none).
- `shape ServerCodec`: ServerCodec reads requests and writes responses. ReadRequestBody returns the call's parameters as JSON text, and WriteResponse takes the reply as JSON text (the codec ignores it when the response has an error).
- `shape ClientCodec`: ClientCodec writes requests and reads responses. WriteRequest takes the parameters as JSON text, and ReadResponseBody returns the result as JSON text.
- `(m typedMethod[A, R]) Call(params str) !str`: Call decodes the first parameter as A (Go's jsonrpc decodes params[0]; an empty list leaves the zero value), runs the handler, and encodes its reply as JSON text.
- `type Server struct`: Server holds the registered methods by their "Service.Method" names.
- `NewServer() Server`: NewServer makes a server with no methods.
- `RegisterMethod[A constraints.Any, R constraints.Any](srv mut Server, name str, h fn(A) !R) !`: RegisterMethod registers the handler of "Service.Method". The request's first parameter is decoded as A, and the reply R is the result; a handler that fails sends its text as the response's error. A name with no dot, or one already registered, is a fault.
- `(srv Server) ServeCodec(codec dyn ServerCodec)`: ServeCodec serves the calls codec reads, until the codec ends a header, as Go's ServeCodec does, and then closes the codec. The calls on one codec run one at a time, in the order they were read.
- `type Client struct`: Client makes calls over a ClientCodec. Its reader is Input, which runs as a task of the caller's scope (a handle cannot outlive its scope); calls are matched to their replies by sequence number.
- `NewClient(codec dyn ClientCodec) Client`: NewClient makes a client over codec. Start its reader in a scope that outlives the calls: s.spawn(fn() ! { c.Input() }).
- `(c mut Client) Input()`: Input reads replies and hands each to the call waiting for it, until the codec ends. Then the calls still waiting fail: with ErrShutdown after Close, with ErrUnexpectedEOF when the peer hung up inside a message, else with the codec's fault. It returns nothing, since a fault would cancel the scope it runs in.
- `(c mut Client) Close() !`: Close closes the codec. The reader ends once the peer has closed its side too, and the calls still waiting then fail with ErrShutdown. A second Close fails with ErrShutdown.
- `type Pending[R constraints.Any] struct`: Pending is a call in flight: Wait takes its reply, decoded as R.
- `Go[A constraints.Any, R constraints.Any](c mut Client, method str, args A) Pending[R]`: Go starts a call of method with args and returns its Pending reply at once, after the request is written (Go's Client.Go).
- `(p mut Pending[R]) Wait() !R`: Wait waits for the call's reply and decodes it as R; a remote error or a lost connection is the call's fault.
- `Call[A constraints.Any, R constraints.Any](c mut Client, method str, args A) !R`: Call invokes method with args and waits for its reply (Go's Client.Call).

## syslog

Package syslog writes messages to the system log and to collectors, as Go's log/syslog does: the local Unix socket (/dev/log and its fallbacks), Unix datagram and stream sockets, TCP and IPv4 UDP, the priorities and facilities, a collector for the receiving side, and a herald sink that writes a log record in the same wire format.

- `type Collector struct`: Collector is the receiving side of a syslog connection: a bound Unix datagram or stream socket, or an IPv4 UDP port. It is what a collector or a test listens with; the messages it reads are the bytes a Writer sent.
- `Listen(network str, addr str) !Collector`: Listen binds a collector: network "unixgram" (Read returns one message per datagram), "unix" (a stream: Read returns the next bytes, accepting the next connection once one ends) or "udp" (addr is "a.b.c.d:port"). A Unix path must not exist yet.
- `(c mut Collector) Read(max i64) !str`: Read returns the next message (a datagram, cut to max bytes) or, for a stream, the next bytes of it (at most max).
- `(c mut Collector) Close()`: Close closes the collector's sockets; it does not remove a Unix path (the caller does).
- `const LogEmerg = 0`: LogEmerg is severity 0: the system is unusable.
- `const LogAlert = 1`: LogAlert is severity 1: action must be taken immediately.
- `const LogCrit = 2`: LogCrit is severity 2: critical conditions.
- `const LogErr = 3`: LogErr is severity 3: error conditions.
- `const LogWarning = 4`: LogWarning is severity 4: warning conditions.
- `const LogNotice = 5`: LogNotice is severity 5: normal but significant conditions.
- `const LogInfo = 6`: LogInfo is severity 6: informational messages.
- `const LogDebug = 7`: LogDebug is severity 7: debug-level messages.
- `const LogKern = 0`: LogKern is the kernel messages facility.
- `const LogUser = 8`: LogUser is the user-level messages facility.
- `const LogMail = 16`: LogMail is the mail system facility.
- `const LogDaemon = 24`: LogDaemon is the system daemons facility.
- `const LogAuth = 32`: LogAuth is the security and authorization facility.
- `const LogSyslog = 40`: LogSyslog is the facility for messages generated by syslogd.
- `const LogLpr = 48`: LogLpr is the line printer subsystem facility.
- `const LogNews = 56`: LogNews is the network news subsystem facility.
- `const LogUucp = 64`: LogUucp is the UUCP subsystem facility.
- `const LogCron = 72`: LogCron is the clock daemon facility.
- `const LogAuthpriv = 80`: LogAuthpriv is the private security and authorization facility.
- `const LogFtp = 88`: LogFtp is the FTP daemon facility.
- `const LogLocal0 = 128`: LogLocal0 is the first local-use facility.
- `const LogLocal1 = 136`: LogLocal1 is the second local-use facility.
- `const LogLocal2 = 144`: LogLocal2 is the third local-use facility.
- `const LogLocal3 = 152`: LogLocal3 is the fourth local-use facility.
- `const LogLocal4 = 160`: LogLocal4 is the fifth local-use facility.
- `const LogLocal5 = 168`: LogLocal5 is the sixth local-use facility.
- `const LogLocal6 = 176`: LogLocal6 is the seventh local-use facility.
- `const LogLocal7 = 184`: LogLocal7 is the eighth local-use facility.
- `type Writer struct`: Writer is a connection to the system log or to a collector, and the priority, tag and host name of its messages. A Writer belongs to one core: give each core its own.
- `Dial(network str, raddr str, priority i64, tag str) !Writer`: Dial connects to the collector at raddr over network ("unixgram", "unix", "tcp" or "udp"), or to the local system log when network is "" (raddr is then ignored, and /dev/log is tried first). priority is a facility | severity; tag "" means the program's name. Like Go's Dial, it fails at once when no connection can be made.
- `New(priority i64, tag str) !Writer`: New connects to the local system log with the given priority and tag (Go's New).
- `(w mut Writer) Write(b []u8) !i64`: Write sends b as one message at the writer's priority and returns len(b) (Go's Writer.Write).
- `(w mut Writer) Emerg(m str) !`: Emerg sends m at severity LogEmerg.
- `(w mut Writer) Alert(m str) !`: Alert sends m at severity LogAlert.
- `(w mut Writer) Crit(m str) !`: Crit sends m at severity LogCrit.
- `(w mut Writer) Err(m str) !`: Err sends m at severity LogErr.
- `(w mut Writer) Warning(m str) !`: Warning sends m at severity LogWarning.
- `(w mut Writer) Notice(m str) !`: Notice sends m at severity LogNotice.
- `(w mut Writer) Info(m str) !`: Info sends m at severity LogInfo.
- `(w mut Writer) Debug(m str) !`: Debug sends m at severity LogDebug.
- `(w mut Writer) Herald(level i64, msg str, kv []str) !`: Herald writes one herald record at the matching severity: LDebug is debug, LInfo info, LWarn warning and LError err. The message is the record's text with its key/value pairs, as HeraldMessage formats them.
- `(w mut Writer) Close()`: Close closes the connection; the next message connects again (Go's Writer.Close).
- `HeraldMessage(msg str, kv []str) str`: HeraldMessage is a herald record's text without its timestamp, level or core: the message, then " key=value" for each pair. A value that is empty or holds a space, a quote, '=', a control byte or a non-ASCII byte is quoted with %q, as herald quotes it.
- `Frame(local bool, pri i64, ts str, host str, tag str, pid i64, msg str) str`: Frame returns one message in Go's wire format: "<PRI>TIME HOST TAG[PID]: MSG" for a network connection, and the same without HOST for a local one (local is true for the Unix sockets). A newline ends the message unless msg already has one.

## crucible

Package crucible is for tests and micro-benchmarks: labeled checks that collect failures, Done to report them (exit status 1 on failure), and Bench to time a function.

```tin body
crucible.EqI("sum", 2 + 3, 5)
crucible.Done()
```

- `EqI(label str, got i64, want i64)`: EqI checks two integers.
- `EqU(label str, got u64, want u64)`: EqU checks two unsigned integers.
- `EqS(label str, got str, want str)`: EqS checks two strings.
- `EqB(label str, got bool, want bool)`: EqB checks two bools.
- `EqF(label str, got f64, want f64, eps f64)`: EqF checks two floats within eps.
- `True(label str, cond bool)`: True checks that cond holds.
- `False(label str, cond bool)`: False checks that cond does not hold.
- `NoFault(label str, err fault)`: NoFault checks that err is nil.
- `HasFault(label str, err fault)`: HasFault checks that err is not nil.
- `Failed() bool`: Failed reports whether any check failed so far.
- `Checks() i64`: Checks is the number of checks run so far.
- `Done()`: Done prints "ok N checks" or every failure, and exits with status 1 if any failed.
- `Bench(label str, n i64, f fn(i64))`: Bench runs f(i) for i in [0, n) and prints the time per call.
- `type T struct`: T is one running test: checks record failures in it, and the test continues.
- `type B struct`: B is one running benchmark: run the measured code b.N times.
- `Configure(pattern str, json bool)`: Configure sets how tin test runs the tests: pattern (a lasso regular expression, "" for every test) picks the tests and benchmarks whose names match, and json prints one JSON event per line instead of text (toolchain/docs/TOOLING.md section 5.2). A pattern that is not a regular expression ends the run with status 2.
- `(t mut T) Error(msg str)`: Error marks the test failed with msg (it keeps running).
- `(t mut T) Log(msg str)`: Log records msg; it is printed only if the test fails.
- `(t T) Failed() bool`: Failed reports whether the test has failed so far.
- `(t mut T) True(label str, cond bool)`: True fails the test with label unless cond holds.
- `(t mut T) False(label str, cond bool)`: False fails the test with label if cond holds.
- `(t mut T) NoFault(label str, err fault)`: NoFault fails the test if err is not nil.
- `(t mut T) HasFault(label str, err fault)`: HasFault fails the test if err is nil.
- `Equal[V constraints.Comparable](t mut T, label str, got V, want V)`: Equal fails the test unless got == want; both are printed on failure.
- `Run(name str, f fn(mut T))`: Run runs one test and prints its result like go test -v (or as JSON events, see Configure); a test that does not match the -run pattern is not run.
- `RunBench(name str, f fn(mut B))`: RunBench runs one benchmark with b.N doubling until it takes at least 1 s, then prints the time per operation.
- `Finish()`: Finish prints PASS or FAIL and exits with status 1 when a test failed.

## crucible/iotest

Package iotest wraps the io shapes to misbehave in the ways tests need, as Go's testing/iotest does: TimeoutReader fails its second read, HalfReader returns half of what each read asks for, DataErrReader turns the end of its source into a fault, and TruncateWriter drops what a writer takes past a limit while it still reports every byte as written.

```tin body
import "crucible/iotest"
import "flume"

let src = try flume.Open("/tmp/tin-test-iotest.txt")
let out = try flume.Create("/tmp/tin-test-iotest-out.txt")
let r = iotest.HalfReader(src)             // reads at most (len(buf)+1)/2 bytes at a time
let w = iotest.TruncateWriter(out, 7)      // the sink gets the first 7 bytes; Write says all
```

Tin has no read that returns data and an error together (a stream ends with a read of 0, and a fault is an error on its own), so DataErrReader returns the data first and its fault on the read after the source's end; Go's version returns the last data with io.EOF in the same call.

- `type TimeoutReaderOf[R io.Reader] struct`: TimeoutReaderOf is the reader TimeoutReader returns.
- `TimeoutReader[R io.Reader](r R) TimeoutReaderOf[R]`: TimeoutReader returns a reader that fails with ErrTimeout on its second read; the reads after it succeed.
- `(t mut TimeoutReaderOf[R]) Read(buf mut []u8) !i64`: Read fails with ErrTimeout on the second call, and reads from the source on every other call.
- `type HalfReaderOf[R io.Reader] struct`: HalfReaderOf is the reader HalfReader returns.
- `HalfReader[R io.Reader](r R) HalfReaderOf[R]`: HalfReader returns a reader that reads at most half of the buffer it is given, rounded up.
- `(h mut HalfReaderOf[R]) Read(buf mut []u8) !i64`: Read reads into the first (len(buf)+1)/2 bytes of buf.
- `type DataErrReaderOf[R io.Reader] struct`: DataErrReaderOf is the reader DataErrReader returns.
- `DataErrReader[R io.Reader](r R, err fault) DataErrReaderOf[R]`: DataErrReader returns a reader that passes its source's data on and fails with err where the source ends (its read of 0), so the data always comes before the fault.
- `(d mut DataErrReaderOf[R]) Read(buf mut []u8) !i64`: Read reads from the source; a read of 0 into a non-empty buffer fails with the reader's fault.
- `type TruncateWriterOf[W io.Writer] struct`: TruncateWriterOf is the writer TruncateWriter returns.
- `TruncateWriter[W io.Writer](w W, n i64) TruncateWriterOf[W]`: TruncateWriter returns a writer that passes the first n bytes it is given to w and drops the rest without an error; each Write reports all of its bytes as written.
- `(t mut TruncateWriterOf[W]) Write(data []u8) !i64`: Write passes the bytes that are still under the limit to the writer and reports all of data as written.

## crucible/quick

Package quick checks properties over generated values, as Go's testing/quick does. Go picks the generator from a function's parameter types at run time; Tin's generics are fully specialized, so each check takes a generator per parameter: Int64, Uint64, Float64, Bool, Str and Bytes are the ones in this package, and a test may pass its own.

```tin body
import "crucible/quick"
import "twine"

try quick.Check(fn(s str) bool { return twine.Join(twine.Split(s, ","), ",") == s }, quick.Str, quick.Config{})
```

Values come from dice seeded by Config.Seed, so a run is the same every time. A failure reports the case number and the input, as Go's error does: "#3: failed on input 42".

- `type Config struct`: Config sets how many cases a check runs and the seed of its generator. The zero Config runs 100 cases from seed 1.
- `Check[A constraints.Any](f fn(A) bool, gen fn(mut dice.Rand) A, cfg Config) !`: Check runs f on MaxCount values from gen and fails at the first value f rejects, as Go's quick.Check.
- `Check2[A constraints.Any, B constraints.Any](f fn(A, B) bool, genA fn(mut dice.Rand) A, genB fn(mut dice.Rand) B, cfg Config) !`: Check2 is Check over two arguments, drawn in order from genA and then genB for each case.
- `CheckEqual[A constraints.Any, B constraints.Comparable](f fn(A) B, g fn(A) B, gen fn(mut dice.Rand) A, cfg Config) !`: CheckEqual fails at the first value on which f and g give different results, as Go's quick.CheckEqual.
- `Int64(r mut dice.Rand) i64`: Int64 is a signed integer of any size, half of them negative.
- `Uint64(r mut dice.Rand) u64`: Uint64 is an unsigned integer of any size.
- `Float64(r mut dice.Rand) f64`: Float64 is a float between -1 and 1.
- `Bool(r mut dice.Rand) bool`: Bool is true or false, each half the time.
- `Str(r mut dice.Rand) str`: Str is a string of up to 24 pieces, including quotes, spaces and multi-byte UTF-8.
- `Bytes(r mut dice.Rand) []u8`: Bytes is a byte slice of up to 24 bytes.

## crucible/fstest

Package fstest is an in-memory file system for tests, and a check that a file system is consistent, as Go's testing/fstest is. MapFS maps slash-separated names to files; the directories are the names' parents, plus any entry whose Mode has ModeDir. TestFS walks a file system with fs.WalkDir and checks what the walk shows against Open, Stat and ReadDir.

```tin body
import "crucible/fstest"

let fsys = fstest.MapFS{"a/b.txt": fstest.MapFile{Data: "hi"}}
try fstest.TestFS(fsys, []str{"a/b.txt"})
```

Go's MapFS also has Glob and Sub; Tin's fs.Glob and fs.Sub work over it, since they take any shape.

- `type MapFile struct`: MapFile is one entry of a MapFS: its contents, its mode (type bits and permissions; 0 is a file with mode 0444) and its modification time in unix nanoseconds.
- `type MapFS map[str]MapFile`: MapFS is a file system held in a map from names to files, as Go's fstest.MapFS.
- `(m MapFS) Open(name str) !dyn fs.File`: Open opens the named file or directory; a directory is one whose name is a parent of an entry, or ".".
- `(m MapFS) Stat(name str) !fs.FileInfo`: Stat describes the named file or directory.
- `(m MapFS) ReadDir(name str) ![]fs.DirEntry`: ReadDir lists the named directory, sorted by name, with the type of each entry.
- `(m MapFS) ReadFile(name str) !str`: ReadFile reads the named file's contents.
- `(f mut mapFile) Read(buf mut []u8) !i64`: Read reads the next bytes of the file into buf: 0 at its end. A directory cannot be read.
- `(f mapFile) Stat() !fs.FileInfo`: Stat describes the open file.
- `(f mut mapFile) ReadDir(n i64) ![]fs.DirEntry`: ReadDir lists the directory's entries, n at a time (all that are left when n <= 0), sorted by name.
- `(f mut mapFile) Close() !`: Close closes the open file.
- `TestFS[F fs.TreeFS](fsys F, expected []str) !`: TestFS checks that fsys is a consistent file system: every name in expected is in it, each file reads the same through Open, ReadFile and Stat, each directory's ReadDir lists the entries that fs.WalkDir visits under it, and every listed entry's Stat agrees with its type. It fails with every problem it finds, as Go's fstest.TestFS does.

## crucible/slogtest

Package slogtest checks a log handler against records, as Go's log/slog/slogtest does for slog handlers. Its handler is herald: Check runs each record through herald.Line under a fixed clock and reports every line that does not have herald's layout.

```tin body
import "crucible/slogtest"
import "crucible"
import "herald"

let problems = slogtest.Check([]slogtest.Record{{Level: herald.LInfo, Msg: "listening", KV: []str{"addr", ":8080"}}})
crucible.True("lines", len(problems) == 0)
```

A line is "TIMESTAMP LEVEL core=N MESSAGE KEY=VALUE..." with a newline at its end. A value is quoted with %q when it is empty or holds a byte that is a space, a quote, '=', a control byte or a byte above 0x7e; a key with no value after it is left out, as herald.Line does.

- `type Record struct`: Record is one log call: a level (herald.LDebug to herald.LError), a message and key/value pairs.
- `Check(records []Record) []str`: Check formats each record and returns one problem per line that is not in herald's layout, in record order; it returns none when every line is right. It replaces herald's clock on this core.

## crucible/cryptotest

Package cryptotest makes the buffers that constant-time comparison tests need: filled and seeded byte slices, copies that differ in one byte, and Equal, which is seal.Equal over byte slices. Go's testing/cryptotest seeds crypto/rand for a test; Tin has no process-wide random source to seed, so each buffer carries its own seed and the same seed gives the same bytes on every run.

```tin body
import "crucible/cryptotest"
import "crucible"

let a = cryptotest.Seeded(7, 32)
let b = cryptotest.Flip(a, 31, 0x80)        // the last byte differs in its top bit
crucible.False("tag", cryptotest.Equal(a, b))
```

- `Filled(n i64, b u8) []u8`: Filled returns n bytes, all of value b.
- `Seeded(seed u64, n i64) []u8`: Seeded returns n pseudo-random bytes from seed: the same bytes for the same seed.
- `Flip(b []u8, i i64, mask u8) []u8`: Flip returns a copy of b with the byte at index i xor-ed with mask, so the copy differs from b in the bits of mask (and is equal to it when mask is 0).
- `Equal(a []u8, b []u8) bool`: Equal reports whether a and b hold the same bytes, by seal.Equal: it takes time that depends only on their lengths, so it is what a secret comparison should use.

## constraints

Package constraints contains the named generic constraints used by the standard library.

- `shape Any {}`: Any imposes no operations on a type parameter.
- `shape Comparable {}`: Comparable admits values that can be compared by value, including structs and enums whose fields are all comparable. The compiler checks this property at each instantiation.

## policy

Package policy is the with policies (design_semantics §7.1, design/interface_policy.md): with p { body } calls p.Run(body) inside a boundary of its own, with the block as body. Slots are typed ambient values that Bind binds for a block and the tasks it spawns; Retry, Trace and Cached are the library policies.

- `shape Policy[T constraints.Any] { mut Run(body fn() !T) !T }`: Policy is what with p { body } needs of p: Run runs body (any number of times) and gives the block's value. Run may only call body, or pass it to a function that only calls it. Run is mut (#644): a policy may keep state between runs (CachedPolicy).
- `type Slot[T constraints.Any] struct`: Slot is a typed ambient value: with policy.Bind(s, v) { } binds it for the block and the tasks the block spawns.
- `NewSlot[T constraints.Any](name str) Slot[T]`: NewSlot makes a slot named name; declare it once, in a package-level let (one per core).
- `(s Slot[T]) Name() str`: Name is the slot's name.
- `(s Slot[T]) Get() !T`: Get is the value of the innermost Bind of s around the running code; it fails when s is not bound.
- `(s Slot[T]) Bound() bool`: Bound reports whether s is bound around the running code.
- `type BindPolicy[V constraints.Any, T constraints.Any] struct`: BindPolicy binds a slot for its block (Bind).
- `Bind[V constraints.Any, T constraints.Any](s Slot[V], v V) BindPolicy[V, T]`: Bind is a policy that binds s to v for its block and the tasks the block spawns: with policy.Bind(requestID, id) { }.
- `(b BindPolicy[V, T]) Run(body fn() !T) !T`: Run binds the slot on the with block's boundary, then runs body once.
- `type RetryPolicy[T constraints.Any] struct`: RetryPolicy runs its block again while it fails (Retry).
- `Retry[T constraints.Any](attempts i64) RetryPolicy[T]`: Retry is a policy that runs its block up to attempts times while it fails and gives the last fault. A cancellation ends it at once: a cancellation fault from the block is given as it is, and a boundary cancelled (or past its deadline) between attempts gives the cancellation's fault. The block's side effects run again on each attempt.
- `(r RetryPolicy[T]) Backoff(d i64) RetryPolicy[T]`: Backoff is r waiting d before the second attempt, and twice as long before each later one.
- `(r RetryPolicy[T]) Run(body fn() !T) !T`: Run runs body until it succeeds, attempts runs have failed, or the boundary is cancelled.
- `SetTracer(f fn(str, i64, fault))`: SetTracer sends this core's trace spans to f(name, duration in ns, fault or nil) instead of the log.
- `type TracePolicy[T constraints.Any] struct`: TracePolicy reports each run of its block (Trace).
- `Trace[T constraints.Any](name str) TracePolicy[T]`: Trace is a policy that reports its block's name, duration and fault to the core's tracer (a herald line by default).
- `(t TracePolicy[T]) Run(body fn() !T) !T`: Run runs body once and reports it.
- `type Cache[T constraints.Any] struct`: Cache is a per-core store for Cached: declare it in a package-level let. Values are kept (copied to the long-lived heap).
- `NewCache[T constraints.Any](max i64) Cache[T]`: NewCache makes a cache of at most max entries (at least one); a full cache drops its oldest entry.
- `(c Cache[T]) Len() i64`: Len is the number of entries, fresh or expired.
- `(c mut Cache[T]) Drop(key str)`: Drop removes key's entry.
- `type CachedPolicy[T constraints.Any] struct`: CachedPolicy answers its block from a cache (Cached).
- `Cached[T constraints.Any](c Cache[T], key str, ttl i64) CachedPolicy[T]`: Cached is a policy that gives the value cached under key while it is younger than ttl (ns), without running its block; otherwise it runs the block and caches a value it gives. Faults are not cached.
- `(p mut CachedPolicy[T]) Run(body fn() !T) !T`: Run gives the cached value, or runs body and caches its value.

## redis

Package redis is a Redis client. Commands are queries: in c.Do("SET user:{id} {body}") the values travel as separate arguments, so a value can never change a command.

Each core keeps one connection per Client. The requests a core serves at the same time share it: their commands are written together and the replies matched in order (pipelining), so a busy server makes few system calls per command. Inside a request task a call waits without blocking the core; outside one it blocks.

```tin body
let cache = redis.Open(redis.Options{Addr: "127.0.0.1:6379"})
try cache.Set("greeting", "hello")
let (v, found) = try cache.Get("greeting")
```

Blocking commands (BLPOP, SUBSCRIBE, ...) would hold up the commands queued behind them and are not supported.

- `type Reply enum`: Reply is one Redis reply.
- `type Options struct`: Options says where and how to connect.
- `ParseURL(url str) !Options`: ParseURL reads "redis://[[user]:password@]host[:port][/db]"; "rediss://" is the same over TLS 1.3 (TLS is set, so the server's certificate is verified for host).
- `type Client struct`: Client sends commands to one Redis server. Open it in a global's initializer (which runs on every core) or once in main, not per request.
- `Open(o Options) Client`: Open makes a client for the server in o. It connects on first use, on each core.
- `(c Client) Do(q query) !Reply`: Do sends one command and returns its reply; an error reply fails.
- `(c Client) Pipe(qs []query) ![]Reply`: Pipe sends commands together and returns their replies in order; error replies come back as Err. The commands go out back to back, so MULTI ... EXEC in one Pipe is atomic.
- `(c Client) Get(key str) !(str, bool)`: Get returns the value at key, and whether there is one.
- `(c Client) Set(key str, value str) !`: Set stores value at key.
- `(c Client) SetEx(key str, value str, ttl i64) !`: SetEx stores value at key for ttl nanoseconds (at least a millisecond).
- `(c Client) Del(key str) !i64`: Del removes key; it returns how many keys it removed (0 or 1).
- `(c Client) Incr(key str) !i64`: Incr adds one to the integer at key and returns the result.
- `(c Client) Expire(key str, ttl i64) !bool`: Expire makes key expire after ttl nanoseconds; false when there is no such key.
- `(c Client) Ping() !`: Ping checks that the server answers.

## mysql

Package mysql is a MySQL client (tested with MySQL 8.0). Statements are queries: in db.Query("SELECT name FROM users WHERE id = {id}") the text becomes "... id = ?" and id a bound parameter of a prepared statement, so a value can never change a statement.

Each core keeps a pool of connections per Client (Options.Pool, default max(2, 64/cores); Options.MaxTotal caps them for the process); a request task waits for a free one without blocking the core. Prepared statements are cached per connection. Authentication: caching_sha2_password (the MySQL 8 default, including the RSA key exchange when the server has no cached entry) and mysql_native_password. Options.TLS connects over TLS 1.3 (SSLRequest), verifying the server's certificate and name.

Sizing: a Client opened in a global's initializer is opened on every core, so a 32-core pod with Pool 16 may open 512 connections to one server, and a fleet of pods multiplies that. Pool, when not set, is max(2, 64/cores) per core: about 64 for the process, at least 2 on each core. Options.MaxTotal caps the connections of the whole process, over all cores (Clients with the same address, user, database and MaxTotal share one cap): a core at the cap waits, within the request's deadline and Options.Timeout, until a connection is released or a core that has one idle gives up its slot. Set MaxTotal to at least the number of cores that serve database requests; below that, cores share connections by closing and dialing again.

```tin body
let pw = quarry.Getenv("MYSQL_PASSWORD")
let id = 7
let db = mysql.Open(mysql.Options{Addr: "127.0.0.1:3306", User: "app", Password: pw, Database: "shop"})
let rows = try db.Query("SELECT id, name FROM users WHERE id = {id}")
for r in rows.Rows {
	say.Line(r[0].Int(), r[1].Text())
}
```

- `type Value enum`: Value is one column of a row.
- `type Rows struct`: Rows is a query's result.
- `type Result struct`: Result is what a statement without rows did.
- `type Options struct`: Options says where and how to connect.
- `type Client struct`: Client runs statements on one MySQL server. Open it in a global's initializer (which runs on every core) or once in main, not per request.
- `type Tx struct`: Tx is a transaction: its statements run on one connection until Commit or Rollback.
- `Open(o Options) Client`: Open makes a client for the server in o. It connects on first use, on each core.
- `(v Value) IsNull() bool`: IsNull reports whether v is NULL.
- `(v Value) Int() i64`: Int is v as an integer (a Text or Float converted, NULL and bad text 0).
- `(v Value) Float() f64`: Float is v as a float.
- `(v Value) Text() str`: Text is v as text ("" for NULL).
- `(r Rows) Col(name str) i64`: Col is the index of the named column, or -1.
- `(c Client) Query(q query) !Rows`: Query runs a statement and returns its rows.
- `(c Client) Exec(q query) !Result`: Exec runs a statement and returns what it changed.
- `(c Client) Ping() !`: Ping checks that the server answers.
- `(c Client) Begin() !Tx`: Begin starts a transaction; finish it with Commit or Rollback, or its connection stays out of the pool.
- `(t mut Tx) Query(q query) !Rows`: Query runs a statement in the transaction and returns its rows.
- `(t mut Tx) Exec(q query) !Result`: Exec runs a statement in the transaction.
- `(t mut Tx) Commit() !`: Commit makes the transaction's changes permanent.
- `(t mut Tx) Rollback() !`: Rollback undoes the transaction's changes.

## postgres

Package postgres implements a database/sql driver for the PostgreSQL client.

- `type SQLDriver struct`: SQLDriver adapts the PostgreSQL client to database/sql.
- `NewSQLDriver(options Options) SQLDriver`: NewSQLDriver creates a database/sql driver with these PostgreSQL connection options.
- `(d SQLDriver) Open(name str) !dyn sql.Conn`: Open creates a PostgreSQL connection for a database/sql data source name.
- `(c sqlConn) Prepare(query query) !dyn sql.Stmt`: Prepare compiles a parameterized PostgreSQL query for this connection.
- `(c sqlConn) Begin() !dyn sql.Conn`: Begin pins a PostgreSQL connection for a database/sql transaction.
- `(c sqlConn) Finish(commit bool) !bool { fail "postgres: no active transaction" }`: End refuses to finish a connection without an active transaction.
- `(c sqlConn) SetMaxOpen(n i64) !bool`: SetMaxOpen updates the client's process-wide connection cap.
- `(c sqlConn) SetMaxIdle(n i64) !bool`: SetMaxIdle updates the client's per-core connection cap.
- `(c sqlConn) Close() ! { try c.client.Close() }`: Close closes the client pool owned by this generic database handle.
- `(c sqlTxConn) Prepare(query query) !dyn sql.Stmt`: Prepare compiles a query for this PostgreSQL transaction.
- `(c sqlTxConn) Begin() !dyn sql.Conn { fail "postgres: nested transaction" }`: Begin rejects nested transactions.
- `(c sqlTxConn) SetMaxOpen(n i64) !bool { fail "sql: cannot set pool limits inside a transaction" }`: SetMaxOpen is invalid on a transaction connection.
- `(c sqlTxConn) SetMaxIdle(n i64) !bool { fail "sql: cannot set pool limits inside a transaction" }`: SetMaxIdle is invalid on a transaction connection.
- `(c sqlTxConn) Finish(commit bool) !bool`: Commit commits the PostgreSQL transaction.
- `(c sqlTxConn) Close() !`: Close rolls back a transaction whose owner closes it.
- `(s sqlStmt) Query() !sql.Rows`: Query runs the prepared query and converts the PostgreSQL result values.
- `(s sqlTxStmt) Query() !sql.Rows`: Query runs the prepared query within its PostgreSQL transaction.
- `(s sqlStmt) Exec() !sql.Result`: Exec runs the prepared query and returns its affected row count.
- `(s sqlTxStmt) Exec() !sql.Result`: Exec runs the prepared statement within its PostgreSQL transaction.
- `(s sqlStmt) Close() ! { }`: Close releases the statement wrapper without closing the shared client.
- `(s sqlTxStmt) Close() ! { }`: Close releases a transaction statement wrapper.
- `type Value enum`: Value is one column of a row.
- `type Rows struct`: Rows is a query's result.
- `type Result struct`: Result is what a statement without rows did.
- `type Options struct`: Options says where and how to connect.
- `type Client struct`: Client runs statements on one PostgreSQL server. Open it in a global's initializer (which runs on every core) or once in main, not per request.
- `type Tx struct`: Tx is a transaction: its statements run on one connection until Commit or Rollback.
- `Open(o Options) Client`: Open makes a client for the server in o. It connects on first use, on each core.
- `(v Value) IsNull() bool`: IsNull reports whether v is NULL.
- `(v Value) Int() i64`: Int is v as an integer (a Text or Float converted, NULL and bad text 0).
- `(v Value) Float() f64`: Float is v as a float.
- `(v Value) Text() str`: Text is v as text ("" for NULL).
- `(r Rows) Col(name str) i64`: Col is the index of the named column, or -1.
- `(c Client) SetMaxOpen(n i64) !`: SetMaxOpen sets the process-wide connection cap for this client (0: no cap). It takes effect at once, also after use: a raised cap wakes this core's waiters, a lowered one closes this core's idle connections above it. Clients that share a MaxTotal cap share the change; other cores close their excess idle connections, and wait for a raised cap, when they next use the client.
- `(c Client) SetMaxIdle(n i64) !`: SetMaxIdle sets the per-core connection cap for this client (0: none kept). It takes effect at once on this core, and on the others when they next use the client.
- `(c Client) Close() !`: Close prevents new use and closes this client's idle connections; checked-out connections close when returned.
- `(c Client) Query(q query) !Rows`: Query returns the first rowset. With no parameters, multiple statements are allowed and all replies are consumed before returning. Integers and booleans use Value.Int; float4/8 use Value.Float; other OIDs (including numeric and bytea) use Value.Text.
- `(c Client) Exec(q query) !Result`: Exec returns the affected count of the last command. Use Query with RETURNING to obtain generated IDs (PostgreSQL has no connection-wide last insert ID).
- `(c Client) Ping() !`: Ping checks that the server answers.
- `(c Client) Begin() !Tx`: Begin pins a connection until Commit or Rollback. SQL errors abort the transaction until Rollback. Copies share its state: finishing one finishes them all. In request tasks an unfinished transaction is dropped when its owning task/scope ends. Outside tasks always finish explicitly. Tx and its rows belong to the caller's pool.
- `(t mut Tx) Query(q query) !Rows`: Query runs a statement in the transaction and returns its first rowset.
- `(t mut Tx) Exec(q query) !Result`: Exec runs a statement in the transaction and returns its affected count.
- `(t mut Tx) Commit() !`: Commit makes the transaction's changes permanent. An aborted transaction must be rolled back explicitly; PostgreSQL's implicit COMMIT-to-ROLLBACK is not success.
- `(t mut Tx) Rollback() !`: Rollback undoes the transaction's changes and releases its connection.

## database

Package database groups database interfaces and drivers.

- `type Value enum`: Value is one database value returned by a driver.
- `type Result struct`: Result reports the affected row count and optional inserted ID.
- `NewResult(affected i64, lastID ?i64) Result`: NewResult creates a result with the affected count and optional inserted ID.
- `shape Driver { Open(name str) !dyn Conn }`: Driver opens a connection for a driver-specific data source name.
- `shape Conn`: Conn prepares statements and closes a driver connection.
- `shape Stmt`: Stmt executes queries and closes a prepared statement.
- `shape Dest`: Dest receives one column's value: Set converts it to the destination's type, as Go's Scan does.
- `type Int64 struct`: Int64 is a scan destination for an integer column; NULL is an error, as in Go.
- `NewInt64() Int64`: NewInt64 makes an Int64 destination.
- `(d Int64) Get() i64`: Get returns the stored value.
- `(d mut Int64) Set(v Value) !`: Set stores the column value as an integer.
- `type Float64 struct`: Float64 is a scan destination for a floating-point column; NULL is an error, as in Go.
- `NewFloat64() Float64`: NewFloat64 makes a Float64 destination.
- `(d Float64) Get() f64`: Get returns the stored value.
- `(d mut Float64) Set(v Value) !`: Set stores the column value as a float.
- `type String struct`: String is a scan destination for a text column; NULL is an error, as in Go.
- `NewString() String`: NewString makes a String destination.
- `(d String) Get() str`: Get returns the stored value.
- `(d mut String) Set(v Value) !`: Set stores the column value as text.
- `type Bool struct`: Bool is a scan destination for a boolean column; NULL is an error, as in Go.
- `NewBool() Bool`: NewBool makes a Bool destination.
- `(d Bool) Get() bool`: Get returns the stored value.
- `(d mut Bool) Set(v Value) !`: Set stores the column value as a boolean.
- `type Bytes struct`: Bytes is a scan destination for a binary or text column; NULL leaves it empty, as in Go.
- `NewBytes() Bytes`: NewBytes makes a Bytes destination.
- `(d Bytes) Get() []u8`: Get returns the stored bytes.
- `(d mut Bytes) Set(v Value) !`: Set stores the column value as bytes.
- `type NullInt64 struct`: NullInt64 is a scan destination for an integer column that may be NULL.
- `NewNullInt64() NullInt64`: NewNullInt64 makes a NullInt64 destination.
- `(d NullInt64) Get() ?i64`: Get returns the stored value, nil for NULL.
- `(d mut NullInt64) Set(v Value) !`: Set stores the column value, or nil for NULL.
- `type NullFloat64 struct`: NullFloat64 is a scan destination for a floating-point column that may be NULL.
- `NewNullFloat64() NullFloat64`: NewNullFloat64 makes a NullFloat64 destination.
- `(d NullFloat64) Get() ?f64`: Get returns the stored value, nil for NULL.
- `(d mut NullFloat64) Set(v Value) !`: Set stores the column value, or nil for NULL.
- `type NullString struct`: NullString is a scan destination for a text column that may be NULL.
- `NewNullString() NullString`: NewNullString makes a NullString destination.
- `(d NullString) Get() ?str`: Get returns the stored value, nil for NULL.
- `(d mut NullString) Set(v Value) !`: Set stores the column value, or nil for NULL.
- `type NullBool struct`: NullBool is a scan destination for a boolean column that may be NULL.
- `NewNullBool() NullBool`: NewNullBool makes a NullBool destination.
- `(d NullBool) Get() ?bool`: Get returns the stored value, nil for NULL.
- `(d mut NullBool) Set(v Value) !`: Set stores the column value, or nil for NULL.
- `type NullBytes struct`: NullBytes is a scan destination for a binary or text column that may be NULL.
- `NewNullBytes() NullBytes`: NewNullBytes makes a NullBytes destination.
- `(d NullBytes) Get() ?[]u8`: Get returns the stored bytes, nil for NULL.
- `(d mut NullBytes) Set(v Value) !`: Set stores the column value, or nil for NULL.
- `type Rows struct`: Rows is a materialized result set with a deterministic cursor.
- `NewRows(columns []str, values [][]Value) Rows`: NewRows creates a result set from column names and row values.
- `type Row struct`: Row holds the first row of a query result, or its query fault.
- `type DB struct`: DB is a database handle backed by the registered driver's connection pool.
- `type Statement struct`: Statement is a prepared statement tied to its database connection.
- `type Tx struct`: Tx is a transaction that uses its connection until it finishes.
- `Register(name str, driver dyn Driver) !`: Register makes a driver available by name to every core; a name already registered is refused, as in Go.
- `Drivers() []str`: Drivers returns the registered names in lexical order.
- `Open(driverName str, dataSourceName str) !DB`: Open opens a database by its registered driver name and data source name.
- `(db mut DB) Close() !`: Close closes the database and prevents later operations.
- `(db DB) Prepare(query query) !Statement`: Prepare creates a reusable statement for query.
- `(db DB) Query(query query) !Rows`: Query executes query and returns its rows.
- `(db DB) QueryRow(query query) Row`: QueryRow executes query and returns its first row or deferred query fault.
- `(db DB) Exec(query query) !Result`: Exec executes a statement and returns its result.
- `(db DB) SetMaxOpen(n i64) !`: SetMaxOpen sets the process-wide cap on open connections (0: no cap); it takes effect at once, also after use.
- `(db DB) SetMaxIdle(n i64) !`: SetMaxIdle sets the per-core cap on idle connections (0: none kept); it takes effect at once, also after use.
- `(s mut Statement) Close() !`: Close closes a prepared statement.
- `(s Statement) Query() !Rows`: Query executes the prepared query and returns rows.
- `(s Statement) Exec() !Result`: Exec executes the prepared statement and returns its result.
- `(r Rows) Columns() []str { return r.columns }`: Columns returns the result column names.
- `(r mut Rows) Next() bool`: Next advances the cursor and reports whether a row is available.
- `(r Rows) Values() []Value`: Values returns the current row's values, or an empty slice before Next or after exhaustion.
- `(r Rows) Scan(dests ...dyn Dest) !`: Scan copies the current row into the destinations, one per column, as Go's Rows.Scan does.
- `(r mut Rows) Close() ! { r.closed = true }`: Close marks the rows exhausted.
- `(r Row) Scan(dests ...dyn Dest) !`: Scan copies the row into the destinations, or fails with its query fault or ErrNoRows.
- `(r Result) LastInsertId() !i64`: LastInsertId returns the inserted ID when the driver reports one.
- `(r Result) RowsAffected() !i64 { return r.affected }`: RowsAffected returns the number of rows affected.
- `(db DB) Begin() !Tx`: Begin starts a transaction on the database connection.
- `(tx Tx) Query(query query) !Rows`: Query executes a query inside the transaction.
- `(tx Tx) Exec(query query) !Result`: Exec executes a statement inside the transaction.
- `(tx mut Tx) Commit() !`: Commit commits the transaction.
- `(tx mut Tx) Rollback() !`: Rollback rolls back the transaction.

## kafka

Package kafka is an Apache Kafka client: a producer (idempotent by default, with batching and gzip, snappy, lz4 and zstd compression), fetching from partitions (read_committed too), consumer groups with rebalancing, transactions, and administration of topics, partitions, records, groups and configs. It speaks Kafka's binary protocol directly (request versions brokers 2.4 to 4.x accept; run against 3.9 and 4.2), over plain TCP or TLS 1.3, with SASL PLAIN, SCRAM-SHA-256 or SCRAM-SHA-512.

Each core keeps one connection per broker for each Client. The requests a core serves at the same time share a connection, and sends of the same turn to one partition share a record batch, so a busy service makes few requests. Inside a request task a call waits without blocking the core; outside one it blocks.

```tin body
let bus = kafka.Open(kafka.Options{Brokers: []str{"127.0.0.1:9092"}})
let ack = try bus.Send("orders", kafka.Message{Key: "7", Value: "paid"})
let records = try bus.Fetch("orders", ack.Partition, ack.Offset, 1s)
```

A key picks the partition the way the Java client does (murmur2), so a key lands on the same partition from either. Consumer groups: Group and design/design_kafka.md (section 3) for where a consumer loop runs. Transactions: Transactional.

- `type TopicSpec struct`: TopicSpec describes a topic to create.
- `type Config struct`: Config is one configuration entry.
- `type Resource enum`: Resource is what a config belongs to.
- `type GroupListing struct`: GroupListing is one group a cluster knows.
- `type GroupMember struct`: GroupMember is one member of a described group.
- `type GroupDescription struct`: GroupDescription is the state of a group.
- `(c Client) CreateTopic(name str, partitions i64, replicas i64) !`: CreateTopic makes a topic. It fails with ErrTopicExists when there already is one.
- `(c Client) CreateTopics(specs []TopicSpec) !`: CreateTopics makes topics; the first failure fails the call (ErrTopicExists for one that exists).
- `(c Client) DeleteTopics(names []str) !`: DeleteTopics removes topics.
- `(c Client) ListTopics() ![]str`: ListTopics is the names of the cluster's topics (internal ones too).
- `(c Client) CreatePartitions(topic str, total i64) !`: CreatePartitions grows topic to total partitions.
- `(c Client) DeleteRecords(topic str, partition i64, before i64) !i64`: DeleteRecords deletes the records of the partition before offset; it returns the partition's new first offset. A leader that moved between the metadata and the request is asked again (NOT_LEADER), as Java's AdminClient does.
- `(c Client) ListGroups() ![]GroupListing`: ListGroups lists the groups of the whole cluster (each broker knows those it coordinates).
- `(c Client) DescribeGroup(group str) !GroupDescription`: DescribeGroup is the state, protocol and members of group.
- `(c Client) DeleteGroups(groups []str) !`: DeleteGroups removes empty groups and their committed offsets.
- `(c Client) DescribeConfigs(kind Resource, name str) ![]Config`: DescribeConfigs is the configuration of a topic or a broker (a broker by its node id).
- `(c Client) SetConfig(kind Resource, name str, key str, value str) !`: SetConfig sets one config of a topic or a broker (IncrementalAlterConfigs: the others stay).
- `(c Client) ResetConfig(kind Resource, name str, key str) !`: ResetConfig removes one config of a topic or a broker, back to its default.
- `(c Client) Close()`: Close closes this core's connections of the client; the next request connects again. Requests waiting on them fail, including one another task is waiting on (a held fetch).
- `type Want struct`: Want names a partition and the offset to read it from.
- `type Part struct`: Part is what a fetch learned about one partition.
- `type Fetched struct`: Fetched is the records of a FetchAll, in partition order, and what it learned of each partition.
- `(c Client) Fetch(topic str, partition i64, offset i64, maxWait i64) ![]Record`: Fetch reads records of topic's partition from offset on. It returns as soon as there are records, or empty after maxWait nanoseconds with none. At most Options.FetchMax bytes of whole record batches come back; a record before offset is skipped. They decompress to at most 64 times the larger of FetchMax and the bytes fetched: batches past that come in the next fetch, and one batch larger than it fails (raise FetchMax). An offset outside the partition fails with ErrOffsetOutOfRange.
- `(c Client) FetchAll(wants []Want, maxWait i64) !Fetched`: FetchAll reads several partitions at once: one request per leader broker, all sent before any is waited for when called inside a task. A partition whose offset is out of range is reported in Parts, not as a fault, and so is one that could not be read at all (no leader yet, the leader refused it): the records of the healthy partitions come back with them, and only the whole request failing (no broker, the request itself refused) fails the call.
- `(c Client) Offsets(topic str, partition i64) !(i64, i64)`: Offsets returns the first offset still in partition and the offset the next record will get.
- `(c Client) OffsetAt(topic str, partition i64, ts i64) !i64`: OffsetAt is the first offset whose record's timestamp is at or after ts (ms since the epoch), or -1 when every record is older.
- `type Assignor enum`: Assignor is how a group's leader spreads partitions over its members.
- `type Start enum`: Start is where a member starts reading a partition the group has no offset for.
- `type GroupOptions struct`: GroupOptions describe a member.
- `type Group struct`: Group is this core's member of a consumer group.
- `type TopicPartition struct`: TopicPartition names a partition and an offset (a position or a committed offset).
- `(c Client) Group(o GroupOptions) !Group`: Group makes this core's member of a consumer group. It joins on the first Poll. A core holds at most 256 members; Close frees the slot again.
- `(g Group) MemberID() str`: MemberID is the id the coordinator gave this member ("" before it joined).
- `(g Group) Generation() i64`: Generation is the group generation this member is in (-1 before it joined).
- `(g Group) Assigned() []TopicPartition`: Assigned is the member's partitions with the offset each will be read from next (-1 until known).
- `(g Group) Seek(topic str, partition i64, offset i64) !`: Seek makes the next Poll read the member's partition from offset.
- `(g Group) Heartbeat() !`: Heartbeat tells the coordinator the member is alive (Poll does it when due). A rebalance makes the next Poll rejoin.
- `(g Group) Poll(maxWait i64) ![]Record`: Poll returns the next records of the member's partitions, waiting up to maxWait (less when a heartbeat falls due). It joins the group first, rejoins after a rebalance or a change in its topics' partitions, heartbeats, and unless ManualCommit is set commits every CommitEvery.
- `(g Group) Commit() !`: Commit stores the member's positions (the offsets after the records Poll returned) as the group's committed offsets. A rebalance in the meantime fails it with ErrRebalance.
- `(g Group) CommitOffsets(parts []TopicPartition) !`: CommitOffsets stores the given offsets (each the next offset to read) for the group.
- `(g Group) Close() !`: Close commits (unless ManualCommit) and leaves the group, so its partitions move to the other members at once. A static member (InstanceID) does not leave: its session keeps its partitions for a restart. A harmless ErrRebalance from the commit (a rebalance is already on its way) is not reported as a failure, and the member's slot is free again (#444).
- `(c Client) Commit(group str, topic str, partition i64, offset i64) !`: Commit stores offset as group's position in the partition, without being a member (the "simple consumer" commit: generation -1). The offset is the next one to read.
- `(c Client) Committed(group str, topic str, partition i64) !i64`: Committed is the offset group last committed for the partition, or -1 when it has none.
- `type Mechanism enum`: Mechanism is the SASL mechanism used when Options.Username is set.
- `type Acks enum`: Acks says which replicas must have a record before Send returns.
- `type Options struct`: Options says where and how to connect, and how to produce and fetch. The idempotent producer (Options.NoIdempotence) is on by default with Acks.All; recording a request (TIN_REPLAY_DIR with TIN_REPLAY_KEY) turns it off for that request's sends, so the recorded effects depend on the request only (design/interface_replay.md, kafka@1).
- `type Client struct`: Client talks to one Kafka cluster. Open it in a global's initializer (which runs on every core) or once in main, not per request.
- `type Ack struct`: Ack says where Send put a record. Offset is -1 with Acks.NoAck, and when an idempotent retry found the batch already written.
- `Open(o Options) Client`: Open makes a client for the cluster in o. It connects on first use, on each core.
- `(c Client) Partitions(topic str) !i64`: Partitions is how many partitions topic has (asking the cluster). A topic created a moment ago may not be in every broker's metadata yet, so an unknown topic is asked about again for a little while (about two seconds) before the call fails with ErrUnknownTopic; so is one still being created, which has no partitions yet.
- `(c Client) Ping() !`: Ping checks that a broker answers.
- `(c Client) Send(topic str, m Message) !Ack`: Send appends one record to topic and returns where it went. A record with a key goes to the partition the key hashes to; one without goes to one partition per call, in turn.
- `(c Client) SendTo(topic str, partition i64, m Message) !Ack`: SendTo appends one record to a chosen partition of topic.
- `(c Client) SendBatchTo(topic str, partition i64, ms []Message) ![]Ack`: SendBatchTo appends records to a chosen partition of topic, in one batch with what other tasks of this core send there meanwhile.
- `(c Client) SendBatch(topic str, ms []Message) ![]Ack`: SendBatch appends records to topic and returns where each went, in order. Records of one partition go in one batch (with what other tasks of this core send meanwhile). A failed batch fails the call; records of other partitions may already be written.
- `type Message struct`: Message is one record to send.
- `type Header struct`: Header is a record header.
- `type Record struct`: Record is a record read from a partition.
- `type Compression enum`: Compression codecs, as the record batch attributes number them.
- `Murmur2(data str) i64`: Murmur2 is the hash Kafka's default partitioner uses for keys (Java's Utils.murmur2), so a key lands on the same partition here as from the Java client.
- `PartitionFor(key str, n i64) i64`: PartitionFor is the partition Kafka's default partitioner picks for key among n partitions; -1 when n is below 1.
- `EncodeBatch(ms []Message, now i64, c Compression) str`: EncodeBatch is ms as one record batch (format 2) compressed with c, the bytes Kafka stores and sends, with offsets counted from 0. A message whose Timestamp is 0 gets now (ms since the epoch).
- `DecodeBatches(data str) ![]Record`: DecodeBatches reads the record batches in data, as a Fetch response carries them, with any codec. A batch the data ends in the middle of is dropped; a damaged one, a changed byte (CRC-32C) or an old message format fails. Control batches (transaction markers) are skipped. All the batches together may decompress to at most 64 times the larger of 1 MiB and len(data).
- `type Txn struct`: Txn is this core's transactional producer for one transactional id. It serves one task at a time: a call made while another task's call is in progress fails with ErrTransaction (two sends to one partition at once would share a sequence, and the broker would drop one as a duplicate). After a send fails the transaction can only be aborted, since the broker may have written that send's records; Abort then starts the producer again with a new epoch.
- `(c Client) Transactional(txid str, timeout i64) !Txn`: Transactional makes this core's producer for transactional id txid (timeout: how long the broker lets a transaction stay open, default 60 s). It fences any older producer with the same id, and aborts what that one left open. Making it again for the same id (after fencing or a transaction timeout) replaces this core's producer of that id: older Txn values of it fail. A core holds at most 64; Close frees one.
- `(t Txn) Close()`: Close frees this core's slot of the producer. A transaction still open is left to the broker, which aborts it at its timeout or when the id is used again.
- `(t Txn) Begin() !`: Begin starts a transaction.
- `(t Txn) Send(topic str, m Message) !Ack`: Send writes one record in the open transaction.
- `(t Txn) SendBatch(topic str, ms []Message) ![]Ack`: SendBatch writes records in the open transaction, one batch per partition; readers with ReadCommitted see them only once the transaction commits.
- `(t Txn) SendOffsets(group str, offsets []TopicPartition) !`: SendOffsets commits a consumer group's offsets as part of the open transaction (consume-transform-produce): they become the group's committed offsets only if the transaction commits.
- `(t Txn) Commit() !`: Commit commits the open transaction: its records become visible to ReadCommitted readers and its offsets the group's. After a failed send it fails: only Abort is left.
- `(t Txn) Abort() !`: Abort discards the open transaction. After a failed send it starts the producer again (InitProducerId: the coordinator aborts the transaction and gives a new epoch, and every partition's sequence starts over), as Java does (KIP-360): records the broker may have written for the failed send cannot make a later send look like their duplicate.

## websocket

Package websocket is the WebSocket protocol (RFC 6455): Accept upgrades an anvil request, Dial connects to a server (ws://, or wss:// over TLS 1.3). Messages are text or binary; pings are answered and fragments joined inside Read. Inside a request task a Read waits without blocking the core, so one core holds many idle connections.

```tin
fn handle(q anvil.Req, w mut anvil.Out) {
	let ws = websocket.Accept(q, mut w) catch _ { return }
	ws.Each(echo) catch _ {}
}

fn echo(ws websocket.Conn, m websocket.Message) ! {
	try ws.WriteText("echo: {m.Data}")
}
```

- `type Message struct`: Message is one complete message.
- `type Conn struct`: Conn is a WebSocket connection.
- `Accept(q anvil.Req, w mut anvil.Out) !Conn`: Accept completes the opening handshake for request q and takes over its connection. A request that is not a WebSocket handshake gets a 400 (426 for another version) in w and fails. The connection and its buffers close when the handler returns.
- `Dial(url str) !Conn`: Dial connects to a ws:// or wss:// URL ("ws://host:port/path"); wss:// verifies the server's certificate against the system's roots. Close it when finished; inside a request task, it is also closed automatically when its scope ends.
- `DialTLS(url str, cfg tls.Config) !Conn`: DialTLS is Dial with the TLS configuration of a wss:// URL (RootCAs, Timeout for the handshake, InsecureSkipVerify for tests); the server name is the URL's host, and ALPN offers http/1.1 whatever cfg.ALPN says (the upgrade is HTTP/1.1).
- `(c Conn) SetTimeout(ns i64)`: SetTimeout limits every later read and write to ns nanoseconds (0: no limit).
- `(c Conn) SetMaxMessage(n i64)`: SetMaxMessage sets the largest message Read accepts (default 16 MiB); a bigger one closes the connection with 1009.
- `(c Conn) WriteText(s str) !`: WriteText sends s as a text message.
- `(c Conn) WriteBinary(b []u8) !`: WriteBinary sends b as a binary message.
- `(c Conn) Ping() !`: Ping sends a ping; the peer's pong is consumed by Read.
- `(c Conn) CloseWith(code i64, reason str) !`: CloseWith sends a close frame with code and reason; the connection then only drains.
- `(c Conn) Close()`: Close sends a normal close (1000) and, for a client, closes the connection.
- `IsClosed(err fault) bool`: IsClosed reports whether err is the normal end of a connection: the peer closed it.
- `(c Conn) Read() !Message`: Read returns the next message; it answers pings and joins fragments on the way. When the peer closes, it answers the close and fails with "websocket: closed (code)". The returned message lives in the caller's pool. For a long-lived stream, use Each to reset message allocations after every callback without invalidating the Conn.
- `(c Conn) Each(h fn(Conn, Message) !) !`: Each reads messages and calls h until a read or callback fails. Every callback has a reusable message pool: use keep() to retain its data after the callback returns. The Conn and all objects allocated before Each remain valid. Callbacks may wait. A closed peer returns the same IsClosed fault as Read; callback faults propagate.

## s3

Package s3 is a client for S3-compatible object stores (AWS S3, Cloudflare R2, MinIO) over wire's HTTP client, signed with AWS Signature Version 4.

Bodies are streamed: Put sends a file from its descriptor (pread into wire's 64 KiB send buffer), GetFile and GetTo write the answer as it arrives, and Upload sends a large file as a multipart upload, one part at a time, so a file of any size moves in the memory of a few buffers. Over https a streamed body is signed UNSIGNED-PAYLOAD (TLS keeps it whole); over http (unless Config.UnsignedPayload), or with Config.SignPayload, each body is hashed first, which reads it twice.

```tin body
let c = try s3.New(s3.Config{Endpoint: "http://127.0.0.1:9000", Region: "us-east-1", AccessKey: "minio", SecretKey: "minio-secret", PathStyle: true})
let etag = try c.Put("packs", "repos/7/packs/ab12.pack", "/tmp/ab12.pack")
let part = try c.GetRange("packs", "repos/7/packs/ab12.pack", 4096, 512)
let info = try c.Head("packs", "repos/7/packs/ab12.pack")
```

Calls that may be repeated (GET, HEAD, PUT, DELETE) are tried again, through policy.Retry, after a connection error or a 408, 429, 500, 502, 503 (SlowDown) or 504 answer; a POST (creating and completing a multipart upload) only after such an answer, never after a lost connection, and a body read from a caller's reader never. A missing object fails with a fault that matches ErrNotFound; any other S3 error answer matches ErrService, and its message holds the Code and Message S3 gave (ErrorCode reads the code back).

Addressing is virtual-hosted (bucket.host/key) unless Config.PathStyle (host/bucket/key), which MinIO and most local servers want. A bucket name with dots cannot be used virtual-hosted over https (the certificate names one level). Keys whose characters XML 1.0 cannot hold (most control characters) cannot be listed.

- `(r mut region) Read(buf mut []u8) !i64`: Read fills buf with the region's next bytes: 0 at its end. A file that shrank fails.
- `(c mut collect) Begin(h wire.Head) !`: Begin keeps the answer's status and fields.
- `(c mut collect) Write(data []u8) !i64`: Write keeps data, refusing an answer longer than most bytes.
- `(f mut fileSink) Begin(h wire.Head) !`: Begin creates the file for a successful answer.
- `(f mut fileSink) Write(data []u8) !i64`: Write appends data to the file, or to the error kept in memory.
- `(g mut gate[W]) Begin(h wire.Head) !`: Begin opens the gate for a successful answer.
- `(g mut gate[W]) Write(data []u8) !i64`: Write passes data on to w, or keeps an error answer.
- `type Config struct`: Config says where the store is and how to sign for it.
- `type Client struct`: Client makes requests to one store; it holds no connections (wire keeps them per core).
- `type Object struct`: Object is what S3 says about an object: in a list, or from Head.
- `type ListOptions struct`: ListOptions select the objects List gives.
- `type ListResult struct`: ListResult is one page of a list.
- `type Part struct`: Part is one uploaded part of a multipart upload: its number (from 1) and ETag.
- `const MinPartSize = 5242880`: MinPartSize is the smallest part S3 takes (but for the last): 5 MiB.
- `const MaxParts = 10000`: MaxParts is the most parts one upload may have.
- `const DefaultPartSize = 16777216`: DefaultPartSize is Upload's part size when it is given 0: 16 MiB.
- `New(cfg Config) !Client`: New checks cfg and makes a client.
- `ErrorCode(err fault) str`: ErrorCode is the S3 error code in err's chain ("NoSuchKey", "SlowDown", "NotFound" for a HEAD's 404, "HTTP502" for an answer without an XML error), or "" when err is no S3 answer.
- `(c Client) Put(bucket str, key str, path str) !str`: Put uploads the file at path as the object key in one request, streamed from the file. A file over 5 GiB needs Upload. It gives the object's ETag.
- `(c Client) PutBytes(bucket str, key str, data str) !str`: PutBytes uploads data as the object key and gives its ETag.
- `PutReader[R io.Reader](c Client, bucket str, key str, src R, size i64) !str`: PutReader uploads size bytes read from src as the object key, streamed, and gives its ETag. The body cannot be read again, so the call is never tried twice, and it cannot be hashed first: it is signed UNSIGNED-PAYLOAD whatever the scheme.
- `(c Client) GetBytes(bucket str, key str, maxBytes i64) !str`: GetBytes gives the whole object key; at most maxBytes of it (a larger one fails).
- `(c Client) GetRange(bucket str, key str, off i64, n i64) !str`: GetRange gives n bytes of the object key from offset off: fewer at the object's end.
- `(c Client) GetFile(bucket str, key str, path str) !i64`: GetFile writes the object key to a file at path, as it arrives (through a temporary file next to it, renamed when the whole object is in), and gives its size.
- `GetTo[W io.Writer](c Client, bucket str, key str, w mut W) !i64`: GetTo writes the object key to w as it arrives and gives how many bytes it wrote. A try is repeated only when nothing reached w yet. w must be a struct (a reference): a value struct would be written as a copy.
- `GetRangeTo[W io.Writer](c Client, bucket str, key str, off i64, n i64, w mut W) !i64`: GetRangeTo writes n bytes of the object key from offset off to w (n < 0: to its end).
- `(c Client) Head(bucket str, key str) !Object`: Head describes the object key; a missing one fails with ErrNotFound.
- `(c Client) Delete(bucket str, key str) !`: Delete removes the object key; removing one that does not exist is not a fault (S3 says so).
- `(c Client) List(bucket str, opt ListOptions) !ListResult`: List gives one page of the bucket's objects (ListObjectsV2).
- `(c Client) ListAll(bucket str, prefix str) ![]Object`: ListAll gives every object whose key starts with prefix, reading page after page.
- `(c Client) CreateBucket(bucket str) !`: CreateBucket makes a bucket (in Config.Region: AWS wants it named outside us-east-1).
- `(c Client) CreateMultipart(bucket str, key str) !str`: CreateMultipart starts a multipart upload of the object key and gives its upload id.
- `(c Client) UploadPart(bucket str, key str, id str, number i64, path str, off i64, n i64) !str`: UploadPart sends bytes [off, off+n) of the file at path as part number (1 to 10000) of the upload id, streamed from the file, and gives the part's ETag.
- `(c Client) CompleteMultipart(bucket str, key str, id str, parts []Part) !str`: CompleteMultipart joins the parts (in number order) into the object and gives its ETag.
- `(c Client) AbortMultipart(bucket str, key str, id str) !`: AbortMultipart stops the upload id and drops its parts.
- `(c Client) Upload(bucket str, key str, path str, partSize i64) !str`: Upload sends the file at path as the object key in parts of partSize bytes (0: DefaultPartSize; raised to MinPartSize, and as needed to stay within MaxParts), one after the other, each streamed from the file: memory stays at a few buffers whatever the size. A file of at most one part goes as a plain Put. A failed upload is aborted. It gives the ETag.
- `(c Client) Presign(method str, bucket str, key str, expires i64) !str`: Presign is a URL that lets anyone holding it make one method call ("GET", "PUT") on the object key, without credentials, for expires (ns, from 1 s to 7 days) from now.
- `(c Client) PresignAt(method str, bucket str, key str, expires i64, unix i64) !str`: PresignAt is Presign signed at the instant unix (seconds): for tests and for URLs made ahead.
- `const UnsignedPayload = "UNSIGNED-PAYLOAD"`: UnsignedPayload is the x-amz-content-sha256 value of a body that is not hashed: S3 then trusts the transport (TLS) for the body's integrity.
- `const EmptyHash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"`: EmptyHash is the SHA-256 of an empty body, in hex.
- `type Request struct`: Request is one HTTP request to sign. Path is the URI path as it goes on the wire, already escaped (EscapePath); Query and Headers are name, value pairs, the query's unescaped.
- `type Signed struct`: Signed is a signed request: the fields to add to its headers (X-Amz-Date, the session token and Authorization, as name, value pairs) and its query string, escaped and in order.
- `EscapePath(s str) str`: EscapePath escapes an object key (or a whole path) for a URL path the way S3 signs it: every byte except A-Z a-z 0-9 - . _ ~ and / becomes %XX.
- `EscapeQuery(s str) str`: EscapeQuery escapes a query parameter's name or value for a signed query: every byte except A-Z a-z 0-9 - . _ ~ becomes %XX (a space is %20, never +).
- `SignRequest(cfg Config, service str, r Request, unix i64) Signed`: SignRequest signs r with the credentials and region of cfg for service ("s3") at the instant unix (seconds): the X-Amz-Date, X-Amz-Security-Token (with a session token) and Authorization fields to send with r, and r's query in its signed form.
- `PresignRequest(cfg Config, service str, r Request, expires i64, unix i64) str`: PresignRequest signs r in its query (a presigned URL) for expires seconds from unix and gives the query string to put after "?": r's parameters, the X-Amz-* ones and X-Amz-Signature last. Headers in r are signed as they are (none are moved to the query).

## atomic

Package atomic has counters and flags that every core may change at once. Keep one in a `shared let` (a value every core reads, built once before the cores start), as in `shared let hits = atomic.NewInt(0)`, and call `hits.Add(1)` from any core; the operations are indivisible and ordered (sequentially consistent) across the whole process. A value made anywhere else (in a handler, in a per-core global) lives in one core's memory and must not be shared. Integers and flags only: build anything bigger with relay messages or per-core state.

- `type Int struct`: Int is an integer that cores read and change with indivisible operations.
- `NewInt(v i64) Int`: NewInt returns an Int holding v.
- `(c Int) Load() i64`: Load returns the value.
- `(c Int) Store(v i64)`: Store sets the value to v.
- `(c Int) Add(n i64) i64`: Add adds n (negative to subtract) and returns the new value.
- `(c Int) Swap(v i64) i64`: Swap sets the value to v and returns the one it replaced.
- `(c Int) CompareSwap(old i64, next i64) bool`: CompareSwap sets the value to next if it is old, and reports whether it did.
- `type Bool struct`: Bool is a flag that cores read and change with indivisible operations.
- `NewBool(v bool) Bool`: NewBool returns a Bool holding v.
- `(c Bool) Load() bool`: Load returns the flag.
- `(c Bool) Store(v bool)`: Store sets the flag to v.
- `(c Bool) Swap(v bool) bool`: Swap sets the flag to v and returns the value it replaced.
- `(c Bool) CompareSwap(old bool, next bool) bool`: CompareSwap sets the flag to next if it is old, and reports whether it did.

## lane

Package lane is a bounded queue between the tasks of one core (Go's buffered channel): lane.New[T](n) makes one that holds n values, Send waits while it is full and Recv while it is empty, and both take the task's deadline and cancellation like any other wait. Close ends it: senders fail at once and receivers drain what is left, then fail with ErrClosed. In main (outside a task) a wait runs the core's other tasks until it can go on. Ready, Watch and Unwatch are what select uses. A lane never crosses cores: relay does that.

A worker ends its loop when the lane is closed and drained, and on nothing else: its loop is `let j = jobs.Recv() catch err { if fault.Is(err, lane.ErrClosed) { return }  fail err }`, or `let (j, ok) = try jobs.RecvOk()` and `if !ok { return }`. A deadline or a cancellation is still fault.DeadlineExceeded or fault.Canceled.

- `type Lane[T constraints.Any] struct`: Lane is a bounded queue between tasks on one core (design_semantics §6, #232). Send waits while it is full and Recv while it is empty; Close wakes every waiter. Waits take the task's deadline and cancellation like any other wait. A lane never crosses cores (relay does).
- `New[T constraints.Any](capacity i64) Lane[T]`: New makes a lane that holds at most capacity values (at least one).
- `(l mut Lane[T]) Send(v T) !`: Send puts v at the back, waiting while the lane is full; it fails with ErrClosed once the lane is closed.
- `(l mut Lane[T]) TrySend(v T) bool`: TrySend puts v at the back if there is room and reports whether it did.
- `(l mut Lane[T]) Recv() !T`: Recv takes the value at the front, waiting while the lane is empty; it fails with ErrClosed once the lane is closed and empty.
- `(l mut Lane[T]) RecvOk() !(T, bool)`: RecvOk is Recv with Go's v, ok := <-ch: ok is false (and v the zero value) once the lane is closed and empty, and only a deadline or a cancellation is a fault.
- `(l mut Lane[T]) Close()`: Close ends the lane: senders fail, receivers drain what is left and then fail.
- `(l Lane[T]) Ready() bool`: Ready reports whether Recv would not wait: a value is there or the lane is closed (select).
- `(l mut Lane[T]) Watch()`: Watch makes the next value or Close wake the running task without taking a value (select).
- `(l mut Lane[T]) Unwatch()`: Unwatch withdraws Watch.
- `(l Lane[T]) Len() i64`: Len is how many values wait in the lane.

## replay

Capsule envelope version 2 (design/interface_replay.md section 6.1; #1004): a fresh data key per capsule, wrapped for each reader (HPKE X25519 and an ML-KEM-768 mask, so a reader's key holds while either does), a plain summary, and the server's ed25519 signature. Version 1 (one symmetric TIN_REPLAY_KEY) stays readable.

- `type Recipient struct`: Recipient is a reader a version 2 capsule is sealed for: its key id (SHA-256 of its public key's bytes), its X25519 public key and its ML-KEM-768 encapsulation key.
- `type Identity struct`: Identity is a reader's private key: its key id, its X25519 private key and its ML-KEM-768 decapsulation key.
- `NewIdentity() !(str, str)`: NewIdentity makes a reader's key pair: the private key's text (for a file of mode 0600, TIN_REPLAY_IDENTITY) and the public key's text (for a server's TIN_REPLAY_RECIPIENTS).
- `ParseIdentity(text str) !Identity`: ParseIdentity reads a reader's private key from its text (surrounding space is ignored).
- `ParseRecipient(text str) !Recipient`: ParseRecipient reads a reader's public key from its text.
- `ParseRecipients(listText str) ![]Recipient`: ParseRecipients reads a comma list of readers' public keys (TIN_REPLAY_RECIPIENTS): one to 64 of them.
- `SealV2(body str, ks str, summary str, readers []Recipient, signSeed str) !str`: SealV2 is the version 2 envelope of a capsule body for readers, signed with the ed25519 seed signSeed; ks is the secret handles' key (section 5.1, carried so a reader replays with the same handles) and summary the plain summary.
- `Version(data str) i64`: Version is a capsule's envelope version (1 or 2), 0 when it is not a capsule.
- `Summary(data str) !(str, str)`: Summary is a version 2 capsule's signer (its ed25519 public key, hex) and plain summary, read without a key; the signature is checked against the signer the capsule names (a forger can only name their own key).
- `UnsealV2(data str, id Identity, signers []str) !(str, str)`: UnsealV2 opens a version 2 capsule for identity, trusting the signers listed (ed25519 public keys, hex): the secret handles' key and the body. It checks, in order, the signer, the signature, that the capsule is sealed for identity, and the tag; only then is the body decrypted.
- `type Capsule struct`: Capsule is a decoded capsule: one recorded request and its effect records.
- `const Kinds = ",sched.select@1,sched.resume@1,sched.cancel@1,tide.now@1,tide.wall@1,dice.seed@1,seal.random@1,wire.http@1,wire.dial@1,wire.read@1,wire.write@1,redis@1,kafka@1,mysql@1,mysql.tx@1,postgres@1,postgres.tx@1,websocket.dial@1,websocket.read@1,websocket.write@1,quarry.read@1,quarry.write@1,quarry.stat@1,quarry.dir@1,quarry.fs@1,"`: Kinds lists the effect kinds (name@version) this build replays (section 4); a capsule with any other kind is refused. The sched.* kinds are the request's scheduling (section 7, #243).
- `Open(path str, keyHex str) !Capsule`: Open reads the capsule at path: a version 1 capsule encrypted under keyHex (the 64 hex digits of TIN_REPLAY_KEY), or a version 2 capsule (section 6.1) opened with the private key in the file TIN_REPLAY_IDENTITY names and checked against the signers TIN_REPLAY_SIGNERS lists. A version 2 capsule's secret handles' key is installed for the replay.
- `Key(keyHex str) !str`: Key is the 32 bytes a TIN_REPLAY_KEY value (64 hex digits) stands for.
- `Unseal(data str, key str) !str`: Unseal checks a capsule envelope's tag under key and returns its decrypted body.
- `Decode(body str) !Capsule`: Decode reads a capsule body (schema 1 or 2) and checks every effect record and its kind.
- `Supported(kind str) bool`: Supported reports whether this build replays effect kind (name@version).
- `Setup(cores i64) bool`: Setup reads the switches (TIN_REPLAY_DIR, TIN_REPLAY_KEY, TIN_REPLAY_SAMPLE, TIN_REPLAY_MAX_MB, TIN_REPLAY_SECRET_HEADERS, TIN_REPLAY_DROP_HEADERS) for a server on n cores, trims the spool and installs the keyed hash of secrets; it reports whether recording is on (never while TIN_REPLAY_CAPSULE replays a capsule). Call it before the cores start. A missing or malformed key, or a spool that cannot be made, prints one line on stderr and leaves recording off.
- `On() bool`: On reports whether Setup turned recording on.
- `Secret(s str) str`: Secret is the handle an effect key or a stored header holds instead of a secret's text: "tin-secret:" and the first 16 bytes of HMAC-SHA256(Ks, s) in hex (section 5.1).
- `Wanted(status i64, panicked bool) i64`: Wanted is the flags a capsule of a request that ended with status is kept with (1 panicked, 2 sampled), or -1 when it is dropped: kept when the status is 500 or more, or it panicked, or it is in the TIN_REPLAY_SAMPLE fraction.
- `Done(tp i64, core i64)`: Done ends the recording tape tp of a request served on core: its capsule is written when the request is kept (Wanted), and the tape is freed. A capsule that cannot be written prints one line on stderr; the server goes on.
- `Write(tp i64, core i64, flags i64) !str`: Write writes the capsule of tape tp (recorded on core, with flags) into the spool, deleting the core's oldest capsules past its share of TIN_REPLAY_MAX_MB; it returns the capsule's path.
- `Encode(tp i64, core i64, flags i64) str`: Encode is the capsule body of tape tp (section 6): the request with its secret headers as handles and its dropped headers empty, the panic, the peer, and the effect records.
- `Seal(body str) str`: Seal is the envelope of a capsule body (section 6): the magic, a random nonce, the body under the HMAC-SHA256 keystream, and the tag over all of it.
- `Scrub(req str) str`: Scrub is a request as a capsule stores it: the values of secret headers (section 1) become their handles and the values of dropped headers become empty; everything else is kept.

## stencil

Package stencil renders templates loaded at run time, like Go's text/template over a dynamic value tree: {{.user.name}}, {{if}}, {{range}}, {{with}}, pipelines with the builtins (len, index, slice, eq, ne, lt, le, gt, ge, and, or, not, printf, print, println, html, urlquery, js), {{define}}, {{template}} and {{block}}, and user functions registered with Func. Parse errors carry line and column; execution is bounded by a template recursion limit and a maximum output size. ParseHTML renders in HTML mode instead: an action's escaping follows its context in the surrounding markup (element text, attribute values, URL attributes and JavaScript inside <script>), and a context the mode cannot judge is a parse error rather than a guess.

URL attributes (href, src, action, formaction, poster, background) are escaped by position, as Go's html/template does: at the start the scheme is filtered (only http, https, mailto and relative URLs pass, else #ZgotmplZ) and the value is percent-encoded where it leaves the URL grammar; after the start it is percent-encoded the same way; after a "?" or "#" every byte outside the unreserved set is percent-encoded, so a value cannot add query parameters. Hex digits are lower case, then the value is HTML-escaped.

Execute keeps the data and the variables in a cell bound to a runtime slot (the pattern policy.Bind uses), so the stores happen inside the runtime.

- `ParseContextual(name str, text str) !Template`: ParseContextual parses text into a Template whose actions are escaped by their context, as Go's html/template does. A context the mode does not support is a parse error (see the file's comment).
- `type State struct`: State is one execution of a template.
- `type Node enum`: Node is one piece of a parsed template.
- `type Branch struct`: Branch is if/with: the condition, the body and the else branch.
- `type RangeNode struct`: RangeNode is range: the optional variables, the pipeline, the body and the else branch.
- `type TemplateCall struct`: TemplateCall is {{template "name" pipe}}; the pipe may be absent.
- `type Pipe struct`: Pipe is a pipeline: commands joined by |.
- `type Cmd struct`: Cmd is one command: its operands.
- `type Arg enum`: Arg is one operand of a command.
- `ParseHTML(name str, text str) !Template`: ParseHTML parses text into a Template whose actions are escaped by their HTML context, as Go's html/template does; a context the mode does not support is a parse error. A {{template}} call renders its own template in element text, so a called template cannot open a tag.
- `Parse(name str, text str) !Template`: Parse parses text into a Template; errors carry name, line and column.
- `type Parser struct`: Parser walks text.
- `type Value struct`: Value is the data a template renders: a tree of strings, numbers, booleans, lists and maps.
- `const KindNone = 0`: The kinds of a Value.
- `const KindStr = 1`
- `const KindInt = 2`
- `const KindFloat = 3`
- `const KindBool = 4`
- `const KindList = 5`
- `const KindMap = 6`
- `None() Value`: None returns the absent value (a missing map key), printed as Go prints it.
- `Str(s str) Value`: Str returns a string value.
- `Int(n i64) Value`: Int returns an integer value.
- `Float(f f64) Value`: Float returns a floating-point value.
- `Bool(b bool) Value`: Bool returns a boolean value.
- `List(xs []Value) Value`: List returns a list value.
- `Map(m map[str]Value) Value`: Map returns a map value; the keys are strings, as {{.name}} looks them up.
- `const TrustNone = 0`: The trusted kinds of a string value: the contextual escapers pass a value of its own kind through, as Go's html/template does for template.HTML, template.JS, template.JSStr, template.CSS and template.URL.
- `const TrustHTML = 1`: TrustHTML marks HTML that is already escaped or markup (template.HTML).
- `const TrustJS = 2`: TrustJS marks a JavaScript expression (template.JS).
- `const TrustJSStr = 3`: TrustJSStr marks text that is already escaped for a JavaScript string (template.JSStr).
- `const TrustCSS = 4`: TrustCSS marks a CSS declaration value (template.CSS).
- `const TrustURL = 5`: TrustURL marks a URL (template.URL).
- `Trusted(t i64, s str) Value`: Trusted returns the string s, of the trusted kind t (a Trust constant), which the contextual escapers pass through in that context. Only Go code makes one: template data from outside the program is never trusted.
- `(v Value) Trust() i64`: Trust returns the trusted kind of a value (a Trust constant), or TrustNone for an ordinary value.
- `(v Value) Kind() i64`: Kind returns the value's kind (one of the Kind constants), for code that inspects data.
- `(v Value) String() str`: String returns the string of a string value.
- `(v Value) Integer() i64`: Integer returns the integer of an integer value.
- `(v Value) Real() f64`: Real returns the float of a floating-point value.
- `(v Value) Boolean() bool`: Boolean returns the boolean of a boolean value.
- `(v Value) Items() []Value`: Items returns the elements of a list value.
- `(v Value) Entries() map[str]Value`: Entries returns the map of a map value.
- `type Template struct`: Template is a parsed template.
- `(t mut Template) Func(name str, f fn([]Value) !Value)`: Func registers f for {{name ...}} calls in this template.
- `(t Template) Execute(data Value) !str`: Execute renders the template with data and returns the output.
- `(t Template) ExecuteTo(w mut twine.Builder, data Value) !`: ExecuteTo renders the template with data into w. The data and the variables live in a cell bound to a runtime slot for the call (the pattern policy.Bind uses).

## htmltpl

- `type Template struct`: Template is a template in the html/template style: a name, the functions registered for it, and its parsed body.
- `New(name str) Template`: New returns an empty template named name, as Go's template.New does; Parse gives it a body.
- `(t Template) Name() str`: Name returns the template's name.
- `(t mut Template) Funcs(funcs map[str]fn([]stencil.Value) !stencil.Value)`: Funcs registers functions for {{name ...}} calls in the template's text; it must be called before Parse, as in Go.
- `(t mut Template) Parse(text str) !`: Parse parses text as the template's body, escaped by context. A later Parse replaces the body. A context the mode does not support is an error (see README.md).
- `(t Template) Execute(w mut twine.Builder, data stencil.Value) !`: Execute writes the template's output for data into w, escaped by context.
- `(t Template) ExecuteString(data stencil.Value) !str`: ExecuteString returns the template's output for data as a string.
- `HTML(s str) stencil.Value`: HTML marks s as HTML that the escapers pass through in element text and RCDATA (template.HTML).
- `JS(s str) stencil.Value`: JS marks s as a JavaScript expression that a <script> or an event attribute passes through (template.JS).
- `JSStr(s str) stencil.Value`: JSStr marks s as text already escaped for a JavaScript string literal (template.JSStr).
- `CSS(s str) stencil.Value`: CSS marks s as a CSS value that a <style> element or a style attribute passes through (template.CSS).
- `URL(s str) stencil.Value`: URL marks s as a URL that the URL escaper passes through without filtering its scheme (template.URL).

## column

Package column aligns tabbed columns in text, like Go's text/tabwriter: the elastic tabstops algorithm.

The writer treats its input as cells terminated by a horizontal ('\t') or vertical ('\v') tab and lines broken by a newline ('\n') or form feed ('\f'). Tab-terminated cells in contiguous lines form a column, and the writer pads the cells so that every cell of a column has the same width:

```tin body
let text = try column.Format("a\tbb\tc\nlonger\tb\tdd\n", 0, 8, 1, ' ', 0)
// text is "a      bb c\nlonger b  dd\n"
```

NewWriter streams instead, into anything with Write (mut dyn io.Writer).

A form feed acts like a newline and also ends every column block (a flush). Columns ended entirely by vertical tabs are dropped when DiscardEmptyColumns is set. With FilterHTML, HTML tags are zero width and entities one; with tab padding (padchar '\t') cells are left-aligned, as Go's tabwriter has it.

- `const FilterHTML = 1`: The flags, as Go's tabwriter: FilterHTML ignores HTML tags and treats entities as one rune, StripEscape strips the Escape characters of escaped segments, AlignRight right-aligns cells, DiscardEmptyColumns drops columns that hold only empty cells ended by vertical tabs, TabIndent pads leading empty cells with tabs, and Debug writes a '|' between columns and a "---" line after a form feed.
- `const StripEscape = 2`
- `const AlignRight = 4`
- `const DiscardEmptyColumns = 8`
- `const TabIndent = 16`
- `const Debug = 32`
- `const Escape = 0xff`: Escape brackets an escaped segment: text between two of them is passed through and counts one rune per byte for the column width. 0xff cannot appear in valid UTF-8, which is why Go chose it.
- `type Writer struct`: Writer inserts padding around tab-terminated columns in what is written to it, and sends the result to put.
- `NewWriter(put dyn io.Writer, minwidth i64, tabwidth i64, padding i64, padchar u8, flags i64) !Writer`: NewWriter returns a writer that pads cells to at least minwidth (plus padding), counts a tab as tabwidth columns, uses padchar for the padding, and follows the flags. Negative minwidth, tabwidth or padding fail.
- `type StrSink struct`: StrSink collects what is written to it, for Format and for tests.
- `(s mut StrSink) Write(data []u8) !i64`: Write appends data to the sink.
- `Format(s str, minwidth i64, tabwidth i64, padding i64, padchar u8, flags i64) !str`: Format aligns the columns of s with the same parameters as NewWriter and returns the result: the common one-shot use.
- `(w mut Writer) Flush() !`: Flush writes the buffered text, padding the columns; an incomplete escape at the end counts as complete.
- `(w mut Writer) Write(buf []u8) !i64`: Write buffers the cells and lines of buf: tabs and vertical tabs end a cell, newlines and form feeds end a line (and a form feed flushes), and a line with a single cell is flushed at once since it cannot affect the following lines.

## scroll

Package scroll is a safe, streaming XML tokenizer and writer, like Go's encoding/xml without reflection: no DTD processing and no external entities, by design, so XXE and billion-laughs attacks cannot happen. Entities are the five predefined names and numeric references; anything else is an error. The tokenizer resolves namespaces into Name.Space and bounds nesting, the attribute count and the token size (fault.LimitExceeded). Writer writes tokens or direct calls with text and attribute escaping and optional indentation; the Go twin (bench/ref/scroll and tools/ci/scroll_check.tin) compares the token streams with encoding/xml over an RSS, SOAP, S3 and SVG corpus.

- `type Token enum`: Token is one piece of an XML document.
- `type Name struct`: Name is a name with its namespace: space is the URI the prefix resolved to, empty when there is none; local is the part after the prefix.
- `type Attr struct`: Attr is one attribute.
- `type Decoder struct`: Decoder reads a document token by token.
- `NewDecoder(text str) Decoder`: NewDecoder returns a decoder over text in strict mode: matching end tags, a single root, valid names, unique attributes and valid characters are enforced.
- `NewLenientDecoder(text str) Decoder`: NewLenientDecoder is NewDecoder without the well-formedness checks.
- `(d mut Decoder) LimitDepth(n i64)`: LimitDepth lowers (or raises) the nesting limit; tests use it to keep documents small.
- `(d mut Decoder) LimitAttrs(n i64)`: LimitAttrs sets the attribute-count limit.
- `(d mut Decoder) LimitToken(n i64)`: LimitToken sets the token-size limit.
- `(d mut Decoder) Next() !Token`: Next returns the next token, or Done at the end of the document.
- `type Writer struct`: Writer writes XML.
- `NewWriter() Writer`: NewWriter returns a writer with no indentation.
- `NewWriterIndent(unit str) Writer`: NewWriterIndent returns a writer that indents each element by unit (for example "  ").
- `(w Writer) String() str`: String returns what has been written.
- `(w mut Writer) Reset()`: Reset empties the writer.
- `(w mut Writer) EscapeText(s str)`: EscapeText writes s as element text: &, <, > and \r are escaped.
- `(w mut Writer) EscapeAttr(s str)`: EscapeAttr writes s as an attribute value: &, <, >, ", ' and the whitespace characters are escaped.
- `(w mut Writer) Start(name str, attrs []Attr) !`: Start writes a start tag with its attributes.
- `(w mut Writer) End(name str) !`: End writes an end tag, which must match the innermost open element.
- `(w mut Writer) Element(name str, text str) !`: Element writes a whole element with escaped text content.
- `(w mut Writer) Text(s str)`: Text writes escaped character data.
- `(w mut Writer) Comment(s str) !`: Comment writes a comment; a comment may not contain "--".
- `(w mut Writer) ProcInst(target str, inst str) !`: ProcInst writes a processing instruction.
- `(w mut Writer) Directive(s str)`: Directive writes a directive such as a doctype, passed through unchanged.
- `(w mut Writer) WriteToken(t Token) !`: WriteToken writes one token, which must nest correctly.

## html

Package html tokenizes, parses and escapes HTML, as Go's html and golang.org/x/net/html do: EscapeString and UnescapeString for text and attribute values; a Tokenizer that splits a document into text, tags, attributes, comments and doctypes with the WHATWG tokenization rules (raw text in script, style, textarea, title and the other raw elements; bogus comments; the legacy references without a semicolon); and Parse, which builds the document tree with the tree-construction rules (implicit closes, the adoption agency, tables, select, svg and math content). Parse does not support the template and frameset modes. The tokenizer reads a whole string, so its tokens are the same as Go's over a reader. The Go twins (bench/ref/html and tools/ci/html_check.tin) compare the token streams and the trees over a corpus of pages and generated documents.

- `EscapeString(s str) str`: EscapeString escapes the characters <, >, &, ' and " and a carriage return to references, as Go's html.EscapeString does.
- `UnescapeString(s str) str`: UnescapeString replaces the character references in s with the characters they stand for, as Go's html.UnescapeString does.
- `const ErrorToken = 0`: ErrorToken means that the input has ended (or failed): Err says why.
- `const TextToken = 1`: TextToken is a run of text.
- `const StartTagToken = 2`: StartTagToken is a start tag, like <a>.
- `const EndTagToken = 3`: EndTagToken is an end tag, like </a>.
- `const SelfClosingTagToken = 4`: SelfClosingTagToken is a tag written with a trailing slash, like <br/>.
- `const CommentToken = 5`: CommentToken is a comment, a bogus comment, a processing instruction or an empty "</>".
- `const DoctypeToken = 6`: DoctypeToken is a <!DOCTYPE ...> declaration.
- `type Attribute struct`: Attribute is one attribute of a tag: Namespace is always empty (it is for the parser), Key is lower-cased and Val is unescaped.
- `type Token struct`: Token is one token: Data is the tag name (lower-cased), the text, the comment or the doctype, unescaped; Attr holds the attributes of a tag.
- `Parse(text str) !Document`: Parse builds the tree of an HTML document, as Go's html.Parse does (scripting enabled; the template and frameset modes are not supported). A tree that the tree builder cannot make, such as one nested more than 512 elements deep, is a fault.
- `type Tokenizer struct`: Tokenizer returns the tokens of an HTML document, one Next call at a time, as Go's Tokenizer does. The text is read in full.
- `NewTokenizer(text str) Tokenizer`: NewTokenizer returns a tokenizer of text.
- `NewTokenizerFragment(text str, contextTag str) Tokenizer`: NewTokenizerFragment returns a tokenizer of text that is the content of an element named contextTag, such as "div" or "script": the content of a raw-text element is not parsed for tags.
- `(z mut Tokenizer) AllowCDATA(allow bool)`: AllowCDATA sets whether <![CDATA[foo]]> is the text foo; by default it is a bogus comment, as outside foreign content.
- `(z mut Tokenizer) NextIsNotRawText()`: NextIsNotRawText makes the next token an ordinary token even when the previous start tag opened a raw-text element.
- `(z Tokenizer) Err() !`: Err fails with ErrEOF after a token that ended the input, and succeeds otherwise.
- `(z Tokenizer) Raw() str`: Raw returns the input bytes of the current token. Consecutive tokens' raw bytes partition the input.
- `(z mut Tokenizer) Next() i64`: Next scans the next token and returns its type: ErrorToken at the end of the input.
- `(z mut Tokenizer) Text() str`: Text returns the unescaped text of the current text, comment or doctype token; it is empty for the other tokens. The data is taken: a second call returns "".
- `(z mut Tokenizer) TagName() (str, bool)`: TagName returns the lower-cased name of the current tag and whether it has attributes; the data is taken, as with Text.
- `(z mut Tokenizer) TagAttr() (str, str, bool)`: TagAttr returns the next attribute of the current start or self-closing tag, with a lower-cased key and an unescaped value, and whether more attributes follow.
- `(z mut Tokenizer) Token() Token`: Token returns the current token, with its data and attributes (which stay valid after the next Next call).
- `const ErrorNode = 0`: ErrorNode is the zero node type; no node has it.
- `const TextNode = 1`: TextNode is a run of text.
- `const DocumentNode = 2`: DocumentNode is the root of a parsed document.
- `const ElementNode = 3`: ElementNode is an element: Data is its name and Namespace is "", "svg" or "math".
- `const CommentNode = 4`: CommentNode is a comment.
- `const DoctypeNode = 5`: DoctypeNode is a document type declaration: Data is its lower-cased name and Attr holds its public and system identifiers.
- `type Document struct`: Document is a parsed tree: node 0 is the root, and the other nodes are reached through Child and Next.
- `(d Document) Root() i64`: Root returns the document node.
- `(d Document) Type(n i64) i64`: Type returns the node type of node n (one of the node type constants).
- `(d Document) Data(n i64) str`: Data returns the name of an element, the text of a text or comment node, or the name of a doctype.
- `(d Document) Namespace(n i64) str`: Namespace returns the namespace of an element: "" for HTML, "svg" or "math".
- `(d Document) Attrs(n i64) []Attribute`: Attrs returns the attributes of node n.
- `(d Document) FirstChild(n i64) i64`: FirstChild returns the first child of node n, or -1 when it has none.
- `(d Document) NextSibling(n i64) i64`: NextSibling returns the node after n under the same parent, or -1 when n is the last.

## lasso

- `type Match struct`: Match is one match's byte offsets: Start is the first byte and End is one past the last.
- `type Regexp struct`: Regexp is a compiled pattern.
- `Compile(pattern str) !Regexp`: Compile parses and compiles pattern, like Go's regexp.Compile. A bad pattern fails with a fault naming the byte offset.
- `MustCompile(pattern str) Regexp`: MustCompile is Compile for a pattern that must be valid (a package-level global, say): it panics when the pattern is bad.
- `(re Regexp) String() str`: String returns the pattern the Regexp was compiled from.
- `(re Regexp) NumSubexp() i64`: NumSubexp returns the number of capturing groups, like Go's NumSubexp.
- `(re Regexp) Named(name str) i64`: Named returns the group index of a named capture, or -1, like Go's SubexpIndex.
- `(re Regexp) Match(s str) bool`: Match reports whether the pattern matches anywhere in s.
- `(re Regexp) Find(s str) (i64, i64, bool)`: Find returns the byte offsets of the leftmost match, like Go's FindStringIndex.
- `(re Regexp) FindAll(s str, n i64) []Match`: FindAll returns up to n matches (n < 0 for all), like Go's FindAllStringIndex.
- `(re Regexp) FindAllSubmatchIndex(s str, n i64) []i64`: FindAllSubmatchIndex returns up to n matches (n < 0 for all) with their groups, flattened: 2*(groups+1) offsets per match, -1 for a group that did not take part, like Go's FindAllStringSubmatchIndex.
- `(re Regexp) SubmatchIndex(s str) []i64`: SubmatchIndex returns the byte offsets of the leftmost match and its groups: 2*(n+1) values, -1 for a group that did not take part, like Go's FindStringSubmatchIndex.
- `(re Regexp) Submatch(s str) []?str`: Submatch returns the text of the leftmost match and its groups, nil for a group that did not take part, like Go's FindStringSubmatch.
- `(re Regexp) Replace(s str, tmpl str) str`: Replace returns a copy of s with every match replaced by tmpl, where $1, ${name} and $$ are expanded, like Go's ReplaceAllString.
- `(re Regexp) ReplaceFunc(s str, f fn(str) str) str`: ReplaceFunc returns a copy of s with every match replaced by f(match), like Go's ReplaceAllStringFunc.
- `(re Regexp) Split(s str, n i64) []str`: Split slices s around every match, like Go's Split: n < 0 returns every piece, n == 0 returns nothing, and n > 0 at most n pieces.
- `QuoteMeta(s str) str`: QuoteMeta returns s with the metacharacters escaped, like Go's QuoteMeta.

## pack

- `type Order struct`: Order is a byte order: LittleEndian or BigEndian.
- `const Size16 = 2`: Size is the number of bytes U16, U32 and U64 read, and PutU16, PutU32 and PutU64 write.
- `const Size32 = 4`
- `const Size64 = 8`
- `(o Order) U16(b []u8) u16`: U16 reads a u16.
- `(o Order) U32(b []u8) u32`: U32 reads a u32.
- `(o Order) U64(b []u8) u64`: U64 reads a u64.
- `(o Order) PutU16(b mut []u8, v u16)`: PutU16 writes v into the first two bytes of b, which must be long enough.
- `(o Order) PutU32(b mut []u8, v u32)`: PutU32 writes v into the first four bytes of b, which must be long enough.
- `(o Order) PutU64(b mut []u8, v u64)`: PutU64 writes v into the first eight bytes of b, which must be long enough.
- `(o Order) AppendU16(b mut []u8, v u16) []u8`: AppendU16 appends v to b.
- `(o Order) AppendU32(b mut []u8, v u32) []u8`: AppendU32 appends v to b.
- `(o Order) AppendU64(b mut []u8, v u64) []u8`: AppendU64 appends v to b.
- `PutUvarint(b mut []u8, v u64) []u8`: PutUvarint appends v in the variable-length form and returns the longer buffer: seven bits a byte, the high bit set while more follow, at most ten bytes.
- `Uvarint(b []u8) !(u64, i64)`: Uvarint reads a variable-length unsigned integer and returns it with the number of bytes it took. A cut-off or over-long encoding fails with a fault.
- `PutVarint(b mut []u8, v i64) []u8`: PutVarint appends v in the zigzag varint form (Go's Varint): small magnitudes take few bytes, negative numbers too.
- `Varint(b []u8) !(i64, i64)`: Varint reads a zigzag varint and returns it with the number of bytes it took.

## asn1

- `const ClassUniversal = 0`: ClassUniversal is the class of the universal types.
- `const ClassApplication = 1`: ClassApplication is the class of application-defined tags.
- `const ClassContextSpecific = 2`: ClassContextSpecific is the class of the [n] tags of a type, such as EXPLICIT and IMPLICIT tags.
- `const ClassPrivate = 3`: ClassPrivate is the class of private tags.
- `const TagBoolean = 1`: TagBoolean is the universal tag of BOOLEAN.
- `const TagInteger = 2`: TagInteger is the universal tag of INTEGER.
- `const TagBitString = 3`: TagBitString is the universal tag of BIT STRING.
- `const TagOctetString = 4`: TagOctetString is the universal tag of OCTET STRING.
- `const TagNull = 5`: TagNull is the universal tag of NULL.
- `const TagOID = 6`: TagOID is the universal tag of OBJECT IDENTIFIER.
- `const TagEnum = 10`: TagEnum is the universal tag of ENUMERATED.
- `const TagUTF8String = 12`: TagUTF8String is the universal tag of UTF8String.
- `const TagSequence = 16`: TagSequence is the universal tag of SEQUENCE and SEQUENCE OF.
- `const TagSet = 17`: TagSet is the universal tag of SET and SET OF.
- `const TagNumericString = 18`: TagNumericString is the universal tag of NumericString.
- `const TagPrintableString = 19`: TagPrintableString is the universal tag of PrintableString.
- `const TagT61String = 20`: TagT61String is the universal tag of T61String.
- `const TagIA5String = 22`: TagIA5String is the universal tag of IA5String.
- `const TagUTCTime = 23`: TagUTCTime is the universal tag of UTCTime.
- `const TagGeneralizedTime = 24`: TagGeneralizedTime is the universal tag of GeneralizedTime.
- `type RawValue struct`: RawValue is one element: its class, its tag, whether its contents are constructed, the contents and, for a parsed element, its whole encoding (Go's asn1.RawValue).
- `type ObjectIdentifier struct`: ObjectIdentifier is a sequence of arcs, such as 1.2.840.113549.
- `type BitString struct`: BitString is a bit string: its bytes, most significant bit first, and its length in bits. Its bytes are ceil(BitLength / 8) long, and the unused bits of the last byte are zero.
- `type DateTime struct`: DateTime is a UTCTime or GeneralizedTime in UTC: its year, month, day, hour, minute and second.
- `OIDFromArcs(arcs []i64) !ObjectIdentifier`: OIDFromArcs returns the object identifier with the given arcs: at least two, the first 0, 1 or 2, the second below 40 unless the first is 2.
- `ParseOID(s str) !ObjectIdentifier`: ParseOID returns the object identifier written as dotted decimal arcs, such as "1.2.840.113549".
- `(o ObjectIdentifier) Arcs() []i64`: Arcs returns a copy of the arcs of o.
- `(o ObjectIdentifier) Equal(other ObjectIdentifier) bool`: Equal reports whether o and other have the same arcs.
- `(o ObjectIdentifier) String() str`: String returns the dotted decimal form of o, such as "1.2.840.113549"; the zero value is "".
- `(b BitString) At(i i64) i64`: At returns the bit at index i (0 for the first bit), or 0 outside the string.
- `(b BitString) RightAlign() []u8`: RightAlign returns the bytes of b with the unused bits of the last byte shifted out, as Go's RightAlign does.
- `Marshal(r RawValue) []u8`: Marshal returns the encoding of r: its FullBytes when it has them, else its header and contents.
- `Element(class i64, tag i64, compound bool, contents []u8) []u8`: Element returns the encoding of an element with the given class, tag, compound flag and contents.
- `Concat(parts [][]u8) []u8`: Concat returns the encodings in parts joined end to end.
- `Int(v i64) []u8`: Int returns the DER encoding of the INTEGER v, in the fewest two's complement octets.
- `IntegerBytes(content []u8) ![]u8`: IntegerBytes returns the INTEGER whose contents are the two's complement bytes content, which must be minimal.
- `Bool(v bool) []u8`: Bool returns the DER encoding of the BOOLEAN v: 0xff for true and 0x00 for false.
- `Null() []u8`: Null returns the DER encoding of NULL.
- `OID(o ObjectIdentifier) ![]u8`: OID returns the DER encoding of the object identifier o, which fails when o is the zero value.
- `Octets(b []u8) []u8`: Octets returns the DER encoding of the OCTET STRING b.
- `Bits(b BitString) ![]u8`: Bits returns the DER encoding of the BIT STRING b. Its bytes must be ceil(BitLength / 8) long.
- `UTF8(s str) []u8`: UTF8 returns the DER encoding of the UTF8String s. As in Go, the bytes are written without a UTF-8 check.
- `Printable(s str) ![]u8`: Printable returns the DER encoding of the PrintableString s.
- `IA5(s str) ![]u8`: IA5 returns the DER encoding of the IA5String s, which must be ASCII.
- `Numeric(s str) ![]u8`: Numeric returns the DER encoding of the NumericString s: digits and spaces.
- `UTCTime(t DateTime) ![]u8`: UTCTime returns the DER encoding of t as a UTCTime, for the years 1950 to 2049.
- `GeneralizedTime(t DateTime) ![]u8`: GeneralizedTime returns the DER encoding of t as a GeneralizedTime, for the years 0 to 9999.
- `Seq(contents []u8) []u8`: Seq returns the DER encoding of a SEQUENCE whose contents are the encodings in contents.
- `Set(contents []u8) []u8`: Set returns the DER encoding of a SET whose contents are the encodings in contents, in the order given.
- `Explicit(tag i64, inner []u8) []u8`: Explicit wraps the encoding inner in a context-specific constructed tag [tag] (an EXPLICIT tag).
- `Implicit(tag i64, r RawValue) []u8`: Implicit returns r with the context-specific tag [tag] in place of its own tag (an IMPLICIT tag).
- `Unmarshal(b []u8) !(RawValue, []u8)`: Unmarshal reads the element at the start of b and returns it with the bytes after it. Its Bytes and FullBytes are views of b.
- `Elements(b []u8) ![]RawValue`: Elements returns the elements of b, which must hold whole elements only (the contents of a SEQUENCE or SET).
- `Expect(r RawValue, class i64, tag i64, compound bool) !`: Expect fails unless r has the class, tag and compound flag given.
- `IntValue(r RawValue) !i64`: IntValue reads an INTEGER that fits in an i64.
- `IntegerContent(r RawValue) ![]u8`: IntegerContent returns the two's complement contents of an INTEGER, of any length.
- `BoolValue(r RawValue) !bool`: BoolValue reads a BOOLEAN: 0x00 is false and 0xff is true.
- `NullValue(r RawValue) !`: NullValue reads a NULL. Its contents are not checked, as in Go's encoding/asn1.
- `OIDValue(r RawValue) !ObjectIdentifier`: OIDValue reads an OBJECT IDENTIFIER.
- `BitsValue(r RawValue) !BitString`: BitsValue reads a BIT STRING.
- `OctetsValue(r RawValue) ![]u8`: OctetsValue reads an OCTET STRING.
- `StringValue(r RawValue) !str`: StringValue reads a string of the UTF8, Numeric, Printable, T61 or IA5 tag as UTF-8 text (T61 as Latin-1, as Go does).
- `TimeValue(r RawValue) !DateTime`: TimeValue reads a UTCTime (years 1950 to 2049) or a GeneralizedTime in UTC.
- `ExplicitValue(r RawValue, tag i64) !RawValue`: ExplicitValue reads the element inside an EXPLICIT tag [tag] that r is.

## gob

- `const KindBool = 1`: KindBool is the kind of bool values.
- `const KindInt = 2`: KindInt is the kind of int values (every signed integer width).
- `const KindUint = 3`: KindUint is the kind of uint values.
- `const KindFloat = 4`: KindFloat is the kind of float64 values.
- `const KindString = 5`: KindString is the kind of string values.
- `const KindBytes = 6`: KindBytes is the kind of []byte values.
- `const KindSlice = 7`: KindSlice is the kind of slices.
- `const KindMap = 8`: KindMap is the kind of maps.
- `const KindStruct = 9`: KindStruct is the kind of structs.
- `const Bool = 0`: Bool is the handle of the builtin bool type.
- `const Int = 1`: Int is the handle of the builtin int type.
- `const Uint = 2`: Uint is the handle of the builtin uint type.
- `const Float = 3`: Float is the handle of the builtin float64 type.
- `const String = 4`: String is the handle of the builtin string type.
- `const Bytes = 5`: Bytes is the handle of the builtin []byte type.
- `type Field struct`: Field is a struct field of a Schema: its name and the type handle of its values.
- `type Schema struct`: Schema is the set of types a stream is made of.
- `NewSchema() Schema`: NewSchema returns a schema holding the builtin types Bool, Int, Uint, Float, String and Bytes.
- `(s mut Schema) Slice(elem i64) i64`: Slice declares the type of slices of elem and returns its handle.
- `(s mut Schema) Map(key i64, elem i64) i64`: Map declares the type of maps from key to elem and returns its handle.
- `(s mut Schema) Struct(name str) i64`: Struct declares a struct type named name, with no fields yet, and returns its handle; AddField adds the fields.
- `(s mut Schema) AddField(t i64, name str, typ i64) !`: AddField appends the field name of type typ to the struct type t; a field is sent in the order added.
- `(s Schema) Kind(t i64) i64`: Kind returns the kind of the type t.
- `type Value struct`: Value is a value of a Schema type: its number (I, U or F), its flag (B), its text or bytes (S), and the elements, fields or map values it holds (Items) and the map keys (Keys).
- `IntV(v i64) Value`: IntV is an Int value.
- `UintV(v u64) Value`: UintV is a Uint value.
- `FloatV(v f64) Value`: FloatV is a Float value.
- `BoolV(v bool) Value`: BoolV is a Bool value.
- `StringV(v str) Value`: StringV is a String value.
- `BytesV(v []u8) Value`: BytesV is a Bytes value.
- `SliceV(items []Value) Value`: SliceV is a slice value holding items.
- `MapV(keys []Value, vals []Value) Value`: MapV is a map value holding keys and their values, in the same order.
- `StructV(fields []Value) Value`: StructV is a struct value holding its fields in declaration order.
- `type Encoder struct`: Encoder writes values of a Schema as a gob stream. It keeps the types it has described, so a type is sent once.
- `NewEncoder(s Schema) Encoder`: NewEncoder returns an encoder for the types of s.
- `(e mut Encoder) Encode(t i64, v Value) ![]u8`: Encode returns the messages that send a value of type t: the descriptions of the types not sent yet, then the value.
- `type Decoder struct`: Decoder reads the messages of a gob stream.
- `NewDecoder(b []u8) Decoder`: NewDecoder returns a decoder of the stream b.
- `(d mut Decoder) Decode(s Schema, t i64) !Value`: Decode reads the next value of the stream as a value of the type t of s, reading the type descriptions before it.
- `(s Schema) Fields(t i64) []Field`: Fields returns the fields of the struct type t, in declaration order.

## mime

- `type Params map[str]str`: Params is a media type's parameters, by lowercased name.
- `ParseMediaType(v str) !(str, Params)`: ParseMediaType parses a media type and its parameters, like Go's mime.ParseMediaType. The media type is lowercased; parameter names are lowercased and their values unquoted; a parameter repeated with the same value is kept once, a different value is an error.
- `FormatMediaType(t str, params Params) str`: FormatMediaType returns the media type with its parameters, like Go's mime.FormatMediaType: parameters are sorted by name and a value that is not a token is quoted.
- `TypeByExtension(ext str) str`: TypeByExtension returns the media type for the extension (which must begin with a dot, as in ".png"), lowercased, or "" when it is unknown.
- `ExtensionsByType(mediatype str) []str`: ExtensionsByType returns the extensions registered for the media type, sorted, or an empty slice when none is.
- `AddExtensionType(ext str, mediatype str) !`: AddExtensionType registers the media type for an extension, like Go's AddExtensionType: the type must be valid and the extension must begin with a dot.
- `type WordDecoder struct{}`: WordDecoder decodes RFC 2047 encoded words in header text (the =?utf-8?q?...?= form).
- `(d WordDecoder) Decode(word str) !str`: Decode decodes one RFC 2047 encoded word, like Go's WordDecoder.Decode: it must be exactly "=?charset?encoding?text?=" with one letter of encoding, and the charset must be one Tin can convert (utf-8, us-ascii or iso-8859-1); anything else is a fault.
- `(d WordDecoder) DecodeHeader(v str) !str`: DecodeHeader decodes every encoded word in a header value, like Go's DecodeHeader: the plain text around the words is kept, the whitespace between two encoded words is dropped, and a word that cannot be decoded is kept as it was.
- `type WordEncoder struct{}`: WordEncoder encodes header text as encoded words when it needs to be, like Go's WordEncoder.
- `(e WordEncoder) EncodeWord(charset str, s str) str`: EncodeWord returns the text as an RFC 2047 encoded word when it has bytes that are not printable ASCII, and the text itself when it does not.

## mail

Package mail reads RFC 5322 messages, addresses and dates.

- `type Address struct`: Address is a name-addr or addr-spec with an optional display name.
- `type Header map[str][]str`: Header holds canonical header names and all values in wire order.
- `type Message struct`: Message is a parsed RFC 5322 message.
- `ReadMessage(src mut dyn io.Reader) !Message`: ReadMessage reads a message and separates its headers from its body, as Go's ReadMessage does: a header ends at the first empty line, a line that starts with a space or a tab continues the one before it, and a message that ends inside its header keeps the fields read so far.
- `(h Header) Get(key str) str`: Get returns the first value associated with key, or an empty string.
- `(h Header) AddressList(key str) ![]Address`: AddressList parses all addresses in the named header field.
- `(h Header) Date() !i64`: Date parses the Date field as an RFC 5322 date.
- `ParseDate(value str) !i64`: ParseDate parses an RFC 5322 date as Go's ParseDate does: the day of the week and the seconds are optional, the year has four or two digits, the zone is a numeric offset or an abbreviation such as UT or EST (read as offset 0), and a comment may follow the zone.
- `ParseAddress(value str) !Address`: ParseAddress parses a single RFC 5322 address, such as "Barry Gibbs <bg@example.com>", with Go's net/mail parser.
- `ParseAddressList(value str) ![]Address`: ParseAddressList parses comma-separated addresses and RFC 5322 groups with Go's net/mail parser; empty entries between commas are skipped (obs-addr-list).
- `DecodeHeader(value str) !str`: DecodeHeader decodes RFC 2047 encoded words in a header value.

## textproto

Package textproto reads and writes the line-oriented framing used by Internet protocols.

- `type Reader struct`: Reader reads CRLF-terminated lines and dot-framed bodies from a bounded string.
- `type Writer struct`: Writer builds line-oriented and dot-framed protocol data.
- `type DotReader struct`: DotReader reads a dot-decoded body from memory.
- `type DotWriter struct`: DotWriter writes dot-stuffed bytes into a Writer.
- `NewReader(data str) Reader`: NewReader creates a reader over data.
- `NewWriter() Writer`: NewWriter creates an empty protocol writer.
- `(r mut Reader) ReadLine() !str`: ReadLine reads one CRLF or LF terminated line; the terminator is not returned.
- `(r mut Reader) ReadContinuedLine() !str`: ReadContinuedLine joins a line and following whitespace-prefixed lines with single spaces, as Go's ReadContinuedLine: each part loses the spaces and tabs around it, and an empty first line has no continuation.
- `(r mut Reader) ReadDotBytes() !str`: ReadDotBytes reads through the terminating dot line and decodes the body as Go's DotReader does: a leading dot is removed from every line, "\r\n" becomes "\n", and the body ends at a line that is only a dot. Input that ends before that line fails.
- `(r mut Reader) ReadDotReader() !DotReader`: ReadDotReader consumes a dot-framed body and returns a reader over its decoded bytes.
- `(r mut DotReader) Read(buf mut []u8) !i64`: Read returns the next decoded bytes, or 0 at the end of the dot body.
- `(w mut Writer) WriteLine(line str)`: WriteLine appends one line and its CRLF terminator.
- `(w Writer) DotWriter() DotWriter`: DotWriter starts a dot-stuffed body writer.
- `(d mut DotWriter) Write(data []u8) !i64`: Write dot-stuffs a chunk and appends it to the associated Writer, as Go's DotWriter: a leading dot is doubled and a bare "\n" becomes "\r\n".
- `(d mut DotWriter) Close() !`: Close ends the last line if it is open and writes the terminating dot line. With nothing written the body is one empty line, as Go's DotWriter writes it.
- `(w mut Writer) WriteDotBytes(body str)`: WriteDotBytes writes a body with dot-stuffing and the terminating dot line.
- `(w Writer) String() str`: String returns the bytes written so far.
- `CanonicalMIMEHeaderKey(key str) str`: CanonicalMIMEHeaderKey returns the canonical capitalization of a header key.

## smtp

Package smtp sends mail with the Simple Mail Transfer Protocol over TCP.

- `type Client struct`: Client is an SMTP connection with buffered protocol input.
- `Dial(addr str) !Client`: Dial opens an SMTP connection and reads its greeting.
- `(c mut Client) Hello(localName str) !`: Hello sends EHLO, falling back to HELO when the server does not support extensions.
- `(c mut Client) Mail(from str) !`: Mail begins a mail transaction with the sender address.
- `(c mut Client) Rcpt(to str) !`: Rcpt adds one recipient to the current mail transaction.
- `(c mut Client) Verify(address str) !`: Verify asks the server whether address is deliverable.
- `(c mut Client) StartTLS(config tls.Config) !`: StartTLS upgrades the connection after the server accepts STARTTLS.
- `(c mut Client) SetTimeout(ns i64)`: SetTimeout limits each later read and write to ns nanoseconds; zero removes the limit.
- `(c mut Client) Data(message str) !`: Data sends the message body after DATA and terminates it with a dot line.
- `(c mut Client) Quit() !`: Quit sends QUIT and closes the connection.
- `(c mut Client) AuthPlain(username str, password str) !`: AuthPlain authenticates with the SMTP AUTH PLAIN mechanism.
- `(c mut Client) AuthLogin(username str, password str) !`: AuthLogin authenticates with the SMTP AUTH LOGIN mechanism.
- `(c mut Client) AuthCramMD5(username str, password str) !`: AuthCramMD5 authenticates with SMTP AUTH CRAM-MD5 (RFC 2195).
- `(c mut Client) Close()`: Close closes the SMTP connection without sending QUIT.
- `SendMail(addr str, from str, to []str, message str) !`: SendMail dials the server, sends one message and quits.

## suffixarray

Package suffixarray indexes byte substrings. An Index keeps its owned text and one i64 per suffix (~9N steady state, ~25N during construction).

- `type Index struct`: Index stores an owned copy of the indexed bytes and one i64 offset per suffix.
- `New(data []u8) Index`: New copies data and builds a suffix array using prefix doubling.
- `(x Index) Bytes() []u8`: Bytes returns the indexed bytes; callers must treat them as read-only.
- `(x Index) Lookup(s []u8, n i64) []i64`: Lookup returns up to n matching offsets in suffix-array order; n < 0 returns all, and empty s or n == 0 returns none.
- `(x Index) FindAllIndex(s []u8) []i64`: FindAllIndex returns all matching offsets in ascending text order.
- `Read[S io.Reader](x mut Index, r mut S) !`: Read loads a Go index/suffixarray binary stream and validates every decoded suffix offset.

## scan

Package scan is a scanner and tokenizer for UTF-8 text, Go's text/scanner: it reads Go-style identifiers, numbers, char, string and raw string literals and comments, with Go's white space and position rules, for tokenizing source code, configuration files and small languages.

```tin body
mut s = scan.New("let x = 1.5 + y // the sum")
s.Filename = "example"
for {
	let tok = s.Scan()
	if tok == scan.EOF {
		break
	}
	say.Line(s.Position().String(), scan.TokenString(tok), s.TokenText())
}
```

The Scanner reads a whole str (a stream is read with io.ReadAll first), so a token's text is a slice of the source and positions are byte offsets into it. Scan returns a token kind (EOF, Ident, Int, Float, Char, String, RawString, Comment, all negative) or the rune itself for any other character. Mode selects the tokens recognized (GoTokens by default: comments are skipped), Whitespace the characters skipped, and SetIdentRune the identifier characters. Errors (a literal not terminated, a bad escape, invalid UTF-8, a NUL) do not stop the scan: they are counted in ErrorCount and the first thousand are kept with their positions, read with Errors and Err. Lines and columns are 1-based, a column counts characters, and a leading byte order mark is skipped; the Go twin (bench/ref/scan and tools/ci/scan_check.tin) checks every token, position and error against Go's.

- `const EOF = -1`: EOF is the end of the source. The token kinds are negative, so a character Scan returns is never one.
- `const Ident = -2`: Ident is an identifier.
- `const Int = -3`: Int is an integer literal.
- `const Float = -4`: Float is a floating-point literal.
- `const Char = -5`: Char is a character literal.
- `const String = -6`: String is an interpreted string literal.
- `const RawString = -7`: RawString is a raw (backquoted) string literal.
- `const Comment = -8`: Comment is a comment, returned when ScanComments is set without SkipComments.
- `const ScanIdents = 4`: ScanIdents recognizes identifiers (the Mode bit 1 << -Ident).
- `const ScanInts = 8`: ScanInts recognizes integer literals.
- `const ScanFloats = 16`: ScanFloats recognizes floating-point literals, integers and hexadecimal floats included.
- `const ScanChars = 32`: ScanChars recognizes character literals.
- `const ScanStrings = 64`: ScanStrings recognizes interpreted string literals.
- `const ScanRawStrings = 128`: ScanRawStrings recognizes raw string literals.
- `const ScanComments = 256`: ScanComments recognizes comments.
- `const SkipComments = 512`: SkipComments, with ScanComments, makes comments white space instead of Comment tokens.
- `const GoTokens = ScanIdents | ScanFloats | ScanChars | ScanStrings | ScanRawStrings | ScanComments | SkipComments`: GoTokens is every Go literal token with comments skipped: the Mode Init sets.
- `const GoWhitespace = 1<<9 | 1<<10 | 1<<13 | 1<<32`: GoWhitespace is the Whitespace Init sets: tab, newline, carriage return and space.
- `type Position value struct`: Position is a place in the source: valid when Line > 0.
- `(p Position) IsValid() bool`: IsValid reports whether the position is valid (Line > 0).
- `(p Position) String() str`: String is "file:line:column", with "<input>" for an empty file name and no numbers when invalid.
- `type Error value struct`: Error is one error the scanner met: where, as Go reports it, and what.
- `(e Error) String() str`: String is "position: message", the line Go prints when no Error function is set.
- `type Scanner struct`: Scanner reads the characters and tokens of a source text; make one with New.
- `New(src str) Scanner`: New returns a Scanner over src, initialized as Init does.
- `(s mut Scanner) Init(src str)`: Init restarts s on src: no errors, Mode GoTokens, Whitespace GoWhitespace and no token position; Filename and the identifier predicate stay.
- `(s mut Scanner) SetIdentRune(f fn(i32, i64) bool)`: SetIdentRune makes f decide the characters of identifiers: f(ch, i) accepts ch as the i-th rune (from 0) of one. It must not accept white space characters.
- `(s mut Scanner) ResetIdentRune()`: ResetIdentRune goes back to Go identifiers: a letter or '_', then letters, digits and '_'.
- `(s mut Scanner) Next() i32`: Next reads and returns the next character (EOF at the end) and makes Position invalid; Pos is the position after it.
- `(s mut Scanner) Peek() i32`: Peek returns the next character without advancing (EOF at the end).
- `(s Scanner) Errors() []Error`: Errors returns the errors met since Init, at most the first thousand (ErrorCount counts them all).
- `(s Scanner) Err() !`: Err fails with the first error ("position: message") when there was one.
- `(s mut Scanner) Scan() i32`: Scan reads the next token or character and returns it: a token kind for a token Mode recognizes, EOF at the end, or else the character itself. Position is where it starts, TokenText its text.
- `(s Scanner) Position() Position`: Position is where the token Scan last returned starts; Init and Next make it invalid.
- `(s Scanner) Pos() Position`: Pos is the position just after the character or token Next or Scan last returned.
- `(s Scanner) TokenText() str`: TokenText is the text of the token Scan last returned ("" after Next).
- `TokenString(tok i32) str`: TokenString is a printable form of a token kind ("EOF", "Ident", ...) or character (Go-quoted).

## image

Package image is Go's image: points and rectangles, the Image shape, and the images that keep their pixels in one byte slice (RGBA, RGBA64, NRGBA, NRGBA64, Gray, Gray16, Alpha, Alpha16, Paletted) plus Uniform. Pixels are never allocated one by one: an image is a Pix slice, a Stride and a Rect, laid out exactly as in Go.

```tin body
mut m = image.NewRGBA(image.Rect(0, 0, 640, 480))
m.Set(10, 20, m.At(0, 0))
let c = m.At(10, 20)
```

Image's At gives a pixel as color.RGBA64 (Go's RGBA64At), so reading a pixel through the shape allocates nothing; each image also has its own typed accessors (RGBAAt, GrayAt, ColorIndexAt...). Layout tells which concrete image a dyn Image is and gives its pixel buffer: it is how image/draw and image/png take their fast paths, and how a caller gets the concrete image back (AsRGBA, AsNRGBA...). The image/jpeg package decodes 8-bit baseline and progressive JPEG data and encodes baseline JPEG images.

- `type Point value struct`: Point is an (X, Y) pair; X grows to the right and Y downwards.
- `Pt(x i64, y i64) Point`: Pt is Point{X: x, Y: y}.
- `(p Point) String() str`: String is "(x,y)".
- `(p Point) Add(q Point) Point`: Add is p + q.
- `(p Point) Sub(q Point) Point`: Sub is p - q.
- `(p Point) Mul(k i64) Point`: Mul is p scaled by k.
- `(p Point) Div(k i64) Point`: Div is p divided by k (truncated toward zero).
- `(p Point) In(r Rectangle) bool`: In reports whether p is inside r (Min inclusive, Max exclusive).
- `(p Point) Mod(r Rectangle) Point`: Mod is the point of r congruent to p modulo r's width and height.
- `(p Point) Eq(q Point) bool`: Eq reports whether p and q are the same point.
- `type Rectangle value struct`: Rectangle holds the points with Min.X <= X < Max.X and Min.Y <= Y < Max.Y; it is well-formed when Min <= Max. A Rectangle is also an Image: opaque inside, transparent outside (a mask).
- `Rect(x0 i64, y0 i64, x1 i64, y1 i64) Rectangle`: Rect is the rectangle with corners (x0, y0) and (x1, y1), swapped as needed to be well-formed.
- `(r Rectangle) String() str`: String is "(x0,y0)-(x1,y1)".
- `(r Rectangle) Dx() i64`: Dx is r's width.
- `(r Rectangle) Dy() i64`: Dy is r's height.
- `(r Rectangle) Size() Point`: Size is r's width and height as a Point.
- `(r Rectangle) Add(p Point) Rectangle`: Add is r moved by p.
- `(r Rectangle) Sub(p Point) Rectangle`: Sub is r moved by -p.
- `(r Rectangle) Inset(n i64) Rectangle`: Inset is r shrunk by n on each side (negative n grows it); a side too short collapses to its midpoint.
- `(r Rectangle) Intersect(s Rectangle) Rectangle`: Intersect is the largest rectangle inside both r and s; the zero rectangle when they do not overlap.
- `(r Rectangle) Union(s Rectangle) Rectangle`: Union is the smallest rectangle holding both r and s (an empty one is ignored).
- `(r Rectangle) Empty() bool`: Empty reports whether r holds no points.
- `(r Rectangle) Eq(s Rectangle) bool`: Eq reports whether r and s hold the same points (any two empty rectangles are equal).
- `(r Rectangle) Overlaps(s Rectangle) bool`: Overlaps reports whether r and s share a point.
- `(r Rectangle) In(s Rectangle) bool`: In reports whether every point of r is in s.
- `(r Rectangle) Canon() Rectangle`: Canon is r with its corners swapped as needed to be well-formed.
- `(r Rectangle) At(x i64, y i64) color.RGBA64`: At is opaque inside r and transparent outside.
- `(r Rectangle) Bounds() Rectangle`: Bounds is r.
- `(r Rectangle) ColorModel() color.Model`: ColorModel is Alpha16Model.
- `(r Rectangle) Layout() Layout`: Layout says a Rectangle has no pixel buffer.
- `type Gray struct`: Gray is an image of 8-bit grays, one byte per pixel.
- `NewGray(r Rectangle) Gray`: NewGray is a black Gray image of r.
- `(p Gray) ColorModel() color.Model`: ColorModel is GrayModel.
- `(p Gray) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Gray) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Gray) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Gray) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p Gray) GrayAt(x i64, y i64) color.Gray`: GrayAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut Gray) Set(x i64, y i64, c color.RGBA64)`: Set stores c's luminance at (x, y) (nothing outside the bounds).
- `(p mut Gray) SetGray(x i64, y i64, c color.Gray)`: SetGray stores c at (x, y) (nothing outside the bounds).
- `(p Gray) SubImage(r Rectangle) Gray`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Gray) Opaque() bool`: Opaque is true: a gray image has no alpha.
- `type Gray16 struct`: Gray16 is an image of 16-bit grays, two big-endian bytes per pixel.
- `NewGray16(r Rectangle) Gray16`: NewGray16 is a black Gray16 image of r.
- `(p Gray16) ColorModel() color.Model`: ColorModel is Gray16Model.
- `(p Gray16) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Gray16) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Gray16) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p Gray16) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p Gray16) Gray16At(x i64, y i64) color.Gray16`: Gray16At is the pixel at (x, y) (zero outside the bounds).
- `(p mut Gray16) Set(x i64, y i64, c color.RGBA64)`: Set stores c's luminance at (x, y) (nothing outside the bounds).
- `(p mut Gray16) SetGray16(x i64, y i64, c color.Gray16)`: SetGray16 stores c at (x, y) (nothing outside the bounds).
- `(p Gray16) SubImage(r Rectangle) Gray16`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Gray16) Opaque() bool`: Opaque is true: a gray image has no alpha.
- `type Alpha struct`: Alpha is an image of 8-bit alphas (a mask), one byte per pixel.
- `NewAlpha(r Rectangle) Alpha`: NewAlpha is a transparent Alpha image of r.
- `(p Alpha) ColorModel() color.Model`: ColorModel is AlphaModel.
- `(p Alpha) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Alpha) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Alpha) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Alpha) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p Alpha) AlphaAt(x i64, y i64) color.Alpha`: AlphaAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut Alpha) Set(x i64, y i64, c color.RGBA64)`: Set stores c's alpha at (x, y) (nothing outside the bounds).
- `(p mut Alpha) SetAlpha(x i64, y i64, c color.Alpha)`: SetAlpha stores c at (x, y) (nothing outside the bounds).
- `(p Alpha) SubImage(r Rectangle) Alpha`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Alpha) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type Alpha16 struct`: Alpha16 is an image of 16-bit alphas, two big-endian bytes per pixel.
- `NewAlpha16(r Rectangle) Alpha16`: NewAlpha16 is a transparent Alpha16 image of r.
- `(p Alpha16) ColorModel() color.Model`: ColorModel is Alpha16Model.
- `(p Alpha16) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Alpha16) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Alpha16) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p Alpha16) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p Alpha16) Alpha16At(x i64, y i64) color.Alpha16`: Alpha16At is the pixel at (x, y) (zero outside the bounds).
- `(p mut Alpha16) Set(x i64, y i64, c color.RGBA64)`: Set stores c's alpha at (x, y) (nothing outside the bounds).
- `(p mut Alpha16) SetAlpha16(x i64, y i64, c color.Alpha16)`: SetAlpha16 stores c at (x, y) (nothing outside the bounds).
- `(p Alpha16) SubImage(r Rectangle) Alpha16`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Alpha16) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `shape Image`: Image is a rectangle of colors (Go's image.Image): At is the 16-bit premultiplied color at (x, y) (outside Bounds, the zero color, or a Paletted image's first palette color), and Layout describes the pixel buffer (Custom for an image without one).
- `type Config value struct`: Config is an image's color model and size, as a decoder reads them from the header.
- `type Kind i64`: Kind says which concrete image a Layout describes.
- `const Custom Kind = 0`: Custom is an image of another package, with no pixel buffer the image package knows.
- `const KindRGBA Kind = 1`: KindRGBA is an RGBA image.
- `const KindRGBA64 Kind = 2`: KindRGBA64 is an RGBA64 image.
- `const KindNRGBA Kind = 3`: KindNRGBA is an NRGBA image.
- `const KindNRGBA64 Kind = 4`: KindNRGBA64 is an NRGBA64 image.
- `const KindAlpha Kind = 5`: KindAlpha is an Alpha image.
- `const KindAlpha16 Kind = 6`: KindAlpha16 is an Alpha16 image.
- `const KindGray Kind = 7`: KindGray is a Gray image.
- `const KindGray16 Kind = 8`: KindGray16 is a Gray16 image.
- `const KindPaletted Kind = 9`: KindPaletted is a Paletted image.
- `const KindUniform Kind = 10`: KindUniform is a Uniform image (no pixel buffer: every pixel is its color).
- `(k Kind) String() str`: String is the kind's type name, such as "RGBA".
- `type Layout value struct`: Layout is how an image keeps its pixels: the pixel at (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*n] with n bytes per pixel (4 for RGBA and NRGBA, 8 for RGBA64 and NRGBA64, 2 for Gray16 and Alpha16, 1 otherwise; 16-bit channels are big-endian). Palette is a Paletted image's.
- `AsRGBA(m dyn Image) ?RGBA`: AsRGBA is m as the RGBA image it is (sharing its pixels), or nil.
- `AsRGBA64(m dyn Image) ?RGBA64`: AsRGBA64 is m as the RGBA64 image it is (sharing its pixels), or nil.
- `AsNRGBA(m dyn Image) ?NRGBA`: AsNRGBA is m as the NRGBA image it is (sharing its pixels), or nil.
- `AsNRGBA64(m dyn Image) ?NRGBA64`: AsNRGBA64 is m as the NRGBA64 image it is (sharing its pixels), or nil.
- `AsAlpha(m dyn Image) ?Alpha`: AsAlpha is m as the Alpha image it is (sharing its pixels), or nil.
- `AsAlpha16(m dyn Image) ?Alpha16`: AsAlpha16 is m as the Alpha16 image it is (sharing its pixels), or nil.
- `AsGray(m dyn Image) ?Gray`: AsGray is m as the Gray image it is (sharing its pixels), or nil.
- `AsGray16(m dyn Image) ?Gray16`: AsGray16 is m as the Gray16 image it is (sharing its pixels), or nil.
- `AsPaletted(m dyn Image) ?Paletted`: AsPaletted is m as the Paletted image it is (sharing its pixels and palette), or nil.
- `type Paletted struct`: Paletted is an image of palette indices, one byte per pixel, over Palette (a color.Palette held as its slice type).
- `NewPaletted(r Rectangle, p color.Palette) Paletted`: NewPaletted is a Paletted image of r over palette p, every pixel index 0.
- `(p Paletted) ColorModel() color.Model`: ColorModel is PaletteModel: the image's Palette.
- `(p Paletted) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Paletted) Layout() Layout`: Layout is the image's pixel buffer and palette.
- `(p Paletted) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Paletted) At(x i64, y i64) color.RGBA64`: At is the palette color of the pixel at (x, y), premultiplied (the first palette color outside the bounds, zero for an empty palette).
- `(p Paletted) ColorIndexAt(x i64, y i64) u8`: ColorIndexAt is the palette index at (x, y) (0 outside the bounds).
- `(p mut Paletted) Set(x i64, y i64, c color.RGBA64)`: Set stores the index of the palette color nearest to c at (x, y) (nothing outside the bounds).
- `(p mut Paletted) SetColorIndex(x i64, y i64, index u8)`: SetColorIndex stores index at (x, y) (nothing outside the bounds).
- `(p Paletted) SubImage(r Rectangle) Paletted`: SubImage is the part of p inside r, sharing p's pixels and palette.
- `(p Paletted) Opaque() bool`: Opaque reports whether every palette color some pixel uses is fully opaque.
- `type Uniform struct`: Uniform is an image of one color everywhere (Go's bounds: a square of side 2e9 around the origin); it is also a color.Color.
- `NewUniform[C color.Color](c C) Uniform`: NewUniform is the image of color c everywhere.
- `(u Uniform) RGBA() (u32, u32, u32, u32)`: RGBA is the uniform color's 16-bit premultiplied channels.
- `(u Uniform) ColorModel() color.Model`: ColorModel is RGBA64Model (Go answers the Uniform itself).
- `(u Uniform) Bounds() Rectangle`: Bounds is (-1e9,-1e9)-(1e9,1e9).
- `(u Uniform) At(x i64, y i64) color.RGBA64`: At is the color, wherever.
- `(u Uniform) Layout() Layout`: Layout says a Uniform has no pixel buffer.
- `(u Uniform) Opaque() bool`: Opaque reports whether the color is fully opaque.
- `type RGBA struct`: RGBA is an image of 8-bit premultiplied colors: R, G, B, A per pixel.
- `NewRGBA(r Rectangle) RGBA`: NewRGBA is a transparent black RGBA image of r.
- `(p RGBA) ColorModel() color.Model`: ColorModel is RGBAModel.
- `(p RGBA) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p RGBA) Layout() Layout`: Layout is the image's pixel buffer.
- `(p RGBA) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p RGBA) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p RGBA) RGBAAt(x i64, y i64) color.RGBA`: RGBAAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut RGBA) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y) (nothing outside the bounds).
- `(p mut RGBA) SetRGBA(x i64, y i64, c color.RGBA)`: SetRGBA stores c at (x, y) (nothing outside the bounds).
- `(p RGBA) SubImage(r Rectangle) RGBA`: SubImage is the part of p inside r, sharing p's pixels.
- `(p RGBA) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type RGBA64 struct`: RGBA64 is an image of 16-bit premultiplied colors: R, G, B, A per pixel, each big-endian.
- `NewRGBA64(r Rectangle) RGBA64`: NewRGBA64 is a transparent black RGBA64 image of r.
- `(p RGBA64) ColorModel() color.Model`: ColorModel is RGBA64Model.
- `(p RGBA64) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p RGBA64) Layout() Layout`: Layout is the image's pixel buffer.
- `(p RGBA64) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p RGBA64) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p RGBA64) RGBA64At(x i64, y i64) color.RGBA64`: RGBA64At is At.
- `(p mut RGBA64) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y) (nothing outside the bounds).
- `(p mut RGBA64) SetRGBA64(x i64, y i64, c color.RGBA64)`: SetRGBA64 is Set.
- `(p RGBA64) SubImage(r Rectangle) RGBA64`: SubImage is the part of p inside r, sharing p's pixels.
- `(p RGBA64) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type NRGBA struct`: NRGBA is an image of 8-bit colors that are not premultiplied: R, G, B, A per pixel.
- `NewNRGBA(r Rectangle) NRGBA`: NewNRGBA is a transparent black NRGBA image of r.
- `(p NRGBA) ColorModel() color.Model`: ColorModel is NRGBAModel.
- `(p NRGBA) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p NRGBA) Layout() Layout`: Layout is the image's pixel buffer.
- `(p NRGBA) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p NRGBA) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y), premultiplied, in 16 bits (zero outside the bounds).
- `(p NRGBA) NRGBAAt(x i64, y i64) color.NRGBA`: NRGBAAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut NRGBA) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y), premultiplication undone (nothing outside the bounds).
- `(p mut NRGBA) SetNRGBA(x i64, y i64, c color.NRGBA)`: SetNRGBA stores c at (x, y) (nothing outside the bounds).
- `(p NRGBA) SubImage(r Rectangle) NRGBA`: SubImage is the part of p inside r, sharing p's pixels.
- `(p NRGBA) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type NRGBA64 struct`: NRGBA64 is an image of 16-bit colors that are not premultiplied: R, G, B, A per pixel, each big-endian.
- `NewNRGBA64(r Rectangle) NRGBA64`: NewNRGBA64 is a transparent black NRGBA64 image of r.
- `(p NRGBA64) ColorModel() color.Model`: ColorModel is NRGBA64Model.
- `(p NRGBA64) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p NRGBA64) Layout() Layout`: Layout is the image's pixel buffer.
- `(p NRGBA64) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p NRGBA64) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y), premultiplied (zero outside the bounds).
- `(p NRGBA64) NRGBA64At(x i64, y i64) color.NRGBA64`: NRGBA64At is the pixel at (x, y) (zero outside the bounds).
- `(p mut NRGBA64) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y), premultiplication undone (nothing outside the bounds).
- `(p mut NRGBA64) SetNRGBA64(x i64, y i64, c color.NRGBA64)`: SetNRGBA64 stores c at (x, y) (nothing outside the bounds).
- `(p NRGBA64) SubImage(r Rectangle) NRGBA64`: SubImage is the part of p inside r, sharing p's pixels.
- `(p NRGBA64) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type Huffman struct`
- `type Component struct`
- `Decode(data str) !dyn image.Image`: Decode decodes an 8-bit baseline or progressive JPEG into NRGBA64 pixels. EXIF orientation is left to the caller.
- `type Bits struct`

## image

Package image is Go's image: points and rectangles, the Image shape, and the images that keep their pixels in one byte slice (RGBA, RGBA64, NRGBA, NRGBA64, Gray, Gray16, Alpha, Alpha16, Paletted) plus Uniform. Pixels are never allocated one by one: an image is a Pix slice, a Stride and a Rect, laid out exactly as in Go.

```tin body
mut m = image.NewRGBA(image.Rect(0, 0, 640, 480))
m.Set(10, 20, m.At(0, 0))
let c = m.At(10, 20)
```

Image's At gives a pixel as color.RGBA64 (Go's RGBA64At), so reading a pixel through the shape allocates nothing; each image also has its own typed accessors (RGBAAt, GrayAt, ColorIndexAt...). Layout tells which concrete image a dyn Image is and gives its pixel buffer: it is how image/draw and image/png take their fast paths, and how a caller gets the concrete image back (AsRGBA, AsNRGBA...). The image/jpeg package decodes 8-bit baseline and progressive JPEG data and encodes baseline JPEG images.

- `type Point value struct`: Point is an (X, Y) pair; X grows to the right and Y downwards.
- `Pt(x i64, y i64) Point`: Pt is Point{X: x, Y: y}.
- `(p Point) String() str`: String is "(x,y)".
- `(p Point) Add(q Point) Point`: Add is p + q.
- `(p Point) Sub(q Point) Point`: Sub is p - q.
- `(p Point) Mul(k i64) Point`: Mul is p scaled by k.
- `(p Point) Div(k i64) Point`: Div is p divided by k (truncated toward zero).
- `(p Point) In(r Rectangle) bool`: In reports whether p is inside r (Min inclusive, Max exclusive).
- `(p Point) Mod(r Rectangle) Point`: Mod is the point of r congruent to p modulo r's width and height.
- `(p Point) Eq(q Point) bool`: Eq reports whether p and q are the same point.
- `type Rectangle value struct`: Rectangle holds the points with Min.X <= X < Max.X and Min.Y <= Y < Max.Y; it is well-formed when Min <= Max. A Rectangle is also an Image: opaque inside, transparent outside (a mask).
- `Rect(x0 i64, y0 i64, x1 i64, y1 i64) Rectangle`: Rect is the rectangle with corners (x0, y0) and (x1, y1), swapped as needed to be well-formed.
- `(r Rectangle) String() str`: String is "(x0,y0)-(x1,y1)".
- `(r Rectangle) Dx() i64`: Dx is r's width.
- `(r Rectangle) Dy() i64`: Dy is r's height.
- `(r Rectangle) Size() Point`: Size is r's width and height as a Point.
- `(r Rectangle) Add(p Point) Rectangle`: Add is r moved by p.
- `(r Rectangle) Sub(p Point) Rectangle`: Sub is r moved by -p.
- `(r Rectangle) Inset(n i64) Rectangle`: Inset is r shrunk by n on each side (negative n grows it); a side too short collapses to its midpoint.
- `(r Rectangle) Intersect(s Rectangle) Rectangle`: Intersect is the largest rectangle inside both r and s; the zero rectangle when they do not overlap.
- `(r Rectangle) Union(s Rectangle) Rectangle`: Union is the smallest rectangle holding both r and s (an empty one is ignored).
- `(r Rectangle) Empty() bool`: Empty reports whether r holds no points.
- `(r Rectangle) Eq(s Rectangle) bool`: Eq reports whether r and s hold the same points (any two empty rectangles are equal).
- `(r Rectangle) Overlaps(s Rectangle) bool`: Overlaps reports whether r and s share a point.
- `(r Rectangle) In(s Rectangle) bool`: In reports whether every point of r is in s.
- `(r Rectangle) Canon() Rectangle`: Canon is r with its corners swapped as needed to be well-formed.
- `(r Rectangle) At(x i64, y i64) color.RGBA64`: At is opaque inside r and transparent outside.
- `(r Rectangle) Bounds() Rectangle`: Bounds is r.
- `(r Rectangle) ColorModel() color.Model`: ColorModel is Alpha16Model.
- `(r Rectangle) Layout() Layout`: Layout says a Rectangle has no pixel buffer.
- `type Gray struct`: Gray is an image of 8-bit grays, one byte per pixel.
- `NewGray(r Rectangle) Gray`: NewGray is a black Gray image of r.
- `(p Gray) ColorModel() color.Model`: ColorModel is GrayModel.
- `(p Gray) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Gray) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Gray) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Gray) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p Gray) GrayAt(x i64, y i64) color.Gray`: GrayAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut Gray) Set(x i64, y i64, c color.RGBA64)`: Set stores c's luminance at (x, y) (nothing outside the bounds).
- `(p mut Gray) SetGray(x i64, y i64, c color.Gray)`: SetGray stores c at (x, y) (nothing outside the bounds).
- `(p Gray) SubImage(r Rectangle) Gray`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Gray) Opaque() bool`: Opaque is true: a gray image has no alpha.
- `type Gray16 struct`: Gray16 is an image of 16-bit grays, two big-endian bytes per pixel.
- `NewGray16(r Rectangle) Gray16`: NewGray16 is a black Gray16 image of r.
- `(p Gray16) ColorModel() color.Model`: ColorModel is Gray16Model.
- `(p Gray16) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Gray16) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Gray16) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p Gray16) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p Gray16) Gray16At(x i64, y i64) color.Gray16`: Gray16At is the pixel at (x, y) (zero outside the bounds).
- `(p mut Gray16) Set(x i64, y i64, c color.RGBA64)`: Set stores c's luminance at (x, y) (nothing outside the bounds).
- `(p mut Gray16) SetGray16(x i64, y i64, c color.Gray16)`: SetGray16 stores c at (x, y) (nothing outside the bounds).
- `(p Gray16) SubImage(r Rectangle) Gray16`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Gray16) Opaque() bool`: Opaque is true: a gray image has no alpha.
- `type Alpha struct`: Alpha is an image of 8-bit alphas (a mask), one byte per pixel.
- `NewAlpha(r Rectangle) Alpha`: NewAlpha is a transparent Alpha image of r.
- `(p Alpha) ColorModel() color.Model`: ColorModel is AlphaModel.
- `(p Alpha) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Alpha) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Alpha) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Alpha) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p Alpha) AlphaAt(x i64, y i64) color.Alpha`: AlphaAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut Alpha) Set(x i64, y i64, c color.RGBA64)`: Set stores c's alpha at (x, y) (nothing outside the bounds).
- `(p mut Alpha) SetAlpha(x i64, y i64, c color.Alpha)`: SetAlpha stores c at (x, y) (nothing outside the bounds).
- `(p Alpha) SubImage(r Rectangle) Alpha`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Alpha) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type Alpha16 struct`: Alpha16 is an image of 16-bit alphas, two big-endian bytes per pixel.
- `NewAlpha16(r Rectangle) Alpha16`: NewAlpha16 is a transparent Alpha16 image of r.
- `(p Alpha16) ColorModel() color.Model`: ColorModel is Alpha16Model.
- `(p Alpha16) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Alpha16) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Alpha16) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p Alpha16) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p Alpha16) Alpha16At(x i64, y i64) color.Alpha16`: Alpha16At is the pixel at (x, y) (zero outside the bounds).
- `(p mut Alpha16) Set(x i64, y i64, c color.RGBA64)`: Set stores c's alpha at (x, y) (nothing outside the bounds).
- `(p mut Alpha16) SetAlpha16(x i64, y i64, c color.Alpha16)`: SetAlpha16 stores c at (x, y) (nothing outside the bounds).
- `(p Alpha16) SubImage(r Rectangle) Alpha16`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Alpha16) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `shape Image`: Image is a rectangle of colors (Go's image.Image): At is the 16-bit premultiplied color at (x, y) (outside Bounds, the zero color, or a Paletted image's first palette color), and Layout describes the pixel buffer (Custom for an image without one).
- `type Config value struct`: Config is an image's color model and size, as a decoder reads them from the header.
- `type Kind i64`: Kind says which concrete image a Layout describes.
- `const Custom Kind = 0`: Custom is an image of another package, with no pixel buffer the image package knows.
- `const KindRGBA Kind = 1`: KindRGBA is an RGBA image.
- `const KindRGBA64 Kind = 2`: KindRGBA64 is an RGBA64 image.
- `const KindNRGBA Kind = 3`: KindNRGBA is an NRGBA image.
- `const KindNRGBA64 Kind = 4`: KindNRGBA64 is an NRGBA64 image.
- `const KindAlpha Kind = 5`: KindAlpha is an Alpha image.
- `const KindAlpha16 Kind = 6`: KindAlpha16 is an Alpha16 image.
- `const KindGray Kind = 7`: KindGray is a Gray image.
- `const KindGray16 Kind = 8`: KindGray16 is a Gray16 image.
- `const KindPaletted Kind = 9`: KindPaletted is a Paletted image.
- `const KindUniform Kind = 10`: KindUniform is a Uniform image (no pixel buffer: every pixel is its color).
- `(k Kind) String() str`: String is the kind's type name, such as "RGBA".
- `type Layout value struct`: Layout is how an image keeps its pixels: the pixel at (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*n] with n bytes per pixel (4 for RGBA and NRGBA, 8 for RGBA64 and NRGBA64, 2 for Gray16 and Alpha16, 1 otherwise; 16-bit channels are big-endian). Palette is a Paletted image's.
- `AsRGBA(m dyn Image) ?RGBA`: AsRGBA is m as the RGBA image it is (sharing its pixels), or nil.
- `AsRGBA64(m dyn Image) ?RGBA64`: AsRGBA64 is m as the RGBA64 image it is (sharing its pixels), or nil.
- `AsNRGBA(m dyn Image) ?NRGBA`: AsNRGBA is m as the NRGBA image it is (sharing its pixels), or nil.
- `AsNRGBA64(m dyn Image) ?NRGBA64`: AsNRGBA64 is m as the NRGBA64 image it is (sharing its pixels), or nil.
- `AsAlpha(m dyn Image) ?Alpha`: AsAlpha is m as the Alpha image it is (sharing its pixels), or nil.
- `AsAlpha16(m dyn Image) ?Alpha16`: AsAlpha16 is m as the Alpha16 image it is (sharing its pixels), or nil.
- `AsGray(m dyn Image) ?Gray`: AsGray is m as the Gray image it is (sharing its pixels), or nil.
- `AsGray16(m dyn Image) ?Gray16`: AsGray16 is m as the Gray16 image it is (sharing its pixels), or nil.
- `AsPaletted(m dyn Image) ?Paletted`: AsPaletted is m as the Paletted image it is (sharing its pixels and palette), or nil.
- `type Paletted struct`: Paletted is an image of palette indices, one byte per pixel, over Palette (a color.Palette held as its slice type).
- `NewPaletted(r Rectangle, p color.Palette) Paletted`: NewPaletted is a Paletted image of r over palette p, every pixel index 0.
- `(p Paletted) ColorModel() color.Model`: ColorModel is PaletteModel: the image's Palette.
- `(p Paletted) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Paletted) Layout() Layout`: Layout is the image's pixel buffer and palette.
- `(p Paletted) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Paletted) At(x i64, y i64) color.RGBA64`: At is the palette color of the pixel at (x, y), premultiplied (the first palette color outside the bounds, zero for an empty palette).
- `(p Paletted) ColorIndexAt(x i64, y i64) u8`: ColorIndexAt is the palette index at (x, y) (0 outside the bounds).
- `(p mut Paletted) Set(x i64, y i64, c color.RGBA64)`: Set stores the index of the palette color nearest to c at (x, y) (nothing outside the bounds).
- `(p mut Paletted) SetColorIndex(x i64, y i64, index u8)`: SetColorIndex stores index at (x, y) (nothing outside the bounds).
- `(p Paletted) SubImage(r Rectangle) Paletted`: SubImage is the part of p inside r, sharing p's pixels and palette.
- `(p Paletted) Opaque() bool`: Opaque reports whether every palette color some pixel uses is fully opaque.
- `type Uniform struct`: Uniform is an image of one color everywhere (Go's bounds: a square of side 2e9 around the origin); it is also a color.Color.
- `NewUniform[C color.Color](c C) Uniform`: NewUniform is the image of color c everywhere.
- `(u Uniform) RGBA() (u32, u32, u32, u32)`: RGBA is the uniform color's 16-bit premultiplied channels.
- `(u Uniform) ColorModel() color.Model`: ColorModel is RGBA64Model (Go answers the Uniform itself).
- `(u Uniform) Bounds() Rectangle`: Bounds is (-1e9,-1e9)-(1e9,1e9).
- `(u Uniform) At(x i64, y i64) color.RGBA64`: At is the color, wherever.
- `(u Uniform) Layout() Layout`: Layout says a Uniform has no pixel buffer.
- `(u Uniform) Opaque() bool`: Opaque reports whether the color is fully opaque.
- `type RGBA struct`: RGBA is an image of 8-bit premultiplied colors: R, G, B, A per pixel.
- `NewRGBA(r Rectangle) RGBA`: NewRGBA is a transparent black RGBA image of r.
- `(p RGBA) ColorModel() color.Model`: ColorModel is RGBAModel.
- `(p RGBA) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p RGBA) Layout() Layout`: Layout is the image's pixel buffer.
- `(p RGBA) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p RGBA) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p RGBA) RGBAAt(x i64, y i64) color.RGBA`: RGBAAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut RGBA) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y) (nothing outside the bounds).
- `(p mut RGBA) SetRGBA(x i64, y i64, c color.RGBA)`: SetRGBA stores c at (x, y) (nothing outside the bounds).
- `(p RGBA) SubImage(r Rectangle) RGBA`: SubImage is the part of p inside r, sharing p's pixels.
- `(p RGBA) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type RGBA64 struct`: RGBA64 is an image of 16-bit premultiplied colors: R, G, B, A per pixel, each big-endian.
- `NewRGBA64(r Rectangle) RGBA64`: NewRGBA64 is a transparent black RGBA64 image of r.
- `(p RGBA64) ColorModel() color.Model`: ColorModel is RGBA64Model.
- `(p RGBA64) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p RGBA64) Layout() Layout`: Layout is the image's pixel buffer.
- `(p RGBA64) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p RGBA64) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p RGBA64) RGBA64At(x i64, y i64) color.RGBA64`: RGBA64At is At.
- `(p mut RGBA64) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y) (nothing outside the bounds).
- `(p mut RGBA64) SetRGBA64(x i64, y i64, c color.RGBA64)`: SetRGBA64 is Set.
- `(p RGBA64) SubImage(r Rectangle) RGBA64`: SubImage is the part of p inside r, sharing p's pixels.
- `(p RGBA64) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type NRGBA struct`: NRGBA is an image of 8-bit colors that are not premultiplied: R, G, B, A per pixel.
- `NewNRGBA(r Rectangle) NRGBA`: NewNRGBA is a transparent black NRGBA image of r.
- `(p NRGBA) ColorModel() color.Model`: ColorModel is NRGBAModel.
- `(p NRGBA) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p NRGBA) Layout() Layout`: Layout is the image's pixel buffer.
- `(p NRGBA) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p NRGBA) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y), premultiplied, in 16 bits (zero outside the bounds).
- `(p NRGBA) NRGBAAt(x i64, y i64) color.NRGBA`: NRGBAAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut NRGBA) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y), premultiplication undone (nothing outside the bounds).
- `(p mut NRGBA) SetNRGBA(x i64, y i64, c color.NRGBA)`: SetNRGBA stores c at (x, y) (nothing outside the bounds).
- `(p NRGBA) SubImage(r Rectangle) NRGBA`: SubImage is the part of p inside r, sharing p's pixels.
- `(p NRGBA) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type NRGBA64 struct`: NRGBA64 is an image of 16-bit colors that are not premultiplied: R, G, B, A per pixel, each big-endian.
- `NewNRGBA64(r Rectangle) NRGBA64`: NewNRGBA64 is a transparent black NRGBA64 image of r.
- `(p NRGBA64) ColorModel() color.Model`: ColorModel is NRGBA64Model.
- `(p NRGBA64) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p NRGBA64) Layout() Layout`: Layout is the image's pixel buffer.
- `(p NRGBA64) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p NRGBA64) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y), premultiplied (zero outside the bounds).
- `(p NRGBA64) NRGBA64At(x i64, y i64) color.NRGBA64`: NRGBA64At is the pixel at (x, y) (zero outside the bounds).
- `(p mut NRGBA64) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y), premultiplication undone (nothing outside the bounds).
- `(p mut NRGBA64) SetNRGBA64(x i64, y i64, c color.NRGBA64)`: SetNRGBA64 stores c at (x, y) (nothing outside the bounds).
- `(p NRGBA64) SubImage(r Rectangle) NRGBA64`: SubImage is the part of p inside r, sharing p's pixels.
- `(p NRGBA64) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type Huffman struct`
- `type Component struct`
- `Decode(data str) !dyn image.Image`: Decode decodes an 8-bit baseline or progressive JPEG into NRGBA64 pixels. EXIF orientation is left to the caller.
- `type Bits struct`

## image

Package image is Go's image: points and rectangles, the Image shape, and the images that keep their pixels in one byte slice (RGBA, RGBA64, NRGBA, NRGBA64, Gray, Gray16, Alpha, Alpha16, Paletted) plus Uniform. Pixels are never allocated one by one: an image is a Pix slice, a Stride and a Rect, laid out exactly as in Go.

```tin body
mut m = image.NewRGBA(image.Rect(0, 0, 640, 480))
m.Set(10, 20, m.At(0, 0))
let c = m.At(10, 20)
```

Image's At gives a pixel as color.RGBA64 (Go's RGBA64At), so reading a pixel through the shape allocates nothing; each image also has its own typed accessors (RGBAAt, GrayAt, ColorIndexAt...). Layout tells which concrete image a dyn Image is and gives its pixel buffer: it is how image/draw and image/png take their fast paths, and how a caller gets the concrete image back (AsRGBA, AsNRGBA...). The image/jpeg package decodes 8-bit baseline and progressive JPEG data and encodes baseline JPEG images.

- `type Point value struct`: Point is an (X, Y) pair; X grows to the right and Y downwards.
- `Pt(x i64, y i64) Point`: Pt is Point{X: x, Y: y}.
- `(p Point) String() str`: String is "(x,y)".
- `(p Point) Add(q Point) Point`: Add is p + q.
- `(p Point) Sub(q Point) Point`: Sub is p - q.
- `(p Point) Mul(k i64) Point`: Mul is p scaled by k.
- `(p Point) Div(k i64) Point`: Div is p divided by k (truncated toward zero).
- `(p Point) In(r Rectangle) bool`: In reports whether p is inside r (Min inclusive, Max exclusive).
- `(p Point) Mod(r Rectangle) Point`: Mod is the point of r congruent to p modulo r's width and height.
- `(p Point) Eq(q Point) bool`: Eq reports whether p and q are the same point.
- `type Rectangle value struct`: Rectangle holds the points with Min.X <= X < Max.X and Min.Y <= Y < Max.Y; it is well-formed when Min <= Max. A Rectangle is also an Image: opaque inside, transparent outside (a mask).
- `Rect(x0 i64, y0 i64, x1 i64, y1 i64) Rectangle`: Rect is the rectangle with corners (x0, y0) and (x1, y1), swapped as needed to be well-formed.
- `(r Rectangle) String() str`: String is "(x0,y0)-(x1,y1)".
- `(r Rectangle) Dx() i64`: Dx is r's width.
- `(r Rectangle) Dy() i64`: Dy is r's height.
- `(r Rectangle) Size() Point`: Size is r's width and height as a Point.
- `(r Rectangle) Add(p Point) Rectangle`: Add is r moved by p.
- `(r Rectangle) Sub(p Point) Rectangle`: Sub is r moved by -p.
- `(r Rectangle) Inset(n i64) Rectangle`: Inset is r shrunk by n on each side (negative n grows it); a side too short collapses to its midpoint.
- `(r Rectangle) Intersect(s Rectangle) Rectangle`: Intersect is the largest rectangle inside both r and s; the zero rectangle when they do not overlap.
- `(r Rectangle) Union(s Rectangle) Rectangle`: Union is the smallest rectangle holding both r and s (an empty one is ignored).
- `(r Rectangle) Empty() bool`: Empty reports whether r holds no points.
- `(r Rectangle) Eq(s Rectangle) bool`: Eq reports whether r and s hold the same points (any two empty rectangles are equal).
- `(r Rectangle) Overlaps(s Rectangle) bool`: Overlaps reports whether r and s share a point.
- `(r Rectangle) In(s Rectangle) bool`: In reports whether every point of r is in s.
- `(r Rectangle) Canon() Rectangle`: Canon is r with its corners swapped as needed to be well-formed.
- `(r Rectangle) At(x i64, y i64) color.RGBA64`: At is opaque inside r and transparent outside.
- `(r Rectangle) Bounds() Rectangle`: Bounds is r.
- `(r Rectangle) ColorModel() color.Model`: ColorModel is Alpha16Model.
- `(r Rectangle) Layout() Layout`: Layout says a Rectangle has no pixel buffer.
- `type Gray struct`: Gray is an image of 8-bit grays, one byte per pixel.
- `NewGray(r Rectangle) Gray`: NewGray is a black Gray image of r.
- `(p Gray) ColorModel() color.Model`: ColorModel is GrayModel.
- `(p Gray) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Gray) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Gray) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Gray) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p Gray) GrayAt(x i64, y i64) color.Gray`: GrayAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut Gray) Set(x i64, y i64, c color.RGBA64)`: Set stores c's luminance at (x, y) (nothing outside the bounds).
- `(p mut Gray) SetGray(x i64, y i64, c color.Gray)`: SetGray stores c at (x, y) (nothing outside the bounds).
- `(p Gray) SubImage(r Rectangle) Gray`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Gray) Opaque() bool`: Opaque is true: a gray image has no alpha.
- `type Gray16 struct`: Gray16 is an image of 16-bit grays, two big-endian bytes per pixel.
- `NewGray16(r Rectangle) Gray16`: NewGray16 is a black Gray16 image of r.
- `(p Gray16) ColorModel() color.Model`: ColorModel is Gray16Model.
- `(p Gray16) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Gray16) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Gray16) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p Gray16) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p Gray16) Gray16At(x i64, y i64) color.Gray16`: Gray16At is the pixel at (x, y) (zero outside the bounds).
- `(p mut Gray16) Set(x i64, y i64, c color.RGBA64)`: Set stores c's luminance at (x, y) (nothing outside the bounds).
- `(p mut Gray16) SetGray16(x i64, y i64, c color.Gray16)`: SetGray16 stores c at (x, y) (nothing outside the bounds).
- `(p Gray16) SubImage(r Rectangle) Gray16`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Gray16) Opaque() bool`: Opaque is true: a gray image has no alpha.
- `type Alpha struct`: Alpha is an image of 8-bit alphas (a mask), one byte per pixel.
- `NewAlpha(r Rectangle) Alpha`: NewAlpha is a transparent Alpha image of r.
- `(p Alpha) ColorModel() color.Model`: ColorModel is AlphaModel.
- `(p Alpha) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Alpha) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Alpha) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Alpha) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p Alpha) AlphaAt(x i64, y i64) color.Alpha`: AlphaAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut Alpha) Set(x i64, y i64, c color.RGBA64)`: Set stores c's alpha at (x, y) (nothing outside the bounds).
- `(p mut Alpha) SetAlpha(x i64, y i64, c color.Alpha)`: SetAlpha stores c at (x, y) (nothing outside the bounds).
- `(p Alpha) SubImage(r Rectangle) Alpha`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Alpha) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type Alpha16 struct`: Alpha16 is an image of 16-bit alphas, two big-endian bytes per pixel.
- `NewAlpha16(r Rectangle) Alpha16`: NewAlpha16 is a transparent Alpha16 image of r.
- `(p Alpha16) ColorModel() color.Model`: ColorModel is Alpha16Model.
- `(p Alpha16) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Alpha16) Layout() Layout`: Layout is the image's pixel buffer.
- `(p Alpha16) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p Alpha16) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p Alpha16) Alpha16At(x i64, y i64) color.Alpha16`: Alpha16At is the pixel at (x, y) (zero outside the bounds).
- `(p mut Alpha16) Set(x i64, y i64, c color.RGBA64)`: Set stores c's alpha at (x, y) (nothing outside the bounds).
- `(p mut Alpha16) SetAlpha16(x i64, y i64, c color.Alpha16)`: SetAlpha16 stores c at (x, y) (nothing outside the bounds).
- `(p Alpha16) SubImage(r Rectangle) Alpha16`: SubImage is the part of p inside r, sharing p's pixels.
- `(p Alpha16) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `shape Image`: Image is a rectangle of colors (Go's image.Image): At is the 16-bit premultiplied color at (x, y) (outside Bounds, the zero color, or a Paletted image's first palette color), and Layout describes the pixel buffer (Custom for an image without one).
- `type Config value struct`: Config is an image's color model and size, as a decoder reads them from the header.
- `type Kind i64`: Kind says which concrete image a Layout describes.
- `const Custom Kind = 0`: Custom is an image of another package, with no pixel buffer the image package knows.
- `const KindRGBA Kind = 1`: KindRGBA is an RGBA image.
- `const KindRGBA64 Kind = 2`: KindRGBA64 is an RGBA64 image.
- `const KindNRGBA Kind = 3`: KindNRGBA is an NRGBA image.
- `const KindNRGBA64 Kind = 4`: KindNRGBA64 is an NRGBA64 image.
- `const KindAlpha Kind = 5`: KindAlpha is an Alpha image.
- `const KindAlpha16 Kind = 6`: KindAlpha16 is an Alpha16 image.
- `const KindGray Kind = 7`: KindGray is a Gray image.
- `const KindGray16 Kind = 8`: KindGray16 is a Gray16 image.
- `const KindPaletted Kind = 9`: KindPaletted is a Paletted image.
- `const KindUniform Kind = 10`: KindUniform is a Uniform image (no pixel buffer: every pixel is its color).
- `(k Kind) String() str`: String is the kind's type name, such as "RGBA".
- `type Layout value struct`: Layout is how an image keeps its pixels: the pixel at (x, y) starts at Pix[(y-Rect.Min.Y)*Stride + (x-Rect.Min.X)*n] with n bytes per pixel (4 for RGBA and NRGBA, 8 for RGBA64 and NRGBA64, 2 for Gray16 and Alpha16, 1 otherwise; 16-bit channels are big-endian). Palette is a Paletted image's.
- `AsRGBA(m dyn Image) ?RGBA`: AsRGBA is m as the RGBA image it is (sharing its pixels), or nil.
- `AsRGBA64(m dyn Image) ?RGBA64`: AsRGBA64 is m as the RGBA64 image it is (sharing its pixels), or nil.
- `AsNRGBA(m dyn Image) ?NRGBA`: AsNRGBA is m as the NRGBA image it is (sharing its pixels), or nil.
- `AsNRGBA64(m dyn Image) ?NRGBA64`: AsNRGBA64 is m as the NRGBA64 image it is (sharing its pixels), or nil.
- `AsAlpha(m dyn Image) ?Alpha`: AsAlpha is m as the Alpha image it is (sharing its pixels), or nil.
- `AsAlpha16(m dyn Image) ?Alpha16`: AsAlpha16 is m as the Alpha16 image it is (sharing its pixels), or nil.
- `AsGray(m dyn Image) ?Gray`: AsGray is m as the Gray image it is (sharing its pixels), or nil.
- `AsGray16(m dyn Image) ?Gray16`: AsGray16 is m as the Gray16 image it is (sharing its pixels), or nil.
- `AsPaletted(m dyn Image) ?Paletted`: AsPaletted is m as the Paletted image it is (sharing its pixels and palette), or nil.
- `type Paletted struct`: Paletted is an image of palette indices, one byte per pixel, over Palette (a color.Palette held as its slice type).
- `NewPaletted(r Rectangle, p color.Palette) Paletted`: NewPaletted is a Paletted image of r over palette p, every pixel index 0.
- `(p Paletted) ColorModel() color.Model`: ColorModel is PaletteModel: the image's Palette.
- `(p Paletted) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p Paletted) Layout() Layout`: Layout is the image's pixel buffer and palette.
- `(p Paletted) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of pixel (x, y).
- `(p Paletted) At(x i64, y i64) color.RGBA64`: At is the palette color of the pixel at (x, y), premultiplied (the first palette color outside the bounds, zero for an empty palette).
- `(p Paletted) ColorIndexAt(x i64, y i64) u8`: ColorIndexAt is the palette index at (x, y) (0 outside the bounds).
- `(p mut Paletted) Set(x i64, y i64, c color.RGBA64)`: Set stores the index of the palette color nearest to c at (x, y) (nothing outside the bounds).
- `(p mut Paletted) SetColorIndex(x i64, y i64, index u8)`: SetColorIndex stores index at (x, y) (nothing outside the bounds).
- `(p Paletted) SubImage(r Rectangle) Paletted`: SubImage is the part of p inside r, sharing p's pixels and palette.
- `(p Paletted) Opaque() bool`: Opaque reports whether every palette color some pixel uses is fully opaque.
- `type Uniform struct`: Uniform is an image of one color everywhere (Go's bounds: a square of side 2e9 around the origin); it is also a color.Color.
- `NewUniform[C color.Color](c C) Uniform`: NewUniform is the image of color c everywhere.
- `(u Uniform) RGBA() (u32, u32, u32, u32)`: RGBA is the uniform color's 16-bit premultiplied channels.
- `(u Uniform) ColorModel() color.Model`: ColorModel is RGBA64Model (Go answers the Uniform itself).
- `(u Uniform) Bounds() Rectangle`: Bounds is (-1e9,-1e9)-(1e9,1e9).
- `(u Uniform) At(x i64, y i64) color.RGBA64`: At is the color, wherever.
- `(u Uniform) Layout() Layout`: Layout says a Uniform has no pixel buffer.
- `(u Uniform) Opaque() bool`: Opaque reports whether the color is fully opaque.
- `type RGBA struct`: RGBA is an image of 8-bit premultiplied colors: R, G, B, A per pixel.
- `NewRGBA(r Rectangle) RGBA`: NewRGBA is a transparent black RGBA image of r.
- `(p RGBA) ColorModel() color.Model`: ColorModel is RGBAModel.
- `(p RGBA) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p RGBA) Layout() Layout`: Layout is the image's pixel buffer.
- `(p RGBA) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p RGBA) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) in 16 bits (zero outside the bounds).
- `(p RGBA) RGBAAt(x i64, y i64) color.RGBA`: RGBAAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut RGBA) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y) (nothing outside the bounds).
- `(p mut RGBA) SetRGBA(x i64, y i64, c color.RGBA)`: SetRGBA stores c at (x, y) (nothing outside the bounds).
- `(p RGBA) SubImage(r Rectangle) RGBA`: SubImage is the part of p inside r, sharing p's pixels.
- `(p RGBA) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type RGBA64 struct`: RGBA64 is an image of 16-bit premultiplied colors: R, G, B, A per pixel, each big-endian.
- `NewRGBA64(r Rectangle) RGBA64`: NewRGBA64 is a transparent black RGBA64 image of r.
- `(p RGBA64) ColorModel() color.Model`: ColorModel is RGBA64Model.
- `(p RGBA64) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p RGBA64) Layout() Layout`: Layout is the image's pixel buffer.
- `(p RGBA64) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p RGBA64) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y) (zero outside the bounds).
- `(p RGBA64) RGBA64At(x i64, y i64) color.RGBA64`: RGBA64At is At.
- `(p mut RGBA64) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y) (nothing outside the bounds).
- `(p mut RGBA64) SetRGBA64(x i64, y i64, c color.RGBA64)`: SetRGBA64 is Set.
- `(p RGBA64) SubImage(r Rectangle) RGBA64`: SubImage is the part of p inside r, sharing p's pixels.
- `(p RGBA64) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type NRGBA struct`: NRGBA is an image of 8-bit colors that are not premultiplied: R, G, B, A per pixel.
- `NewNRGBA(r Rectangle) NRGBA`: NewNRGBA is a transparent black NRGBA image of r.
- `(p NRGBA) ColorModel() color.Model`: ColorModel is NRGBAModel.
- `(p NRGBA) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p NRGBA) Layout() Layout`: Layout is the image's pixel buffer.
- `(p NRGBA) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p NRGBA) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y), premultiplied, in 16 bits (zero outside the bounds).
- `(p NRGBA) NRGBAAt(x i64, y i64) color.NRGBA`: NRGBAAt is the pixel at (x, y) (zero outside the bounds).
- `(p mut NRGBA) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y), premultiplication undone (nothing outside the bounds).
- `(p mut NRGBA) SetNRGBA(x i64, y i64, c color.NRGBA)`: SetNRGBA stores c at (x, y) (nothing outside the bounds).
- `(p NRGBA) SubImage(r Rectangle) NRGBA`: SubImage is the part of p inside r, sharing p's pixels.
- `(p NRGBA) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type NRGBA64 struct`: NRGBA64 is an image of 16-bit colors that are not premultiplied: R, G, B, A per pixel, each big-endian.
- `NewNRGBA64(r Rectangle) NRGBA64`: NewNRGBA64 is a transparent black NRGBA64 image of r.
- `(p NRGBA64) ColorModel() color.Model`: ColorModel is NRGBA64Model.
- `(p NRGBA64) Bounds() Rectangle`: Bounds is the image's rectangle.
- `(p NRGBA64) Layout() Layout`: Layout is the image's pixel buffer.
- `(p NRGBA64) PixOffset(x i64, y i64) i64`: PixOffset is the index in Pix of the first byte of pixel (x, y).
- `(p NRGBA64) At(x i64, y i64) color.RGBA64`: At is the pixel at (x, y), premultiplied (zero outside the bounds).
- `(p NRGBA64) NRGBA64At(x i64, y i64) color.NRGBA64`: NRGBA64At is the pixel at (x, y) (zero outside the bounds).
- `(p mut NRGBA64) Set(x i64, y i64, c color.RGBA64)`: Set stores c at (x, y), premultiplication undone (nothing outside the bounds).
- `(p mut NRGBA64) SetNRGBA64(x i64, y i64, c color.NRGBA64)`: SetNRGBA64 stores c at (x, y) (nothing outside the bounds).
- `(p NRGBA64) SubImage(r Rectangle) NRGBA64`: SubImage is the part of p inside r, sharing p's pixels.
- `(p NRGBA64) Opaque() bool`: Opaque reports whether every pixel is fully opaque.
- `type Huffman struct`
- `type Component struct`
- `Decode(data str) !dyn image.Image`: Decode decodes an 8-bit baseline or progressive JPEG into NRGBA64 pixels. EXIF orientation is left to the caller.
- `type Bits struct`

## tar

Package tar reads and writes bounded ustar archives with PAX and GNU long-name extensions. Reader applies PAX records (x) to the next entry, global PAX records (g) to every later entry until a record with the same keyword replaces or empties them, and GNU long name and link entries (L, K) to the next entry; those extension entries are consumed by Next and never returned. Writer stores a name up to 100 bytes directly or splits a path at a slash into the 155-byte prefix and 100-byte name fields; otherwise, and for a link name, user or group name, uid or gid past 7 octal digits, or an mtime with a fraction or past the octal field, it writes a PAX entry before the header and truncates the ustar field. It never writes GNU records. Reader uses the supplied archive bytes; Writer buffers at most MaxArchiveSize bytes, and extension payloads are limited to MaxExtensionSize. Sparse formats are not supported.

- `const BlockSize = 512`: BlockSize is the size of a tar header and data-alignment block.
- `const MaxArchiveSize = 67108864`: MaxArchiveSize bounds archives built by Writer and accepted by the default examples.
- `const MaxExtensionSize = 1048576`: MaxExtensionSize bounds the payload of one PAX or GNU extension entry, read or written.
- `type TypeFlag enum`: TypeFlag identifies the kind of an archive entry.
- `type Header struct`: Header describes one tar archive entry; MtimeNsec is the fraction of Mtime, in nanoseconds.
- `type Reader struct`: Reader reads entries from a bounded archive in order.
- `NewReader(data []u8, maxBytes i64) !Reader`: NewReader creates a reader over an archive, rejecting inputs above limit bytes.
- `(r mut Reader) Next() !?Header`: Next advances to the next header, returning nil at the end of the archive.
- `(r mut Reader) Read(buf mut []u8) !i64`: Read returns the current entry's next bytes, or zero at its end.
- `type Writer struct`: Writer constructs a ustar archive in bounded memory, with a PAX entry before a header whose fields do not fit ustar.
- `NewWriter() Writer`: NewWriter creates an empty archive writer.
- `(w mut Writer) WriteHeader(h Header) !`: WriteHeader appends a header, preceded by a PAX entry when a field needs one; the following Write calls must provide Size bytes.
- `(w mut Writer) Write(data []u8) !i64`: Write appends file content and returns its byte count.
- `(w mut Writer) Close() !`: Close pads the final entry and writes the two zero blocks ending the archive.
- `(w Writer) Bytes() ![]u8`: Bytes returns the archive bytes after Close.

## textedit

Package textedit is the editing model behind Tinland: a text buffer with a cursor, a selection, undo and redo, search, and the syntax highlighting of Tin source. It does no I/O and draws nothing, so it runs (and is tested) on every platform; the editor program supplies the keys, the pixels and the files.

- `const KindPlain = 0`: Syntax classes of Tin source, from the edition 1 lexical rules (toolchain/docs/LANGUAGE.md): the reserved words, // comments, "strings", `raw strings` (which may run over several lines), runes, numbers with their units.
- `const KindKeyword = 1`
- `const KindString = 2`
- `const KindNumber = 3`
- `const KindComment = 4`
- `const KindConstant = 5`
- `const KindType = 6`
- `const KindFunc = 7`
- `type Span struct`: Span is the text from Start to End (byte offsets in the line) of one class.
- `Highlight(line str, raw bool) ([]Span, bool)`: Highlight classifies one line. raw says the line starts inside a raw string; the second result says it ends inside one. Text that is not in any span is plain.
- `const LangTin = 0`: Highlighting for the languages besides Tin that a project holds: the same classes (keyword, string, number, comment, constant, type, function) from the usual lexical rules of each family: C like (Go, Rust, JavaScript and TypeScript, C and C++, Java, Swift), Python, shell, JSON, YAML and TOML, and Markdown. It is a lexer for one line at a time, with a state that carries what runs over lines (a block comment, a multi-line string, a code fence).
- `const LangGo = 1`
- `const LangRust = 2`
- `const LangJS = 3`
- `const LangPython = 4`
- `const LangC = 5`
- `const LangJava = 6`
- `const LangSwift = 7`
- `const LangShell = 8`
- `const LangJSON = 9`
- `const LangYAML = 10`
- `const LangMarkdown = 11`
- `const LangPlain = 12`
- `const StateNone = 0`: What a line starts inside, for HighlightLang.
- `const StateBlock = 1`
- `const StateRaw = 2`
- `LanguageOf(path str) i64`: LanguageOf is the language of a file by its name.
- `HighlightLang(lang i64, line str, state i64) ([]Span, i64)`: HighlightLang classifies one line of a file of the language. state says what the line starts inside (StateNone, StateBlock for a /* */ comment or a Markdown code fence, StateRaw for a multi-line string); the second result is the state the next line starts in.
- `type Pos struct`: Pos is a place in the text: a line and a byte offset in it (always on a rune boundary).
- `type Buffer struct`: Buffer is the text being edited, split into lines (without their newlines), with the cursor and an optional selection from (SelRow, SelCol) to the cursor.
- `New() Buffer`: New returns an empty buffer: one empty line, the cursor at its start.
- `FromText(text str) Buffer`: FromText returns a buffer holding text; both \n and \r\n end a line.
- `(b Buffer) Text() str`: Text is the whole text, lines joined with \n.
- `(b Buffer) FileText() str`: FileText is the text as a file holds it: lines joined with \r\n when the buffer was read from CRLF text, else \n.
- `(b Buffer) Cur() Pos`: Cur is the cursor.
- `RuneAt(s str, i i64) i64`: RuneAt is the code point of the character that starts at byte i of s (0xfffd for bytes that are not UTF-8).
- `RuneWidth(r i64) i64`: RuneWidth is how many screen columns a code point takes: 2 for the East Asian wide and fullwidth characters and emoji, 0 for combining marks, 1 for everything else.
- `DisplayCol(line str, col i64, tabWidth i64) i64`: DisplayCol is the screen column of byte offset col in line: runes are one column, a tab goes to the next multiple of tabWidth.
- `ColForDisplay(line str, dcol i64, tabWidth i64) i64`: before reports whether a comes before b in the text. ColForDisplay is the byte column of the character at display column dcol of line (tabs count to the next multiple of tabWidth): where a mouse click lands.
- `(b Buffer) SelStart() Pos`: SelStart and SelEnd are the ends of the selection in text order (both the cursor when nothing is selected).
- `(b Buffer) SelEnd() Pos`
- `(b Buffer) SelectedText() str`: SelectedText is the text of the selection ("" when there is none).
- `(b mut Buffer) Undo() bool`: Undo reverts the last edit; it reports whether there was one.
- `(b mut Buffer) Redo() bool`: Redo re-applies the last undone edit; it reports whether there was one.
- `(b mut Buffer) Insert(text str)`: Insert types text at the cursor, replacing the selection; text may hold newlines.
- `(b mut Buffer) Newline()`: Newline splits the line at the cursor; the new line keeps the indentation, one more after an opening brace.
- `(b mut Buffer) Backspace()`: Backspace deletes the selection, or the rune before the cursor, or joins the line to the one above.
- `(b mut Buffer) Delete()`: Delete removes the selection, or the rune after the cursor, or joins the next line to this one.
- `(b mut Buffer) Left(extend bool)`: Left moves one rune left (to the end of the line above at the line's start).
- `(b mut Buffer) Right(extend bool)`: Right moves one rune right (to the start of the next line at the line's end).
- `(b mut Buffer) Up(extend bool)`
- `(b mut Buffer) Down(extend bool)`
- `(b mut Buffer) PageUp(n i64, extend bool)`: PageUp and PageDown move n lines.
- `(b mut Buffer) PageDown(n i64, extend bool)`
- `(b mut Buffer) Home(extend bool)`: Home goes to the first non-blank character of the line, or to the start when already there.
- `(b mut Buffer) End(extend bool)`: End goes to the end of the line.
- `(b mut Buffer) DocStart(extend bool)`: DocStart and DocEnd go to the first and the last position of the text.
- `(b mut Buffer) DocEnd(extend bool)`
- `(b mut Buffer) WordLeft(extend bool)`: WordLeft and WordRight move to the previous start and the next end of a word.
- `(b mut Buffer) WordRight(extend bool)`
- `(b mut Buffer) SelectAll()`: SelectAll selects the whole text, the cursor at its end.
- `(b mut Buffer) MoveTo(row i64, col i64, extend bool)`: MoveTo puts the cursor at row and col (clamped to the text), extending the selection when asked.
- `(b mut Buffer) Indent()`: Indent adds a tab at the start of every selected line (or the cursor's line); Unindent removes one tab or up to four spaces from each.
- `(b mut Buffer) Unindent()`
- `(b mut Buffer) Find(needle str, forward bool) bool`: Find looks for needle after the cursor (before it when backward), wrapping around the end of the text, and selects the match; it reports whether there was one.
- `(b mut Buffer) SelectNext() bool`: SelectNext selects the next occurrence of the selected text after the selection and reports whether there was one (it selects nothing without a selection): the way a repeated "select next occurrence" grows from one match to every match in the file.
- `(b mut Buffer) ReplaceSelection(text str)`: ReplaceSelection replaces the selection with text (a no-op without a selection).
- `(b mut Buffer) ToggleComment()`: ToggleComment comments every touched line with "// ", or uncomments them when all of them are commented.
- `(b mut Buffer) DeleteLine()`: DeleteLine removes the cursor's line (or every touched line).
- `(b mut Buffer) DuplicateLine()`: DuplicateLine copies the touched lines below themselves and moves the cursor into the copy.
- `(b mut Buffer) MoveLines(dir i64)`: MoveLines moves the touched lines up (dir -1) or down (dir 1) by one line, the cursor going with them.
- `(b mut Buffer) ReplaceAll(needle str, repl str) i64`: ReplaceAll replaces every occurrence of needle with repl as one undo step and returns how many there were; the cursor goes to the start of the text.
- `(b mut Buffer) SelectWordAt(row i64, col i64)`: SelectWordAt selects the word (letters, digits and underscores) around column col of row, or the one character there when it is not part of a word.
- `(b mut Buffer) SetText(text str)`: SetText replaces the whole text as one undo step, keeping the cursor on its line and column (or the nearest place that exists).
- `(b mut Buffer) JoinLines()`: JoinLines joins the current line with the line below, collapsing leading indentation into a single space.
- `(b mut Buffer) SortLines()`: SortLines sorts the touched lines (the cursor's line when nothing is selected) by their text in bytewise order, one undo step; the cursor stays on its line. sift wants a slice it may move, so the lines are copied, sorted and written back.
- `(b mut Buffer) TrimTrailingSpace()`: TrimTrailingSpace removes the spaces and tabs at the end of every touched line (the cursor's line when nothing is selected), one undo step for the whole thing.
- `(b mut Buffer) TransformCase(upper bool)`: TransformCase converts the selected text (or the word under the cursor) to uppercase or lowercase.
- `(b mut Buffer) SelectLine(row i64)`: SelectLine selects line row, including its newline when it is not the last line.

## tinjson

- `type J struct`: J is a parsed JSON value.
- `HexVal(c u8) i64`
- `Parse(text str) (J, bool)`: Parse reads one JSON value; ok is false when the text is not valid.
- `(j J) Get(key str) J`: Get is the member of an object with that key (null when there is none).
- `(j J) At(i i64) J`: At is element i of an array (null past the end).
- `(j J) Text() str`
- `(j J) Int() i64`
- `Quote(s str) str`: Quote is s as a JSON string.
- `(j J) Len() i64`: Len is the number of elements of an array (or members of an object).
- `(j J) Bool() bool`: Bool is the value of a true or false (false for anything else).
- `(j J) IsString() bool`: IsString reports whether the value is a string.
- `(j J) IsNull() bool`: IsNull reports whether the value is null (or missing).
- `(j J) IsNumber() bool`: IsNumber reports whether the value is a number.
- `(j J) Items() []J`: Items are the elements of an array.
- `(j J) Keys() []str`: Keys are the keys of an object, in the order they were written (none for another kind of value).
- `(j J) IsObject() bool`: IsObject reports whether the value is an object.

## tinsym

- `type Sym struct`: Sym is one declaration.
- `type Member struct`: Member is a line of a struct, enum or shape body: a field and its type, a variant and its payload.
- `type Diag struct`: Diag is one error.
- `type Item struct`: Item is one candidate for completion: its text, what it is (a Sym kind, or field, package, keyword) and a description.
- `Parse(out str) ([]Sym, []Diag)`: Parse reads the JSON lines of `tinc -symbols -json`: the declarations and the errors.
- `DirOf(path str) str`: DirOf is the directory part of a path.
- `LineOf(text str, n i64) str`: LineOf is line n (0-based) of text without its line break ("" past the end).
- `WordAt(text str, n i64, col i64) (str, i64, i64)`: WordAt is the identifier around byte column col of line n of text, with where it starts and ends in the line.
- `ImportsOf(text str) []str`: ImportsOf are the package names the text imports (the last element of each import path).
- `CurrentPkg(text str) str`: CurrentPkg is the package of the text: "" for main, as the compiler names it.
- `TypeParts(t str) (str, str)`: TypeParts splits a type as the compiler writes it ("mut geo.Point", "?Point", "[]str") into the package ("" when unqualified) and the name of the named type it is, or "" when it is not one (a slice, a map, a number).
- `Resolve(syms []Sym, path str, text str, n i64, col i64) []Sym`: Resolve is the declarations the word at line n, byte column col of the text can mean: after pkg. the exported name in that package; after any other dot a method of that name; otherwise a name of the text's package (in its directory), else of any package.
- `const Keywords = "break case catch const continue default defer detach else enum extern fail fn for go guard if import keep let limit map match mut package parallel range return secret shared struct switch try type var while within use on shape"`: Keywords are the reserved words.
- `Complete(syms []Sym, path str, text str, n i64, col i64) []Item`: Complete is the candidates at line n, byte column col of the text (the word being typed is not filtered out: the caller matches it): after pkg. its exported names; after another dot every method and field name (the type of the value is not known here); otherwise the package's names, the imported packages and the keywords.

## tinfmt

- `Format(src str) str`: Format returns the canonical form of the source: tabs for indentation, no trailing whitespace, at most one blank line in a row and none after an opening bracket, before a closing one or at either end of the file, and a final newline.
