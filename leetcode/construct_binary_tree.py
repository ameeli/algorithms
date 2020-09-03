"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(preorder, inorder):
    if inorder:
        root_val = preorder.pop(0)
        root_inorder_idx = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left = construct_binary_tree(
            preorder, inorder[:root_inorder_idx])
        root.right = construct_binary_tree(
            preorder, inorder[root_inorder_idx + 1:])

        return root
