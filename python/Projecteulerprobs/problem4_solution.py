max_palindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:  # Check if the product is a palindrome
            if product > max_palindrome:
                max_palindrome = product
print(max_palindrome)
# This code finds the largest palindrome made from the product of two 3-digit numbers.                