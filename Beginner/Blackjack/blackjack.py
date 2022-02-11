import art
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calculate_score(list): 
    if sum(list) == 21 and len(list) == 2:
      return 0
    elif sum(list)>21 and 11 in list:
      list.remove(11)
      list.append(1)
    
    return sum(list)

def compare(user_score, comp_score):
  if user_score == comp_score:
    return "It's a draw"
  elif user_score == 0:
    return "You win with a blackjack"
  elif comp_score == 0:
    return "Computer win with a blackjack"
  elif user_score > 21:
    return "You went over, you lose"
  elif comp_score > 21:
    return "Computer went over, you win"
  elif user_score>comp_score:
    return "You win"
  else:
    return "Computer win"


def blackjack():
  print(art.logo)

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  comp_cards = []

  for i in range(2):
    user_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))

  user_score = calculate_score(user_cards)
  comp_score = calculate_score(comp_cards)

  print(f"Your cards: {user_cards}, Your score: {user_score}")
  print("Computer's first card:", comp_cards[0])

  while user_score<21 and user_score != 0:
   
    get_card = input("Type 'y' to get another card or type 'n' to pass: ")
    
    if get_card == 'y':
      user_cards.append(random.choice(cards))
      user_score = calculate_score(user_cards)
      print("You choose a card")
      
      print(f"Your cards: {user_cards}, Your score: {user_score}")
    else:
      break

  while comp_score<17 and sum(user_cards)<=21 and comp_score != 0:
    comp_cards.append(random.choice(cards))
    comp_score = calculate_score(comp_cards)
    print("Computer chooses card")

  print(f"Computer's cards: {comp_cards}, Computer score: {comp_score}")
  print(compare(user_score,comp_score))
  play_again = input("Would you like to play again? Type 'y' or 'n': ")

  if play_again == 'y':
    cls()
    blackjack()

blackjack()