# Finding prime is slow, so we can use the fact that p and q are close to each other

import random
from Crypto.Util.number import bytes_to_long, isPrime

def getPrimes(bitsize):
    r = random.getrandbits(bitsize)
    p, q = r, r
    while not isPrime(p):
        p += random.getrandbits(bitsize//4)
    while not isPrime(q):
        q += random.getrandbits(bitsize//8)
    return p, q


m = bytes_to_long(b'Bro\'s onto nothing')
p, q = getPrimes(2048)
n = p * q
e = 65537
c = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")