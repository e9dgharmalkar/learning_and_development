"""Part B
Write a function in python that returns the largest
 prime factor of a given number.
Edit the file solver.py to update the function solver
 to return the answer when called as in the below example."""


def solver(value):
    """Return the largest prime factor of a given value."""
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            value //= factor
        else:
            factor += 1
    # When the loop ends, value is prime
    return value


if __name__ == "__main__":
    print(solver(600851475143))
    # This function calculates the largest prime factor of 600851475143
    # output: 6857
    # It uses a while loop to divide the number by its smallest factor until it becomes prime
