import random
from art import logo
from art import vs
from game_data import data
print(logo)
def check_guess(a, b, user_input):
    if a['follower_count'] > b['follower_count']:
        return user_input == "A"
    else:
        return user_input == "B"
def high_low():
    score = 0
    a = "A"
    b = "B"
    random_a = random.choice(data)
    random_b = random.choice(data)
    wrong_guess = False
    while not wrong_guess:
        print(f"Compare {a.upper()}: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.")
        print(vs)
        print(f"Against {b.upper()}: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 10)
        print(logo)
        if check_guess(random_a, random_b, user_input):
            score += 1
            print(f"You're right! Current score: {score}")
            random_a = random_b
            random_b = random.choice(data)
            while random_b == random_a:
                random_b = random.choice(data)
        else:
            print("\n"*10)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            wrong_guess = True

high_low()

