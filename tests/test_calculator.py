"""Tests for the calculator module."""
import pytest

from src.calculator import add, subtract, multiply, divide, power, factorial


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_add_mixed_sign(self):
        assert add(10, -3) == 7

    def test_add_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_add_zero(self):
        assert add(0, 5) == 5


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_negative_result(self):
        assert subtract(3, 7) == -4

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(100, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_multiply_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_returns_float(self):
        assert isinstance(divide(7, 2), float)

    def test_divide_negative_numbers(self):
        assert divide(-8, 4) == -2.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestPower:
    def test_power_positive_exponent(self):
        assert power(2, 10) == 1024

    def test_power_zero_exponent(self):
        assert power(999, 0) == 1

    def test_power_one_base(self):
        assert power(1, 100) == 1

    def test_power_negative_exponent(self):
        assert power(2, -1) == pytest.approx(0.5)


class TestFactorial:
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120

    def test_factorial_large(self):
        assert factorial(10) == 3628800

    def test_factorial_negative_raises(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-1)

    def test_factorial_non_integer_raises(self):
        with pytest.raises(TypeError, match="only defined for integers"):
            factorial(3.5)
