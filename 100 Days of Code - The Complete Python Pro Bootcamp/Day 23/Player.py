from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(0,-280)

    def move_right(self):
        self.setheading(0)  # 0° is East (Right)
        self.forward(20)

    def move_left(self):
        self.setheading(180)  # 180° is West (Left)
        self.forward(20)

    def move_up(self):
        self.setheading(90)  # 90° is North (Up)
        self.forward(20)

    def move_down(self):
        self.setheading(270)  # 270° is South (Down)
        self.forward(20)
    def edges(self):
        return self.ycor() == 280
    def reset(self):
        self.goto(0,-280)

    def check_collision(self, car):
        x_distance = abs(self.xcor() - car.xcor())
        y_distance = abs(self.ycor() - car.ycor())
        if y_distance < 25 and x_distance < (car.shapesize()[1] * 10 + 10):
            return True
        return False