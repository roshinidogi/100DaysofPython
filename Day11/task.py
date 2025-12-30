from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play.lower() == "y":
    print("\n"*100)
    print(logo)
    my_cards = []
    current_score = 0
    computer_score = 0
    computer_cards = []
    for i in range(2):
        my_cards.append(random.choice(cards))
        current_score = sum(my_cards)
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
    print(f"Your cards: {my_cards}, current score: {current_score} \n")
    print(f"Computer's first card: {computer_cards[0]}\n")
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
    more = input("Type 'y' to get another card or 'n' to pass: ")
    if more.lower() == "y":
        s = random.choice(cards)
        my_cards.append(s)
        current_score += s
    for i in my_cards and computer_cards:
        if i == 11 and current_score > 21:
            i = 1
            current_score -= 10
    print(f"Your cards: {my_cards}, current score: {current_score} \n")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}\n")
    if current_score > 21:
        print("You Lose!")
    elif computer_score > 21:
        print("You Win!")
    elif computer_score == 21:
        print("You Lose!")
    elif computer_score == current_score:
        print("It's a tie!")
    elif current_score == 21:
        print("You Win!")
    elif current_score and computer_score < 21:
        if current_score > computer_score:
            print("You Win!")
        elif current_score < computer_score:
            print("You Lose!")

elif play.lower() == "n":
    print("Thank you for playing!")