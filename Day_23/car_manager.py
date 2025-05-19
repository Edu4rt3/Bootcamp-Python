from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.random_chance = random.randint(1, 6)
        if self.random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        if self.car_speed < 20:
            self.car_speed += MOVE_INCREMENT
        else:
            self.car_speed = 20
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_speed > 20:
            self.car_speed = 20

    def reset_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        for car in self.all_cars:
            car.goto(1000, 1000)
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_speed > 20:
            self.car_speed = 20
