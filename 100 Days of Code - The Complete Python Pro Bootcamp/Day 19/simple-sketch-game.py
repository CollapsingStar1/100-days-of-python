import random
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.colormode(255)
screen.bgcolor("#eeeeee")
screen.tracer(0)

t = Turtle(shape="turtle")
t.color("#f4a261")
t.pensize(5)
t.speed(0)

# Movement & Physics Variables
speed = 0.0
max_speed = 6.0
acceleration = 0.3
friction = 0.95
turn_rate = 4.5

is_busy = False  # Flag to freeze manual driving while the turtle executes an auto-shape

keys = {"Up": False, "Down": False, "Left": False, "Right": False}

def press(k):
    keys[k] = True

def release(k):
    keys[k] = False

for key in ["Up", "Down", "Left", "Right"]:
    screen.onkeypress(lambda k=key: press(k), key)
    screen.onkeyrelease(lambda k=key: release(k), key)

def random_color():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# ----------------- Auto-Control Shape Routines -----------------
def auto_draw_star():
    global is_busy, speed
    if is_busy:
        return
    is_busy = True
    speed = 0.0  # Stop momentum

    t.color(random_color())
    t.begin_fill()
    for _ in range(5):
        t.forward(40)
        t.right(144)
        screen.update()
        time.sleep(0.05)  # Brief pause so you can watch the turtle steer
    t.end_fill()
    screen.update()

    is_busy = False

def auto_draw_square():
    global is_busy, speed
    if is_busy:
        return
    is_busy = True
    speed = 0.0

    t.color(random_color())
    t.begin_fill()
    for _ in range(4):
        t.forward(35)
        t.right(90)
        screen.update()
        time.sleep(0.05)
    t.end_fill()
    screen.update()

    is_busy = False

def auto_draw_circle():
    global is_busy, speed
    if is_busy:
        return
    is_busy = True
    speed = 0.0

    t.color(random_color())
    t.begin_fill()
    for _ in range(24):
        t.forward(5)
        t.left(15)
        screen.update()
        time.sleep(0.02)
    t.end_fill()
    screen.update()

    is_busy = False

def clear_canvas():
    t.clear()
    screen.update()

screen.onkeypress(auto_draw_star, "q")
screen.onkeypress(auto_draw_square, "w")
screen.onkeypress(auto_draw_circle, "e")
screen.onkeypress(clear_canvas, "x")

screen.listen()

# ----------------- Main Game Loop -----------------
def game_loop():
    global speed
    if not is_busy:
        if keys["Left"]:
            t.left(turn_rate)
        if keys["Right"]:
            t.right(turn_rate)

        if keys["Up"]:
            speed = min(speed + acceleration, max_speed)
        elif keys["Down"]:
            speed = max(speed - acceleration, -max_speed / 2)
        else:
            speed *= friction

        t.forward(speed)

        # Screen wrapping
        x, y = t.xcor(), t.ycor()
        if abs(x) > 400:
            t.penup()
            t.setx(-x)
            t.pendown()
        if abs(y) > 400:
            t.penup()
            t.sety(-y)
            t.pendown()
        screen.update()
    screen.ontimer(game_loop, 16)

game_loop()
screen.exitonclick()