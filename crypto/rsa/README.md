---
title: rsa
level: beginner
flag: FLAG{0SS1FR4G3}
writer: IK
---

# rsa

## 問題文

Do you know how the RSA cipher works?

## 解法

一般的なRSA暗号の問題。

今回の場合、pとqのbit数が少ないためnを素因数分解することで秘密鍵を求めることができる。

1. nを素因数分解して、pとqを求める。
2. pとqとeから秘密鍵を求める。
3. 秘密鍵を使って、暗号文cを復号する。

## solver
```python
import math

import sympy
from Crypto.Util.number import *

n = 89765553359668267846115148791526510167
e = 65537
c = 43726401623720020767763547639229741559

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

factors = sympy.factorint(n)
factors = list(factors.keys())

p = factors[0]
q = factors[1]
d = extended_gcd(e,lcm(p-1,q-1))[1]
decrypted_flag = pow(c,d,n)

# phi = (p-1) * (q-1)
# d = pow(e,-1,phi)
# decrypted_flag = pow(c,d,n)

print(long_to_bytes(decrypted_flag))
```
