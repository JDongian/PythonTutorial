# Project Euler problem 1
# Sum the multiples of 3 or 5 below 1000
# We explore different approaches to solving the problem.

def sum_multiples0():
    """
    This is a straightforward implementation. We iterate from 1 to 999 and
    collect all the numbers divisible by 3 or 5. Then we sum them.

    TIP: Python conventions use snake_case for function and variable names.
    """
    numbers = range(1, 1000)
    results = []
    for n in numbers:
        if n % 3 == 0 or n % 5 == 0:
            results.append(n)
    return sum(results)


def sum_multiples1():
    """
    We iterated, collected, and summed in sum_multiples0. Here we iterate
    through only the multiples as opposed to all natural numbers under 1000.

    TIP: Standard spacing conventions use two newlines between methods or
    functions.
    """
    multiples_of_3 = range(0, 1000, 3)
    multiples_of_5 = range(0, 1000, 5)
    multiples_of_15 = range(0, 1000, 15)
    return sum(multiples_of_3) + sum(multiples_of_5) - sum(multiples_of_15)


def sum_multiples2():
    """
    And now we go for the one liner, just because. Note that this approach
    does only iterates from 0 to 1000 once. Generators are good.

    TIP: One liners can be short and efficient, but due to readability may
    not always be the best choice. How would you refactor this code to do
    the same thing without sacrificing runtime?
    """
    return sum((n for n in range(0, 1000) if n % 3 == 0 or n % 5 == 0))
