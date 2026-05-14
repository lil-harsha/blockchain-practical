KEY = [[3, 3], [2, 5]]  # determinant is 9, inverse exists modulo 26


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def mod_inverse(a, m):
    g, x, y = egcd(a % m, m)
    if g != 1:
        raise ValueError('No inverse exists')
    return x % m


def inverse_2x2(key):
    a, b = key[0]
    c, d = key[1]
    det = (a * d - b * c) % 26
    det_inv = mod_inverse(det, 26)
    return [
        [(d * det_inv) % 26, (-b * det_inv) % 26],
        [(-c * det_inv) % 26, (a * det_inv) % 26]
    ]


def process(text, key):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    if len(text) % 2:
        text += 'X'
    result = ''
    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i + 1]) - 65
        result += chr((key[0][0] * x + key[0][1] * y) % 26 + 65)
        result += chr((key[1][0] * x + key[1][1] * y) % 26 + 65)
    return result


def encrypt(plaintext):
    return process(plaintext, KEY)


def decrypt(ciphertext):
    return process(ciphertext, inverse_2x2(KEY))


pt = input('Plaintext: ')
ct = encrypt(pt)
print('Encrypted:', ct)
print('Decrypted:', decrypt(ct))
