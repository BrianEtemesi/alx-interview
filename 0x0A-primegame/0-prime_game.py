#!/usr/bin/python3
"""
This script defines a function isWinner to determine the winner between
Maria and Ben in a game based on prime numbers.

Parameters:
    x (int): The number of rounds to play.
    nums (list of ints): A list of positive integers representing the
    upper bounds for each round.

Returns:
    str: The name of the winner ('Maria' or 'Ben') or None if there's no
    winner.

"""


def isWinner(x, nums):
    """
    takes two parameters: x and nums, then determins winner
    """

    # Check if x is less than 1 or if the nums list is empty
    if not nums or x < 1:
        return None

    # Initialize counters for Maria's and Ben's wins
    marias_wins = 0
    bens_wins = 0

    # Find the maximum number in the nums list
    n = max(nums)

    # Create a list of boolean values to represent prime numbers from 1 to n
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False  # 1 is not a prime number

    # Sieve of Eratosthenes: Mark multiples of each prime number as non-prime
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Iterate through the rounds
    for _, n in zip(range(x), nums):
        # Count the number of prime numbers in the range [1, n]
        primes_count = len(list(filter(lambda x: x, primes[0: n])))

        # Update wins based on whether the count of primes is even or odd
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the winner based on the number of wins
    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return 'Maria'
    else:
        return 'Ben'
