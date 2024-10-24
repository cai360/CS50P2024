import pytest
from um import count

def main():
    test_in_vocab()
    test_captilize()
    test_with_symbal()

def test_in_vocab():
    assert count("umbralla") == 0
    assert count("yummy") == 0

def test_captilize():
    assert count("UM, I dunno") == 1
    assert count("um, I do not know, um") == 2

def test_with_symbal():
    assert count("um...I don't know, ...um") == 2

if __name__ == "__mian__":
    main()
