# Rock Paper Scissors Game
from random import random
import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

# Paper
paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

# Scissors
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')
rps = [rock, paper, scissors]
option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
if option < 0 or option > 2:
    print("Choose a valid option!")
else:
    print("You choose\n", rps[option])
    print("Computer choose\n", rps[computer_choice])
    if option == computer_choice:
        print("That's a tie!")
    elif option != computer_choice:
        if (option == 0 and computer_choice == 2) or \
                (option == 1 and computer_choice == 0) or \
                (option == 2 and computer_choice == 1):
            print("You Win!")
        else:
            print("You Lose!")

# Write your code by following the steps that needed to be done
# Don't blindly write code by thinking it is correct check the syntax
# I forgot to change the option from string to int