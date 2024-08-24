import random

print('''The rules of Rock, Paper, Scissors are straightforward:\n
Rock crushes Scissors.\n
Scissors cuts Paper.\n
Paper covers Rock.\n
''')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("Choose 0- rock, 1 - paper, 2 - scissors:\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
#User - Rock (0) beats Scissors (2)
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
# The following condition checks which choice is 'greater'
# Rock (0) < Paper (1) < Scissors (2) in this context
# So, if the computer's choice is greater than the user's choice,
# the computer wins.
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
