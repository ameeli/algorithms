"""
Given this Node class, create a method that checks if a BST is valid.
A valid binary tree is one in which smaller values are to the left and larger 
values are to the right.
"""

class Node(object):
    """Node representing Binary Search Tree. Each node is a subtree of the root node."""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_valid(self):
        """Method checks if a binary tree is valid starting at the root node."""

        if not self.left and not self.right:
            return True

        if self.left:
            if self.left.data < self.data:
                left_bool = self.left.is_valid()
            else:
                return False

        if self.right:
            if self.right.data > self.data:
                right_bool = self.right.is_valid()
            else:
                return False

        return left_bool and right_bool

# Some tests for running interactively
t = Node(4, Node(2, Node(1), Node(3)),Node(6, Node(5), Node(7)))
# t.is_valid() should return True

w = Node(4, Node(2, Node(3), Node(3)), Node(6, Node(5), Node(7)))
# w.is_valid() should return False

print t
print w