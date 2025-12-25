# Loops with Python Lists.

"""
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "-pie")

print(fruits)
"""

student_score = [150, 142, 185, 140, 171, 59, 189, 175, 45, 29, 128]
"""
total_score = sum(student_score)
print(total_score) # Option 1

addition = 0
for i in student_score:
    addition += i

print(addition)
"""
"""
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)
print(max(student_score))
"""
