import time
import turtle
import random
from turtle import Screen, Turtle
from Car import Car
from Player import Player
from ScoreBoard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Game")

player = Player()
scoreboard = ScoreBoard()
random_cars = []
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


def random_car():
    chance = random.randint(1, 6)
    if chance == 1:
        new_car = Car()
        new_car.spawn_random()
        random_cars.append(new_car)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_car()
    for car in random_cars:
        if player.check_collision(car):
            game_is_on = False
            scoreboard.game_over()
        car.update_color()
        car.move()
    if player.edges():
        scoreboard.update_score()
        player.reset()
        for car in random_cars:
            car.increase_speed()

screen.exitonclick()