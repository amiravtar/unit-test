import unittest
from calc import Calculator


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-10, 15), 5)
        self.assertEqual(self.calc.add(1, 2.5), 3.5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 3), 10 / 3)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
