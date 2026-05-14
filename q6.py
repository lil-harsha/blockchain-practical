import string

ALPHABET = string.ascii_uppercase
MONO_KEY = 'QWERTYUIOPASDFGHJKLZXCVBNM'


def mono_encrypt(plaintext):
    plaintext = plaintext.upper()
    return ''.join(MONO_KEY[ALPHABET.index(c)] if c in ALPHABET else c for c in plaintext)


def mono_decrypt(ciphertext):
    ciphertext = ciphertext.upper()
    return ''.join(ALPHABET[MONO_KEY.index(c)] if c in MONO_KEY else c for c in ciphertext)


def vigenere_encrypt(plaintext, key):
    result = ''
    key = key.upper()
    key_index = 0
    for ch in plaintext.upper():
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += ch
    return result


def vigenere_decrypt(ciphertext, key):
    result = ''
    key = key.upper()
    key_index = 0
    for ch in ciphertext.upper():
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
            key_index += 1
        else:
            result += ch
    return result


print('1. Monoalphabetic cipher')
print('2. Polyalphabetic cipher (Vigenere)')
choice = input('Choose option (1/2): ').strip()

if choice == '1':
    pt = input('Plaintext: ')
    ct = mono_encrypt(pt)
    print('Encrypted:', ct)
    print('Decrypted:', mono_decrypt(ct))
elif choice == '2':
    pt = input('Plaintext: ')
    key = input('Key word: ')
    ct = vigenere_encrypt(pt, key)
    print('Encrypted:', ct)
    print('Decrypted:', vigenere_decrypt(ct, key))
else:
    print('Invalid choice')
