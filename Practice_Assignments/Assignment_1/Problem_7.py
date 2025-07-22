# Write a Python program to find given number is positive ,negative or zero.

a = int(input("Enter the number: "))
if a < 0:
    print("Number is negative!")
elif a > 0:
    print("Number is positive")
else:
    print("It sure is zero!")
