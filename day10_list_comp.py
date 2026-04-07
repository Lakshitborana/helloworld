# List Comprehensions (POWER FEATURE)

# Basic idea

numbers = [1,2,3,4,5]
squares = []

for num in numbers:
    squares.append(num * num)

# Instead use this: [expression for item in iterable]

squares = [num * num for num in numbers]

squares = [x*x for x in range(5)]
print(squares)

# With condition: [expression for item in iterable if condition]

numbers = [1,2,3,4,5]
even_numbers = [num for num in numbers if num % 2 == 0]

# if-else in List Comprehension:
# [expression_if_true if condition else expression_if_false for item in iterable]

result = ["Even" if x % 2 == 0 else "odd" for x in range(5)] 
print(result)

# With Strings:

words  = ["ai", "ml", "python"]
upper_words = [word.upper() for word in words]

word = "python"
letters = [ch.upper() for ch in word]
print(letters)

# Nested List Comprehension 

matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)

# Flattening a List (Advanced)

matrix = [[1,2,3], [4,5,6], [7,8,9]]

flat = [num for row in matrix for num in row]
print(flat)

# Multiple Conditions 

nums = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(nums)

# Using Functions 

def square(x):
    return x*x

result = [square(x) for x in range(5)]
print(result)

# Dictionary + List Comprehension Combo (Advanced)

data = {"a":1, "b":2, "c":3}

result = [key for key, value in data.items() if value > 1]
print(result)

# When NOT to use List Comprehension
# Avoid when:
            # logic is too complex
            # Too many nested loops
            # Hard to read

# Practice challenge: Create a list of squares of numbers from 1 to 10

squares = [x*x for x in range(1,11)]
print(squares)

# Practice challenge: Create a list of only vowels from a string 

string = input("Enter a string: ")
vowels = [ char for char in string if char.lower() in "aeiou"]
print(vowels)

# Practice challenge: convert this 
# for i in range(10):
#     if i % 2 != 0:
#         print(i*i)

i = [1 ,3 ,5 ,7 ,9]
nums = [i*i for i in range(10) if i % 2 != 0 ]
print(nums) 

# Next level Challenge: 
# create a list of numbers from 1-20:
# if number is Even -> "Even"
# if odd -> square of numbers

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = ["Even" if x % 2 == 0 else x*x for x in nums] 
print(result)

# Next level challenge: Length of each word in a list

words = ["python", "is", "high", "level", "language"]
length = [len(word) for word in words]
print(length)

# Program challenge: Take a list of numbers from user

# Take a list of numbers from user
nums = [int(x) for x in input("Enter numbers: ").split()]
print(nums)

# List of squares
squares = [x**2 for x in nums]
print("squares: ", squares)

# List of even numbers
even_numbers = [num for num in nums if num % 2 == 0]
print("even numbers: ", even_numbers)

# List of numbers > 10
greater_than_10 = [num for num in nums if num > 10]
print("numbers > 10: ", greater_than_10)

# Bonus : Convert all numbers to strings using list comprehension
string_numbers = [str(x) for x in nums]
print("string numbers: ", string_numbers)
