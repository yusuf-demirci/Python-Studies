from turtle import Turtle
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-240, 260)
        self.level = 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)