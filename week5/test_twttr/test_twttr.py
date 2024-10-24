from twttr import shorten
import pytest

def main():
    test_vowl()
    test_upper_vowl()
    test_number()
    test_punctuation()


def test_vowl():
    assert shorten("hello") == "hll"

def test_upper_vowl():
    assert shorten("HELLO") == "HLL"

def test_number():
    assert shorten("124") == "124"

def test_punctuation():
    assert shorten(",..") == ",.."

if __name__ == main:
    main()




