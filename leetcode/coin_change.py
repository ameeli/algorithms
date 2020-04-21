"""
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [2, 4, 5], amount = 11
Output: 3
Explanation: 11 = 2 + 4 + 5
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


def coin_change(coins, amount):
    min_combos = [float('inf')] * (amount + 1)
    min_combos[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            min_combos[i] = min(min_combos[i], min_combos[i - coin] + 1)

    if min_combos[amount] != float('inf'):
        return min_combos[amount]
    return -1


print(coin_change([2, 4, 5], 11), 'expected: 3')
