"""
You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

Example:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) i.e. 617 + 295
Output: 2 -> 1 -> 9 i.e. 912
"""


def sum_linked_lists(llist1, llist2):
    """
    Look at the first node on llist1, add the data with first node on llist2
    keep track of the tenth place if there is one to carry onto the next
    addition, make note of the answer in new llist
    """

