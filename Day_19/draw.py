from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_backwards():
    tim.backward(10)

def move_forwards():
    tim.forward(10)

def turn_right():
    tim.right(15)

def turn_left():
    tim.left(15)

def clear():
    tim.reset()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")
screen.exitonclick()