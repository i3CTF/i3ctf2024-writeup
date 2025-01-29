---
title: crack
level: easy
flag: FLAG{F1r57_P455w0rd_Cr4ck}
writer: tare
---

# crack

## 問題文

John : Bob, what's wrong?<br>
Bob : I forgot the password to the zip file with all the important data!<br>
John : That's terrible!<br>
Bob : I thought I made the password easy...




## 解法
John the Ripper などのツールを使いzipファイルをクラックする問題。<br>

1. [John the Ripper](https://www.openwall.com/john/) をインストールする。
2. 問題文に「I thought I made the password easy...」とあるので、総当たりもしくは辞書攻撃が想定されるが総当たりが時間がかかるので、辞書攻撃を行う。
3. [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)などの辞書ファイルを用意し、クラックを行う。

4. zipファイルの中身をみるとFlagが得られる。

参考サイト<br>
[John the Ripperでzipファイルをクラックする方法](https://iomat.hatenablog.com/entry/2022/07/11/183012)