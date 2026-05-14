def caesar(text, shift):
    result = ''
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result


def rail_encrypt(text, rails):
    if rails <= 1:
        return text
    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1
    for ch in text:
        fence[rail] += ch
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return ''.join(fence)


def rail_decrypt(ciphertext, rails):
    if rails <= 1:
        return ciphertext
    pattern = []
    rail = 0
    direction = 1
    for _ in ciphertext:
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    counts = [pattern.count(r) for r in range(rails)]
    chunks = []
    index = 0
    for count in counts:
        chunks.append(list(ciphertext[index:index + count]))
        index += count
    result = ''
    for r in pattern:
        result += chunks[r].pop(0)
    return result


def encrypt(plaintext, shift, rails):
    after_caesar = caesar(plaintext.upper(), shift)
    return rail_encrypt(after_caesar, rails)


def decrypt(ciphertext, shift, rails):
    after_rail = rail_decrypt(ciphertext, rails)
    return caesar(after_rail, -shift)


pt = input('Plaintext: ')
shift = int(input('Caesar shift: '))
rails = int(input('Rail count: '))
ct = encrypt(pt, shift, rails)
print('Encrypted:', ct)
print('Decrypted:', decrypt(ct, shift, rails))
