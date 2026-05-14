def build_matrix(key):
    key = key.upper().replace('J', 'I')
    chars = []
    for ch in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if ch.isalpha() and ch not in chars:
            chars.append(ch)
    return [chars[i:i + 5] for i in range(0, 25, 5)]


def find_pos(matrix, ch):
    for r, row in enumerate(matrix):
        if ch in row:
            return r, row.index(ch)
    raise ValueError(f'Character not found in matrix: {ch}')


def prepare(text):
    text = ''.join(c for c in text.upper().replace('J', 'I') if c.isalpha())
    result = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2:
        result += 'X'
    return result


def encrypt(plaintext, key):
    matrix = build_matrix(key)
    text = prepare(plaintext)
    result = ''
    for i in range(0, len(text), 2):
        r1, c1 = find_pos(matrix, text[i])
        r2, c2 = find_pos(matrix, text[i + 1])
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result


def decrypt(ciphertext, key):
    matrix = build_matrix(key)
    result = ''
    ciphertext = ''.join(c for c in ciphertext.upper().replace('J', 'I') if c.isalpha())
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(matrix, ciphertext[i])
        r2, c2 = find_pos(matrix, ciphertext[i + 1])
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result


pt = input('Plaintext: ')
key = input('Key: ')
ct = encrypt(pt, key)
print('Prepared text:', prepare(pt))
print('Encrypted:', ct)
print('Decrypted:', decrypt(ct, key))
