import random
from turtle import Screen, Turtle

t = Turtle()
d = Turtle()
g = Turtle()
j = Turtle()
k = Turtle()
l = Turtle()
m = Turtle()
turtles = [t, d, g, j, k, l, m]
for turtle in turtles:
  turtle.shape("classic")
  turtle.speed("fastest")
  turtle.pensize(10)

# RGB color mode for vivid random colors
screen = Screen()
screen.colormode(255)

# The 4 cardinal headings: East, North, West, South
directions = [0, 90, 180, 270]
distance = [10,30,50,80,30,12,43,63,11,3]


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)


# 200 consecutive connected steps
for _ in range(200):
    for turtle in turtles:
        turtle.pencolor(random_color())
        turtle.setheading(random.choice(directions))
        turtle.forward(random.choice(distance))


screen.exitonclick()