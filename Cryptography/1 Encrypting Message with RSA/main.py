from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

m = b"Hello, it's secret message"
m = bytes_to_long(m)

# Generate 2 prime numbers: p and q
p = getPrime(512)
q = getPrime(512)

# Calculate modulus, n = p * q
n = p * q

# Calculate φ(n), phi = (p-1) * (q-1)
phi = (p-1) * (q-1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 65537

# Calculate d such that d * e = 1 mod phi
d = pow(e, -1, phi)

# n, e, d
# public key: (e, n)
# private key: (d, n)


# Encrypt the message, c = m^e mod n
c = pow(m, e, n)
# print("public key: ", e, n)
# print("private key: ", d, n)
# print("Encrypted message: ", c)
# print(long_to_bytes(c))

# Decrypt the message, m = c^d mod n
m = pow(c, d, n)
print(m)
print(long_to_bytes(m))