import random
import time
from turtle import Screen, Turtle

screen = Screen()
screen.title("Turtle Race")
screen.colormode(255)
screen.setup(width=600, height=600)
STARTING_X = - 200
turtles = []
moves = [1,2,3,4,5]
MAX_TURTLES = 20


def ask_for_nr():
  # numinput(title, prompt, default, minval, maxval)
  nr = screen.numinput(
      title="Turtle Setup",
      prompt="How many turtles do you want? (1-20):",
      default=5,
      minval=1,
      maxval= MAX_TURTLES,
  )

  # Check if user clicked 'Cancel' or closed the dialog
  if nr is None:
    return turtles

  nr = int(nr)

  for i in range(nr):
    t = Turtle(shape="turtle")
    t.turtleId = i + 1
    t.speed("fastest")
    t.penup()
    turtles.append(t)
  return turtles

def get_user_bet(max_turtles):
    bet = screen.numinput(
        title="Place Your Bet",
        prompt=f"Which turtle will win? Enter a number (1 to {max_turtles}):",
        minval=1,
        maxval=max_turtles,
    )
    if bet is None:
        return None
    return int(bet)

def set_pos():
    global TOP_Y
    TOP_Y = 250
    for turtle in turtles:
        colors = (random.randint(10, 255), random.randint(20, 255), random.randint(30, 255))
        turtle.penup()
        turtle.goto(STARTING_X, TOP_Y)
        TOP_Y = TOP_Y - 50
        turtle.color(colors)

def move_turtles(user_bet):
  is_race_on = True
  while is_race_on:
    for turtle in turtles:
      turtle.forward(random.choice(moves))
      if turtle.xcor() > 280:  # Note: in a 600-wide window, edge is +300
        is_race_on = False
        print(f"The winner is {turtle.turtleId}!")
        if user_bet == turtle.turtleId:
            print("You won the race!")
        else:
            print("You lost the race!")
        break


ask_for_nr()
set_pos()
move_turtles(get_user_bet(MAX_TURTLES))
screen.exitonclick()