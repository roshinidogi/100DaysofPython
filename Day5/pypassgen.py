#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# letters = random.sample(letters, nr_letters)
# symbols = random.sample(symbols, nr_symbols)
# numbers = random.sample(numbers, nr_numbers)
# password = ""
# for nr_letters in range(len(letters)):
#     password += letters[nr_letters]
# for nr_numbers in range(len(numbers)):
#     password += numbers[nr_numbers]
# for nr_symbols in range(len(symbols)):
#     password += symbols[nr_symbols]
# print(f"Your generated password is: {password}")

#2 simple but I did not get it
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for i in range(0, nr_numbers):
#     password += random.choice(numbers)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# print(f"Your generated password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Convert the password to a list to shuffle the order of items in the list use random.shuffle(list) function
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your generated password is: {password}")