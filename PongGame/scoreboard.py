from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.display()

    def display(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", False, "center", ("arial", 30, "bold"))

    def left_score(self):
        self.l_score += 1
        self.display()

    def right_score(self):
        self.r_score += 1
        self.display()