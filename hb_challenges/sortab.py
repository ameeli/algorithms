"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    a_idx = 0
    b_idx = 0
    merged = []

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            merged.append(a[a_idx])
            a_idx += 1
        elif a[a_idx] > b[b_idx]:
            merged.append(b[b_idx])
            b_idx += 1
        else:
            merged.extend(a[a_idx], b[b_idx])
            a_idx += 1
            b_idx += 1

    merged.extend(a[a_idx:])
    merged.extend(b[b_idx:])

    return merged


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
