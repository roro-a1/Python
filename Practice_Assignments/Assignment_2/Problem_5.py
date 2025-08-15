# Write a function to return simple interest.

def simple_int(p, r, t):
    interest = (p * r * t)/ 100
    return interest

p = int(input("Enter principle amount: "))
r = float(input("The rate of interest: "))
t = float(input("Please enter time in terms of years: "))

print("Simple interest is", simple_int(p, r, t))
