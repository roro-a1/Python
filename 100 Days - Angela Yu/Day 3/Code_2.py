# Nested if Statements and elif Statements.

"""
print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm? "))

if height >= 120 :
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12 :       # Nested if Statement.
        print("Your fare is 5$.")
    elif age <= 18 :
        print("Your fare is 7$.")
    else:
        print("Your fare is 12$.")
else:
    print("Sorry you have to grow taller before you can ride.")
"""

# Multiple if Statements in Succession.

print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm? "))

if height >= 120 :
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12 :  # Nested if Statement.
        bill = 5
        print(f"Child tickets are {bill}$.")
    elif age <= 18 :
        bill = 7
        print(f"Youth tickets are {bill}$.")
    else:
        bill = 12
        print(f"Adult tickets are {bill}$.")
    
    want_photo = input("Do you want to have a photo? Type y for Yes and n for No.")
    if want_photo == "y":
        print(f"Your final bill is {bill + 3}$")
    else:
        print(f"Your final bill is {bill}$")
    
else:
    print("Sorry you have to grow taller before you can ride.")

