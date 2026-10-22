
import pytest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    average,
    maximum,
    minimum,
    percentage,
    absolute_difference,
    square,
    cube,   
)

def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_add_decimal():
    assert add(2.5, 1.5) == 4.0


def test_subtract_positive():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(4, 10) == -6


def test_multiply_positive():
    assert multiply(6, 7) == 42


def test_multiply_by_zero():
    assert multiply(100, 0) == 0


def test_divide_exact():
    assert divide(10, 2) == 5


def test_divide_decimal():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_modulus_remainder():
    assert modulus(17, 5) == 2


def test_modulus_by_zero():
    with pytest.raises(ZeroDivisionError):
        modulus(10, 0)


def test_power_positive():
    assert power(2, 5) == 32


def test_power_zero_exponent():
    assert power(9, 0) == 1


def test_power_negative_exponent():
    assert power(2, -2) == 0.25


def test_average_integers():
    assert average(10, 20) == 15


def test_average_decimals():
    assert average(2.5, 3.5) == 3.0


def test_maximum():
    assert maximum(12, 20) == 20


def test_minimum():
    assert minimum(12, 20) == 12


def test_percentage():
    assert percentage(25, 200) == 12.5


def test_percentage_zero_whole():
    with pytest.raises(ValueError):
        percentage(10, 0)


def test_absolute_difference_first_greater():
    assert absolute_difference(12, 5) == 7


def test_absolute_difference_second_greater():
    assert absolute_difference(5, 12) == 7


def test_square_positive():
    assert square(6) == 36


def test_square_negative():
    assert square(-4) == 16


def test_cube_positive():
    assert cube(3) == 27


def test_cube_negative():
    assert cube(-3) == -27
