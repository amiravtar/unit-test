from calc import Calculator
import pytest


@pytest.fixture
def calc() -> Calculator:
    calc = Calculator()
    return calc


def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(-1, -1) == 0


def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10


class Test_divide:
    def test_divide1(self):
        calc = Calculator()
        assert calc.divide(5, 2) == 2.5
        assert calc.divide(5, 1) == 5
        assert calc.divide(5, -1) == -5
        try:
            calc.divide(5, 0)
        except ValueError as e:
            str(e) == "Cannot divide by zero"

    @pytest.mark.xfail()
    def test_divide_fail(self, calc):
        calc = Calculator()
        calc.divide(5, 0)


@pytest.mark.parametrize("nums", [((1, 2), 3), ((5, -5), 0), ((2, 3.5), 5.5)])
def test_add_param(calc, nums: tuple[tuple[int, int], int]):
    assert calc.add(nums[0][0], nums[0][1]) == nums[1]
