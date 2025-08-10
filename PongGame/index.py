from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

S = Screen()
S.setup(800, 600)
S.title("Pong Game")
S.bgcolor("black")
S.tracer(0)
S.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

score = Scoreboard()
ball = Ball()

S.onkey(r_paddle.move_up, "Up")
S.onkey(r_paddle.move_down, "Down")
S.onkey(l_paddle.move_up, "w")
S.onkey(l_paddle.move_down, "s")

flag = True
while flag:
    S.update()
    sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    if ball.xcor() > 380:
        score.left_score()
        ball.recenter()
    if ball.xcor() < -380:
        score.right_score()
        ball.recenter()

S.exitonclick()
