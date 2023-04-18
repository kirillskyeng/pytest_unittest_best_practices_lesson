import unittest
from parameterized import parameterized
from src.math_fnc import is_prime, divisible_by_number


class TestIsPrime(unittest.TestCase):
    @parameterized.expand([(0, False),
                           (1, False),
                           (2, True),
                           (3, True),
                           (4, False),
                           ])
    def test_is_prime(self, number, expected):
        self.assertEqual(is_prime(number), expected)


class TestDivisibleByNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.numbers = [1, 2, 3, 4, 5, 6]

    @parameterized.expand([(1, [1, 2, 3, 4, 5, 6]),
                           (2, [2, 4, 6]),
                           (3, [3, 6]),
                           (5, [5]),
                           (7, []),
                           ])
    def test_divisible_by_number(self, number, expected):
        self.assertEqual(divisible_by_number(self.numbers, number), expected)

    def test_divisible_by_negative_number(self):
        """Проверяем, что функция корректно обрабатывает отрицательные числа."""
        self.assertEqual(divisible_by_number(self.numbers, -2), [2, 4, 6])

    def test_divisible_by_zero(self):
        """Проверяем, что функция выдает ошибку при попытке деленя на 0."""
        with self.assertRaises(ZeroDivisionError):
            divisible_by_number(self.numbers, 0)

