import random
from art import logo
from art import again
print(logo)
print("Welcome to the Guessing Number Game!\nI am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty (easy, hard): ")
def guess_type(n):
    num = random.randint(1, 100)
    # print(f"Correct guess is {num}")
    guessed = False
    while not guessed and n > 0:
        print(f"You have {n} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == num:
            guessed = True
            print(f"You got it right! The number was {num}.\n")
        elif guess < num:
            print("\nYour guess is too low.\n")
        else:
            print("\nYour guess is too high.\n")
        n -= 1
    if not guessed and n == 0:
        print(f"\nYou are out of guesses, The correct guess is {num}. Better luck next time.\n")
def guess_function():
    if difficulty == "easy":
        guess_type(10)
    elif difficulty == "hard":
        guess_type(5)
guess_function()
game_over = False
while not game_over:
    print(again)
    guess_again = input("Do you want to guess again? Type 'y' or 'n': ")
    if guess_again == "y":
        difficulty = input("Choose a difficulty (easy, hard): ")
        guess_function()
    else:
        game_over = True