# Write a Python function to find the maximum of three numbers.

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))

if (a1 >= a2 and a1 >= a3):
    print("Greatest of 3: ", a1)
elif(a2 >= a1 and a2 >= a3):
    print("Greatest of 3: ", a2)
else:
    print("Greatest of 3: ", a3)
