from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Score

#creating the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#create snake body
#useing SNAKE CLASS
snake = Snake()
snake.create_snake()
food=Food()
score = Score()
# used to navigate our snake
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

#for moveing the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect colision with food

    if snake.head.distance(food) < 18 :
        food.refresh()
        snake.extend()
        score.increse_score()
    #detect collision with wall
    if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:

        #Modify it to reset score
        #score.game_over()

        snake.reset()
        print("Game over")
        score.reset()
    #detect colision with tail.
     # if the head colid with any segment then game is over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:

            snake.reset()
            score.reset()
            break
screen.exitonclick()
