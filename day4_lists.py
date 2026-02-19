# 1.what is a list

numbers = [10,20,30,40]
# numbers -> variable name
# [] -> square brackets define a list
# 10,20,30,40 -> elements of the list

# 2.different typer of list

# list of numbers

marks = [85,90,45,60]

# list of strings

names = ["ankit","rahul","aman"]

# mixed list

data = [10,"ankit","true",95.5]

# accessing elements(indexing)

numbers = [10,20,30,40]

print(numbers[0])
print(numbers[2])

# negative indexing 

print(numbers[-1])
print(numbers[-2])

# changing list elements

numbers = [18,20,30]
numbers[1] = 99

print(numbers)

# adding elements

# append() -> adds one item at end 

numbers = [1,2,3]
numbers.append(4)

print(numbers)

# insert() -> add at specific position

numbers.insert(1,100)
print(numbers)

#removing elements 

# remove() ->removes by value

numbers.remove(100)

# pop() -> removes by index 

numbers.pop(0)

# length of list 

numbers  = [10,20,30]
print(len(numbers))

# looping through a list

numbers = [10,20,30]

for num in numbers:
    print(num)

# slicing lists
 
numbers = [10,20,30,40,45]

print(numbers[1:4])

# day4 tasks

numbers = [11,22,33,44,55]
print(numbers[2])

numbers = [10,20,30,40,50]
numbers[3] = 35

print(numbers)

numbers = [9,8,7,6,5,4]
numbers.append(3)

print(numbers)

numbers = [2,4,6,8]
numbers.remove(6)
numbers.pop(2)

print(numbers)