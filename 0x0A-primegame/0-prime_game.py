#!/usr/bin/python3
"""
Prime Game
"""


def primeNumbers(n):
    """
    Returns the list of prime numbers up to n using the Sieve of Eratosthenes algorithm.
    :param n: The upper limit to find prime numbers.
    :return: A list of prime numbers up to n.
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    
    return primeNos


def isWinner(x, nums):
    """
    Determines the winner of the prime game.
    :param x: The number of rounds.
    :param nums: A list of integers representing the upper limits for each round.
    :return: The name of the winner ('Maria' or 'Ben') or None if there is no winner.
    1. Maria starts first and removes a prime number from the list.
    2. Ben then removes a prime number from the list.
    3. The player who cannot make a move loses.
    4. If both players can make moves, the game continues until all primes are removed.
    5. If Maria has more rounds won than Ben, she is the winner.
    6. If Ben has more rounds won than Maria, he is the winner.
    7. If both have the same number of rounds won, there is no winner.
    :rtype: str or None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])

        if len(primeNos) % 2 == 0:
            Ben += 1

        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    
    elif Ben > Maria:
        return 'Ben'
    
    else:
        return None
