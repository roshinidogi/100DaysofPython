import random
from hangman_words import word_list
from hangman_art import welcome
from hangman_art import logo
from hangman_art import stages

print(welcome)
print(logo)

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
place_holder = ""
for letter in range(len(chosen_word)):
    place_holder += "_"
print(place_holder)

# display = ["_"]*len(chosen_word)
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     # guesses.append(guess)
#     for i in range(len(chosen_word)):
#         if chosen_word[i] == guess:
#             display[i] = guess
#     print("".join(display))

game_over = False
correct_letters = []
while not game_over and lives > 0:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in correct_letters:
        print("You have already guessed this letter!Try again!")
        continue
    elif guess in chosen_word:
        correct_letters.append(guess)
    else:
        lives -= 1
        print("Lives left: ", lives)
    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    print(stages[lives])
    if "_" not in display:
        game_over = True
        print("You win!")
if lives == 0:
    print(f"You are all out of lives, you lose!. The word was: {chosen_word}.")