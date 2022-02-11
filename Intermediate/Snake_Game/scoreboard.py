from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        with open("Data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()



        
