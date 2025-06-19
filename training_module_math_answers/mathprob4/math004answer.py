"""Problem 4
A palindromic number reads the same both ways.
 The largest palindrome made from the product
   of two 2-digit numbers is 9009.
9009 = 91 x 99
Part A
Find the largest palindrome made from the
 product of two 3-digit numbers.
Edit the file answer.py and update the
 function answer() to return the answer."""


def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]


def answer():
    """Return the largest palindrome made from the product of two 3-digit numbers."""
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome


if __name__ == "__main__":
    print(answer())
    # This function calculates the largest palindrome made from the product of two 3-digit numbers
    # output: 906609
    # It uses nested loops to iterate through all products of two 3-digit numbers
