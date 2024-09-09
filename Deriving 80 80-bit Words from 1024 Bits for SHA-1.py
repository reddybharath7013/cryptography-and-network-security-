def sha1_expand(block):
    words = list(block)
    for i in range(16, 80):
        word = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
        words.append(((word << 1) | (word >> 31)) & 0xFFFFFFFF)  # Rotate left by 1 bit
    return words

block = [0] * 16  # Example block with 16 zeroed 32-bit words
expanded_words = sha1_expand(block)

print("W16:", hex(expanded_words[16]))
print("W17:", hex(expanded_words[17]))
print("W18:", hex(expanded_words[18]))
print("W19:", hex(expanded_words[19]))
