import struct

def md5_padding(message):
    original_length = len(message) * 8
    message += b'\x80'
    while (len(message) * 8 + 64) % 512 != 0:
        message += b'\x00'
    message += struct.pack('<Q', original_length)
    return message

def md5_round_function(A, B, C, D, M, s, K):
    A = (A + ((B & C) | (~B & D)) + M + K) & 0xFFFFFFFF
    A = ((A << s) | (A >> (32 - s))) & 0xFFFFFFFF
    A = (A + B) & 0xFFFFFFFF
    return A

message = b"1000"
padded_message = md5_padding(message)

print("Padded message:", padded_message.hex())
