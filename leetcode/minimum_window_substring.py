"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the
empty string "".
If there is such window, you are guaranteed that there will always be only one
unique minimum window in S.
"""


def find_substring(s, t):
    if len(t) > len(s):
        return ''

    chars_subset = []
    found = False
    for i, char in enumerate(s):
        if char in t:
            chars_subset.append((i, char))

    t_char_count = track_char_count(t)
    left = 0
    right = len(t)
    correct_window_left = 0
    correct_window_right = 0
    min_window = len(s)

    while right < len(chars_subset):
        sub = chars_subset[left:right + 1]
        sub_char_count = track_char_count_tuple(sub)

        if all(item in sub_char_count for item in t_char_count) and all(
                t_char_count[item] <= sub_char_count[item] for item in t_char_count):
            found = True
            s_left = chars_subset[left][0]
            s_right = chars_subset[right][0]

            if s_right - s_left <= min_window:
                correct_window_left = s_left
                correct_window_right = s_right
                min_window = s_right - s_left
            left += 1
        else:
            right += 1

    if found:
        return s[correct_window_left:correct_window_right + 1]
    return ''


def track_char_count(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


def track_char_count_tuple(list):
    char_count = {}
    for idx, char in list:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


# print(find_substring('ADOBECODEBANC', 'ABC'))
print(find_substring('ab', 'a'))
