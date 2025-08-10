from turtle import Screen
from snakeBody import Snake
from time import sleep
from food import Food
from scoredboard import Scoreboard

S = Screen()
S.setup(height=600, width=600)
S.bgcolor("black")
S.title("Snake Game")
S.tracer(0)
S.listen()

snake = Snake()
food = Food()
score = Scoreboard()

S.update()

S.onkey(key="Right", fun=snake.move_right)
S.onkey(key="Left", fun=snake.move_left)
S.onkey(key="Up", fun=snake.move_up)
S.onkey(key="Down", fun=snake.move_down)

flag = True

while flag:
    S.update()
    sleep(0.1)
    snake.move()
    score.display()
    snake_head = snake.turtle_l[0]
    if snake_head.distance(food) < 15:
        food.refresh()
        snake.expand_snake()
        score.score_inc()

    if snake.collision():
        score.game_over()
        flag = False

S.exitonclick()
