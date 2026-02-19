# 1.even numbers btw 1 and 20

for i in range (1,20):
    if i % 2 ==0:
        print(i)

# 2.print squares of numbers from 1 to 5

for i in range(1,6):
    print(i,"square is", i*i)

# 3.print numbers from 1 to n 

n = int(input("enter n: "))

for i in range(1,n+1):
    print(i)

# 4.print numbers from 10 to 1 

for i in range(10, 0, -1):
       print(i)

# 5.multiplication table of a number 

num = int(input("enter a number: "))

for i in range(1,11):
     print(num, "x", i,"=",num*i)

# 6.count numbers divisible by 3(1 to 50)

count = 0

for i in range(1,51):
     if i % 3 == 0:
          count+= 1

print("count:",count)

# 7.sum of numbers from 1 to n 

n = int(input("enter n:"))
total = 0

for i in range(1,n+1):
     total+= i

print("sum:",total)

# 8.divisible by both 3 and 5(1-100)

for i in range(1,101):
     if i % 3== 0 and i % 5 == 0:
          print(i)

# 9.largest of 5 numbers

largest = int(input("enter number:"))

for i in range(4):
     num = int(input("enter number:"))
     if num > largest:
          largest = num 

print("largest number:",largest)

# 10.star patter (increasing)

for i in range(1,6):
     print("*" * i)

# 11.number pattern

for i in range(1,6):
     for j in range(1,i+1):
          print(j,end="")
     print()
    
# 12.reverse star pattern

for i in range(5,0,-1):
     print("*" * i)

# 13.check prime number 

num  =  int(input("enter number:"))
is_prime = True

if num <= 1:
     is_prime = False
else:
     for i in range(2,num):
          if num % i == 0:
               is_prime = False
               break

if is_prime:
     print("prime number")
else:
     print("not prime")

# 14.prime numbers btw 1 to 100

for num in range(2,101):
     is_prime = True
     for i in range(2,num):
          if num % i == 0:
               is_prime = False
               break 
     if is_prime:
          print(num)

# 15.factorial of a number

n = int(input("enter number:"))
fact = 1

for i in range(1,n+1):
    fact *= i

print("factorial:",fact)

# 16.count digits in a number

n = int(input("enter number:"))
fact = 1

for i in range(1,n + 1):
     fact *= 1

print("factorial:", fact)

# 17.reverse a number 

num = input("enter number:")
rev = ""

for digit in num:
     rev = digit + rev

print("reversal",rev)

# 19.sum of even & odd numbers(1-n)

n = int(input("enter n:"))
even_sum = 0
odd_sum = 0

for i in range(1,n + 1):
     if i % 2 == 0:
          even_sum += i
     else:
          odd_sum += i

print("even sum:", even_sum)
print("odd sum",odd_sum)

#20.fibonacci series

n = int(input("enter terms:"))
a,b = 0,1

for i in range(n):
     print(a, end="")
     a,b = b, a+b 