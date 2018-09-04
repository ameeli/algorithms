"""
Given an array of integers, return indices of the two numbers such that they add 
up to a specific target. You may assume that each input would have exactly one 
solution, and you may not use the same element twice.
"""

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    to_add = {}
    
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in to_add:
            return to_add[remainder], i
        to_add[nums[i]] = i