"""
Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""


def return_matrix_in_spiral_order(matrix):
    spiral_order = []
    direction = 'down'

    while matrix:
        if direction == 'down':
            for lst in matrix:
                if lst == matrix[0]:
                    spiral_order.extend(lst)
                elif lst == matrix[-1]:
                    lst.reverse()
                    spiral_order.extend(lst)
                    matrix.pop()
                    direction = 'up'
                else:
                    spiral_order.append(lst.pop())

            matrix.pop(0)
        else:
            for lst in reversed(matrix):
                if lst == matrix[0]:
                    direction = 'down'
                else:
                    spiral_order.append(lst.pop(0))

    return spiral_order


print(
    return_matrix_in_spiral_order(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
)
