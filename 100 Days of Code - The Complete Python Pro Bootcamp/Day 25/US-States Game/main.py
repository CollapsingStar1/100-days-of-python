import pandas as pd
from turtle import Screen, Turtle
from Write_states import Write_states

image = "blank_states_img.gif"
screen = Screen()
screen.setup(width=700, height=600)
screen.bgpic(image)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

write_states = Write_states()


def ask_for_state():
  user_input = screen.textinput(title="Guess the state", prompt="Enter a state")
  return user_input


guessed_states = []

while len(guessed_states) < 50:
  raw_input = ask_for_state()

  if raw_input is None:
    break

  user_state = raw_input.title()

  if user_state in states and user_state not in guessed_states:
    guessed_states.append(user_state)

    state_row = data[data["state"] == user_state]

    x = state_row["x"].item()
    y = state_row["y"].item()

    write_states.goto(x, y)
    write_states.write(user_state, align="center", font=("Arial", 8, "normal"))

screen.mainloop()