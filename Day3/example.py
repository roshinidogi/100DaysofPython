# 1 Odd or Even
# a= int(input("Enter a number:\n"))
# if a % 2 == 0:
#     print("The number is even")
# else :
#     print("The number is odd")
# 2 Height and Age req for a ride
# print("Welcome to the PRIMEVAL WHIRL!!\n")
# height = int(input("What is the height of the customer in cm?\n"))
# bill = 0
# if height > 120:
#     print("You are eligible to play!!\n")
#     age = int(input("What is the age of the customer in years?\n"))
#     if age < 12:
#         bill = 5
#         print("YAY!!, The children ticket price is $5 only.")
#     elif age <= 18:
#         bill = 7
#         print("The youth ticket price is $7 only.")
#     else:
#         bill = 12
#         print("The adult ticket price is $12 only.")
#     photo = input("Do you want your photo taken? Type Y for yes or N for no\n")
#     if photo == "Y":
#         bill += 3
#         print(f"It will be $3 more!! The total payment is $ {bill} only.")
#     else:
#         print("No extra charge, Please enjoy your ride!!")
# else:
#     print("Your height did not the reach the eligible requirement, Sorry : (")
# 3 Pizza delivery
# print("Welcome to the Python PIZZA DELIVERIES!!\n")
# size = input("What size pizza would you like to have? S, M or L\n")
#
# if size == "S":
#     pepperoni = input("Would you like to add pepperoni to your pizza? Y or N\n")
#     extra_cheese = input("Would you like to add extra cheese to your pizza? Y or N\n")
#     size = 8
#     pep = 2
#     che = 1
#     if pepperoni == "Y" and extra_cheese == "Y":
#         print(f"Your final bill is: ${size+pep+che}\n")
#     elif pepperoni == "N" and extra_cheese == "Y":
#         print(f"Your final bill is: ${size+che}\n")
#     elif pepperoni == "Y" and extra_cheese == "N":
#         print(f"Your final bill is: ${size+pep}\n")
#     else:
#         print(f"Your final bill is: ${size}\n")
# elif size == "M":
#     pepperoni = input("Would you like to add pepperoni to your pizza? Y or N\n")
#     extra_cheese = input("Would you like to add extra cheese to your pizza? Y or N\n")
#     size = 10
#     pep = 3
#     che = 1
#     if pepperoni == "Y" and extra_cheese == "Y":
#         print(f"Your final bill is: ${size+pep+che}\n")
#     elif pepperoni == "N" and extra_cheese == "Y":
#         print(f"Your final bill is: ${size+che}\n")
#     elif pepperoni == "Y" and extra_cheese == "N":
#         print(f"Your final bill is: ${size+pep}\n")
#     else:
#         print(f"Your final bill is: ${size}\n")
# elif size == "L":
#     pepperoni = input("Would you like to add pepperoni to your pizza? Y or N\n")
#     extra_cheese = input("Would you like to add extra cheese to your pizza? Y or N\n")
#     size = 12
#     pep = 3
#     che = 1
#     if pepperoni == "Y" and extra_cheese == "Y":
#         print(f"Your final bill is: ${size+pep+che}\n")
#     elif pepperoni == "N" and extra_cheese == "Y":
#         print(f"Your final bill is: ${size+che}\n")
#     elif pepperoni == "Y" and extra_cheese == "N":
#         print(f"Your final bill is: ${size+pep}\n")
#     else:
#         print(f"Your final bill is: ${size}\n")
# else:
#     print("You typed the incorrect option. Please try again.")
#3 Another easy way
print("Welcome to the Python Pizza Delivery!\n")
size = input("What size would you like to have? S, M or L\n")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry, Please enter S, M, or L")
pepperoni = input("Would you like pepperoni? (y/n)\n")
if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3
cheese = input("Would you like cheese? (y/n)\n")
if cheese == "y":
    bill += 1
print(f"Your final bill is ${bill}")