from turtle import Screen, Turtle
from turtle import Turtle
class Write_states(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")



    def write_state(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name, align="center", font=("Arial", 12, "normal"))