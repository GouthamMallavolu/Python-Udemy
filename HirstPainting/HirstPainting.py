# The Hirst Painting with turtle

import random
import colorgram
import turtle

rgb_colors = []
image = input("Enter the File name of image with extension : ")
speed = input("Enter the speed of your Turtle should be 'slow/fast/fastest' : ")
dot_num = int(input("Enter how many lines you want the dots should be in multiples of 10 : "))
dot = int(input("Enter the Dot size you want : "))

try:
    colors = colorgram.extract(image, 30)
    for _ in colors:
        r = _.rgb.r
        g = _.rgb.g
        b = _.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    turtle.colormode(255)

    t = turtle.Turtle()
    t.penup()
    t.hideturtle()

    t.speed(speed)

    t.setheading(225)
    t.forward(300)
    t.setheading(0)

    for _ in range(1, dot_num + 1):
        t.dot(dot, random.choice(rgb_colors))
        t.forward(50)

        if _ % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)

    screen = turtle.Screen()
    screen.exitonclick()

except FileNotFoundError:
    print("Oops ! There was no such Image file in the Path")
