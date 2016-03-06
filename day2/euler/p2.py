# Project Euler problem 2
# Sum the even Fibonacci numbers.
# We introduce decorators.
#
# Read technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/
# for more on calculating Fibonacci numbers in python.
# Read http://www.python-course.eu/python3_memoization.php for more on
# decorators in this situation.

import collections
import functools


class memoized(object):
    """
    Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    Copied from https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize

    TIP: Documentation of a function inside the function is referred to as a
    'docstring'. The current standard of docstring formatting is detailed in
    PEP 0287 and PEP 0257.
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


@memoized
def fibonacci(n):
    """
    The Python decorator syntax modifies the function quietly. The __call__
    method in decorator is invoked with fibonacci as its argument, and wraps
    the function such that the result is memoized.
    """

    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_sum():
    """
    It's nice knowing that that there isn't a massive calculation happening
    every time we call fibonacci(n). Our unclever code is quite efficient.
    """

    result = 0
    n = 0
    while fibonacci(n) < 4000000:
        if fibonacci(n) % 2 == 0:
            result += fibonacci(n)
        n += 1
    return result


if __name__ == "__main__":
    """
    __name__ refers to the name assigned to the running file as assigned by
    the Python interpreter. When you run a script from the command line,
    Python sets __name__ to '__main__'. This means the print statement is
    only invoked when you run this function as a script, and not when you
    include this file in another file.
    """

    print(fibonacci_sum())
