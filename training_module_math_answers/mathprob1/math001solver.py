"""This module provides a function to
calculate the sum of all multiples of
given factors within a specified range."""


def sum_of_multiples(factors, start, end):
    """Calculate the sum of all multiples of given factors within a specified range."""
    return sum(
        x for x in range(start, end + 1) if any(x % factor == 0 for factor in factors)
    )


# test
if __name__ == "__main__":
    print(sum_of_multiples([3, 5, 12], 1, 100))
    # output: 233168
