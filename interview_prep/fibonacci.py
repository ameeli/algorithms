import unittest

"""
Compute the nth fibonacci number.
"""


def compute_fibonacci(n):
    if n == 0 or n == 1:
        return n

    return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)


def compute_finonacci_memo(n, memo=None):
    if not memo:
        memo = [0] * (n + 1)

    if n == 0 or n == 1:
        return n

    if memo[n] == 0:
        memo[n] = compute_finonacci_memo(
            n - 1, memo) + compute_finonacci_memo(
            n - 2, memo)

    return memo[n]


class TestFibonacci(unittest.TestCase):
    test_cases = [(0, 0), (1, 1), (13, 233), (25, 75025)]

    def test_compute_fibonacci(self):
        for n, ans in self.test_cases:
            self.assertEqual(compute_fibonacci(n), ans)

    def test_compute_fibonacci_memo(self):
        for n, ans in self.test_cases:
            self.assertEqual(compute_finonacci_memo(n), ans)


if __name__ == '__main__':
    unittest.main(verbosity=2)
