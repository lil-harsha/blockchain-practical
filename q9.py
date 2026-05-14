def encrypt(text, rails):
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


def decrypt(ciphertext, rails):
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


pt = input('Plaintext: ')
rails = int(input('Number of rails: '))
ct = encrypt(pt, rails)
print('Encrypted:', ct)
print('Decrypted:', decrypt(ct, rails))
