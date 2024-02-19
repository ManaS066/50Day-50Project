STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 270
from turtle import Turtle





class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)
    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

