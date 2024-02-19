import random
from turtle import Turtle, Screen, colormode
import turtle as t
t.colormode(255)

def rand_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r, g, b)
    return random_color

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue1")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
from random import Random
# timmy.home()
# for _ in range(100):
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)



# i=3
# while i<10:
#     for _ in range(i):
#         timmy.speed(10)
#         timmy.forward(60)
#         timmy.color(random.choices(color))
#         ang=360/i
#         timmy.left(ang)
#     i+=1







# Function to move the screen up
def scroll_up():
    canvas.yview_scroll(-1, "units")

# Function to move the screen down
def scroll_down():
    canvas.yview_scroll(1, "units")

# Create a turtle screen
screen = t.Screen()
screen.setup(width=400, height=300)

# Create a turtle canvas
canvas = screen.getcanvas()

# Set up event listeners for mouse wheel scrolling
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# Create a turtle for demonstration

# Listen for scroll events
screen.listen()











color = ["red","green","blue","cyan","orange red","dark magenta"]
dir = [0 , 90 , 180 , 270]
for _ in range(1000):
    timmy.speed(100000)
    timmy.pensize(8)

    timmy.pencolor(rand_col())
    timmy.pencolor()
    timmy.forward(30)
    timmy.setheading(random.choice(dir))













