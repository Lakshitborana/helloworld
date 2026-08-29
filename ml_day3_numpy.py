# 1. 2D Array (2D Array has rows and columns)

import numpy as np

marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [76, 84, 80]
])

print(marks)

# 2. Understanding Shape:

print(marks.shape)

# Youll get : (3(rows),3(columns))

# 3. Number of dimensions:

print(marks.ndim)

# compare:

a = np.array([1,2,3])

print(a.shape)
print(a.ndim)

# 4. Indexing a 2D array:

marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [76, 84, 80]
])

# Python indexing starts at zero

# To get the first row :

print(marks[0])

# 5. Accessing one Element:

# array[row,column]
print(marks[0,1])

print(marks[2,0])

# Slicing

print(marks[0:2])

# start at 0 , stop before 2.
# So you get rows 0 and 1.

# 7. Get an Entire Column 
# This is especially important for ML
# suppose the columns are:
# DBMS Python ML

# To get the python marks:

print(marks[:,1])

# What does ':' mean?
marks[:,1]
# Take all rows, column 1.

# This concept is extremely important when working with datasets.

# 8. Now connect This to Machine Learning:
# We can represent it wiht Numpy:

data = np.array([
    [1000, 2, 20],
    [1500, 3, 30],
    [2000, 4, 40],
    [2500, 4, 50]
])

# Now we have:
# Rows > different houses
# Columns > different information

# 9. Features vs Label:

# Features = inputs (e.g., house size, number of bedrooms)
# Label = what we want to predict (e.g., house price)

# These are our features:

x = data[:,0:2]

# Thats our label:

y = data[:, 2]

# This is very important:
# In ML youll constantly see:

# X > Features
# Y > Label

# Dont worry if you dont understand every ML convention yet. youll see this repeatedly.

# Numpy Task:

# Use this dataset:

import numpy as np

data = np.array([
    [1000, 2, 20],
    [1500, 3, 30],
    [2000, 4, 40],
    [2500, 4, 50]
])

print(data)
print("Shape:", data.shape)

# Number of rows:
print("Number of rows:", data.shape[0])

# Number of columns:
print("Number of columns:", data.shape[1])

# First row:
print("First row:", data[0])  # First row

# House sizes only:
print("House sizes:", data[:, 0])

# Prices only:
print("Prices:", data[:, 2])

# Features and Labels:

# Features:
X = data[:, 0:2]
print("Features (X):")
print(X)

# Labels:
Y = data[:, 2]
print("Labels (Y):")
print(Y)

# Day 3 challenge: 

# Challenge 1:
print("Shape of Features (X):", X.shape)

# Challenge 2:
print("Shape of Labels (Y):", Y.shape)

# Challenge 3:
# Get the bedroom values only: 
Bedrooms = data[:,1]
print("Bedrooms:", Bedrooms)

# Challenge 4:
# Get the first two houses features:

rows = data[0:2, 0:2]  # First two rows, first two columns

print("First two houses features:")
print(rows)
