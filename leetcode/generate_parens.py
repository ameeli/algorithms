import unittest

"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generate_parens(n):
    complete_combos = []

    def make_combos(combo='', left=0, right=0):
        if len(combo) == n * 2:
            complete_combos.append(combo)
            return
        if left < n:
            make_combos(combo + '(', left + 1, right)
        if right < left:
            make_combos(combo + ')', left, right + 1)

    make_combos()
    return complete_combos


class TestGenerateParens(unittest.TestCase):
    def test_three(self):
        actual = generate_parens(3)
        expected = [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]

        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
