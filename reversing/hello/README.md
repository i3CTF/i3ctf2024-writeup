---
title: hello
level: beginner
flag: FLAG{Th3_5tr1ngs}
writer: IK
---

# hello

## 問題文

For starters

## 解法

`strings`コマンドを使用して解く問題。

まず、`file`コマンドでどのようなファイルか確認する。

```shell
file hello
hello: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), statically linked, no section header
```

実行してみる。

```shell
./hello
FLAG{is_not_here^v^}
Flag is with i3ctf.
```

`strings`コマンドを実行してみる。

```shell
strings hello
UPX!
tdoPC
...
```

`upx`で圧縮されているため、展開してから`strings`コマンドを実行する

```shell
upx -d hello | strings hello
...
garbage_content_grape666
placeholder_words_honey777
i3ctf_F_is_here
random_string_alpha
...
```

明らかにダミーな文字列の中で「i3ctf」の文字を見つけることができる。

先程の実行結果である「Flag is with i3ctf.」のヒントを加味すると、i3ctfで`grep`することでFlagが手に入ると予想する。

```shell
strings hello | grep i3ctf
Flag is with i3ctf.
i3ctf_F_is_here
i3ctf_L_is_here
i3ctf_A_is_here
i3ctf_G_is_here
i3ctf_{_is_here
i3ctf_T_is_here
i3ctf_h_is_here
i3ctf_3_is_here
i3ctf___is_here
i3ctf_5_is_here
i3ctf_t_is_here
i3ctf_r_is_here
i3ctf_1_is_here
i3ctf_n_is_here
i3ctf_g_is_here
i3ctf_s_is_here
i3ctf_}_is_here
```

Flagを手に入れることができた。