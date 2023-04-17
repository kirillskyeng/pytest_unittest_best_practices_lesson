def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def divisible_by_number(numbers: list[int], divisor: int) -> list[int]:
    """Находит элементы, которые без остатка делятся на переданное число."""
    return [n for n in numbers if n % divisor == 0]
