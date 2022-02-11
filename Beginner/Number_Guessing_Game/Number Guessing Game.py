import art
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def number_guessing_game():
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  number = random.randint(1, 20)
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  remaining_attempt = 5

  if difficulty == "easy":
    remaining_attempt += 5
    
  print(f"You have {remaining_attempt} attempts remaining to guess the number.")

  while True:
    user_guess = int(input("Make a guess: "))
    if user_guess == number :
      print(f"You got it! The answer was {number}.")
      break
    elif user_guess < 1 or user_guess > 100:
      print("Invalid input.")
    elif user_guess > number :
      print("Too high.")
    elif user_guess < number :
      print("Too low.")
    remaining_attempt -= 1
    if remaining_attempt == 0:
      print("You've run out of guesses, you lose.")
      break
    print("Guess again.")
    
    print(f"You have {remaining_attempt} attempts remaining to guess the number.")
    
  play_again = input("Do you want to play again? Type 'y' or 'n' ")

  if play_again == 'y':
    cls()
    number_guessing_game()

number_guessing_game()




 
