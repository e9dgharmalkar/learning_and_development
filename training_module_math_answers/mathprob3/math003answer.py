"""Problem 3
The prime factors of 13,195 are 5, 7, 13, and 29.
Part A
What is the largest prime factor
 of the number 600,851,475,143?
Edit the file answer.py and update the function
 answer() to return the answer."""


def answer():
    """Return the largest prime factor of 600851475143."""
    num = 600851475143
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            num //= factor
        else:
            factor += 1
    # When the loop ends, num is prime
    return num


if __name__ == "__main__":
    print(answer())
    # This function calculates the largest prime factor of 600851475143
    # output: 6857
    # It uses a while loop to divide the number by its smallest factor until it becomes prime
