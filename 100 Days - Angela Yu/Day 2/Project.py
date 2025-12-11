# Split Calculator

print("Welcome to the Split Calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? "))
number_of_folks = int(input("How many people are going to split the bill? "))
split = (bill * (1 + tip/100)) / number_of_folks
print(f"Each person should pay: {round(split, 2)}")
