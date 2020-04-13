"""
2D Spiral Array

Find the pattern and complete the function:
def spiral(n):
    # Your code here.
    return spiral
where n is the size of the 2D array.

Sample Results:
input = 3
123
894
765

input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

input = 8
1 2 3 4 5 6 7 8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
"""


def create_spiral(n):
    spiral = [[0] * n for _ in range(n)]
    row = col = direction = 0
    row_dir = [0, 1, 0, -1]
    col_dir = [1, 0, -1, 0]

    for val in range(1, n * n + 1):
        spiral[row][col] = val

        row += row_dir[direction]
        col += col_dir[direction]

        if coor_invalid(spiral, row, col):
            row -= row_dir[direction]
            col -= col_dir[direction]

            direction = (direction + 1) % 4

            row += row_dir[direction]
            col += col_dir[direction]

    return spiral


def coor_invalid(spiral, row, col):
    return (
        (row < 0) or (row >= len(spiral)) or (col < 0) or (
            col >= len(spiral)) or (spiral[row][col] != 0)
    )


print(create_spiral(8))
