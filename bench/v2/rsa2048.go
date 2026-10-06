package main

import (
	"crypto"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/x509"
	"encoding/hex"
	"encoding/pem"
	"fmt"
)

// 100 RSA-2048 signatures (PKCS #1 v1.5, SHA-256) of 100 messages with one key: a TLS server's
// RSA handshake cost (#488). The signatures are deterministic, so Tin and Go print the same.
const keyPEM = `-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAt2Iy/B15ZGUz6f2+YaTZ96KNnVZ9a7BK1D8/fMLnMys4GFyr
VJftOSR5y8TkUZTHt98eyhCtSuTRfc2EhQ53bzQ1dmW4oNrmWwlF9xIcWBPk+wjI
M6n36TtqPPLVKnTeJCvpQ7GAWUDSEiA49MAdwqV7k0mY9LWUuXWjMEP2jiQfcWXp
3EdnTptcfjC+NizyrCWKr9yysPdGQshgTe+NuBcrX2SoOSQNXugIGnjI+nVE7w/U
IHCd0OSoSN4Z5xb4qJB9xzCIqEuE/ZbZ4RKCLyD6sxkNOwdwIh3a10ssrvxwvQYK
TjwS6wzWxZhPMAbFN4i/w4+IVaSmdWv6Z1otiQIDAQABAoIBADM4FbZuAwhD7e6G
ZSS/lvN/7t7Jl+k6iYPjkHdntoyHnzjKtT3A20yRAAWmXgDdNbUI+AAHDWe0JkDl
ZISHSFuCcQY7Hgiraxh1LBn4cHs3P0bQKp6nc+ssIZ2ZU2lyz9K5gwLZslf7b1EJ
t+7AM++4KZ43OaXri3kLPsONz/Dd86YvNkfU39zapvqsGej7JwQf/yBjwnnWh7Vr
LlWboqu1n+Ryq/cko9TidimU+sBiVnUeJA4LTFyq2IkXDqwI3MCO4S+QGADMndxs
XXCON1kTLB8JBMJTWMUDLz5xiAJASrQknBoPOtJK8WekLOpBORyk36etU75O8kTw
ttRkQIsCgYEA6IefUbwr/ixbozMZONIoIWzQ6334BfGX8U1ZIDFrmLhs1SDITwux
1z0VQpjv2JhTd39BLTFdN2cwYmrI42NHvXuzC9sCOBlSUVAvMna06N5LhCiaSZeY
As8AHG+gT9JZoA/Yk5gPhPP7EBNeZ6DJrw8AI9kZGeqvSMvpLGwWIT8CgYEAyeSu
EF3EfodSp9sPEMqU4ibySQ1O9eJQvoQYt8EiPhUxL1evosBkRm6ZsEEUhJdKST7D
5taxooJ4R1nTkVYXCU+DOGS7sAFDKaKXQYgBiGcuvpzwtUGh25/T+RRy9nyQgjJv
cADNwS4gjmOMhFGGbA2OOFguHqYbqE4YFyjrtzcCgYBzHuHzl1O4bMGZlKzCAtm3
YqY0UJNAbhGpd3/OfmkknPnUsnw5FjMfurAR3qGv/AomuSvNcgkSatX7g56dZQOZ
fepwzibVG0Qz2ZzkQPzj5VpBvdBU6uZpTY5ihak6m4ufwPiaacgVLK15kf1FFMeF
Ecoh9VOGDzhks/9m7MQwBQKBgQCzh/0ZZKik82UXCv9cqSi36nYta/45POUcZY8t
aDsxBdtVBB6VFYyV7SgRye2a8oYGmB/QmD4iCu82U7SFWw7lIqXHchxMqPK2hXUH
uw/R4h95NUn/hLuP95KhvgN1GNPQU1UxPiW5kXE17WQ5Dd4BHBTKGe/5JTEW+0sE
3UivBQKBgHI2J9JJlnTXhVobpnTaBQZufjrPkS3SwjkOJ8A0hUoJPekpxjUusWmE
UQ+J0ngfHBX/LcpeRbirZDNZBmtNQAoJG7fcmRATyErcnwiVdtPGfKCixrmKetkA
pQMwL8os5x/DTYjLInzNiYIAbs1lQDrxfURwdUXKAkmu+oCtlRCk
-----END RSA PRIVATE KEY-----
`

func main() {
	block, _ := pem.Decode([]byte(keyPEM))
	key, err := x509.ParsePKCS1PrivateKey(block.Bytes)
	if err != nil {
		fmt.Println(err)
		return
	}
	acc := sha256.Sum256(nil)
	for i := 0; i < 100; i++ {
		digest := sha256.Sum256([]byte(fmt.Sprintf("message %d", i)))
		sig, err := rsa.SignPKCS1v15(nil, key, crypto.SHA256, digest[:])
		if err != nil {
			fmt.Println(err)
			return
		}
		acc = sha256.Sum256(append(acc[:], sig...))
	}
	fmt.Println(hex.EncodeToString(acc[:]))
}
