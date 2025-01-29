from Crypto.Util.number import *

flag = b'FLAG{dummy_dummy}'
length = len(flag)

p = getStrongPrime(2048)
q = getStrongPrime(2048)
n = p * q
e = 3
c = pow(pow(pow(pow(bytes_to_long(flag),e,n),e,n),e,n),-1,n)

print(f'length = {length}')
print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
