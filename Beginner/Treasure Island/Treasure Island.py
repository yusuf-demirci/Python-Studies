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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

cross_road = input("You are at a cross-road. Where do you want to go? 'left' or 'right?' ").lower()

if cross_road != "left":
    print("You fell into a hole. Game Over!")
else:
    lake = input("""You came to a lake. There is an island in the middle of the lake. 
Type 'wait' to wait for a boat. Type 'swim' to swim to the island. """).lower()
    
    if lake != "wait":
        print("You are attacked by  crocodile. Game Over!")
    else:
        door = input("""You arrived at the island. There is a house with 3 doors.
Red, yellow and blue. Which one do you choose? """).lower()

        if door == "red":
            print("You are burned by fire. Game Over!")
        elif door == "yellow":
            print("Congragulations! You found the treasure.")
        elif door == "blue":
            print("You are eaten by beasts. Game Over!")
        else:
            print("Game Over!")
input()