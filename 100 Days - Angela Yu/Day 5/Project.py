# Password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '+']

print("Welcome to my Password generator!")
number_letters = int(input("How many letters should your password have?\n"))
number_symbols = int(input("How many symbols should your password have?\n"))
number_numbers = int(input("How many numbers should your password have?\n"))

# Easy Level
"""
password = ""

for chat in range(1, number_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for sign in range(1, number_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

for num in range(1, number_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char

print(password)
"""

# Hard Level

password_list = []

for chat in range(1, number_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char

for sign in range(1, number_symbols + 1):
    random_char = random.choice(symbols)
    password_list += random_char

for num in range(1, number_numbers + 1):
    random_char = random.choice(numbers)
    password_list += random_char

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i

print(password)