# task 1

numbers = [10,20,30,40,50]
print(numbers[2])

numbers[4] = 45
print(numbers)

numbers.append(50)
print(numbers)

numbers.pop(0)
print(numbers)

# task 2

nums = [1,2,3]
nums.append([4,5])
print(nums)

# task 3

nums = [10,20,30]
nums.insert(1,[40,50])
print(len(nums))

# task 4

nums = [[1,2],[3,4],[5,6]]
print(nums[1][0])

# task 5

nums = [[10,20],[30,40]]
print(nums[0][1])

# task 6

nums = [ [1,2,3],
         [4,5,6],
         [7,8,9] ]

print(nums[2][1])

# task 7 list comprehension

numbers = [1,2,3,4,5]

squares = []
for num in numbers:
    squares.append(num** 2)

print(squares)

# in ONE LINE

numbers = [1,2,3,4,5]
squares = [num ** 2 for num in numbers]
print(squares)

# task 8 

nums = [1,2,3,4,5]
even = [n for n in nums if n % 2 == 0]
print(even)

# task 9

nums = [1,2,3,4,5]
result = [n * 2 for n in nums if n > 2]
print(result)

# task 10

nums = [[1,2],[3,4],[5,6]]

result = [row[1] for row in nums]
print(result)

# final task 

marks = [78,92,56,89,67,45,33]

total = sum(marks)
average = total / len(marks)

print("total:",total)
print("average: ",average)
print("highest:",max(marks))
print("lowest:",min(marks))

passed = [m for m in marks if m >=50]
print("students passed",len(passed))

# challenge task 

marks = [78,92,56,89,67,45,33]

total = sum(marks)
average = total / len(marks)

print("total:",total)
print("average: ",average)
print("highest:",max(marks))
print("lowest:",min(marks))

passed = [m for m in marks if m >=50]
failed = [m for m in marks if m < 50]
distinction = [m for m in marks if m >= 90]
print("distinction:",distinction)

for m in marks:
    if m >= 90:
        print(m, "Grade A")
    elif m >= 70:
        print(m, "Grade B")
    elif m >= 50:
        print(m, "Grade C")
    else:
        print(m, "→ Fail")

print(" students failed",len(failed))
print("students passed",len(passed))
