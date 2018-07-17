"""
Given an ordered list of numbers and a number, return the index of the largest number in the list that is smaller than that number.

For example:

>>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
2

>>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
4

>>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
1
Never find xnumber — it’s not smaller than itself!

>>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
1
If no such number exists, return None:

>>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
True
We’ve given you a stub function. Implement it:

"""


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""
    left_index = 0
    right_index = len(nums) - 1
    
    if xnumber < nums[0]:
        return None
    elif xnumber > nums[-1]:
        return len(nums) - 1
    
    while right_index - left_index > 1:
        current_index = (left_index + right_index) / 2
        if nums[current_index] < xnumber:
            left_index = current_index
        elif nums[current_index] > xnumber:
            right_index = current_index
        elif nums[current_index] == xnumber:
            return current_index - 1
                     
    return left_index


print find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
#1
print find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
#1
print find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
#4
print find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
#2