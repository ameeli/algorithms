import heapq

def merge_k_lists(lsts):
    """Given a list of k sorted lists, merge into one sorted list."""
    k = len(lsts)
    indices = [0 for i in xrange(k)]
    merged = []
    compare_nums = []

    for i, lst in enumerate(lsts):
        heapq.heappush(compare_nums, (lst[0], i))

    while compare_nums:
        min_num, min_idx = heapq.heappop(compare_nums)
        merged.append(min_num)
        indices[min_idx] += 1

        if indices[min_idx] < len(lsts[min_idx]):
            heapq.heappush(compare_nums, (lsts[min_idx][indices[min_idx]], min_idx))

    return merged


print merge_k_lists([[1, 5, 10], [2, 3, 7], [4, 8, 9]])