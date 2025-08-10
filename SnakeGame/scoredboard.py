from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        with open("HighScore.txt") as HighScore:
            self.h_score = int(HighScore.read())

    def score_inc(self):
        self.score += 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.h_score}", False, "center", ('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over Your score {self.score}", False, "center", ('Arial', 24, 'bold'))
        if self.score > self.h_score:
            with open("HighScore.txt", "w") as HighScore:
                HighScore.write(str(self.score))
