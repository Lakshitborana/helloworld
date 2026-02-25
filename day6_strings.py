# a string is a sequence of characters 
# anything inside quotes is a string in python

name = "lakshit"
city = "mumbai"
message = "i am learning python"

# creating strings

"double quotes"
'single quotes'
'''triple quotes'''

a = "hello"
b = 'world'
c = '''this is multi-line string'''

# printing strings

print("hello world")

# string indexing (very important)

text = "python"

print(text[0])
print(text[3])

# negative  indexing

text  = "python"

print(text[-1])
print(text[-2])

# string slicing (very powerful)
# syntax : [start:end]

text = "python"

print(text[0:3])
print(text[2:5])
print(text[:4])
print(text[2:])

# string length

text = "python"
print(len(text))

# string concatenation(joining strings)

first = "lakshit"
last = "borana"

full = first + " " + last
print(full)

# repeating strings

print("hello" * 3)

# important string methods(very important)

# 1. lowercase/uppercase

text = "python"

print(text.lower()) # python
print(text.upper()) # PYTHON

# 2. strip (remove spaces)

text = " hello "
print(text.strip())

# 3. replace

text = "i like java"
print(text.replace("java", "python"))

# 4. split (very important for data science)

text ="apple,banana,orange"
print(text.split(","))

# 5. find 

text = "python is powerful"
print(text.find("is"))

# f-strings (super important)
# used to insert variables inside strings

name = "lakshit"
age = "22"

print(f"my name is {name} and i am {age} years old")

# strings are immutable 
# you cannot change a character directly

text = "python"
new_text = "j" + text[1:] 
print(new_text)

# practice 

text = "machinelearning"
print(text[7:15])

print("AI" * 2)

text = " python "
print(len(text.strip()))

# Advanced string concepts

# 1. check if substring exists

text = "machine learning"

print("learning" in text) #true
print("AI" in text)       #false

# 2. count occurences

text = "banana"
print(text.count("a"))

# 3. startswith / endswith

text = "python.py"

print(text.startswith("py")) #true
print(text.endswith(".py"))  #true

# 4. isalpha() , isdigit() ,isalnum()
# very important in validation tasks

print("hello".isalpha())    #true
print("123".isdigit())      #true
print("hello123".isalnum()) #true

# 5. join (opposite of split)

words = ["machine","learning","AI"]

sentence = " ".join(words)
print(sentence)

# Real ML example 
# in NLP (natural language processing) you often do:

text = "i love machine learning"
words = text.lower().split()

# challenge 1 (without running code)

text = "datascience"
print(text[::-1])

text = "mississippi"
print(text.count("ss"))

text = "python3"
print(text.isalpha())

# very important concept 

text = "abcdef"
print(text[::2])
print(text[1::2])

# super importsnt rule
# text[::2]  -> even index characters
# text[1::2] -> odd index characters
# text[::-1] -> reverse string

# challenge 2 

text = "pythonprogramming"
print(text[6:13:2])

text = "artificialintelligence"
print(text[-10:-1:2])

# Interview level string questions

# problem 1: palindrome check

def palindrome(string):
    string = string.replace(" ", "").lower() #improvement
    if string == string[::-1]:
     return "true ,string is palindrome"
    else:
       return "false ,string is not palindrome"
    
string = "  "
result = palindrome(string)
print(result)

string = string.lower()  #improvement
vowels = "aeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(count)

print(string.replace(" ", "")) #improvement

# challenge 3 

def analyze_sentence(sentence):
   sentence = sentence.strip()

# total characters (excluding spaces)
total_characters = len(sentence.replace(" ",""))

# total words 
words = sentence.split()
total_words = len(words)

# Uppercase
uppercase_sentence = sentence.upper()

# vowel count (case insensitive)
vowels = "aeiou"
vowel_count = sum(1 for char in sentence.lower() if char in vowels)

# check if "AI" exists (case insensitive)
ai_exists = "ai" in sentence.lower()

# reverse sentence
reversed_sentence = sentence[::-1]

# print results
print("\n--- sentence analysis ---")
print(f"total characters (no spaces):{total_characters}")
print(f"total words: {total_words}")
print(f"uppercase: {uppercase_sentence}")
print(f"vowel count: {vowel_count}")
print(f"contains 'AI': {ai_exists}")
print(f"reversed sentence: {reversed_sentence}")

#take input from user
user_sentence = input("enter a sentence: ")
analyze_sentence(user_sentence)

