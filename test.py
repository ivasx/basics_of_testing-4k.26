import pytest
from math_operations import *
from string_operations import *


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide_result():
    assert divide(6, 3) == 2


def test_divide_error():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8


def test_square_root_result():
    assert square_root(9) == 3


def test_square_root_error():
    with pytest.raises(ValueError):
        square_root(-4)


def test_factorial_result():
    assert factorial(5) == 120


def test_factorial_error():
    with pytest.raises(ValueError):
        factorial(-1)


def test_is_float_true():
    assert is_float(3.14) is True


def test_is_float_false():
    assert is_float(5) is False


def test_capitalize_name():
    assert capitalize_name('ivas') == 'Ivas'


def test_contains_substring_true():
    assert contains_substring('hello world', 'world') is True


def test_contains_substring_false():
    assert contains_substring('hello world', 'python') is False


def test_is_palindrome_true():
    assert is_palindrome('madam') is True


def test_is_palindrome_false():
    assert is_palindrome('hello') is False