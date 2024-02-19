from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scorebord import Scoreboard

ball = Ball()
# Creating Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG game")
screen.tracer(0)
scoreboard = Scoreboard()
# creating paddles

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# event listener

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()
    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    # detect when right paddle misses
    if ball.xcor() > 370:
        ball.reset_ball()
        l_paddle.reset_paddle((-350, 0))
        r_paddle.reset_paddle((350, 0))
        scoreboard.l_point()
    # detect when left paddle misses
    if ball.xcor() < -370:
        ball.reset_ball()
        l_paddle.reset_paddle((-350, 0))
        r_paddle.reset_paddle((350, 0))
        scoreboard.r_point()

screen.exitonclick()
