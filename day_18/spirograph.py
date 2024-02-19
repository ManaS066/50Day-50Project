import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()


def rand_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed("fastest")


def draw_spiralgraph(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.pencolor(rand_col())
        tim.pensize(2)
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)
draw_spiralgraph(10)

screen = Screen()
screen.exitonclick()
