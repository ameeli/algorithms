import unittest

"""
I have a list of n + 1n+1 numbers. Every number in the range 1..n1..n appears
once except for one number that appears twice.

Write a function for finding the number that appears twice.
"""


def find_repeat(numbers_list):
    n = len(numbers_list) - 1
    no_duplicate_sum = (n ** 2 + n) / 2
    actual_sum = sum(numbers_list)

    return actual_sum - no_duplicate_sum


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
