import unittest
from parameterized import parameterized
from src.math_fnc import is_prime


class TestIsPrime(unittest.TestCase):
    @parameterized.expand([(0, False),
                           (1, False),
                           (2, True),
                           (3, True),
                           (4, False),
                           ])
    def test_is_prime(self, number, expected):
        self.assertEqual(is_prime(number), expected)
