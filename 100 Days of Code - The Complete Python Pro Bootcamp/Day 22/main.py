from turtle import Turtle, Screen
from Pattel import Pattel
from Ball import Ball
from ScoreBoard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.colormode(255)
screen.setup(width=800, height=600)
screen.tracer(0)

pattel = Pattel(350)
pattel2 = Pattel(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(pattel.move_up, "Up")
screen.onkey(pattel.move_down, "Down")
screen.onkey(pattel2.move_up, "w")
screen.onkey(pattel2.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    miss = ball.check_miss()
    if miss == "right":
        scoreboard.update_score("left")
        ball.reset()
        ball.r_shapes()
        ball.update_color()
        ball.bounce_x()
    elif miss == "left":
        scoreboard.update_score("right")
        ball.r_shapes()
        ball.update_color()
        ball.reset()
        ball.bounce_x()

    if ball.pattele_collision(pattel, pattel2):
        ball.bounce_x()

    pattel.update_color()
    pattel2.update_color()
screen.exitonclick()