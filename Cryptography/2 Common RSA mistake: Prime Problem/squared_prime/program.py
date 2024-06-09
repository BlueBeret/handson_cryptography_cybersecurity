# I am too lazy to generate another prime, I will just use the same prime for both p and q
# In fact, it's big enough to be used as n

from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

p = q = getPrime(512)
n = p*q
m = bytes_to_long(b'I don\'t even know what to say...')

e = 65537
c = pow(m, e, n)

print(f"n = {n}\ne = {e}\nc = {c}")
