
# Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit price is Rs 5 and there is a discount of 10 percent for quantities over 30
# and a 15 percent discount for quantities over 50.

def price(quant):
    unit = 5
    if quant <= 30:
        total = unit * quant
    elif quant > 30 and quant <= 50:
        total = unit * quant * 0.9
    else:
        total = unit * quant * 0.85
    print("Price for given quantity is Rs.", total)


quant = int(input("Enter the quantity: "))
price(quant)