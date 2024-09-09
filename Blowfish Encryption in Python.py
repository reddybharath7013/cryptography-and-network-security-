from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

def blowfish_encrypt(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    return cipher.encrypt(data)

def blowfish_decrypt(key, ciphertext):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    return cipher.decrypt(ciphertext)

key = get_random_bytes(16)
plaintext = b"Data1234"  # Blowfish requires 8-byte blocks
ciphertext = blowfish_encrypt(key, plaintext)
decrypted = blowfish_decrypt(key, ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
