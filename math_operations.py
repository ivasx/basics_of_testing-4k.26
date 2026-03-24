def add(a, b):
    # 1 test
    return a + b


def multiply(a, b):
    # 1 test
    return a * b


def divide(a, b):
    # 2 tests: Result, Error
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    # 2 tests: Result, Error
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return a ** 0.5


def factorial(n):
    # 2 tests: Result, Error
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_float(number):
    # 2 tests: True, False
    return isinstance(number, float)
