def caesar_encrypt(text, shift):
    result = ''
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


plaintext = input('Plaintext: ')
shift = int(input('Shift: '))
ciphertext = caesar_encrypt(plaintext, shift)
print('Encrypted:', ciphertext)
print('Decrypted:', caesar_decrypt(ciphertext, shift))
