# Pizza Order Project.

print("Welcome to Angela Pizza Deliveries!!")
special = input("Do you want Angela's special pizza? Y or N: ")
size = input("What size pizza do you want? S, M or L: ")
extra_cheese = input("Do you need extra cheese? Y or N: ")

# work out how much they need to pay based on their pizza choice
price = 120
if special == "Y":
    price *= 1.5
    if size == "S":
        price += 0
    elif size == "M":
        price += 50
    else:
        price += 100

    if extra_cheese == "Y":
        price += 5
    else :
        price += 0

else:
    if size == "S":
        price += 0
    elif size == "M":
        price += 50
    else:
        price += 100

    if extra_cheese == "Y":
        price += 5
    else:
        price += 0

print(f"Your total bill is {price}$, Our delivery boy Roro is on his way to deliver your Pizza.")