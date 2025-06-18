a, b = 1, 2
total = 0
while b <= 4000000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
print(total)
# This code calculates the sum of even Fibonacci numbers that do not exceed 4 million.