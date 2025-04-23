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
    if len(key) < len(message):
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

message = "helloworld"
key = "abcdefgijkl"
print(encrypt(message, key))