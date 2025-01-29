import random as rd

import gmpy2
from Crypto.Util.number import *

flag = b'FLAG{dummy}'

rd_number = rd.getrandbits(64) | 1
p = gmpy2.next_prime(rd_number)

rd_number = rd.getrandbits(64) | 1
q = gmpy2.next_prime(rd_number)

n = p * q
e = 65537

c = pow(bytes_to_long(flag),e,n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
