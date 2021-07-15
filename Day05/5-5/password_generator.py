# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for l in range(1, nr_letters + 1):
  password += random.choice(letters)

for s in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for n in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)

## Without using for loop
# selected_letters = random.choices(letters, k=nr_letters)
# selected_symbols = random.choices(symbols, k=nr_symbols)
# selected_numbers = random.choices(numbers, k=nr_numbers)
# combination = selected_letters + selected_symbols + selected_numbers
# easy_generated_password = ''.join(combination)
# print(easy_generated_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for l in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for s in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for n in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

strong_password = ""
for e in password_list:
  strong_password += e

print(strong_password)

## Without using for loop
# new_combination = random.sample(combination, len(combination))
# hard_generated_password = ''.join(new_combination)
# print(hard_generated_password)