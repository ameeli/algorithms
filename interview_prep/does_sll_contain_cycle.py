import unittest


def contains_cycle(first_node):
    """Given the first node of a singly linked list, check if the list has a
    cycle (when a node's next points back to a previous node)."""
    nodes_seen = set()

    if first_node:
        curr_node = first_node

        while curr_node.next:
            if curr_node in nodes_seen:
                return True
            else:
                nodes_seen.add(curr_node)
                curr_node = curr_node.next

    return False


def contains_cycle_o1_space(first_node):
    """Accomplish the above task using O(1) space by using 2 pointers advancing
    through the linked list at different speeds. If there is a cycle, the
    faster pointer will lap the slower one."""
    if first_node and first_node.next:
        slow_pointer = first_node.next
        fast_pointer = first_node.next.next

        while fast_pointer:
            if slow_pointer.value == fast_pointer.value:
                return True
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

    return False


class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def test_linked_list_with_no_cycle(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_two_node_cycle_at_end(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = fourth
        result = contains_cycle(first)
        self.assertTrue(result)

    def test_empty_list(self):
        result = contains_cycle(None)
        self.assertFalse(result)

    def test_one_element_linked_list_no_cycle(self):
        first = Test.LinkedListNode(1)
        result = contains_cycle(first)
        self.assertFalse(result)

    def test_one_element_linked_list_cycle(self):
        first = Test.LinkedListNode(1)
        first.next = first
        result = contains_cycle(first)
        self.assertTrue(result)


unittest.main(verbosity=2)
