import unittest

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def verify_valid_parens(s):
    open_brackets = []
    parens_map = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket not in parens_map:
            open_brackets.append(bracket)
        else:
            if (not open_brackets) or (
                    open_brackets.pop() != parens_map[bracket]):
                return False

    return not open_brackets


class TestVerifyValidParens(unittest.TestCase):
    def test_valid(self):
        actual = verify_valid_parens('{[]}')
        expected = True
        self.assertEqual(actual, expected)

    def test_invalid(self):
        actual = verify_valid_parens('([)]')
        expected = False
        self.assertEqual(actual, expected)

    def test_extra_opens(self):
        actual = verify_valid_parens('({')
        expected = False
        self.assertEqual(actual, expected)

    def test_extra_close(self):
        actual = verify_valid_parens('}')
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
