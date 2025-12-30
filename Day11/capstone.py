import random
from art import logo
def deal_card():
    """Returns a random card from the list."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Computer has a Blackjack, You lose"
    elif u_score == 0:
        return "You have a Blackjack!, You win"
    elif u_score > 21:
        return "You went over, You lose"
    elif c_score > 21:
        return "You win! Computer went over"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def calculate_score(cards):
    """Takes a list of cards and returns the score of the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def blackjack():
    print("\n" * 100)
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Type 'y' to get another card or 'n' to pass: ")
            if draw_card.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final cards: {user_cards}, and it's total score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, and it's total score: {computer_score}")
    print("\n", compare(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    blackjack()