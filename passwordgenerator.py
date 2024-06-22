# Password Strong Generator

import random

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Strong Generator!")

nr_lowercase_letters = 2
nr_uppercase_letters = 1
nr_symbols = 3
nr_numbers = 3


list_password = []

for char in range(1, nr_lowercase_letters + 1):
    list_password += random.choice(lowercase_letters)

for char in range(1, nr_uppercase_letters + 1):
    list_password += random.choice(uppercase_letters)

for char in range(1, nr_symbols + 1):
    list_password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    list_password += random.choice(numbers)

random.shuffle(list_password)

password = ""

for char in list_password:
    password += char

print(f'Your passaword is: {password}')
