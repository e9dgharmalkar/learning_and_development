"""Part A
Find the sum of all the multiples of 3 or 5 below 1000.

Edit the file answer.py and update the
function sum_of_multiples to return the answer.

sum_of_multiples()
Part B
Write a function in python that returns the
 sum of all the multiples of a list of factors
   where the multiples are between the start
   and end, inclusive.

Edit the file solver.py to update the function sum_
of_multiples which returns the answer when called
as in the below example.

sum_of_multiples([3, 5, 12], 400, 1842)
"""


def sum_of_multiples():
    """Return the sum of all multiples of 3 or 5 below 1000 that are multiples of either."""
    return sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)


if __name__ == "__main__":
    print(sum_of_multiples())
# output: 233168
# This function calculates the sum of all multiples of 3 or 5 below 1000
# It uses a generator expression to iterate through the range from 1 to 999
