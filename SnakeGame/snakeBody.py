from turtle import Turtle


class Snake:
    def __init__(self):
        self.turtle_l = []
        self.distance = 10
        self.create_snake()

    def create_snake(self):
        x, y = 0, 0
        for _ in range(3):
            t = Turtle(shape="circle")
            t.color("green")
            t.penup()
            t.goto(x, y)
            x = x - 20
            self.turtle_l.append(t)

    def move(self):
        for _ in range(len(self.turtle_l) - 1, 0, -1):
            self.turtle_l[_].goto(self.turtle_l[_ - 1].xcor(), self.turtle_l[_ - 1].ycor())
        self.turtle_l[0].forward(self.distance)

    def move_right(self):
        if self.turtle_l[0].heading() != 180:
            self.turtle_l[0].setheading(0)

    def move_left(self):
        if self.turtle_l[0].heading() != 0:
            self.turtle_l[0].setheading(180)

    def move_up(self):
        if self.turtle_l[0].heading() != 270:
            self.turtle_l[0].setheading(90)

    def move_down(self):
        if self.turtle_l[0].heading() != 90:
            self.turtle_l[0].setheading(270)

    def expand_snake(self):
        x, y = self.turtle_l[len(self.turtle_l) - 1].xcor() - 20, self.turtle_l[len(self.turtle_l) - 1].ycor()
        t = Turtle(shape="circle")
        t.color("green")
        t.penup()
        t.goto(x, y)
        self.turtle_l.append(t)

    def collision(self):
        head = self.turtle_l[0]
        if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 210 or head.ycor() < -280:
            return True
        else:
            for _ in self.turtle_l[1:]:
                if head.distance(_) < 10:
                    return True
                else:
                    return False

