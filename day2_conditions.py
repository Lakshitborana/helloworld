# step1 (comparison operators)
a = 10
b = 5

print(a>b)
print(a == b)
print(a != b)

# step2 (if,else)(indentation is important)
age = int(input("Enter your age: "))

if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# step3 (if-elif-else)
marks = int(input("enter marks"))

if marks >= 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 68:
    print("grade C")
else:
    print("Fail")

# step4 (logical operators)
age = 20
has_id = True

if age >= 18 and has_id:
    print("entry allowed")
else:
    print("entry denied")

# day2 task1
age = int(input("enter your age: "))
marks = int(input("enter marks"))

has_id_input = input("do you have an id? (yes/no): ").lower()
has_id = has_id_input == "yes"

if age < 18:
    print("Not eligible: Age must be 18 or above")

elif marks >= 85 and has_id:
     print("Eligible for scholarship interview")

elif 60<= marks <=84 and has_id:
     print("eligible for general interview")

else: 
     print("Not eligible: insufficient marks or ID missing")

# day2 task2
num = int(input("enter a number"))

if num > 0:
    print("the number is positive")

    if num % 2 == 0:
        print("it is even")
    else: 
        print("it is odd")

elif num < 0:
    print("the number is negative")

    if num % 2 == 0:
        print("it is even")
    else:
        print("it is odd")

else:
    print("the number is zero")
    