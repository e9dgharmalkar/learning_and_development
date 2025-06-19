"""Part B
Write a function that returns the largest palindrome
from the product of two n-digit numbers where
both numbers are inside a range.
solver(n, p=None, q=None)
The range is defined as between:
the first n digit number to to p if only
 p is provided
p and q if p and q are both provided"""


def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]


def solver(n, p=None, q=None):
    """Return the largest palindrome made from
    the product of two n-digit numbers."""
    start = 10 ** (n - 1)
    end = (10**n) - 1
    if p is not None and q is None:
        end = p
    elif p is not None and q is not None:
        start = p
        end = q
    max_palindrome = 0
    for i in range(end, start - 1, -1):
        for j in range(i, start - 1, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome


if __name__ == "__main__":
    print(solver(3))
    # output: 906609
    # This function calculates the largest palindrome made from the product of two 3-digit numbers
    # It uses nested loops to iterate through all products of two n-digit numbers
    # and checks if the product is a palindrome, updating the maximum found.
