# step 1 basic syntax

def function_name():
    print()

# step 2

def greet():
    print("hello lakshit")

# step 3 function with parameters(input)

def greet(name):
    print("hello",name)

# step 4 function with return value 

def add(a,b):
    return a + b

result =  add(5,4)
print(result)

# step 5 difference : print() vs return 

def add(a,b):
    print(a+b)

def add(a,b):
    return a + b

# step 6 default parameters

def greet (name="guest"):
    print("hello" ,name)

# step 7 example from real learning (ML style)

def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)

marks = [45,56,67,78,98]
avg = calculate_average(marks)

print("average:", avg)

# functions task 1

def square(number):
    return number * number

num  = int(input("enter a number:"))
result = square(num)

print("square is:", result)  

# functions task 2

def evenodd (number):
    if number % 2 == 0:
        return "even " 
    else:
        return "odd"
    
print(evenodd(7))
print(evenodd(3))

