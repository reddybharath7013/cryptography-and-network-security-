import math

def columnar_transposition_encrypt(plaintext, key):
    n = len(key)
    columns = [''] * n

    for i, char in enumerate(plaintext):
        columns[i % n] += char

    cipher = ''.join([''.join(col) for col in columns])
    return cipher

def columnar_transposition_decrypt(ciphertext, key):
    n = len(key)
    rows = math.ceil(len(ciphertext) / n)
    columns = [''] * n

    for i in range(n):
        columns[i] = ciphertext[i * rows: (i + 1) * rows]

    plaintext = ''.join([''.join(row) for row in zip(*columns)])
    return plaintext

key = "4312"  # Column indices based on the key
plaintext = "thisisplaintext"
ciphertext = columnar_transposition_encrypt(plaintext, key)
decrypted = columnar_transposition_decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
