def shift(letter, shift_amount):
    MAX_KEY_SIZE = 126
    unicode_value = ord(letter) + shift_amount
    new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ''
    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    return encrypt(message,-1 * shift_amount)

secret_message = "helloO how are YOU!?~"
encrypted_message = encrypt(secret_message, 5)

print(encrypted_message)
