import unittest


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    next_take_out_order = next_dine_in_order = 0

    for served_order in served_orders:
        if (next_take_out_order < len(take_out_orders)) and (
                served_order == take_out_orders[next_take_out_order]):
            next_take_out_order += 1
        elif (next_dine_in_order < len(dine_in_orders)) and (
                served_order == dine_in_orders[next_dine_in_order]):
            next_dine_in_order += 1
        else:
            return False

    if (next_take_out_order != len(take_out_orders)) or (
            next_dine_in_order != len(dine_in_orders)):
        return False

    return True


class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served(
            [1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served(
            [1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served(
            [27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)


unittest.main(verbosity=2)
