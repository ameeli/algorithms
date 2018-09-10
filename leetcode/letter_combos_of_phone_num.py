"""
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in 
any order you want.
"""

def letter_combinations(digits):
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(digit_to_letters[digits])
    prev = letter_combinations(digits[:-1])
    additional = digit_to_letters[digits[-1]]
    return [s + c for s in prev for c in additional]