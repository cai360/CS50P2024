import pytest
from seasons import convert



def main():
    test_convert()

def test_convert():
    assert convert(366) == "Five hundred twenty-seven thousand forty minutes"
    assert convert(9099) == "Thirteen million, one hundred two thousand, five hundred sixty minutes"

if __name__ == "__main__":
    main()
