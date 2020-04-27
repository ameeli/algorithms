"""
Given two binary trees, find if they are mirror images of each other.
  1                      1
2   3                  3   2
   4 1                1 4

"""


def mirror_binary_trees(tree1, tree2):
    if tree1.value != tree2.value:
        return False
    else:
        mirror_binary_trees(tree1.left, tree1.right)
        mirror_binary_trees(tree1.right, tree1.left)

    return True
