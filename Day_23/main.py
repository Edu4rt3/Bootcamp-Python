#Turtle crossing game 

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.listen()
player = Player()
screen.onkey(player.move_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars() 
    for car in car_manager.all_cars:
        if player.player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.finish_line():
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        car_manager.increase_speed()

screen.exitonclick() 