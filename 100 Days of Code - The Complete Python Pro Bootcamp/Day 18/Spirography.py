from turtle import Turtle, Screen
import random

t = Turtle()
t.speed("fastest")
t.pensize(2)

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")  # High contrast makes bright colors pop

def random_bright_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_polygon(sides, side_length):
    turn_angle = 360 / sides
    for _ in range(sides):
        t.forward(side_length)
        t.right(turn_angle)

# ---------------- Layer 1: Core Circle Rosette ----------------
# 18 circles * 20 degrees = exact 360-degree radial ring
for _ in range(18):
    t.pencolor(random_bright_color())
    t.circle(70)
    t.right(20)

# ---------------- Layer 2: Triangles, Squares, Pentagons, Hexagons ----------------
# Each shape family gets drawn with adjusted side lengths so they stay balanced.
shapes = [
    (3, 110, 12),  # (3 sides, length 110, repeat 12 times -> 360/12 = turn 30 deg)
    (4, 85,  12),  # (4 sides, length 85,  repeat 12 times -> 360/12 = turn 30 deg)
    (5, 65,  12),  # (5 sides, length 65,  repeat 12 times -> 360/12 = turn 30 deg)
    (6, 50,  12),  # (6 sides, length 50,  repeat 12 times -> 360/12 = turn 30 deg)
    (7, 35,   12),
    (8, 25,    12),
]

for sides, side_length, count in shapes:
    t.pencolor(random_bright_color())
    step_turn = 360 / count
    for _ in range(count):
        draw_polygon(sides, side_length)
        t.right(step_turn)

t.hideturtle()
screen.exitonclick()