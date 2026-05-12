import unittest
from utils import ErrorAnalyzer


class TestErrorAnalyzer(unittest.TestCase):

    def test_absolute_error_basic(self):
        self.assertEqual(ErrorAnalyzer.absolute_error(100, 95), 5)

    def test_absolute_error_zero_difference(self):
        self.assertEqual(ErrorAnalyzer.absolute_error(50, 50), 0)

    def test_absolute_error_negative_direction(self):
        self.assertEqual(ErrorAnalyzer.absolute_error(95, 100), 5)

    def test_relative_percentage_error_basic(self):
        self.assertAlmostEqual(ErrorAnalyzer.relative_percentage_error(100, 95), 5.0)

    def test_relative_percentage_error_zero_difference(self):
        self.assertAlmostEqual(ErrorAnalyzer.relative_percentage_error(50, 50), 0.0)

    def test_relative_percentage_error_negative_direction(self):
        self.assertAlmostEqual(ErrorAnalyzer.relative_percentage_error(95, 100), 5.263157894736842)

    def test_relative_percentage_error_raises_on_zero_true_value(self):
        with self.assertRaises(ValueError):
            ErrorAnalyzer.relative_percentage_error(0, 10)


if __name__ == "__main__":
    unittest.main()
