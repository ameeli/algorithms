import unittest
"""
Write an efficient function that takes stock_prices and returns the best profit
I could have made from one purchase and one sale of one share of stock
yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

No "shorting"—you need to buy before you can sell. Also, you can't buy and sell
in the same time step—at least 1 minute has to pass.
"""


def get_max_profit(stock_prices):
    max_profit = stock_prices[1] - stock_prices[0]
    buy_idx = 0

    while buy_idx < len(stock_prices) - 1:
        sell_idx = buy_idx + 1

        while sell_idx < len(stock_prices):
            profit = stock_prices[sell_idx] - stock_prices[buy_idx]
            if profit > max_profit:
                max_profit = profit
            sell_idx += 1

        buy_idx += 1

    return max_profit


class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
