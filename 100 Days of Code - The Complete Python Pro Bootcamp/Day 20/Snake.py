import colorsys
import random
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.step_count = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(10):
            new_segment = Turtle("turtle")
            new_segment.penup()
            new_segment.goto(-20 * i, 0)
            self.segments.append(new_segment)
        self.update_colors()

    def update_colors(self):
        for idx, seg in enumerate(self.segments):
            hue = ((idx * 8) + (self.step_count * 10)) % 360 / 360.0
            r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
            seg.color(int(r * 255), int(g * 255), int(b * 255))

    def move(self):
        self.step_count += 1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].setheading(self.segments[seg_num - 1].heading())

        self.head.forward(MOVE_DISTANCE)


        x, y = self.head.xcor(), self.head.ycor()
        if x > 300:
            self.head.setx(-300)
        elif x < -300:
            self.head.setx(300)

        if y > 300:
            self.head.sety(-300)
        elif y < -300:
            self.head.sety(300)

        self.update_colors()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)