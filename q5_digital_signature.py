from base64 import b64encode

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


document = b"I, Alice, approve payment of 10 coins to Bob."

private_key = RSA.generate(1024)
public_key = private_key.publickey()

digest = SHA256.new(document)
signature = pkcs1_15.new(private_key).sign(digest)

print("Document:", document.decode())
print("SHA-256 digest:", digest.hexdigest())
print("Digital signature:", b64encode(signature).decode())

try:
    pkcs1_15.new(public_key).verify(SHA256.new(document), signature)
    print("Signature valid: document is authentic")
except (ValueError, TypeError):
    print("Signature invalid")
