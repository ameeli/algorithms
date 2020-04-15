"""
Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Input: "abcdcboa"
Output: True

Note:
The string will only contain lowercase characters a-z. The maximum length of
the string is 50000.
"""


def is_palindrome(s, head, tail):
    while head < len(s) / 2:
        if s[head] != s[tail]:
            return False
        head += 1
        tail -= 1

    return True


def is_palindrome_possible(s):
    head = 0
    tail = -1

    while head < len(s):
        if s[head] != s[tail]:
            return any([is_palindrome(s, head + 1, tail),
                        is_palindrome(s, head, tail - 1)])
        head += 1
        tail -= 1

    return True


print(is_palindrome_possible('gmlcupuufxoohdffdhooxfuupuculmg') is True)
print(is_palindrome_possible('eeccccbebaeeabebccceea') is False)
