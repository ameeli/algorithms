# recursively
def merge_sort_recursive(list1, list2, merged_list=None):
    """Merge 2 sorted lists in order recursively"""
    if merged_list is None:
        merged_list = []

    if list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
        return merge_sort_recursive(list1, list2, merged_list)

    elif list1:
        merged_list.extend(list1)
        return merged_list
    elif list2:
        merged_list.extend(list2)
        return merged_list


# iteratively
def merge_sort_iterative(list1, list2):
    """Merge 2 sorted lists"""
    merged_list = []

    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))

    if list1:
        merged_list.extend(list1)
    elif list2:
        merged_list.extend(list2)

    return merged_list


# improved solution with indexing
def merge_sort_index(list1, list2):
    """Merge 2 sorted lists with O(n) space and runtime"""
    merged_list = []
    list1_index = 0
    list2_index = 0

    while (list1_index < len(list1) - 1) and (list2_index < len(list2) - 1):
        if list1[list1_index] < list2[list2_index]:
            merged_list.append(list1[list1_index])
            list1_index += 1
        else:
            merged_list.append(list2[list2_index])
            list2_index += 1

    if list1_index < len(list1) - 1:
        merged_list.extend(list1[list1_index:])
    else:
        merged_list.extend(list2[list2_index:])

    return merged_list