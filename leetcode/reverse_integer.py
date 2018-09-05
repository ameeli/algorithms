"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""

# string and list solution
def reverse(self, x):
    """Given an integer, return the reverse not exceeding within 32 bit signed
    integer range."""
    if x > 0:
        digits = [digit for digit in str(x)]
        reversed_digits = digits[::-1]
        reversed_int = int(''.join(reversed_digits))
        if reversed_int > 2**31:
            return 0
        return reversed_int
    else:
        x = -x
        digits = [digit for digit in str(x)]
        reversed_digits = digits[::-1]
        reversed_int = -int(''.join(reversed_digits))
        if reversed_int < -2**31:
            return 0
        return reversed_int


# mathematical solution
def reverse(x):
    """Given an integer, return the reverse not exceeding within 32 bit signed
    integer range."""
    reverse = 0
    
    if x > 0:
        while x != 0:
            digit = x % 10
            x /= 10
            if (reverse > 2**31 / 10) or (reverse == 2**31 / 10 and digit > 7):
                return 0         
            reverse = reverse * 10 + digit
    else:
        x = -x
        while x != 0:
            digit = x % 10
            x /= 10
            if (reverse > 2**31 / 10) or (reverse == 2**31 / 10 and digit > 7):
                return 0          
            reverse = reverse * 10 + digit
        reverse = -reverse
        
    return reverse
