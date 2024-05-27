points = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

def scrabble(p1: str, p2: str) -> str:
    p1_score = score(p1)
    p2_score = score(p2)
    if p1_score > p2_score:
        return "Player 1"
    elif p1_score < p2_score:
        return "Player 2"
    return "Tie"

def score(sentence: str) -> int:
    result = 0
    for s in sentence:
        if not s.isalpha():
            continue
        result += points[(ord(s.lower()) - ord('a')) % 26]
    return result
