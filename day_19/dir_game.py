from turtle import Turtle,Screen
tim =Turtle()
screen = Screen()
def move_forward():

    tim.forward(100)

def move_back():

    tim.backward(100)

def turn_left():
    new_heading =tim.heading()+20
    tim.setheading(new_heading)

def turn_right():
    new_heading =tim.heading()-20
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="d" ,fun=move_forward )
screen.onkey(key="a" ,fun=move_back )
screen.onkey(key="w" ,fun=turn_left )
screen.onkey(key="s" ,fun=turn_right )
screen.onkey(key="c" ,fun=clear )
screen.exitonclick()
