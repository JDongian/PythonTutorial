# Project Euler problem 3
# Largest prime factor
# We go module searching in the PyPi for what we want

from pyprimes import factors


if __name__ == "__main__":
    """
    Oftentimes, it's more about finishing the problem than getting the most
    efficient solution. Go look for the pyprimes module on PyPi and install it
    to run this code.

    TIP: PyPi has almost everything you've ever wanted. Unfortunately, Python
    hasn't fully transitioned to 3 yet.
    """
    print(max(factors(600851475143)))
