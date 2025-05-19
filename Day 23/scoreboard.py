from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 260)
        self.update_scoreboard()
        self.scoreboard.color("black")
        self.scoreboard.write(f"Score: {self.score}", align="center", font=FONT)
    
    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.goto(0, 230)
        self.scoreboard.write(f"Score: {self.score}", align="center", font=FONT)
        
    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write(f"Game Over", align="center", font=FONT)
        
