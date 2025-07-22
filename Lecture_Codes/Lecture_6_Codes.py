# Functions in Python - Block of statements that perform a specific task.
"""
def calc_sum(a, b): #Function definition
    return a + b # a & b are parameters

print(calc_sum(10, 20)) # Function & arguments
"""
"""
def avg_of_nums(a, b, c):
    avg = (a + b + c) / 3
    return avg

print("Average of 3 numbers is", avg_of_nums(int(input("1st number : ")), int(input("2nd number : ")), int(input("3rd number : "))))
"""

# Built-in function - print(), len(), range(), type()
# User defined functions - Functions constructed by programmer.

# Default parameters - Assigning a default value to parameter, which is used when no argument is passed.
"""
def avg_of_nums(a = 2, b = 2, c = 5): # Note - Non default arguments(if any) must come first, defaulted ones come last
    avg = (a + b + c) / 3
    return avg

print(avg_of_nums())
"""

# Practice
# WAF to print the length of a list(list ois the parameters)
"""
def list_len(list):
    return len(list)

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ["r", "o", "h", "a", "n"]

print((list_len(list_2)))
"""

# WAF to print the elements of the list in a single line.
"""
def print_list(list):
    for i in list:
        print(i, end = " ")

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ["r", "o", "h", "a", "n"]

print_list(list_2)
"""

# WAF to find the factorial of n
"""
def facto(n, fact = 1):
    for i in range(1, n+1, 1):
        fact *= i
    print(fact)

facto(int(input("Enter number : ")
"""

# WAF to convert USD to INR
"""
def usd_to_inr(usd):
    inr = usd * 90
    print(usd, "USD =", inr, "INR")

usd_to_inr(int(input("Enter your money in USD : ")))
"""

# WAF to take a number as input and check weather it is off or even.
"""
def odd_even():
    num = int(input("Enter number : "))
    if (num % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

odd_even()
"""

# Recursion - When a function calls itself repeatedly
"""
def show(n):
    if (n == 0):
        return
    print(n)
    show(n - 1)

show(5)
"""
"""
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n - 1) * n

print(fact(int(input("Enter number : "))))
"""

# Write a recursive function to calculate the sum of first n natural numbers.
"""
def sum_n(n):
    if (n == 0):
        return 0
    return sum_n(n -1) + n

print(sum_n(int(input("Enter number : "))))
"""

# Write a recursive function to print all elements in a list. Hint - Use list & index as parameters
"""
def print_list(list, i = 0):
    if (i == len(list)):
        return
    print(list[i], end = " ")
    print_list(list, i + 1)

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ["r", "o", "h", "a", "n"]

print_list(list_2)
"""

