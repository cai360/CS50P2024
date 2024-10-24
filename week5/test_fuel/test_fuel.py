import fuel
import pytest


def main():
    test_convert_error()
    test_convert()
    test_gauge()

def test_convert_error():
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("10/0")

def test_convert():
    assert fuel.convert("10/100") == 10

def test_gauge():
    assert fuel.gauge(10) == "10%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"

if __name__ == "__main__":
    main()
