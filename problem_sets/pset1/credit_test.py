import pytest

from credit import credit

def test_visa():
    assert credit("4003600000000014") == "VISA"

def test_visa1():
    assert credit("4111111111111111") == "VISA"

def test_visa2():
    assert credit("4012888888881881") == "VISA"

def test_mastercard():
    assert credit("5196285159966449") == "MASTERCARD"

def test_mastercard1():
    assert credit("5352432590799795") == "MASTERCARD"

def test_mastercard2():
    assert credit("5251263802936756") == "MASTERCARD"

def test_amex():
    assert credit("378282246310005") == "AMEX"

def test_amex1():
    assert credit("378734493671000") == "AMEX"

def test_invalid1():
    assert credit("6176292929") == "INVALID"

def test_not_numeric_string():
    with pytest.raises(ValueError):
        credit("378734-49367-1000")
    

