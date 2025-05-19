#pong game

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        Scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        Scoreboard.r_point()

    if Scoreboard.l_score == 5:
        Scoreboard.goto(0, 0)
        Scoreboard.write("Left Player Wins!", align="center", font=("Courier", 24, "normal"))
        game_is_on = False
    
    if Scoreboard.r_score == 5:
        Scoreboard.goto(0, 0)
        Scoreboard.write("Right Player Wins!", align="center", font=("Courier", 24, "normal"))
        game_is_on = False




screen.exitonclick()