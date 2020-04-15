"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Input: [[1, 4], [0, 4]]
Output: [[0, 4]]

Input: [[1,4],[0,1]]
Output: [[0, 4]]

Input: [[1, 4], [0, 0]]
Output: [[0, 0], [1, 4]]
"""


def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        max_merged_interval = merged[-1]
        compare_interval = intervals[i]

        if (compare_interval[0] <= max_merged_interval[1]) and (
                compare_interval[1] >= max_merged_interval[1]):
            max_merged_interval[1] = compare_interval[1]
        elif (compare_interval[0] >= max_merged_interval[0]) and (
                compare_interval[1] <= max_merged_interval[1]):
            pass
        else:
            merged.append(compare_interval)

    return merged


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) ==
      [[1, 6], [8, 10], [15, 18]])
print(merge_intervals([[1, 4], [4, 5]]) == [[1, 5]])
print(merge_intervals([[1, 4], [0, 4]]) == [[0, 4]])
print(merge_intervals([[1, 4], [0, 1]]) == [[0, 4]])
print(merge_intervals([[1, 4], [0, 0]]) == [[0, 0], [1, 4]])
print(merge_intervals([[1, 4], [2, 3]]) == [[1, 4]])
