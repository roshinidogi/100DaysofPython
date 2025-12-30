from coffeemenu import MENU
from art import logo
from coffeemenu import report

def print_report(rep):
    print(f"Water: {str(rep['ingredients']['water'])}ml")
    print(f"Milk: {str(rep['ingredients']['milk'])}ml")
    print(f"Coffee: {str(rep['ingredients']['coffee'])}g")
    print(f"Money: ${str(rep['cost'])}")

def coins(user_choice):
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    user_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if user_coins < MENU[user_choice]["cost"]:
        remain = MENU[user_choice]["cost"] - user_coins
        print(f"Sorry, you don't have enough money! You need ${round(remain, 2)} more.") # round(variable, number) to round the decimal part by number ex: 2.450001 to 2.45
        return False
    elif user_coins > MENU[user_choice]["cost"]:
        change = user_coins - MENU[user_choice]["cost"]
        print(f"It's only ${MENU[user_choice]['cost']}, Here is ${round(change,2)} in change.")
        print(f"Here is your {user_choice} ☕ Enjoy!")
        return True
    else:
        print(f"That's perfect change, Here is your {user_choice} ☕️ Enjoy!")
        return True

print(logo)
print(" ☕️ ☕️ ☕️  Welcome to the Roshini's Coffee Machine! ☕️ ☕️ ☕️ ")
making_coffee = True
while making_coffee:
    user_input = input("What kind of coffee ☕️  would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        making_coffee = False
    elif user_input in MENU:
        coffee_available = True
        for item in MENU[user_input]["ingredients"]:
            if MENU[user_input]["ingredients"][item] > report["ingredients"][item]:
                print(f"Sorry, {item} is too low.")
                coffee_available = False
                break
        if coffee_available:
            payment_success = coins(user_input)  # Always make sure to print function if you use 'return' in the function
            if payment_success:
                for item in MENU[user_input]["ingredients"]:
                    report["ingredients"][item] -= MENU[user_input]["ingredients"][item]
                report["cost"] += MENU[user_input]["cost"]
    elif user_input == "report":
        admin = input("Reports are accessible for only Managers. Are you a Manager? (yes/no): ")
        if admin == "yes":
            user_name = input("What is your username?: ")
            password = input("What is your password?: ")
            if report["username"] != user_name or report["password"] != password:
                print("Sorry, your username or password is incorrect.")
            else:
                print(f"Woohoo! Here you go")
                print_report(report)
        else:
            print("Sorry, Please try again later.")
    else:
        print("Sorry, Invalid Input.")