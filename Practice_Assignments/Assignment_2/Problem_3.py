# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def fact(a):
    fact_num = 1
    if a == 0:
        fact_num = 1
    else:
        for i in range(1, a + 1):
            fact_num = fact_num * i
    print("Factorial =", fact_num)

num = int(input("Enter the number: "))
fact(num)