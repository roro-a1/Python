# Write a function to return compound interest.

def comp_interest(p, r, t):
    amount = p*(1 + (r/100))**t
    interest = amount - p
    return interest

p = int(input("Enter principle amount: "))
r = float(input("The rate of interest: "))
t = float(input("Please enter time in terms of years: "))

print("Compound interest is", comp_interest(p, r, t))