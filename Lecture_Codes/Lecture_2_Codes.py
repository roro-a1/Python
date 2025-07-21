"""
str1 = "This is a string."
str2 = 'Rohan'
str3 = "This is a string."
"""

# Escape sequence characters.
# \n - Next line, \t - Tab

# Concatenation -
# We use '+' operator to concat 2 different strings
'''
str1 = "This is a string. "
str2 = 'Rohan'
str3 = str1 + str2
print(str3)
'''

# Length of string - len(str)
'''
str1 = "This is a string."
print(len(str1))
'''
'''
str1 = "This is a string. "
str2 = 'Rohan'
len1 = len(str1)
len2 = len(str2)
print(type(len1))
print(len1 + len2)
'''

# Indexing - In python indexing of any str starts with 0.
# Index can only be used to have access, and it is not available for modifying string
'''
str1 = "This is a string."
print(str1[4])
'''

# Slicing - Accessing parts of string
'''
str1 = "This is a string."
print(str1[0 : len(str1)])
'''

# String Functions -
'''
str1 = "I am a coder."
print(str1.endswith("er.")) 
# Returns True if true, False otherwise.
print(str1.capitalize()) 
# Capitalizes first letter.
print(str1.replace("er.", "ing.")) 
# Replace new value in place of old one, in all occurrences.
print(str1.find("am")) 
# Returns Index of first char of given sub-string, in first occurrence.
print(str1.count("coder")) 
# Checks for count of given sub-string in string.
'''

# Practice
# WAP to input user's first name & print its length
'''
str = input("Enter user's first name: ")
print(len(str))
'''

# WAP to find the occurrence of $ in a string
'''
str = input("Enter string: ")
occ = str.count("$")
print("$ appears in the string", occ, "times")
'''

# Conditional Statements - if-elif-else syntax
'''
age = int(input("Enter age: "))
if (age >= 18 and age <= 45):
    print("Adult my man..")
elif(age > 45):
    print("Hey old fellow")
else:
    print("Go home kid!!")
'''

'''
marks = int(input("Enter your marks: "))
if (marks >= 90 and marks <= 100):
    print("Congrats! A grade.")
elif(marks < 90 and marks >= 80):
    print("Got B grade.")
elif(marks < 80 and marks >= 70):
    print("Got C grade.")
elif(marks < 70 and marks >= 60):
    print("Got D grade, Just a fluke!")
elif(marks < 60 and marks >= 0):
    print("Failed successfully!")
else:
    print("Enter correct score kid! Are you drunk??")
'''

# Nesting of Condition Statements
'''
age = int(input("Enter age: "))
if (age >= 18):
    if (age > 45):
        print(("Adult but an old man."))
    else:
        print("Right age my man..")
else:
    print("Go home kid!!")
'''

# Practice
# WAP to check if a number entered by the user is odd or even
'''
num = int(input("Enter number: "))
if (num%2 == 0):
    print("Number is Even.")
else:
    print("Number is odd.")
'''

# WAP to find the greatest of 3 numbers entered by the user
'''
a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))

if (a1 > a2):
    if(a1 > a3):
        print("Greatest of 3: ", a1)
    else:
        print("Greatest of 3: ", a3)
elif (a2 > a1):
    if(a2 > a3):
        print("Greatest of 3: ", a2)
    else:
        print("Greatest of 3: ", a3)
else:
    print("Greatest of 3: ", a3)
'''
'''
a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))

if (a1 >= a2 and a1 >= a3):
    print("Greatest of 3: ", a1)
elif(a2 >= a1 and a2 >= a3):
    print("Greatest of 3: ", a2)
else:
    print("Greatest of 3: ", a3)
'''

# WAP to check if a number is a multiple of 7 or not
'''
num = int(input("Enter number: "))
if (num % 7 == 0):
    print("Number is multiple of 7.")
else:
    print("Number is not multiple of 7.")
'''
