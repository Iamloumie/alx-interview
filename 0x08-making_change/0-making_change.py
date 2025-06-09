#!/usr/bin/python3
"""
A function to determine the fewest number of coins needed to meet a
given amount total.
"""


def makeChange(coins, total):
    """
    makeChange - returns the fewest number of coins needed to meet
      a given amount total.
    @coins: a list of the values of the coins in your possession
    @total: the total amount you need to meet
    Return: the fewest number of coins needed to meet the total,
        or -1 if it is not possible
    """
    # If the amount (total) is zero or negative,
    # there's no need for coins. Return 0.
    if total <= 0:
        return 0

    # This ensures the algorithm starts with the largest coin value,
    # which is the essence of the greedy approach.
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0

        for i in coin:          # For each coin (starting from the largest)
            while (total >= i):      # Use as many of that coin as possible
                counter += 1    # Count each coin used with counter
                total -= i      # Subtract the coin value from total

        # If total is reduced to zero, return the counter.
        # If total is not zero, it means we couldn't meet the total
        # with the given coins, so return -1.
        if total == 0:
            return counter
        return -1
