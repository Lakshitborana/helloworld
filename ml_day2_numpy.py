# Step 1: Check Installation 

import numpy as np 
print(np.__version__)

# Step 2: Create Arrays

import numpy as np 
arr = np.array([10,20,30,40])
print(arr)

# Step 3: Check Type

print(type(arr))

# Step 4: Array Properties

print(arr.ndim) # Number of dimensions
print(arr.shape) # Shape of the array
print(arr.size) # Total number of elements
print(arr.dtype) # Data type of the array

# Step 5: Create Special Arrays
zeros = np.zeros(5)
ones = np.ones(5)
sequence = np.arange(1,11)

# Step 6: Basic Math

arr = np.array([1,2,3])
print(arr * 2)
print(arr + 10)
print(arr ** 2)

# Numpy Task :

import numpy as np

# Array:
arr = np.array([2,4,6,8,10])
print(arr)

# Array type:
print(type(arr))

# Array shape:
print(arr.shape)

# Array size:
print(arr.size)

# Data type:
print(arr.dtype)

# Dimensions :
print(arr.ndim)

# Create zeros:
zeros = np.zeros(5)
print(zeros)

# Create ones:
ones = np.ones(5)
print(ones)

# Create sequence:
sequence = np.arange(2,11)
print(sequence)

# Multiply the original array by 2:

print(arr * 2)

# Add 100 to every element:

print(arr + 100)

# Mini assignment:

import numpy as np

marks = np.array([85, 90, 78, 92, 88])

print("Originals:" ,marks)
print("After adding 5 bonus marks:", marks + 5)
print("After doubling the marks:", marks * 2)
print("Maximum mark:", np.max(marks))
print("Minimum mark:", np.min(marks))
print("average mark:", np.mean(marks))

# ML Track Day 2 - Next Part (Statistics with Numpy)

import numpy as np 

marks = np.array([85, 90, 78, 92, 88])

print("Maximum mark:", np.max(marks))
print("Minimum mark:", np.min(marks))
print("Average mark:", np.mean(marks))
print("Sum of marks:", np.sum(marks))
print("Standard deviation of marks:", np.std(marks))

# Final Challenge:

import numpy as np 

marks = np.array([85, 90, 78, 92, 88])

print("original marks:", marks)

new_marks = (marks + 5)
print("marks after adding 5 bonus marks:", new_marks)

# Find the new average:

new_average = np.mean(new_marks)
new_max = np.max(new_marks)
new_min = np.min(new_marks)
new_sum = np.sum(new_marks)

print("New average mark:", new_average)
print("New maximum mark:", new_max)
print("New minimum mark:", new_min)
print("New sum of marks:", new_sum)