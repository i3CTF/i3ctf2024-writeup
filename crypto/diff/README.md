---
title: diff
level: expert
flag: FLAG{Fr4nk1in-Re1t3r_R3l4t3d_M3ss4g3_4tt4ck_W4s_1t_e4sy_f0r_y0u?}
writer: IK
---

# diff

## 問題文

Let's go warm up ?

## 解法

RSA暗号の脆弱性をつく問題。

今回の場合は2つの平文、m1とm2の差が一定の値より小さく、同じ公開鍵と法数で暗号化されている場合、平文を復号することができるという攻撃「Franklin-Reiter Related Message Attack」を使用する。

攻撃の詳細については下記がおすすめ。

- [RSA 暗号を理解して有名な攻撃を試してみる](https://zenn.dev/anko/articles/ctf-crypto-rsa#%E4%B8%8A%E4%BD%8D%E3%83%93%E3%83%83%E3%83%88%E3%81%8C%E5%85%B1%E9%80%9A%E3%81%99%E3%82%8B%E4%BA%8C%E3%81%A4%E3%81%AE%E5%B9%B3%E6%96%87%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E6%9A%97%E5%8F%B7%E6%96%87%E3%82%92%E7%9F%A5%E3%82%89%E3%82%8C%E3%81%A6%E3%81%AF%E3%81%84%E3%81%91%E3%81%AA%E3%81%84-(franklin-reiter-related-message-attack))
- [SECCON CTF 13 writeup stream / reiwa_rot13](https://www.youtube.com/watch?v=KO-txEysFHU)

作問時に参考にした問題。

- SECCON CTF 13 Quals / reiwa_rot13

最終的に何を求めることができればFlagを復号できるか考える。

下記の部分から、`key`と`nonce`を求めることができたらAES暗号を復号し、Flagを手に入れることができそう。

```python
key_hash = hashlib.sha256(key).digest()
cipher = AES.new(key_hash, AES.MODE_GCM, nonce=nonce)
encrypted_flag = cipher.encrypt(flag)
```

また下記の部分から、`key`、`key2`、`nonce`を同じ法数と公開鍵で暗号化していることがわかる。

```python
c1 = pow(bytes_to_long(key), e, n)
c2 = pow(bytes_to_long(key2), e, n)
c3 = pow(bytes_to_long(nonce), e, n)
```

次にkeyの生成部分だが、`key`は英小文字10文字を重複なくランダムに生成されている。

```python
key = ''.join(rd.sample(string.ascii_lowercase, 10))
```

`key2`、`nonce`は`key`の値と`func`関数で生成されたランダムな配列（総当り可能）に基づいて生成される。

```python
def func(a, b, c, n):
    sequence = [a, b, c]
    for i in range(3, n):
        next_value = (sequence[i-1] + sequence[i-2] + sequence[i-3]) % 2**4
        sequence.append(next_value)
    return sequence

l = func(rd.randint(1, 10),rd.randint(1, 10),rd.randint(1, 10),10)
l2 = func(rd.randint(1, 10),rd.randint(1, 10),rd.randint(1, 10),10)

for i in range(len(key)):
    key2 += long_to_bytes(key[i] + l[i])

for i in range(len(key2)):
    nonce += long_to_bytes(key2[i] + l2[i])
```

ここまでのことを式に表すと下記のようになる。

$$key2 = key + α$$
$$nonce = key2 + β$$

`key`に少しの差を付与されたのが`key2`であり、その`key2`に少しの差を付与したのが`nonce`というかたちになる。

最終的にRSA暗号で暗号化し暗号文が与えられているため、「Franklin-Reiter Related Message Attack」を使用することができる。

$$c1 \equiv key^e \pmod{n}$$
$$c2 \equiv (key + diff1)^e \pmod{n}$$
$$c3 \equiv ((key + diff1) + diff2)^e \pmod{n}$$

diffをすべて列挙し「Franklin-Reiter Related Message Attack」を試していくことでFlagを得ることができる。

## solver
```python
import hashlib

from Crypto.Cipher import AES
from Crypto.Util.number import *
from tqdm import tqdm

def func(a, b, c, n):
    sequence = [a, b, c]
    for i in range(3, n):
        next_value = (sequence[i-1] + sequence[i-2] + sequence[i-3]) % 2**4
        sequence.append(next_value)
    return sequence

def franklinReiter(n, e, r, c1, c2):
    R.<x> = Zmod(n)[]
    f1 = x^e - c1
    f2 = (x + r)^e - c2
    return - polygcd(f1, f2).coefficients()[0]

def polygcd(a, b):
    if(b == 0):
        return a.monic()
    else:
        return polygcd(b, a % b)

n = 125812611979945115221928682035706228361683959586355651897879026865038436166200397949525342449234538054987997478153748697594276821005898898103048845565381869652505983771193310415824333371173405099764055250024705231294396725664851201662815929127636249682255712439537934608541374787760748381129105699166574853533
e = 137
c1 = 64345707535269330555601262411980486171117778551704279297084233657655504119977290555561518734637874332290332292263240229177163980874459306266861862202162378892326615262540909851390426775436944551416764032427687415538997782696857073234260383513934921674066154432045340274366084586427438058369972507477644605667
c2 = 63587237824494224620736543555525886576549416639747786844932664493660706815925867823636290246186609083248808996890464410321462409102705295023504165464983889848227199081272789787178593083938533515519526631619077013722041113221887408535016633712581286998250897640088713390078482469967822357211169548377434598677
c3 = 62806307091724972469516214133990870906122810630011544276172192239582489285509987431197971507264687366150902881569557808916708607942289209506373418593663680787566534770831912984128910420579059821980478636376628604430459943859688064576695441160276392530128904920975927121620027921007265910545379738842408182890
encrypted_flag = b"\xadn\xdb\xce\x05\xdf^\xa6\x05\xfd\xc9\x9ak\xde\xac\xf8L\xdd\x18w\xac\xc4\xb9X\x84\xe7\x06\xde'\x91\xeb\xa3y\x1b\xe4\xbdo<\x05g\x98\xa5u\xc9\xf3\xa4t\x80\xae\x87\xa4*&\xb1\x0bJ\x07\xf4\xbe:Rn\xbb\xc5\xe0\xf4\xdd\xed\x10\x95\xa4\xa7b[\x04H\x88\x85\xb9_"

lists = []
for i1 in range(1,11):
    for i2 in range(1,11):
        for i3 in range(1,11):
            lists.append(list(func(i1,i2,i3,10)))

diffs = []
temp = b'aaaaaaaaaa'
for i1 in range(len(lists)):
    temp2 = b''
    for i2 in range(10):
        temp2 += long_to_bytes(temp[i2] + lists[i1][i2])
    diff = bytes_to_long(temp2) - bytes_to_long(temp)
    diffs.append(diff)

for diff in tqdm(diffs):
    try:
        key = long_to_bytes(int(franklinReiter( n, e, diff, c1, c2)))
        if len(key) == 10:
            print(key)
            cnt = 0
            for diff in tqdm(diffs):
                key2 = long_to_bytes(int(franklinReiter( n, e, diff, c2, c3)))
                if len(key2) == 10:
                    print(key2)
                    nonce = b''
                    print(lists[cnt])
                    for i in range(len(key2)):
                        nonce += long_to_bytes(key2[i] + lists[cnt][i])
                    print(nonce)
                    key = hashlib.sha256(key).digest()
                    cipher = AES.new(key, AES.MODE_GCM , nonce=nonce)
                    print(cipher.decrypt(encrypted_flag))
                cnt += 1
    except:
        pass
```
