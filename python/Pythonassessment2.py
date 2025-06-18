# Function to find and print all prime numbers up to a given number n
def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            print(primes)

prime_numbers(31)

my_list = [10, 20, 30, 40, 50]
my_list.pop()
print(my_list)

def find_maximum(numbers):
    if not numbers:
        return None  

    max_num = numbers[0]  
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

my_list = [10, 20, 5, 70, 30]
print("Maximum number is:", find_maximum(my_list))

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()  
    merged.update(dict2)   
    return merged

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print(merge_dictionaries(d1, d2))

def remove_occurrences(lst, target):
    return [x for x in lst if x != target]

nums = [1, 2, 3, 2, 4, 2, 5]
print(remove_occurrences(nums, 2))


def most_expensive_item(items_dict):
    max_price = 0
    expensive_item = ""
    
    for item, price in items_dict.items():
        if price > max_price:
            max_price = price
            expensive_item = item
    
    return expensive_item, max_price

items = {
    "laptop": 1000,
    "phone": 800,
    "tablet": 600
}


result = most_expensive_item(items)
print("Most expensive item:", result[0])
print("Price:", result[1])

def swap_keys_values(input_dict):
    swapped_dict = {}
    for key, value in input_dict.items():
        swapped_dict[value] = key
    return swapped_dict

original_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

swapped = swap_keys_values(original_dict)
print("Original Dictionary:", original_dict)
print("Swapped Dictionary:", swapped)

def remove_items_by_value(input_dict, value_to_remove):
    filtered_dict = {key: value for key, value in input_dict.items() if value != value_to_remove}
    return filtered_dict

sample_dict = {
    "apple": 3,
    "banana": 2,
    "cherry": 2,
    "date": 5
}

result = remove_items_by_value(sample_dict, 2)
print("Filtered Dictionary:", result)

def merge_tuples(tuple1, tuple2):
    return tuple1 + tuple2
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
result= merge_tuples(tuple_a, tuple_b)
print("Merged Tuple:", result)

def count_occurrences(input_tuple, element):
    return input_tuple.count(element)
my_tuple = (1, 2, 3, 2, 4, 2, 5)
target =2
result = count_occurrences(my_tuple, target)
print(f"The element {target} occurs {result} times in the tuple.")

def average_height(heights):
    if len(heights) == 0:
        return 0
    total= sum(heights)
    count= len(heights)
    return total / count
heights_tuple= (150, 160, 170, 180)
print("Average height:", average_height(heights_tuple))

def find_index(numbers, target):
    if target in numbers:
        return numbers.index(target)
    else:
        return -1  
    
numbers_tuple = (5, 8, 2, 8, 10)
print("Index of 8:", find_index(numbers_tuple, 8))

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)


text = "hello world from divyank"
print(capitalize_words(text)) 

def reverse_words(sentence):
    words = sentence.split()          
    reversed_words = words[::-1]     
    return ' '.join(reversed_words) 
 
text = "the dog follows the cat"
print(reverse_words(text)) 

def find_longest_word(sentence):
    words = sentence.split()              
    longest = ""                          
    for word in words:
        if len(word) > len(longest):      
            longest = word                
    return longest

text = "Python programming is powerful"
print(find_longest_word(text))  


