import unittest

"""
Writing programming interview questions hasn't made me rich yet ... so I might
give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been
trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called
stock_prices, where:

the indices are the time (in minutes) past trade opening time, which was 9:30am
local time.
the values are the price (in us dollars) of one share of apple stock at that
time.
so if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

write an efficient function that takes stock_prices and returns the best profit
i could have made from one purchase and one sale of one share of apple stock
yesterday.

for example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# returns 6 (buying for $5 and selling for $11)

no "shorting"—you need to buy before you can sell. also, you can't buy and sell
in the same time step—at least 1 minute has to pass.
"""


def find_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for curr_time in range(1, len(stock_prices)):
        curr_price = stock_prices[curr_time]

        max_profit = max(max_profit, curr_price - min_price)
        min_price = min(min_price, curr_price)

    return max_profit


class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = find_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = find_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = find_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = find_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = find_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            find_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            find_max_profit([1])


unittest.main(verbosity=2)
