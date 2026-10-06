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
        self.high_score = self.return_high_score()

    def update_score(self):
        self.score += 1
        self.clear()
        board = f"Score: {self.score} High Score: {self.high_score}"
        self.write(board, align="center", font=("Arial", 14, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.write_board()

    def write_board(self):
        self.clear()
        board = f"Score: {self.score} High Score: {self.high_score}"
        self.write(board, align="center", font=("Arial", 14, "normal"))

    def return_high_score(self):
        try:
            with open("data.txt") as f:
                content = f.read().strip()
                return int(content) if content else 0
        except FileNotFoundError:
            with open("data.txt", "w") as f:
                f.write("0")
                return 0
