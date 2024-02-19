import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
count=0
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score=Scoreboard()
game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkeypress(player.move, "Up")
    car_manager.create()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False

    score.print_score(count)
    if player.is_at_finish():
        count+=1
        time.sleep(0.2)
        player.go_to_start()
        car_manager.level()
        score.clear()
        score.print_score(count)

screen.exitonclick()