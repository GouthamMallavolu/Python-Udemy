from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(250, 250)

    def display_score(self):
        self.clear()
        self.write(f"{self.score} / 50", align="right", font=("Arial", 12, "bold"))

    def score_inc(self):
        self.score += 1
