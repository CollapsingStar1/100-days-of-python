from turtle import Turtle
import colorsys
class Pattel(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor,0)
        self.current_hue = 0
        self.update_color()

    def move_up(self):
        ycor = self.ycor() + 50
        self.sety(ycor)


    def move_down(self):
       ycor = self.ycor() - 50
       self.sety(ycor)


    def update_color(self):
        self.current_hue = (self.current_hue + 3) % 360
        hue_ratio = self.current_hue / 360.0
        r, g, b = colorsys.hsv_to_rgb(hue_ratio, 1.0, 1.0)
        self.color((int(r * 255), int(g * 255), int(b * 255)))
