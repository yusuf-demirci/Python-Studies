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

import random

print("Welcome to the Rock-Paper-Scissors Game!")
number = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))

if number == 0:
  choice = rock
elif number == 1:
  choice = paper
elif number == 2:
  choice = scissors

choice_list = [rock, paper, scissors]
comp_choice = random.choice(choice_list)

if number>2 or number<0:
  print("You entered an invalid number. You lose!")
else:
  print(choice)
  print("Computer's choice:\n", comp_choice)

  if choice == comp_choice:
    print("It's a draw!")
  elif (choice == rock and comp_choice == paper) or (choice == paper and comp_choice == scissors) or (choice == scissors and comp_choice == rock):
    print("You lose!")
  else:
    print("You win!")


input()



