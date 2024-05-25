import pytest
from cash import cash

def test_penne():
    assert cash(1) == 1

def test_nickle():
    assert cash(5) == 1

def test_dime():
    assert cash(10) == 1

def test_quarter():
    assert cash(25) == 1

def test_zero():
    assert cash(0) == 0

def test_negative():
    with pytest.raises(ValueError):
        cash(-1)

def test_70():
    assert cash(70) == 4

def test_113():
    assert cash(113) == 8