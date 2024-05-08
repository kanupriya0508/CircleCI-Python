import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        """Test the correctness of the Fibonacci sequence generator."""
        test_cases = [
            (0, []),
            (1, [0]),
            (2, [0, 1]),
            (5, [0, 1, 1, 2, 3]),
            (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        ]

        for n, expected_sequence in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected_sequence)

if __name__ == "__main__":
    unittest.main()
