"""
Given a string, find the length of the longest substring without repeating 
characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence 
             and not a substring.
"""

def lengthOfLongestSubstring(s):
    """Given a string, return the length of the longest substring without 
    repeating chars."""
    max_count = start_idx = curr_idx = 0
    curr_letters = set()

    while curr_idx < len(s):
        if (s[curr_idx] in curr_letters):
            start_idx += 1
            curr_idx = start_idx
            curr_letters.clear()
        else:
            curr_letters.add(s[curr_idx])
            curr_idx += 1
            max_count = max(max_count, curr_idx - start_idx)

    return max_count