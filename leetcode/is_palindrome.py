"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: True
Example 2:

Input: "race a car"
Output: False
"""


def is_palindrome(s):
    only_alnum = ''.join(char for char in s if char.isalnum())
    lower_alnum = only_alnum.lower()

    head_idx = 0
    tail_idx = -1

    while head_idx < len(lower_alnum) / 2:
        if lower_alnum[head_idx] != lower_alnum[tail_idx]:
            return False
        head_idx += 1
        tail_idx -= 1

    return True


print(is_palindrome('A man, a plan, a canal: Panama'), True)
print(is_palindrome('race a car'), False)
