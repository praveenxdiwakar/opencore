import unittest
from src.utils import reverse_string, is_even

class TestUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Open"), "nepO")

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

if __name__ == "__main__":
    unittest.main()
