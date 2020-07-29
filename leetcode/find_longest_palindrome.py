import unittest

"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


def find_longest_palindrome_substring(s):
    longest = ''

    for i in range(len(s)):
        odd = make_palindrome(s, i, i)
        even = make_palindrome(s, i, i + 1)
        longest = max(longest, odd, even, key=len)

    return longest


def make_palindrome(s, left, right):
    while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
        left -= 1
        right += 1

    return s[left+1:right]


class TestFindPalindrome(unittest.TestCase):
    def test_one_character(self):
        actual = find_longest_palindrome_substring('a')
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_short_string(self):
        actual = find_longest_palindrome_substring('ac')
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_long_string(self):
        actual = find_longest_palindrome_substring('babad')
        expected = 'bab'
        self.assertEqual(actual, expected)

    def test_even_string(self):
        actual = find_longest_palindrome_substring('bccd')
        expected = 'cc'
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
