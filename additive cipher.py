from collections import Counter
import string

def calculate_frequencies(text):
    text = text.lower()
    counts = Counter(text)
    total_letters = sum(counts.values())
    frequencies = {char: counts[char] / total_letters for char in string.ascii_lowercase}
    return frequencies

def print_possible_plaintexts(ciphertext, top_n=10):
    def decrypt_caesar(ciphertext, shift):
        decrypted = []
        for char in ciphertext:
            if char in string.ascii_lowercase:
                shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                decrypted.append(shifted)
            else:
                decrypted.append(char)
        return ''.join(decrypted)
    
    for shift in range(26):
        plaintext = decrypt_caesar(ciphertext, shift)
        frequencies = calculate_frequencies(plaintext)
        # Assuming we want to print out the decrypted texts
        print(f"Shift {shift}: {plaintext}")

ciphertext = "uifsf jt b tfdsfu ebuf"  # Example cipher text
print_possible_plaintexts(ciphertext)
