from hypothesis import given
from hypothesis.strategies import text, characters

from caesar import caesar

@given(text(characters(codec='ascii')))
def test_key_26(s: str):
    assert caesar(26, s) == s

def test_hello_key_1():
    assert caesar(1, "HELLO") == "IFMMP"

def test_key_13():
    assert caesar(13, "Hi there!") == "Uv gurer!"
