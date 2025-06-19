"""Part B
Write a function in python that returns the sum of all
 even and/or odd terms of the Fibonacci sequence that
   are inside the range defined by start and end inclusive.
Consider even numbers when even is True and disregard
 when even is False.
Consider odd numbers when odd is True and
 disregard when odd is False.
Edit the file solver.py to update the function
 solver to return the answer when called as in the below example.
The function should return None if start is greater than end."""


# This module provides a function to calculate the sum of even and/or odd Fibonacci numbers
def solver(start, end, even=True, odd=True):
    """Calculate the sum of Fibonacci numbers within a specified range."""
    if start > end:
        return None
    a, b = 1, 2
    total = 0
    while a <= end:
        if start <= a <= end:
            if even and a % 2 == 0:
                total += a
            if odd and a % 2 != 0:
                total += a
        a, b = b, a + b
    return total


if __name__ == "__main__":
    print(solver(10, 100, even=True, odd=False))
    # output: 34
    # This function calculates the sum of even Fibonacci numbers between 10 and 100
