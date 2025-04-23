def char_to_code(char):
    if char == ' ':
        return 26
    return ord(char) - ord('a')

def code_to_char(code):
    if code == 26:
        return ' '
    return chr(code + ord('a'))