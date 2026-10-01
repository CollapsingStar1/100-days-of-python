import time
from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)

snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


food = Food()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on and not snake.wall() and not snake.collision_with_body():
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.eat(food):
        food.refresh()
        snake.extend()
        scoreboard.update_score()
scoreboard.game_over()






screen.exitonclick()