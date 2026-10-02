from turtle import Turtle, TNavigator
import random
import colorsys
class Ball(Turtle):
    shapes = ["circle", "square", "triangle"]
    def __init__(self):
        super().__init__()
        self.shape(self.r_shapes())
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.random_dir = [-1,-1.1,-1.2]
        self.hue = 0
        self.reset()


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.wall_bounce()
    def r_shapes(self):
        new_shape = random.choice(self.shapes)
        self.shape(new_shape)
    def bounce_y(self):
        self.y_move *= random.choice(self.random_dir)
    def bounce_x(self):
        self.x_move *= random.choice(self.random_dir)

    def wall_bounce(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.bounce_y()

    def reset(self):
        self.goto(0,0)

    # Inside Ball class:
    def check_miss(self):
        if self.xcor() > 380:
            return "right"
        elif self.xcor() < -380:
            return "left"
        return None

    def pattele_collision(self, pattel, pattel2):
        hit_right = ( self.distance(pattel) < 50 and self.xcor() > 320 and self.x_move > 0)
        hit_left = (self.distance(pattel2) < 50 and self.xcor() < -320 and self.x_move < 0)
        return hit_right or hit_left

    def update_color(self):
        self.hue = random.randint(0,360)
        hue_ratio = self.hue / 360.0
        r, g, b = colorsys.hsv_to_rgb(hue_ratio, 1.0, 1.0)
        self.color(int(r * 255), int(g * 255), int(b * 255))
