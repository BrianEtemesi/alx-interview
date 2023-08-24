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

    # Sort the coin denominations in descending order
    coins.sort(reverse=True)

    num_coins = 0
    remaining = total

    # Iterate through each coin denomination
    for coin in coins:
        # While the remaining amount is greater than/equal to the current coin
        while remaining >= coin:
            remaining -= coin  # Subtract coin value from the remaining amount
            num_coins += 1     # Increment the count of used coins

    # If the remaining amount is 0, return the number of coins used
    if remaining == 0:
        return num_coins
    else:
        return -1  # Return -1 if the total amount cannot be reached
