"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums):
    """
    Solves problem using set and tuples.
    """
    nums.sort()
    sums_to_zero = set()

    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1

        while l < r and nums[i] <= 0:
            triplet_sum = nums[i] + nums[l] + nums[r]
            if triplet_sum > 0:
                r -= 1
            elif triplet_sum < 0:
                l += 1
            else:
                sums_to_zero.add((nums[i], nums[l], nums[r]))
                r -= 1
                l += 1

    return sums_to_zero


print(three_sum([-1, 0, 1, 2, -1, -4]))
