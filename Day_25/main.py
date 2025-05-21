# U.S. States Game

import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game ")
image =  "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()

guessed_states = []
score = 0
game_is_on = True


while game_is_on:
    answer_states = screen.textinput(title="Gues the State", prompt="What's another state's name?r").title()

    if answer_states == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
        screen.clear()
        t.hideturtle()
        t.penup()
        t.goto(0, 0)
        t.write(f"The Game is over, your score is {score}", align="center", font=("Courier", 24, "normal"))

    if answer_states in all_states:
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_states)
        guessed_states.append(answer_states)
        score += 1
    
screen.exitonclick()




