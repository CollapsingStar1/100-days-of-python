from turtle import Turtle
import random
import colorsys
class Car(Turtle):
    car_speeds = [1,2,3,4,5, 6, 7, 8, 9, 10]

    lenght = [1.5,2,2.5,3,3.5]
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hue = 0
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=random.choice(self.lenght))
        self.update_color()
        self.goto(0,0)
        self.speed_value = random.choice(self.car_speeds)

    def update_color(self):
        self.hue = random.randint(0, 360)
        hue_ratio = self.hue / 360.0
        r, g, b = colorsys.hsv_to_rgb(hue_ratio, 1.0, 1.0)
        self.color(r, g, b)
    def spawn_random(self):
        self.setx(300)
        self.sety(random.choice(range(-280,280,30)))
    def move(self):
        self.setx(self.xcor() - self.speed_value)

    def increase_speed(self):
        self.speed_value *= 1.5


