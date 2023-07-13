#!/usr/bin/python3
"""
calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def get_factor(n):
    """
    get sum of prime factors of n or n if n is prime
    """
    i = 2
    j = 0

    while i <= n:
        if n % i == 0:
            n = n // i
            j += i
            i -= 1
        i += 1
    return j


def minOperations(n):
    """
    returns the fewest number of operations needed
    """

    if not isinstance(n, int) or n < 2:
        return 0
    return get_factor(n)
