from bisect import bisect_left

"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    furthest = 0

    for hole in range(num_holes):
        distance = min([abs(hole - cafe) for cafe in cafes])

        furthest = max(furthest, distance)

    return furthest


def furthest_optimied(num_holes, cafes):
    """Optimize find longest distance for run time."""
    furthest = 0

    for hole in range(num_holes):
        idx = bisect_left(cafes, hole)

        if idx == 0:
            dist = cafes[idx] - hole
        elif idx == len(cafes):
            dist = hole - cafes[idx]
        elif cafes[idx] == hole:
            dist = 0
        else:
            dist = min(hole - cafes[idx - 1], cafes[idx] - hole)

        furthest = max(furthest, dist)

    return furthest


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED\n")
