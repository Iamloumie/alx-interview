#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

from typing import List


def factorize(n: int) -> List[int]:
    """
    This function returns the fewest number of operations needed to result
    in exactly n H characters in the file
    Returns the prime factorization of n.
    """
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors


def minOperations(n: int) -> int:
    """Return the minimum number of operations to reach n from 1."""
    if n <= 1:
        return 0
    factors = factorize(n)
    return sum(factors)
