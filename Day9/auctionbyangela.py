from art import logo
print(logo)
print("Welcome to the secret auction program!")
credentials = {}

def find_the_highest_bidder(bid_dictionary):
    max_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        amount = bid_dictionary[bidder]
        if amount > max_bid:
            max_bid = amount
            winner = bidder
    print("\n" * 100)
    print(f"The highest bidder is: '{winner}' and the amount is: ${max_bid}")
more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    credentials[name] = bid
    more = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if more == "no":
        find_the_highest_bidder(credentials)
        more_bidders = False
    else:
        print("\n" * 100)

# Extra
all = input("Do you want the list of all bidders? Type 'yes' or 'no'.")
if all == "yes":
    print(credentials)