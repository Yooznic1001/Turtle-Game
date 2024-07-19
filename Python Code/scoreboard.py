FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0



    def scoree(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.write(f"score: {self.score}", align="center", font=FONT)
        self.score += 1


    def end(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 50, "normal"))
