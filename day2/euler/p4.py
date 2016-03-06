# Project Euler problem 4
# Largest palindrome product
# Welcome to typecasting in Python

from itertools import combinations_with_replacement


def is_palindrome(n):
    """This, while not the most efficient, is too easy."""
    return str(n) == str(n)[::-1]


def largest_palindrome():
    """
    The biggest plus of this solution is that we stop on the first result,
    with no wasted brute forcing.

    TIP: Many small functions are better than few big functions.
    """
    trials = combinations_with_replacement(range(999, 99, -1), 2)
    # We sort the products so we can stop on the first number that is a
    # palindrome.
    products = sorted([a * b for (a, b) in trials], reverse=True)
    # If you were to take the product of an arbitrary list of numbers, the
    # following expression may be more appropriate:
    # [functools.reduce(operator.mul, trial, 1) for trial in trials]

    for product in products:
        if is_palindrome(product):
            return product


if __name__=='__main__':
    print(largest_palindrome())
