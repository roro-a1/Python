# Loops in Python - Loops are used to repeat instructions.
# Note - be wary of infinite loops.
"""
count = 1 #Iterator

while count <= 5:
    print("Roro is gonna be google data engineer") #Iteration
    count += 1

print(count)
"""
"""
i = 1
while i <=5:
    print(i)
    i += 1
"""

# Practice
# Print numbers from 1 to 100
"""
i = 1
while i <=100:
    print(i)
    i += 1
"""

# Print numbers 100 to 1
"""
i = 100
while i >=1:
    print(i)
    i -= 1
"""

# Print multiplication table of number n
"""
n = int(input("Please enter the number : "))
i = 1

while i <= 10:
    print(n*i)
    i += 1
"""

# Print elements of the following list using a loop - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
i = 1
while i <= 10:
    print(i * i)
    i += 1
"""

# Search for a number x in this tuple using loop
"""
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number to search : "))
i = 0
while i < len(num):
    if (num[i] == x):
        print(x, "is found in tuple at index", i)
        break # Break - Used to terminate the loop when encountered.
    else:
        print("Searching")
    i += 1
"""

# Break & Continue
# Break - Used to terminate the loop when encountered.
# Continue - Terminates execution in the current iteration & continue execution of the loop with the next iteration.
"""
i = 0
while i <= 5:
    if (i % 2 == 0):
        i += 1
        continue # Skips if executed in iteration
    print(i)
    i += 1

"""

# For loops in Python - These are used for sequential traversal. For traversing list, string, tuples etc.
"""
names = ["Roro", "Naks", "Bulbul", "GDE"]
for val in names:
    print(val)
"""
"""
str1 = "Google data engineer"
for char in str1:
    if (char == "d"):
        print(char, "Found")
        break
    else:
        print("finding")
"""

#Practice
# Print the elements from the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in list1:
    print(i)
"""

# Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number to search : "))
for i in tup1: # Linear search.
    if (i == x):
        print(x, "Found")
        break
    else:
        print("Searching..")
else:
    print("Not found!! Regret, try next time")
"""

# Range() function - Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# range(start(o), stop, step(o)). (o) - Optional
"""
for el in range(5, 30, 5):
    print(el)
"""

# Practice
# Print numbers from 1 to 100
"""
for i in range(1, 101, 1):
    print(i)
"""

# Print numbers from 100 to 1
"""
for i in range(100, 0, -1):
    print(i)
"""

# Print the multiplication table of a number n.
"""
n = int(input("Enter the number : "))
for i in range(1, 11, 1):
    print(i * n)
"""

# pass Statement - pass is a null statement that does nothing. It is used as a placeholder for future code.
"""
for i in range(10):
    pass # Can be used in if as well

print("Some useful work!!")
"""

# WAP to find the sum of first n numbers
"""
n = int(input("Enter the number : "))
sum = 0

for i in range(0, n + 1, 1):
    sum += i

print(sum)
"""

# WAP to find the factorial of the number
"""
n = int(input("Enter the number : "))
fac = 1

for i in range(1, n + 1, 1):
    fac *= i

print(fac)
"""
