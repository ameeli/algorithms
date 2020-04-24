"""
Implement the merge sort algorithm with optimal runtime.
"""


def merge_sort(lst):
    """Given an unsorted list, returns the sorted list using merging."""
    if len(lst) < 2:
        return lst

    mid = len(lst) / 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return make_merge(left, right)


def make_merge(lst1, lst2):
    """Given 2 lists, return one sorted list."""
    merged = []
    lst1_idx = lst2_idx = 0

    while lst1_idx < len(lst1) and lst2_idx < len(lst2):
        if lst1[lst1_idx] <= lst2[lst2_idx]:
            merged.append(lst1[lst1_idx])
            lst1_idx += 1
        else:
            merged.append(lst2[lst2_idx])
            lst2_idx += 1

    if lst1_idx < len(lst1):
        merged.extend(lst1[lst1_idx:])
    if lst2_idx < len(lst2):
        merged.extend(lst2[lst2_idx:])

    return merged


print(merge_sort([2, 1, 7, 4, 5, 3, 6, 8]))
