---
title: Matryoshka
level: easy
flag: FLAG{Mr_decode_master}
writer: tare
---

# Matryoshka

## 問題文

I can't read it as it is!



## 解法
複数のデコードを行う問題。<br>

1. 次の順番にデコードするとFlagが得られる(base62以降の「〇〇->」は削除する)<br>
base64<br>
↓<br>
base62<br>
↓<br>
base58<br>
↓<br>
base45<br>
↓<br>
base32<br>
↓<br>
base16<br>
↓<br>
uuencode

使用したサイト<br>
[CyberChef](https://gchq.github.io/CyberChef/)

[base16 decoder](https://simplycalc.com/base16-decode.php)

[uuencode方式エンコード、デコード変換](https://www.motohasi.net/Misc/UUConv.php)