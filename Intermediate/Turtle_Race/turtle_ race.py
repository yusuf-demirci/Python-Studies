from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(700, 500)
user_bet = screen.textinput("Make your bet:", "Choose a color: ")


color_list = ["red", "green", "blue", "orange", "yellow", "purple"]
turtle_list = []
a = -125
is_race_on = False

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color_list[i])
    tim.penup()
    tim.goto(-250, a)
    a += 50
    turtle_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 330:
            is_race_on = False
            winner = turtle
            if winner.pencolor() == user_bet:
                print(f"You've won. {winner.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost. {winner.pencolor()} turtle is the winner!")


screen.exitonclick()