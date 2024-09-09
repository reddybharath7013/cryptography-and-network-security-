def substitution_cipher(text, key):
    alphabet = string.ascii_lowercase
    table = str.maketrans(alphabet, key)
    return text.translate(table)

def main():
    key = "bcdefghijklmnopqrstuvwxyza"  # Example key
    plaintext = "hello"
    ciphertext = substitution_cipher(plaintext, key)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
