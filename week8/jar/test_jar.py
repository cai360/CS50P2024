import pytest
from jar import Jar
from unittest.mock import Mock, patch


def test_init():
    jar = Jar()
    jar = Jar(3)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(13)



def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
