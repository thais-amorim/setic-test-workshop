import pytest
from app.calculator import BubbleSort

testdata = [
    ([], []),
    ([7], [7]),
    ([7, 5], [5, 7]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 5, 1, 4], [1, 3, 4, 5]),
    ([3, 3, 3, 3], [3, 3, 3, 3]),
    ([191, 2, 73, 1, 7, 3, 5], [1, 2, 3, 5, 7, 73, 191]),
    (['C', 'B', 'D'], ['B', 'C', 'D']),
    ([-9, 0, 1, 5, 3, -1, 4, 2], [-9, -1, 0, 1, 2, 3, 4, 5]),
    ([-16, -3, -55], [-55, -16, -3])
]


@pytest.mark.parametrize("original, expected", testdata)
class TestSortClass:

    def test_bubble_sort(self, original, expected):
        algo = BubbleSort()
        obtained = algo.sort(original)

        assert expected == obtained