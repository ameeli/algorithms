"""Determine whether an integer is a palindrome. An integer is a palindrome when 
it reads the same backward as forward. 

***Solve this without turning the integer into a string.*** 

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 
121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def isPalindrome(num):
    """
    :type x: int
    :rtype: bool
    """
    reverse_num = 0
    holder_num = num
    
    if num < 0:
        return False
    while holder_num > 0:
        digit = holder_num % 10
        reverse_num = reverse_num * 10 + digit
        holder_num /= 10
        
    return num == reverse_num 