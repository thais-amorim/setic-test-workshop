#!/usr/bin/python
import pytest
from app.calculator import Calculator as c

testdata = [
    (1, 1, 2),
    (1, 0, 1),
    (5, 5, 10)
]

@pytest.mark.parametrize("x, y, expected", testdata)
class TestCalculatorClass:

    def test_add(self, x, y, expected):
        obtained = c.add(x,y)
        assert expected == obtained