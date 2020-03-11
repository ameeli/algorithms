"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """
    nums = set(nums)

    for i in range(1, max_num + 1):
        if i not in nums:
            return i


def missing_number_min_runtime(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_min_runtime([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8

    """
    expected_sum = sum(range(max_num + 1))
    actual_sum = sum(nums)

    return expected_sum - actual_sum

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS.\n")
