import unittest
import subprocess

class TestCLI(unittest.TestCase):

    def test_greet_cli(self):
        result = subprocess.run(
            ["python", "src/cli.py", "--greet", "Tester"], capture_output=True, text=True
        )
        self.assertIn("Hello, Tester! Welcome to Open Core.", result.stdout)

if __name__ == "__main__":
    unittest.main()
