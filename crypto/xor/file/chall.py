import hashlib
import random
import string

from Crypto.Util.number import bytes_to_long, long_to_bytes

flag = b'kore_ha_dummy_desu_anata_ha_tadori_tuku_beki_da_FLAG{dummy}'

key = random.choice(string.printable.strip()).encode()

hash = hashlib.blake2b(flag).hexdigest()

enc = b''

for i in range(len(flag)):
    a = flag[i] ^ bytes_to_long(key)
    enc += long_to_bytes(a)

print(f'enc = {enc}')
print(f'hash = {hash}')