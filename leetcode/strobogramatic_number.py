"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees 
(looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is 
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""

def is_strobogrammatic(number):
    """Given and integer, return true if integer is strobogrammatic."""
    input = str(number)
    strobs = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    
    if len(input) == 1:
        if input not in strobs or input == '6' or input == '9':
            return False
    
    for i, j in zip(range(len(input)), range(len(input) - 1, 0, -1)):
        if input[i] not in strobs:
            return False
        elif strobs[input[i]] != input[j]:
            return False
            
    return True   