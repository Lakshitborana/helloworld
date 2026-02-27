# step 1 what is dictionary?

student = {
    "name": "lakshit",
    "age" :  22,
    "subject": "database management system",
    "marks":  85,
    "cgpa": 8.7
}
print(student)

teacher = {
    "name": "priya birla",
    "age" :  38,
    "subject": "database management system",
    "city" : "jaipur",
    "experience": "9 years"
}
print(teacher)

# step 2 access values

print(student["name"])
print(student["age"])

print(teacher["name"])
print(teacher["subject"])

# step 3 Adding and Modifying

student["city"] = "jodhpur"
student["age"] = 23
print(student)

teacher["subject"] = "computer network"
teacher["city"] = "jodhpur"
print(teacher)

student.pop("cgpa")
teacher.pop("experience")

# step 4 loop through dictionary 

for key in student:
    print(key, ":", student[key])

# loop through dictionary (better way)

for key, value in student.items():
    print(key, value)
# step 5 dictionary from user input

student["name"] = input("enter name:")
student["age"]  = int(input("enter age"))

teacher["name"] = input("enter name")
teacher["age"] = int(input("enter age:"))

print(student)
print(teacher)

# challenge 1

person = {
    "name": "lakshit",
    "age" : 23,
    "skills": ["python", "ML", "SQL"]
}
# 1 print second skill
print(person["skills"][1])

# 2 add new skill
person["skills"].append("java")
print(person["skills"])

# 3 change age
person["age"] = 24

# 4 print keys and values
print(person.keys())
print(person.values())

# challenge 2

user = {}

user["name"] = input("enter name: ")
user["age"]  = int(input("enter age: "))

#store marks in dictionary
user["subjects"] = { 
   "DBMS":   int(input("DBMS marks: ",)),
   "CN":     int(input("CN marks: ")),
   "PYTHON": int(input("PYTHON marks: ")) 
    }


print("\nstudent details: ")
print(user)

# calculate average
marks = user["subjects"].values()
average = sum(marks) / len(marks)
print("average marks: ", average)

# highest marks
highest = max(marks)
print("highest mark: ", highest)

# pass check
if average >= 50:
    print("status : passed")
else:
    print("status : failed")
