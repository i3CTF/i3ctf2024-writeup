---
title: pqrneca
level: easy
flag: FLAG{IxMxq1SgIyMBIIMGI0q4G1MeIaABEyWlIJgjoSIHZQx}
writer: IK
---

# pqrneca

## 問題文

The characters are these guys!

## 解法

式にしてみると下記のようになる。

$$a = \left( (p + q + r)^{(p - 1)(q - 1)(r - 1)} \mod n \right) \cdot \left( (p + q + r) \mod n \right)$$

一見、複雑そうだが、左の部分（下記）は[オイラーの定理](https://mathlandscape.com/euler-theorem/)により、1となる。
$$\left( (p + q + r)^{(p - 1)(q - 1)(r - 1)} \mod n \right)$$

右の部分（下記）は、常に $p + q + r < pqr$ が成り立つため、$p + q + r$ となる。

$$\left( (p + q + r) \mod n \right)$$

つまり、 $a = p + q + r$ が成り立つ。

rは総当たりをすることができるので下記の連立式を解くことでpとqを求めることができる。

$a = p + q$<br>$n = pq$ 

作問時に参考にした問題
- [wanictf2023-writeup/cry
/pqqp](https://github.com/wani-hackase/wanictf2023-writeup/tree/main/cry/pqqp)

## solver
```python
from Crypto.Util.number import *
from sympy import *
from tqdm import tqdm

n = 7894997768843371051574283923889875949721549839948585431580528447785849377661136272711123916225949784565233102445109630200343891690246762600340629461935948515407628802882457327053777870536555165662186532079820972702954015707071221070209358667015358289159157419015372445758520554044321210772301888768815760388448403
e = 65537
c = 6281522859197520614425409590475837816922605179191893610058697196067537825716766495028792492058040491214412166881301355310380609363649895438105952796445812639877335162580538764889271710182530354193361284113009767902488689490066322103879429684251062356174055644278678270417287815150325455601016928165357679401805198
a = 25399154773300599428558856611099482336783148755690795638447359076396917531510107618424856270044438660480517767775671272426470020074846949629619656297238653

primes_in_range = list(primerange(32768, 65536)) # 0b1000000000000000 = 32768 ~ 0b1111111111111111 = 65536

for r in tqdm(primes_in_range):
    p, q = var('p q')
    eq1 = Eq(p + q + r, a)  # p + q + r = a
    eq2 = Eq(p * q * r, n)  # p * q * r = n
    try:
        result = solve((eq1, eq2), (p, q))
        p = result[0][0]
        q = result[0][1]
        phi = (p - 1) * (q - 1) * (r -1)
        d = pow(e,-1,int(phi))
        flag = long_to_bytes(pow(c,d,n))
        if b'FLAG' == flag[:4]:
            print(flag)
            break
    except:
        pass
```
