import pytest
from working import convert


def main():
    test_convert()


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

    with pytest.raises(ValueError):
        convert("8:60 AM to 4:90 PM")
    with pytest.raises(ValueError):
        convert("9:00 PM 4:00 PM")



if __name__ == "__main__":
    main()

