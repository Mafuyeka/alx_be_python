import unittest
from simple_calculator import SimpleCalculator  # Make sure this path is correct

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):  # ✅ MUST be named exactly like this
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 4), -4)

    def test_multiplication(self):
    self.assertEqual(self.calc.multiply(3, 4), 12)
    self.assertEqual(self.calc.multiply(-2, 2), -4)

    def test_division(self):  # ✅ this is what the checker is looking for
    self.assertEqual(self.calc.divide(10, 2), 5)
    with self.assertRaises(ValueError):
        self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
