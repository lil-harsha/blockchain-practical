def encrypt(plaintext, key):
    plaintext = ''.join(ch for ch in plaintext.upper() if ch.isalpha())
    cols = len(key)
    rows = (len(plaintext) + cols - 1) // cols
    padded = plaintext.ljust(rows * cols, 'X')
    grid = [padded[i * cols:(i + 1) * cols] for i in range(rows)]
    order = sorted(range(cols), key=lambda i: key[i])
    return ''.join(row[col] for col in order for row in grid)


def decrypt(ciphertext, key):
    cols = len(key)
    rows = len(ciphertext) // cols
    order = sorted(range(cols), key=lambda i: key[i])
    grid = [[''] * cols for _ in range(rows)]
    index = 0
    for col in order:
        for r in range(rows):
            grid[r][col] = ciphertext[index]
            index += 1
    return ''.join(''.join(row) for row in grid)


pt = input('Plaintext: ')
key_text = input('Key digits, for example 4312567: ')
key = [int(ch) for ch in key_text]
ct = encrypt(pt, key)
print('Encrypted:', ct)
print('Decrypted:', decrypt(ct, key))
