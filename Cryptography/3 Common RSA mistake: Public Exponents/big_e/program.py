# ░▒▓████████▓▒░ 
# ░▒▓█▓▒░        
# ░▒▓█▓▒░        
# ░▒▓██████▓▒░   
# ░▒▓█▓▒░        
# ░▒▓█▓▒░        
# ░▒▓████████▓▒░ 

# Okay, apparently I small e with big N is not safe, but what about big e with big N?

from Crypto.Util.number import getPrime, bytes_to_long, inverse
from random import getrandbits
from math import gcd


m = bytes_to_long(b"https://www.youtube.com/watch?v=Qskm9MTz2V4")

def get_huge_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        d = getrandbits(512)
        if (3*d)**4 > N and gcd(d,phi) == 1 and d < 9223372036854775807:
            e = inverse(d, phi)
            break
    return N,e


N, e = get_huge_RSA()
c = pow(m, e, N)

print(f'N = {hex(N)}')
print(f'e = {hex(e)}')
print(f'c = {hex(c)}')