# test_core.py

import unittest
from src.core import greet

class TestCore(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Developer"), "Hello, Developer! Welcome to Open Core.")

if __name__ == "__main__":
    unittest.main()
