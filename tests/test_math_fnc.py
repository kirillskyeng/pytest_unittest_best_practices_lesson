import pytest
from src.math_fnc import is_prime


@pytest.mark.parametrize('number, expected', [(0, False),
                                              (1, False),
                                              (2, True),
                                              (3, True),
                                              (4, False),
                                              ])
def test_is_prime(number, expected):
    assert is_prime(number) == expected
