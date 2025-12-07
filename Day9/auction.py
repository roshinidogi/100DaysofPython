from art import logo
print(logo)
print("Welcome to the secret auction program!")
credentials = {}
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
credentials[name] = bid
more = input("Are there any other bidders? Type 'yes' or 'no'.")
max_bid = 0
winner = ""
more_bidders = True
while more_bidders:
    if more == "yes":
        print("\n"*100)
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        credentials[name] = bid
        more = input("Are there any other bidders? Type 'yes' or 'no'.")
    else:
        more_bidders = False
for bidder in credentials:
    amount = credentials[bidder]
    if amount > max_bid:
        max_bid = amount
        winner = bidder 
print("\n"*100)
print(f"The highest bidder is: '{winner}' and the amount is: ${max_bid}")
# Extra

# print("\n"*50)

admin = input("If you verify as an ADMIN!! You can view the list of all bidders? Type 'yes' or 'no'.")
if admin == "yes":
    username = input("What is your username?: \n")
    password = input("What is your password?: \n")
    if username == "pdcfy" and password == "Rosh@01":
        print(credentials)
    else:
        print("Invalid username or password!!")