from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# Generate 2 prime numbers: p and q

# Calculate modulus, n = p * q

# Calculate φ(n), phi = (p-1) * (q-1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1

# Calculate d such that d * e = 1 mod phi

# Encrypt the message, c = m^e mod n

# Decrypt the message, m = c^d mod n
