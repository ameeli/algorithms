import unittest
from collections import deque


def get_path(graph, start_node, end_node):
    """Find the shortest path between the start_node and end_node."""
    if start_node not in graph:
        raise Exception('Start node not found in graph')
    if end_node not in graph:
        raise Exception('End node not found in graph')

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    steps = {start_node: None}

    while nodes_to_visit:
        curr_node = nodes_to_visit.popleft()

        if curr_node == end_node:
            return retrace_steps(steps, end_node)

        for neighbor in graph[curr_node]:
            if neighbor not in steps:
                nodes_to_visit.append(neighbor)
                steps[neighbor] = curr_node

    return None


def retrace_steps(steps, node):
    path = []
    curr_node = node

    while curr_node:
        path.append(curr_node)
        curr_node = steps[curr_node]

    path.reverse()
    return path


class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
