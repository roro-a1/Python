# Lists in Python - A built-in data type that stores set of values
# It can store elements of different types (integers, floats, string, etc.)
"""
marks = ["Rohan", "Sandman", "Gwen", "Spidy"]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
"""

# Unlike strings, lists are mutable(i.e. they can be modified)
"""
student = ["Rohan", 100, "O & M"]
print(student)
student[0] = "Sam"
student[1] = 10
print(student)
"""

# List Slicing - list_name[start_idx : end_idx]
"""
student = ["Rohan", 100, "O & M", "Kolhapur", "Data engineer"]
print(student[:])
"""

# List Methods
"""
student = ["Rohan", 100, "O & M"]
print(student)
student.append("Kolhapur") # Adds one element at the end of list
print(student)
marks = [10, 12, 13, 7, 4]
marks.sort() # Sorts list in ascending order - only integer or float allowed
print(marks)
marks.sort(reverse = True) # Sorts in descending order.
print(marks)
print(student.append("Data engineer")) # Returns 'None' if printed a method.
student.reverse() # Reverses the index of list.
print(student)
student.insert(len(student), "Future GDE - Google data engineer")
print(student)
marks.pop(-1) # Deletes a value at given index in the list.
print(marks)
marks.remove(7) # Deleted the given value from list.
print(marks)
"""

# Tuples in Python - A built-in data type that lets us create immutable sequence of values.
"""
student = ("Rohan", 100, "O & M", "Kolhapur", "Data engineer")
print(student)
print(type(student))
print(student[4])
# student[4] = "GDE" - Not allowed, TypeError: 'tuple' object does not support item assignment
tup1 = (1, )
print(type(tup1))
tup2 = (1)
print(type(tup2))
"""

# Tuple Methods
"""
student = ("Rohan", 100, "O & M", "Kolhapur", "Data engineer", "O & M")
print(student.index("Kolhapur")) # Returns index of given value in tuple.
print(student.count("O & M")) # Returns count of times given value occurs in tuple.
"""

# Practice
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
"""
movies = []
print("Please enter your top 3 favorite movies")
movies.append(input("1st Movie: "))
movies.append(input("2nd Movie: "))
movies.append(input("3rd Movie: "))
print(movies)
"""

# WAP to check if a list contains a palindrome of elements.
"""
list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("List is palindrome")
else:
    print("List is not palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if (copy_list2 == list2):
    print("List 2 is palindrome")
else:
    print("List 2 is not palindrome")
"""

# WAP to count the number of students with the "A" grade in the following tuple - ["C", "D", "A", "A", "B", "B", "A"]
"""
tup = ("C", "D", "A", "A", "B", "B", "A")
print("Count of students with A grade is", tup.count("A"))
"""

# Store the above values in a list & sort them from "A" to "D".
"""
list1 = ["C", "D", "A", "A", "B", "B", "A"]
list1.sort()
print(list1)
"""
