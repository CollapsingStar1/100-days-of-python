from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.l_score = 0
        self.r_score = 0
        self.goto(0,250)
        self.write("0 : 0", align="center", font=("Arial", 24, "normal"))

    def update_score(self, player):
        if player == "left":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        score = f"{self.l_score} : {self.r_score}"
        self.write(score, align="center", font=("Arial", 24, "normal"))
