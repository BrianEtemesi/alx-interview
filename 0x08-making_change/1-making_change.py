#!/usr/bin/python3
"""
implementation of a make change function
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    # create list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each amount
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the min number of coins for the total is still infinity, return -1
    if dp[total] == float('inf'):
        return -1
    # Otherwise, return the minimum number of coins needed for the total
    return dp[total]
