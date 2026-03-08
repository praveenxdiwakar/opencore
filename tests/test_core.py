import unittest
from src.core import greet, calculate_sum, calculate_product

class TestCore(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Test"), "Hello, Test! Welcome to Open Core.")

    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(3, 4), 7)

    def test_calculate_product(self):
        self.assertEqual(calculate_product(3, 4), 12)

if __name__ == "__main__":
    unittest.main()
