import unittest
"""
Given a list of integers, find the highest product you can get from three of
the integers.
"""


def highest_product_of_3(list_of_ints):
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_prod_of_2 = lowest_prod_of_2 = list_of_ints[0] * list_of_ints[1]
    highest_prod_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        curr_num = list_of_ints[i]

        highest_prod_of_3 = max(highest_prod_of_3,
                                highest_prod_of_2 * curr_num,
                                lowest_prod_of_2 * curr_num)

        highest_prod_of_2 = max(highest_prod_of_2,
                                highest * curr_num,
                                lowest * curr_num)
        lowest_prod_of_2 = min(lowest_prod_of_2,
                               highest * curr_num,
                               lowest * curr_num)

        highest = max(highest, curr_num)
        lowest = min(lowest, curr_num)

    return highest_prod_of_3


class Test(unittest.TestCase):
    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
