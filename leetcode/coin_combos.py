"""
Given coins of different denominations and a total amount of money, write
a function to compute the number of combinations that make up that amount.

Example
Input: [1, 2, 5], 12
Output: 13
"""


def find_total_combos(coins, amount):
    combos = [0] * (amount + 1)
    combos[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            combos[i] += combos[i - coin]

    return combos[amount]


print(find_total_combos([1, 2, 5], 12), 'expected: 13')
