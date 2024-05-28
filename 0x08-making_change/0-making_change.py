#!/usr/bin/python3

"""
Solution for making change problem

"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initailize the amount table
    table = [float('inf')] * (total + 1)
    table[0] = 0

    # Compute the minimum coins required for each amount
    for coin in coins:
        for amount in range(coin, total + 1):
            if table[amount - coin] != float('inf'):
                table[amount] = min(table[amount], table[amount - coin] + 1)

    if table[total] == float('inf'):
        return -1
    return table[total]
