from turtle import Turtle

class ScoreBoard(Turtle):

    score = 0
    screen_height = 280

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(self.screen_height)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()