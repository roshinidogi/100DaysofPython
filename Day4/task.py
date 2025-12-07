import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random.random() function is to print the next floating point number from 0.0 to 1.0
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random.uniform(a,b) function is to get the random floating point number from a range
# randon_float_number = random.uniform(1, 10)
# print(randon_float_number)

# Heads or Tails Program
# random_choice = random.randint(1,2)
# if random_choice == 1:
#     print("Heads")
# elif random_choice == 2:
#     print("Tails")

# Who will pay the bill? Banker Roulette
# random.choice() function is to print something randomly in a sequence or list
# friend = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friend))

# 2nd Option
# random_index = random.randint(0, len(friend)-1)
# print(friend[random_index])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])