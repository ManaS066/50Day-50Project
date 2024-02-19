import turtle

from turtle import *
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("coral")
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)
# timmy.color('red')
# timmy.fillcolor('yellow')
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break

# from turtle import Turtle
# from random import random
#
# t = Turtle()
# for i in range(100):
#     steps = int(random() * 500)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
#t.screen.mainloop()

# my_screen = Screen()  #my_screen is object
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

from prettytable import *
table=PrettyTable()
table.add_column("pokemon name", ['pikachu','sqirtle','charmender'])
table.add_column('field type' ,['electric','water','fire'])
table.align="l"
print(table)






















