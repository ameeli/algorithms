"""
Given a binary tree, find the length of the longest path where each node in the
path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges
between them.

Example 1
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the
tree is not more than 1000.
"""


def find_longest_univalue_path(node):
    longest = [0]

    def traverse(node):
        if not node:
            return 0

        left_length = traverse(node.left)
        right_length = traverse(node.right)

        if node.left and node.left.val == node.val:
            left = left_length + 1
        elif node.right and node.right.val == node.val:
            right = right_length + 1
        else:
            left = right = 0

        longest[0] = max(longest[0], left + right)
        return max(left, right)

    traverse(node)
    return longest
