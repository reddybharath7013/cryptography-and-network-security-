from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def triple_des_encrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(data)

def triple_des_decrypt(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.decrypt(ciphertext)

key = get_random_bytes(24)  # 24-byte key for Triple DES
plaintext = b"Data123456"  # 8-byte block for DES3
ciphertext = triple_des_encrypt(key, plaintext)
decrypted = triple_des_decrypt(key, ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def triple_des_encrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.encrypt(data)

def triple_des_decrypt(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    return cipher.decrypt(ciphertext)

key = get_random_bytes(24)  # 24-byte key for Triple DES
plaintext = b"Data123456"  # 8-byte block for DES3
ciphertext = triple_des_encrypt(key, plaintext)
decrypted = triple_des_decrypt(key, ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
