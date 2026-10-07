package main

// The scroll twin, Go side: read an XML document on stdin and print its token stream with
// encoding/xml's Decoder.Token, one token per line, in the format tools/ci/fixtures/scroll_twin.tin
// prints. The check (tools/ci/scroll_check.py) feeds both the same corpus and compares the lines.

import (
	"encoding/xml"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	body, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Fprintln(os.Stderr, "read:", err)
		os.Exit(1)
	}
	d := xml.NewDecoder(strings.NewReader(string(body)))
	var pendingText strings.Builder
	flush := func() {
		if pendingText.Len() > 0 {
			fmt.Println("text", pendingText.String())
			pendingText.Reset()
		}
	}
	for {
		t, err := d.Token()
		if err == io.EOF {
			flush()
			fmt.Println("done")
			return
		}
		if err != nil {
			flush()
			fmt.Println("fault", err)
			return
		}
		switch v := t.(type) {
		case xml.StartElement:
			flush()
			parts := []string{"start", v.Name.Space, v.Name.Local}
			for _, a := range v.Attr {
				parts = append(parts, a.Name.Space+":"+a.Name.Local+"="+a.Value)
			}
			fmt.Println(strings.Join(parts, " "))
		case xml.EndElement:
			flush()
			fmt.Println("end", v.Name.Space, v.Name.Local)
		case xml.CharData:
			// Adjacent character data is merged, as the Tin side merges it.
			pendingText.Write([]byte(v))
		case xml.Comment:
			flush()
			fmt.Println("comment", string(v))
		case xml.ProcInst:
			flush()
			fmt.Println("pi", v.Target, string(v.Inst))
		case xml.Directive:
			flush()
			fmt.Println("directive", string(v))
		}
	}
}
