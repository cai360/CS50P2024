from bank import value
import pytest

def main():
    test_0()
    test_20()
    test_100()

def test_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value(" Hello") == 0

def test_20():
    assert value("hi") ==20
    assert value("HI") == 20
    assert value(" HI") == 20

def test_100():
    assert value("djif") == 100
    assert value("Dear") == 100


if __name__ == "__main__":
    main()

