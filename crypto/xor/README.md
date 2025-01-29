---
title: xor
level: beginner
flag: FLAG{z3br4s_ar3_als0_x0r}
writer: IK
---

# xor

## 問題文

Let's go warm up !

## 解法

排他的論理和の性質を使った問題。

今回の場合、ランダムに選ばれたkey（1文字）がFlagの文字列1文字ずつを排他的論理和で暗号化している。

排他的論理和は同じ値で行うことで、効果を打ち消すことができる性質を持っている。（詳しくは[このブログ](https://ikbase.net/blog/2024/05/04/key-xor/)を参照）

なので、同じkeyで排他的論理和をし直せば復号することができる。

keyは1文字であるため総当たりが可能。

```python
key = random.choice(string.printable.strip()).encode()`
```

総当たりでFlagを求める。


## solver
```python
import string
import hashlib

from Crypto.Util.number import bytes_to_long,long_to_bytes

enc = b'\x12\x16\x0b\x1c&\x11\x18&\x1f\x15\x18\x1e&\x1d\x1c\n\x0c&\x18\x17\x18\r\x18&\x11\x18&\r\x18\x1d\x16\x0b\x10&\r\x0c\x10\r\x18&\x17\x16&\x1d\x18&?58>\x02\x03J\x1b\x0bM\n&\x18\x0bJ&\x18\x15\nI&\x01I\x0b\x04'
hash = '50806af7b4cb65abe94969ce3a3f8792d8205bb250b12117e56dcd79b048205aa74d7087ed1984e8a8d071ce9606f9e56e9cd1a5ebd19057a47d49a3c2ee291b'

for key in string.printable:
    dec = b''
    for i in range(len(enc)):
        b = enc[i] ^ bytes_to_long(key.encode())
        dec += long_to_bytes(b)
    hash_dec = hashlib.blake2b(dec).hexdigest()
    if hash_dec == hash:
        print(dec)
        break
```
