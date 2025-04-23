def char_to_code(char):
    if char == ' ':
        return 26
    return ord(char) - ord('a')

def code_to_char(code):
    if code == 26:
        return ' '
    return chr(code + ord('a'))

def encrypt(message, key):
    if len(key) < len(message):
        raise ValueError("The key can't be shorter than the message.")

    encrypted = []

    for message_char, key_char in zip(message, key):
        message_code = char_to_code(message_char)
        key_code = char_to_code(key_char)
        encrypted_code = (message_code + key_code) % 27
        encrypted_char = code_to_char(encrypted_code)
        encrypted.append(encrypted_char)

    return ''.join(encrypted)
