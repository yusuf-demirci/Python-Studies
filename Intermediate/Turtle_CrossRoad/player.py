from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(15)

    def reset_position(self):
        self.goto(STARTING_POSITION)
