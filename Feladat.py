def char_to_code(char):
    if char == ' ':
        return 26
    return ord(char) - ord('a')

def code_to_char(code):
    if code == 26:
        return ' '
    return chr(code + ord('a'))

def encrypt(message, key):
    if not key_check(key):
        raise ValueError("The key is only allowed to contain lowercase letters of the english alphabet and space")
    if not message_check(message):
        raise ValueError("The message is only allowed to contain lowercase letters of the english alphabet and space")
    if not length_check(key, message):
        raise ValueError("The key can't be shorter than the message.")

    encrypted = []

    for message_char, key_char in zip(message, key):
        message_code = char_to_code(message_char)
        key_code = char_to_code(key_char)
        code_sum = message_code + key_code
        if (code_sum>26):
            encrypted_code = code_sum % 27
        else:
            encrypted_code = code_sum
        encrypted_char = code_to_char(encrypted_code)
        encrypted.append(encrypted_char)

    return ''.join(encrypted)

def decrypt(encryptedtext, key):

    decrypted = []

    for encryptedtext_char, key_char in zip(encryptedtext, key):
        encryptedtext_code = char_to_code(encryptedtext_char)
        key_code = char_to_code(key_char)
        code_diff = encryptedtext_code - key_code
        if (code_diff<0):
            decrypted_code = code_diff % 27
        else:
            decrypted_code = code_diff
        decrypted_char = code_to_char(decrypted_code)
        decrypted.append(decrypted_char)

    return ''.join(decrypted)

def message_check(message):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz ")
    for character in message:
        if character not in allowed_chars:
            return False
    return True

def key_check(key):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz ")
    for character in message:
        if character not in allowed_chars:
            return False
    return True

def length_check(key, message):
    if len(key) < len(message):
        return False
    return True

def encrypt_length_check(key, encryptedtext):
    if len(key) < len(encryptedtext):
        return False
    return True

message = "helloworld"
key = "abcdefgijkl"
encryptedtext = encrypt(message, key)
print(encrypt(message, key))
print(decrypt(encryptedtext, key))
