def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def integer_multiplication(x: int, y: int) -> int:
    return x * y


def integer_division(x: int, y: int) -> int:
    return x // y


def max_integer_comparator(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    return 0


def min_integer_comparator(x: int, y: int) -> int:
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
