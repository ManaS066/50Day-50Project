FONT = ("Courier", 14, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 250)

    def print_score(self, level):
        self.write(f"Level : {level} ", align="center", font=FONT)
