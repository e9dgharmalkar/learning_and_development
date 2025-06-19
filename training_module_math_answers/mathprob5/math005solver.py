"""Part B
Write a function in python that returns the smallest positive
 number that is evenly divisible by all of the numbers between
   the range p and q, inclusive.
Use the range from the lesser of p and q to the greater of p
 and q. Make no assumption about which is lesser or greater.
Edit the file solver.py to update the function solver to return
 the answer when called as in the below example."""

from functools import reduce
from math import gcd


def lcm(a, b):
    """Compute the Least Common Multiple (LCM) of two integers a and b."""

    return abs(a * b) // gcd(a, b)


def solver(p, q):
    """Find the smallest positive number that is evenly divisible by all
    the numbers between p and q (inclusive)."""

    low = min(p, q)
    high = max(p, q)
    return reduce(lcm, range(low, high + 1))


if __name__ == "__main__":
    print(solver(1, 20))
    # This function calculates the smallest positive number
    # that is evenly divisible by all numbers from 1 to 20
    # output: 232792560
    # It uses the reduce function to apply the lcm function
    # across the range of numbers from p to q (inclusive)
