from turtle import Turtle
score = 0
class Scoreboard(Turtle):
    def __init__(self, score=0):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.score = score
        self.write("score: 0", align="center", font=("Arial", 14, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        board = f"Score: {self.score}"
        self.write(board, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 14, "normal"))

