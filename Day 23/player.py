from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("black")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(STARTING_POSITION)

    def move_up(self):
        self.player.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.player.ycor() > FINISH_LINE_Y:
            self.player.goto(STARTING_POSITION)
            return True
        return False
    
    def reset_position(self):
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)
        self.player.forward(MOVE_DISTANCE)
        

