import heapq


def merge_k_lists(lsts):
    """Given a list of k sorted lists, merge into one sorted list."""
    lst_idx = [0] * len(lsts)
    compare_nums = []
    merged = []

    for i, lst in enumerate(lsts):
        heapq.heappush(compare_nums, (lst[0], i))

    while compare_nums:
        min_val, min_val_lst_idx = heapq.heappop(compare_nums)
        merged.append(min_val)
        lst_idx[min_val_lst_idx] += 1

        if lst_idx[min_val_lst_idx] < len(lsts[min_val_lst_idx]):
            add_from_lst = lsts[min_val_lst_idx]
            item_idx = lst_idx[min_val_lst_idx]
            heapq.heappush(compare_nums, (
                add_from_lst[item_idx], min_val_lst_idx)
            )

    return merged


print(merge_k_lists([[2, 3, 7], [1, 5, 10], [4, 8, 9], [6]]))
