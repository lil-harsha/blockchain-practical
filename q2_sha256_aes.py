from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Hash import SHA256


message = b"Hello World"
password = b"blockchain"

key = SHA256.new(password).digest()

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(message)

decipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = decipher.decrypt_and_verify(ciphertext, tag)

print("Message:", message.decode())
print("SHA-256 key:", key.hex())
print("Ciphertext:", b64encode(ciphertext).decode())
print("Decrypted:", decrypted.decode())
