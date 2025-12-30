import random


# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You win!")
# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# Ans: The for loop is assigning the temp i value in a range of 1 to 20 (not including 20), it can be any value but should be in the range, range(1,3) = 0, 1, 2
# 2. When is the function meant to print "You win"?
# Ans: If the i value is 20
# 3. What are your assumptions about the value of i?
# Ans: The i value in if condition is out of range, so it doesn't print anything

# from random import randint
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_number = randint(0, 5)
# print(dice_images[dice_number])

# year = int(input("What's your year of birth?\n"))

# if 1980 < year < 1994:
    # print("You are a Millennial.")
# elif year >= 1994:
    # print("You are a Gen Z.")
# else:
    # print("You are old.")

# try:
#     age = int(input("What's your age?\n"))
# except ValueError:
#     print("Sorry, you didn't enter a number. Enter a numeric value like 12.")
#     age = int(input("What's your age?\n"))
#
# if age < 18:
#     print(f"Sorry, you are under {age} years old.")
# else:
#     print(f"You are over {age} years old.")

# word_per_page = 0
# pages = int(input("How many pages? "))
# word_per_page = int(input("How many words per page? "))
# total_words = pages * word_per_page
# print(total_words)

# import maths
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1, 2, 3, 5, 13])

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# print(is_leap(1994))

def fizz_buzz(target):
    for number in range(1, target+1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(15)
