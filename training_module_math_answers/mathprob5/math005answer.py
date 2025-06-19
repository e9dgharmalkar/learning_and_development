"""Problem 5
2520 is the smallest number that can be divided by each
 of the numbers from 1 to 10 without any remainder.
Part A
What is the smallest positive number that is
 evenly divisible by all of the numbers from 1 to 20?
Edit the file answer.py and update the function 
answer() to return the answer."""
from functools import reduce
from math import gcd


def lcm(a, b):
    """
    Compute the Least Common Multiple (LCM) of two integers a and b."""

    return abs(a * b) // gcd(a, b)


def answer():
    """Find the smallest positive number that is evenly divisible by all
    of the numbers from 1 to 20."""
    return reduce(lcm, range(1, 21))


if __name__ == "__main__":
    print(answer())
    # This function calculates the smallest positive number
    #  that is evenly divisible by all numbers from 1 to 20
    # output: 232792560
    # It uses the reduce function to apply the lcm function
    #  across the range of numbers from 1 to 20
