import pytest
from numb3rs import validate

def main():
    test_validate()

def test_validate( ):
    assert validate("car") == False
    assert validate("0.0.0.0") == True
    assert validate("255.256.0.1") == False

if __name__ == "__mian__":
    main()


