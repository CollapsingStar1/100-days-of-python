from turtle import Turtle, Screen
import random
t = Turtle()
t.speed("fastest")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]


def draw_shape(sides):
    angle = round(367/sides)
    for i in range(sides):
        t.forward(100)
        t.right(angle)


for i in range(3,16):
    t.color(random.choice(colors))
    draw_shape(i)


screen = Screen()
screen.exitonclick()