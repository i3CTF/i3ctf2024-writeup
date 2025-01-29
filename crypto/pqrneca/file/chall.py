from Crypto.Util.number import *

flag = b"FLAG{dummy}"

p = getPrime(512)
q = getPrime(512)
r = getPrime(16)

n = p * q * r

e = 65537

c = pow(bytes_to_long(flag),e,n)
a = pow(p + q + r, (p - 1) * (q - 1) * (r - 1), n) * ((p + q + r) % n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
print(f'a = {a}')
