# Turtle Race using Turtle module in Python

from turtle import Turtle, Screen
import random

S = Screen()
S.setup(width=500, height=400)

hidden_t = Turtle()
hidden_t.hideturtle()

S.title("Turtle Race")
S.bgcolor("light grey")

colors = ["red", "green", "yellow", "blue", "purple", "violet"]

x, y = -230, -100

turtle_l = []
loc = []

for _ in colors:
    t = Turtle(shape="turtle")
    t.color(_)
    t.penup()
    t.goto(x, y)
    y = y + 40
    turtle_l.append(t)

choice = S.textinput(title="Turtle Race", prompt="Who will WIN the race ?")

flag = True
winner = ""

while flag:
    for _ in turtle_l:
        _.forward(random.randint(10, 50))
        if _.xcor() >= 210:
            flag = False
            winner = _
            break

if winner.pencolor() == choice:
    hidden_t.color("green")
    hidden_t.write("You have WON !!", align="right", font=("Arial", 13, "normal"))
else:
    hidden_t.color("red")
    hidden_t.write("You have Lost !!", align="right", font=("Arial", 13, "normal"))

S.exitonclick()
