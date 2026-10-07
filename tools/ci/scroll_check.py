#!/usr/bin/env python3
"""Compare scroll's token stream with Go's encoding/xml over a small real-world corpus.

Both sides read one document on stdin and print one token per line
(bench/ref/scroll and tools/ci/fixtures/scroll_twin.tin); the check compares the lines for an
RSS feed, a SOAP envelope, an S3 ListObjects response and an SVG document.
"""
import os
import subprocess
import tempfile
from pathlib import Path

from suite import ROOT

DOCS = {
    'rss': '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Tom &amp; Jerry</title>
    <link>https://example.com/feed</link>
    <item><title>One</title><pubDate>Mon, 01 Jan 2024 00:00:00 GMT</pubDate></item>
    <item><title>Two &#233;</title><guid isPermaLink="false">tag:example.com,2024:2</guid></item>
  </channel>
</rss>''',
    'soap': '''<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xml:lang="en">
  <soap:Header><auth xmlns="urn:example"><token>abc&lt;def</token></auth></soap:Header>
  <soap:Body>
    <m:GetPrice xmlns:m="urn:example:price"><m:Item>Apple</m:Item></m:GetPrice>
  </soap:Body>
</soap:Envelope>''',
    's3': '''<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Name>bucket</Name><Prefix/>
  <KeyCount>2</KeyCount><MaxKeys>1000</MaxKeys><IsTruncated>false</IsTruncated>
  <Contents>
    <Key>a&amp;b.txt</Key><LastModified>2024-01-01T00:00:00.000Z</LastModified>
    <ETag>&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</ETag><Size>0</Size>
  </Contents>
  <Contents><Key>c d.txt</Key><Size>42</Size></Contents>
</ListBucketResult>''',
    'svg': '''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
  <!-- a comment -->
  <title>Shapes</title>
  <rect x="1" y="2" width="3" height="4" fill="#fff"/>
  <text x="5" y="6">a &lt; b &amp;&amp; c &gt; d</text>
  <path d="M0 0 L10 10"/>
</svg>''',
}


def run(exe, doc):
    result = subprocess.run([str(exe)], input=doc.encode(), capture_output=True, check=True,
                            cwd=ROOT, timeout=60)
    return result.stdout.decode().splitlines()


def main():
    directory = ROOT / 'bin/ci/scroll'
    directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, TIN_ROOT=str(ROOT))
    with tempfile.TemporaryDirectory(prefix='scroll-', dir=directory) as tmp:
        work = Path(tmp)
        tin = work / 'scroll-tin'
        subprocess.run([str(ROOT / 'bin/tinc'), '-o', str(tin),
                        'tools/ci/fixtures/scroll_twin.tin'], check=True, cwd=ROOT, env=env,
                       timeout=120)
        go = work / 'scroll-go'
        subprocess.run(['go', 'build', '-o', str(go), './bench/ref/scroll'], check=True,
                       cwd=ROOT, timeout=120)
        total = 0
        for name, doc in DOCS.items():
            want = run(go, doc)
            got = run(tin, doc)
            for i, (a, b) in enumerate(zip(want, got)):
                if a != b:
                    raise AssertionError(f'scroll {name} line {i + 1}: Go {a!r}, Tin {b!r}')
            assert len(got) == len(want), f'scroll {name}: {len(got)} lines against {len(want)}'
            total += len(got)
        print(f'PASS scroll: {total} tokens over {len(DOCS)} documents match Go\'s encoding/xml '
              f'({", ".join(DOCS)})')


if __name__ == '__main__':
    main()
