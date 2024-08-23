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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("\n\nWelcome to the treasure Island\n\n")
print("Your mission is to find the treasure \n ")
choice_1 = input('You\'re at the Crossroad, Where do you want to go? Type to go "left" or "right": ')

if choice_1.lower() == "right":
    choice_2 = input('A big lake...An island in the middle of the lake...Type to "swim" or "wait" for the boat :? \n')
    if choice_2.lower() == "wait":
        choice_3 = input("Which door do you want to choose? Red or blue or yellow:? \n")
        if choice_3.lower() == "yellow":
            print("Eureka! You have won the treasure!!")
        else:
            print("The door is locked! You are being attacked by zombies! Keep trying your luck.")
    else:
        print("You swim in shark-infested waters! You're dead. Restart your treasure hunt.")
else:
    print("Game Over! Rise from the ashes and restart. There's never a Game Over!\n")
