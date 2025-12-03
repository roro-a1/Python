# File Input/Output in Python.
# Python can be used to perform operations on a file.(read & write data)
# Types of all files
# 1. Text files - .txt, .docx, .log etc.  2. Binary files - .mp4, .mov, .png, .jpeg etc.

# Reading a file
"""
f = open("/home/dell/Desktop/Python Codes/Demo.txt", "r") # If file is in different folder than the location of .py file, give whole file path.
data = f.read()
print(data)
print(type(data))
f.close()
"""
"""
f = open("Demo.txt", "r")
data = f.read() # Read entire file
data_1 = f.read(5) # Read only certain number of characters from the file.
data_2 = f.readline() # Read first line from the file.
data_3 = f.readline() # This command will read next line from the file.
print(data)
print(type(data))
f.close() # Closing is must for file security.
"""

# "r" - Open for reading(Default).
# "w" - Open for writing, truncating the file first.
# "x" - Create a new file and open it for writing.
# "a" - Open for writing, appending to the end of the file if it exists.
# "b" - Binary mode.
# "t" - Text mode (default).
# "+" - Open a disk file for updating (reading and writing).

# Writing to a file.
"""
f = open("Demo.txt", "w")
f.write("I am seriously going to be a Google Data Engineer")
f.close()
"""
"""
f = open("Demo.txt", "a")
f.write("For sure, just know it.")
f.close()
"""

# With syntax
"""
with open("Demo.txt", "r") as f:
    data = f.read()
    print(data)
"""

# Deleting a File - Using the 'os' module
"""
import os
os.remove("/home/dell/Desktop/Python Codes/Demo.txt")
"""

# Practice
# Create a new file "practice.txt" using python. Add following data in it.
"""
with open("practice.txt", "w") as f:
    f.write("I am practicing python now in 2025.\nIt is because tho I can usually vibe code most of the stuff.\n")
    f.write("I want to be a best one out there.\nI want to own my own Business Empire.")
"""

# WAF that replaces all occurrences of "best" with "most outstanding" in above file.
"""
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("a best", "most outstanding")
print(new_data)

with open("practice.txt", "w") as f:
    data = f.write(new_data)
"""

# WAP to search if the word "Empire" exists in the file or not.
"""
word = "Empire"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not found")
"""

# WAF to find in which line of the file does the word "Empire" occur first. Print -1 if the word not found.
"""
def check_for_line():
    word = "Empire"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()
"""

# From a file containing numbers separated by comma, print the count of even numbers.
"""
count = 0
with open("practice1.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)
"""

