# step1 loop way
for i in range(1,5):
    print(i)
   
for j in range(1,50):
    print(j)

# step2 for loop(range, variable)
for i in range(6):
    print(i)

for j in range(0,11):
    print(j)

# step3 for loop task

for i in range(1,100):
    print(i)

for i in range(1,100):
    if i % 3 == 0:
        print(i, "is odd")

count = 1
while count <= 10:
    print(count)
    count += 1

total =  0

for i in range(1,11):
    total += i
    
print("sum", total)

total = 0

for i in range(1,51):
    total += i

print("sum", total)

total = 0 

for i in range(1,11):
        if i % 2 == 0:  #check if number is even
         total += i 
        print("sum of even numbers:", total)

total = 0

for i in range(2,11,2):
    total +=i

    print("final sum", total)

# day3 task1

n = int(input("enter n:"))
for i in range(1,n):
    print(i)

n = int(input("enter n:"))
total = 0

for i in range(1,n+1):
    total += i
    print("sum is", total)

# day3 task2

n = int(input("enter a number:"))
count = 0

for i in range(1,n+1):
    if i % 2 == 0:
        count += 1
    
print("count of even numbers" ,count) 