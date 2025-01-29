import hashlib
import random as rd
import string

from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
e = 137

def func(a, b, c, n):
    sequence = [a, b, c]
    for i in range(3, n):
        next_value = (sequence[i-1] + sequence[i-2] + sequence[i-3]) % 2**4
        sequence.append(next_value)
    return sequence

flag = b'FLAG{dummy}'
flag = pad(flag, 16)

key = ''.join(rd.sample(string.ascii_lowercase, 10))
key = key.encode()
key2 = b''
nonce = b''

l = func(rd.randint(1, 10),rd.randint(1, 10),rd.randint(1, 10),10)
l2 = func(rd.randint(1, 10),rd.randint(1, 10),rd.randint(1, 10),10)

for i in range(len(key)):
    key2 += long_to_bytes(key[i] + l[i])

for i in range(len(key2)):
    nonce += long_to_bytes(key2[i] + l2[i])

c1 = pow(bytes_to_long(key), e, n)
c2 = pow(bytes_to_long(key2), e, n)
c3 = pow(bytes_to_long(nonce), e, n)

key_hash = hashlib.sha256(key).digest()
cipher = AES.new(key_hash, AES.MODE_GCM, nonce=nonce)
encrypted_flag = cipher.encrypt(flag)

print(f'n = {n}')
print(f'e = {e}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')
print(f'c3 = {c3}')
print(f'encrypted_flag = {encrypted_flag}')
