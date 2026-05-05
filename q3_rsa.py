p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

message = "A"
m = ord(message)

cipher = pow(m, e, n)
plain = pow(cipher, d, n)

print("p:", p)
print("q:", q)
print("n:", n)
print("phi:", phi)
print("Public key (e, n):", (e, n))
print("Private key (d, n):", (d, n))
print("Message:", message)
print("Encrypted:", cipher)
print("Decrypted:", chr(plain))
