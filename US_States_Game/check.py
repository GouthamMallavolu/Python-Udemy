import pandas as pd
from states import States

data = pd.read_csv("50_states.csv")
s = data["state"].tolist()

state = States()
guessed = []
missed_states = []


def check_state(name):
    if name in s and name not in guessed:
        guessed.append(name)
        s1 = data[data["state"] == name]
        x, y = int(s1["x"]), int(s1["y"])
        state.setpos(x, y, name)
        return True
    else:
        return False


def states_missed():
    for _ in s:
        if _ not in guessed:
            missed_states.append(_)
    missed = pd.DataFrame(missed_states).to_csv("states_missed.csv")
