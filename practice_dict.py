
# practice_dict.py

names = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty"
]

num_dict = {name: i for i, name in enumerate(names)}

# Print all keys
print("All keys:")
print(list(num_dict.keys()))

# Print all values
print("\nAll values:")
print(list(num_dict.values()))

# Print key + "two" and value + 2
print("\nEach key + 'two' and value + 2:")
for key, value in num_dict.items():
    print(f"{key} + two : {value + 2}")
