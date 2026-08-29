# Numpy Data Manipulation:

# 1. reshape() - Changing the Shape 

import numpy as np 

data = np.array([
    [10,20,30],
    [40,50,60]
])

print(data.shape)

# We can reshape it:

new_data = data.reshape(3,2)
print(new_data)

print(new_data.shape)

# Important Rule:
# The total number of elements cannot change when reshaping.

# Original - 2 * 3 = 6
# New - 3 * 2 = 6 
# So this works

# 2. Understanding axis:
# This is one of the most important Numpy concepts for ML

marks = np.array([
    [80,90,70],
    [60,75,85],
    [90,95,88]
]) 

#            DBMS Python ML
# Student 1 = 80    90   70
# Student 2 = 60    75   85
# Student 3 = 90    95   88

# axis = 0 
# Means operate down the rows, column by column.

print(np.mean(marks, axis=0))

# You're asking:
# Whats he average for each subject?

# axis = 1
# Means operate across the columns row by row:

print(np.mean(marks, axis=1))

# You're asking:
# Whats the average mark for each student?

# Easy way to remember:
# axis = 0 = down
# axis = 1 = across >

# 3. Boolean Filtering:
# Now we are getting itno something youll use constantly in data analysis.

marks = np.array([45,67,82,39,91,55])
# We want marks greater than 50

print(marks > 50)

# Numpy creates a boolean mask:
# Then:

print(marks[marks > 50])

# This means - Give me only the value where the condition is True.

# 4. More Filtering Examples:

# Marks >= 80

print(marks[marks >= 80])

# Marks < 50

print(marks[marks < 50])

# Even Numbers

numbers = np.array([10,15,20,25,30])

print(numbers[numbers % 2 == 0])

# 5. ML Connection:

# House Dataset:

data = np.array([
    [1000, 2, 20],
    [1500, 3, 30],
    [2000, 4, 40],
    [2500, 4, 50]
])

# Suppose we want houses larger than 1500 sq ft.
# House size is column 0 

large_houses = data[data[:, 0] > 1500]
print(large_houses)

# This is actual data Filtering.
# Later, pandas will make this even easier.

# 6. Another Important Operation: sum(axis=...)

marks = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88]
])

# Total marks for each Student:
print(np.sum(marks, axis=1))

# Total for each subject:
print(np.sum(marks, axis=0))

# axis=0 > column wise
# axis=1 > row wise

# Day 4 Task:

import numpy as np

marks = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [90, 95, 88],
    [55, 65, 72]
])

# 1. Print the shape:
print(marks.shape)

# 2. Calculate the average mark for each subject:
print(np.mean(marks, axis=0))

# 3. calculate the average mark for each student:
print(np.mean(marks, axis=1))

# 4. Calculate the total marks for each student:
print(np.sum(marks, axis=1))

# 5. Find all individual marks greater than 80:
print(marks[marks > 80])

# 6. Find all students whose average mark is greater than 80

averages = np.mean(marks, axis=1)
print(marks[averages > 80])

# For Example:

averages = np.mean(marks, axis=1)
students_above_80 = marks[averages > 80]

# Thats already a simple form of data preprocessing

