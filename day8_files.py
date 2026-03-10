# step 1 writing to a file

file = open("data.txt", "w")
file.write("hello AI\n")
file.write("machine learning")
file.close()

# better code (with is safer (important))

with open ("data.txt","w")as file:
    file.write("hello AI\n")

# step 2  reading file 

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# step 3 reading line by line

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# step 4 adding values

with open("mark.txt", "a")as file:
    file.write("95\n")

# practice 1

marks = [78,85,90,67,88]

with open("marks.txt", "w") as file:
    for m in marks:
        file.write(str(m) + "\n")

# now read the file
with open("marks.txt", "r")as file:
    content = file.readlines()

# convert to integers
new_marks = []

for line in content:
    new_marks.append(int(line.strip()))

# calculate average
average =  sum(new_marks) / len(new_marks)

print("print from file", new_marks)
print("average:", average)

# practice 2

# take input 

sentences = []

# take 3 sentences from user
for i in range(3):
    s = input(f"Enter sentence {i+1}: ")
    sentences.append(s)

# write to file
with open("sentences.txt", "w") as file:
    for s in sentences:
        file.write(s + "\n")
    
# read file
with open("sentences.txt", "r") as file:
    content = file.readlines()

# total lines
total_lines = len(content)

# total words 
total_words = sum(len(line.split()) for line in content) # Generator expression

# longest line 
longest_line = max(content, key=len)

print("\n--- File Analysis ---")
print("Total lines:", total_lines)
print("Total words:", total_words)
print("longest line:", longest_line.strip())
