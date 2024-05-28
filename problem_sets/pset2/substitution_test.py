import pytest

from substitution import substitution
from hypothesis.strategies import text, integers, booleans, characters
from hypothesis import given

@given(s=text(characters(codec='ascii')), 
       i=integers(min_value=0, max_value=25), 
       u=booleans())
def test_same_text_if_key_is_the_alphabet_insensitive(s: str, 
                                                      i: int, 
                                                      u: bool) -> None:
    key = "abcdefghijklmnopqrstuvwxyz"
    if u:
        key = key[:i] + key[i].upper() + key[i + 1:]
    assert substitution(key, s) == s

def test_proposed():
    assert substitution("YTNSHKVEFXRBAUQZCLWDMIPGJO", "Hello!") == "Ehbbq!"

@given(key=text(characters(codec='ascii')), 
       plaintext=text(characters(codec='ascii')))
def test_invalid_key(key: str, plaintext: str):
    if len(key) == 26:
        substitution(key, plaintext)
    else:
        with pytest.raises(ValueError):
            substitution(key, plaintext)