# Threading, because why not. This is probably the worst algorithm possible.

import math
import concurrent.futures
from concurrent.futures import FIRST_COMPLETED
from multiprocessing import Value


# This is the way to do global variables in Python.
STEP = 20
MIN = 200000000
MAX = math.factorial(20)
# You may ask what's the point of doing math when I'm brute forcing, but the
# point of this example is to showcase multithreading.


def is_divisible(n, divisors=range(10,21)):
    """
    This function specifies a default argument for divisors. I cheat a little
    here by not dividing by every number from 1 to 20.
    """
    for divisor in divisors:
        if n % divisor != 0:
            return False
    return True


def get_first_result(numbers, function=is_divisible):
    """
    Every thread will execute this function.

    TIP: Functions need not return a value. Functions that don't explicitly
    return actually return the 'None' value.
    """
    for number in numbers:
        if is_divisible(number):
            return number


if __name__ == '__main__':
    """
    This is one of the few ways to do real threading in Python. Python
    multiprocessing is a detailed topic that has gone through many changes.

    This algorithm isn't totally correct since the first result returned may
    not be the smallest one (with a tiny probability). It also doesn't
    terminate when it gets the answer.
    """
    # split up the work
    tasks = [range(MIN + offset, MAX + 1, STEP) for offset in range(STEP)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=STEP) as executor:
        futures = [executor.submit(get_first_result, task) for task in tasks]
        future = concurrent.futures.wait(futures,
                                         return_when=FIRST_COMPLETED)[0].pop()
        print(future.result())
