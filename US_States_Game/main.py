from turtle import Turtle, Screen
from scoreboard import Scoreboard
import check

S = Screen()
S.title("USA States Game")
S.addshape("blank_states_img.gif")
S.tracer(0)

T = Turtle()
T.shape("blank_states_img.gif")

flag = True

score = Scoreboard()

while flag:
    S.update()
    score.display_score()
    name = S.textinput("USA State Game", "Please mention the state name / enter 'quit' to exit").title()
    if name == "Quit":
        check.states_missed()
        flag = False
        break
    checking = check.check_state(name)
    if checking:
        score.score_inc()

