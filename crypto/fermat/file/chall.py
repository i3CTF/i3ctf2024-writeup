import gmpy2
from Crypto.Util.number import *

flag = b'FLAG{dummy}'

p = getStrongPrime(2048)
q = gmpy2.next_prime(p)
n = p * q
e = 65537
c = pow(bytes_to_long(flag),e,n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')