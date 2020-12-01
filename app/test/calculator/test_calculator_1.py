#!/usr/bin/python
import pytest
from app.calculator import Calculator as c


def test_add():
    x = 1
    y = 2
    expected = 3

    obtained = c.add(x,y)
    assert expected == obtained
    
def test_subtract():
    x = 1
    y = 2
    expected = -1

    obtained = c.subtract(x,y)
    assert expected == obtained
    
def test_multiply():
    x = 1
    y = 2
    expected = 2

    obtained = c.multiply(x,y)
    assert expected == obtained
    
def test_divide():
    x = 1
    y = 2
    expected = 0.5

    obtained = c.divide(x,y)
    assert expected == obtained