from plates import is_valid
import pytest

def main():
    test_lengh()
    test_first_two_letters()
    test_number0()
    test_puncture()


def test_lengh():
    #lengh 2-6
    assert is_valid("") == False
    assert is_valid("ade900") == True
    assert is_valid("afdg999") == False

def test_first_two_letters():
    assert is_valid("83") == False
    assert is_valid("aa") == True

def test_number0():
    assert is_valid("dd03") == False
    assert is_valid("dd39gj") == False

def test_puncture():
    assert is_valid("yr_3") == False

if __name__ == "__main__":
    main()
