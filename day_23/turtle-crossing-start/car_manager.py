COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE: int = 5
MOVE_INCREMENT: int = 5
import random
from turtle import Turtle


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create(self):
        rand_choice = random.randint(1, 5)
        if rand_choice == 1:
            new_car = Turtle("square")
            new_car.color(random.choices(COLORS))
            new_car.penup()

            new_car.shapesize(stretch_wid=1, stretch_len=2)
            Y = random.randint(-230, 250)
            new_car.goto(300, Y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level(self):
        self.car_speed += MOVE_INCREMENT
