from scrabble import scrabble

def test_player1_wins():
    assert scrabble("COMPUTER", "science") == "Player 1"

def test_player2_wins():
    assert scrabble("red", "wheelbarrow") == "Player 2"

def test_tie():
    assert scrabble("Question?", "Question!") == "Tie"

def test_player1_wins_1():
    assert scrabble("Scrabble", "wiNNeR") == "Player 1"