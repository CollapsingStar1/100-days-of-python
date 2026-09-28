import random
import colorgram
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=550, height=550)
screen.colormode(255)

# Extract and filter colors
colors = colorgram.extract("x.jpeg", 30)
palette = []
for c in colors:
    # Ignore pure white / near-black backgrounds
    if sum(c.rgb) > 80 and sum(c.rgb) < 700:
        palette.append((c.rgb.r, c.rgb.g, c.rgb.b))

t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

row = 10
col = 10
SPACING = 35
t.setheading(-225)
for i in range(row):
  for j in range(col):
    t.setpos(j * SPACING, i * SPACING)
    t.dot(20, random.choice(palette))


screen.exitonclick()