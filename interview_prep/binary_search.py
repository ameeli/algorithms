"""
Given a sorted array of intergers and an target integer, return the index of
the target integer. If the target in not found, return None.
"""

def binary_search(lst, num):
    left = 0 
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) / 2
        if lst[mid] == num:
            return mid 
        elif lst[mid] > num:
            right = mid - 1
        elif lst[mid] < num:
            left = mid + 1

    return None