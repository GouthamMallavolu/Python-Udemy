from turtle import Turtle


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def setpos(self, x, y, name):
        self.goto(x, y)
        self.write(name, align="center", font=("Arial", 9, "normal"))
