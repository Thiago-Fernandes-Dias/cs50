from scrabble import scrabble
from hypothesis import given
from hypothesis.strategies import text, characters

@given(text(characters(codec='ascii')))
def test_same_text(s):
    assert scrabble(f"{s}!", f"{s}?") == "Tie"

@given(text(characters(codec='ascii')))
def test_same_text_case_insensitive(s: str):
    assert scrabble(f"{s.upper()}!", f"{s.lower()}?") == "Tie"

def test_player1_wins():
    assert scrabble("COMPUTER", "science") == "Player 1"

def test_player2_wins():
    assert scrabble("red", "wheelbarrow") == "Player 2"

def test_player1_wins_1():
    assert scrabble("Scrabble", "wiNNeR") == "Player 1"