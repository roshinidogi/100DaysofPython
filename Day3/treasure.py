print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("\n   Welcome to the Treasure Island!\nYour mission is to find the treasure.\n")
dir = input("       Type 'Left' or 'Right'\n")
if dir == "Left":
    print("You have come to a lake. There is an island in the middle of the lake.\n")
    des = input("   Type 'Swim' to swim across or 'Wait' to wait for a boat.\n")
    if des == "Wait":
        print("\nYou have arrived at the island unharmed. There is a house with three doors.\n")
        door = input("   One 'Red', one 'Blue' and one 'Yellow'. Which color do you choose?\n")
        if door == "Yellow":
            print("Congratulations!! You Won.")
        elif door == "Red":
            print("Burned by Fire ## GAME OVER ##")
        elif door == "Blue":
            print("Eaten by Beasts ## GAME OVER ##")
        else:
            print("Sorry, you lose ## GAME OVER ##")
    else:
        print("Attacked by Trout ## GAME OVER ##")
else:
    print("Fall into a Hole ## GAME OVER ##")