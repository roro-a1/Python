# Logical Operators. and, or, not.
"""
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

print(not True)
print(not False)
"""

# Rollercoaster program with twist for midlife crisis folks.
print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:  # Nested if Statement.
        bill = 5
        print(f"Child tickets are {bill}$.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are {bill}$.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on us")
    else:
        bill = 12
        print(f"Adult tickets are {bill}$.")

    want_photo = input("Do you want to have a photo? Type y for Yes and n for No.")
    if want_photo == "y":
        bill = 5
        print(f"Your final bill is {bill + 3}$")
    else:
        bill = 5
        print(f"Your final bill is {bill}$")

else:
    print("Sorry you have to grow taller before you can ride.")
