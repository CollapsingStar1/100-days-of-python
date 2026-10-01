import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(self.shapes())
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.colorss())
        self.speed("fastest")
        self.refresh()

    def shapes(self):
        shapess = ["circle", "square"]
        return random.choice(shapess)
    def colorss(self):
        return (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.shape(self.shapes())

