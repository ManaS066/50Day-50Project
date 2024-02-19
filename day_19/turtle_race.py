import turtle
from turtle import Turtle,Screen

screen=Screen()
import random
screen.setup(500,500)
bet=screen.textinput(title="select the turtle",prompt="enter the color of turtle on which you want to bet")
is_race_on=False
rang=["red","orange","yellow","green","blue","purple"]
all_turtle=[]
y=200
x = -230
for i in rang:
    new_turtle = Turtle("turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtle.append(new_turtle)
    y-=80
if bet:
    is_race_on=True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() >230:
            wining_color= turtle.pencolor()
            if wining_color==bet:
                print(f"you win with {bet} color")
            else:
                print("you loose")
                print(f"{turtle.pencolor()} won the race")
            is_race_on=False

        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)




















screen.exitonclick()