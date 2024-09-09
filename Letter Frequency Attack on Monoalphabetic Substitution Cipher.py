from collections import Counter
import string

def calculate_frequencies(text):
    text = text.lower()
    counts = Counter(text)
    total_letters = sum(counts.values())
    frequencies = {char: counts[char] / total_letters for char in string.ascii_lowercase}
    return frequencies

def main():
    ciphertext = "example encrypted text"
    frequencies = calculate_frequencies(ciphertext)
    
    for char in string.ascii_lowercase:
        print(f"{char}: {frequencies.get(char, 0):.2f}")

if __name__ == "__main__":
    main()
