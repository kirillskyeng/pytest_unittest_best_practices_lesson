import pytest
from src.math_fnc import is_prime, divisible_by_number


@pytest.mark.parametrize('number, expected', [(0, False),
                                              (1, False),
                                              (2, True),
                                              (3, True),
                                              (4, False),
                                              ])
def test_is_prime(number, expected):
    assert is_prime(number) == expected


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize('divisor, expected', [(1, [1, 2, 3, 4, 5, 6]),
                                               (2, [2, 4, 6]),
                                               (3, [3, 6]),
                                               (5, [5]),
                                               (7, []),
                                               ])
def test_divisible_by_number(numbers, divisor, expected):
    assert divisible_by_number(numbers, divisor) == expected


def test_divisible_by_negative_number(numbers):
    assert divisible_by_number(numbers, -2) == [2, 4, 6]


def test_divisible_by_zero(numbers):
    with pytest.raises(ZeroDivisionError):
        divisible_by_number(numbers, 0)
