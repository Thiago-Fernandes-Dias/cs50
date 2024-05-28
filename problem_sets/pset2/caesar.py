def caesar(key: int, text: str) -> str:
    result = ""
    for c in text:
        if not c.isalpha():
            result += c
            continue
        base_char = 'A' if c.isupper() else 'a'
        cipher_char_code = (ord(c) + key - ord(base_char)) % 26 + ord(base_char)
        result += chr(cipher_char_code)
    return result
