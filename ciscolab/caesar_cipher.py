"""Using caesar cipher to encrypt a message"""

def encrypt(message: str):
    encrypted = ""
    for char in message:
        if not char.isalpha():
            encrypted += char
            continue
        code = ord(char)
        match code:
            case 90: code = 64
            case 122: code = 96
            case _: pass
        encrypted += chr(code + 1)
    return encrypted

def decrypt(message: str):
    decrypted = ""
    for char in message:
        if not char.isalpha():
            decrypted += char
            continue
        code = ord(char)
        match code:
            case 65: code = 91
            case 97: code = 123
            case _: pass
        decrypted += chr(code - 1)
    return decrypted

# print(encrypt("I love you baby"))
# print(decrypt(encrypt("I love you baby")))