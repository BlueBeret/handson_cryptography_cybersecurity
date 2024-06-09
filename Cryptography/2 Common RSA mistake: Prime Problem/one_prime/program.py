# Why would I need two prime if I can just use one?

from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

p = getPrime(512)

n = p
e = 65537
m = bytes_to_long(b'{this_is_not_real_message}')
c = pow(m, e, n)

print(f"n = {n}\ne = {e}\nc = {c}")
