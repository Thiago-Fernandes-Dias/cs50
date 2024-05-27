def readability(text: str) -> str:
    l = s = words = letters = sentences = 0
    for c in text:
        if c == ' ':
            words += 1
        elif c in ['!', '.', '?']:
            sentences += 1
        elif c.isalpha():
            letters += 1
    words += 1 # the last word doesn't is not followed by a space
    l = 100 * letters / words
    s = 100 * sentences / words
    index = round(0.0588 * l - 0.296 * s - 15.8)
    if index > 16:
        return "Grade 16+"
    elif index < 1:
        return "Before Grade 1"
    return f"Grade {index}"
