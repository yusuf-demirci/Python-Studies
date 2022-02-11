import art
import random
from game_data import data
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def choose_data():
  return random.choice(data)

def compare(answer, followerA, followerB):
  if answer == "a" and followerA > followerB:
    return True
  elif answer == "b" and followerB > followerA:
    return True
  else:
    return False

score = 0
print(art.logo)


  
  
comparison1 = choose_data()
should_continue = True
 
while should_continue:
  comparison2 = choose_data()
  print("Compare A: ", comparison1["name"],"\b, a", comparison1["description"],"\b, from", comparison1["country"])
  
  print(art.vs)
  print("Against B:", comparison2["name"],"\b, a", comparison2["description"],"\b, from", comparison2["country"])

  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
  should_continue = compare(answer, comparison1["follower_count"], comparison2["follower_count"])

  cls()
  print(art.logo)

  if should_continue == True:
    score += 1
    print(f"You're right. Your current score: {score}")
    if answer == "b":
      comparison1 = comparison2
  else:  
    print(f"Sorry, that's wrong. Your final score: {score}")

