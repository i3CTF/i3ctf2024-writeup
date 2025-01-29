import random as rd

from Crypto.Util.number import *

from FLAG import FLAG

n = len(FLAG) * 8
m = bytes_to_long(FLAG)

su = getRandomNBitInteger(512)
w = [su]

for i in range(n-1):
    w.append(rd.randint(su + 1, 3 * su))
    su += w[-1]

b = len(bin(su)) -2

assert float(n/b) < 0.645

q = getRandomInteger(su.bit_length() + 1)

r = q
while GCD(r,q) != 1:
    r = rd.randrange(2,q)

beta = list(map(lambda x: (r * x % q), w))

c = sum(beta[i] for i in range(n) if (m >> i) & 1)

print(f'beta = {beta}')
print(f'c = {c}')
