import unittest

"""
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def find_longest_common_prefix(strs):
    if not strs:
        return ''

    longest_common_prefix = strs[0]

    for word in strs:
        curr_longest = ''
        for i in range(min(len(longest_common_prefix), len(word))):
            if longest_common_prefix[i] == word[i]:
                curr_longest += word[i]
            else:
                break

        longest_common_prefix = curr_longest

    return longest_common_prefix


class TestFindLongestCommonPrefix(unittest.TestCase):
    def test_standard(self):
        actual = find_longest_common_prefix(['flower', 'flow', 'flight'])
        expected = 'fl'
        self.assertEqual(actual, expected)

    def test_no_common_prefix(self):
        actual = find_longest_common_prefix(['dog', 'racecar', 'car'])
        expected = ''
        self.assertEqual(actual, expected)

    def test_short_prefix(self):
        actual = find_longest_common_prefix(['aa', 'a'])
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_empty_input(self):
        actual = find_longest_common_prefix([])
        expected = ''
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
