from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-250,260)
        self.score = 0
        self.write("Level: 0", align="center", font=("Arial", 14, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        board = f"Level: {self.score}"
        self.write(board, align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))
