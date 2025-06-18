sum_of_squares = sum(i**2 for i in range(1, 101))
square_of_sum = sum(range(1, 101)) ** 2
difference = square_of_sum - sum_of_squares
print(difference)
# This code calculates the difference between the square of the sum and the sum of the squares of the first 100 natural numbers.