# Part 1 - what is an error?

age = int(input("enter age: ")) # if twenty entered
print(age)                      # value error

# Part 2 - Error handling (try / except)
# we protect risky code using try

try:
    age = int(input("Enter age: "))
    print(age)
except:
    print("Invalid input. Please enter a number.")

# now if user enters text: program does not crash

# Part 3 - Catch Specific Errors: Better practice

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Please enter a valid integer.")

# Part 4 - Multiple Exceptions  

try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero") 

# This protects against:
# Invalid numbers
# Division by zero

# Part 4 - else in Error Handling 
# else runs if no error happens

try:
    num = int(input("Enter number:"))
    result = 10 / num

except:
    print("Error occured")

else:
    print("Result:",result)

# Part 5 - finally - finally runs no matter what happens

try:
    num = int(input("Enter numbers: "))
    print(num)
except ValueError:
    print("Invalid number")
finally:
    print("Program finished") # Even if there's an error , finally executes 

# Full Structure 

#try:
   # Code 

# except Errortype:
    #handle Error 

#else:
    #runs if no error

#finally:
    #always runs

# Example Program (Very Important)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("Please enter numbers only")

else:
    print("result:", result)

finally:
    print("program ended")

# Advanced Error Handling in Python 

# 1. Multiple Exceptions in One Block
# sometimes one code can produce different types of errors 

try: 
    num = int(input("Enter number: "))
    result = 10 / num

except (ZeroDivisionError,ValueError):
    print("Invalid input or division by zero")

# Explanation:
# ZeroDivisionError -> if user enters 0
# ValueError -> if user enters text

# 2. Using "as" Keyword (Very Important)
# This lets you see the actual error message

try:
    a = 10
    b = 0
    print(a/b)

except ZeroDivisionError as e:
    print("Error:",e)

# output: Error: division by zero
# e = actual error message

# 3. finally Block (Advanced Use)
# finally always runs , even if error happens

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Closing program")

# fianlly is commonly used for:
# closing files
#closing database connection
# cleanup tasks

# 4. raise keyword (Very Important)
# raise lets you create your own error

age = int(input("Enter age: ")) 

if age < 18:
    raise ValueError("you must be at least 18") 

print("Access granted")

# ValueError: You must be at least 18
# meaning: You manually triggered the error

# 5. Custom Exceptions (Advanced)
# you can create your own exceptions class

class NegativeNumberError(Exception):
    pass

num = int(input("Enter number: "))

if num < 0:
    raise NegativeNumberError("Negative numbers not allowed ")

print("number is:", num)

# output:
# NegativeNumberError: Negative numbers not allowed 
# this is used in large applications

# 6. Real Example (Professional Code)

try:
    num = int(input("Enter number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")

else:
    print("Result:",result)

finally:
    print("Execution completed")

# Practice challenge 1 (guess the output)

try:
    X = int("hello")
except ValueError:
    print("A")
except:
    print("B")
else:
    print("C")
finally:
    print("D")

# Practice challenge 2 

try:
    X = 10 / 0
except ZeroDivisionError:
    print("A")
finally:
    print("B")

# Practice challenge 3

try:
    x = int("20")
except ValueError:
    print("A")
else:
    print("B")
finally:
    print("C")

# Practice challenge 4

try:
    print("Hello")
except:
    print("Error")
else:
    print("World")
finally:
    print("Done")

# Practice challenge 5

try:
    a = [1,2,3]
    print(a[5])
except IndexError:
    print("Index error")

# Practice challenge 6 (Important)

try:
    x = int("abc")
except ValueError:
    print("A")
except:
    print("B")
finally:
    print("C")

# Practice challenge 7 

try:
    print(5)
    X = 10/2
except:
    print("A")
else:
    print("B")
finally:
    print("C")

# Practice challenge 

try:
    print("A")
    X = int("10")
    Y = 10 / 0
    print("B")

except ValueError:
    print("C")

except ZeroDivisionError:
    print("D")

else:
    print("E")

finally:
    print("F")

# Practice challenge (Important)

while True:
   try:
       num1 = int(input("Enter first number:"))
       num2 = int(input("Enter second number:"))

       div = num1/num2

   except ValueError:
    print("Please enter valid integers")

   except ZeroDivisionError:
    print("cannot divide by Zero")

   else:
    print("division is: ", div)
    break  
   
   # else runs only if:
   # no exception
   # AND no break / return

   finally:
    print("Process Completed")
