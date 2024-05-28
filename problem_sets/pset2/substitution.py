def substitution(key: str, plaintext: str) -> str:
    if len(key) != 26:
        raise ValueError("Key must contain 26 characters")
    result = ""
    for c in plaintext:
        if not c.isalpha():
            result += c
            continue
        key_char = key[alphabet_index(c)]
        result += key_char.upper() if c.isupper() else key_char.lower() 
    return result

def alphabet_index(char: str) -> int:
    assert len(char) == 1 and char.isalpha()
    return (ord(char.lower()) - ord('a')) % 26