import random
import turtle
import colorama
from turtle import Turtle,Screen
  #only use for extract color
# import colorgram
# rgb_color=[]
# color = colorgram.extract('image.jpg',7)
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
turtle.colormode(255)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188),(40,50,60),(38,67,43)]


tim=Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dot = 100

for dot_count in range(1,num_of_dot+1):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen= Screen()
screen.exitonclick()