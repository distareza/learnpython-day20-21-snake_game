from turtle import Turtle


class ScoreBoard(Turtle):
    score = 0
    screen_height = 280
    file_score_name = "snake_score.txt"

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.read_high_score()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(self.screen_height)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align="center",
                   font=("Arial", 18, "normal"))
        self.save_high_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        try:
            with open(self.file_score_name) as file_score:
                self.high_score = int(file_score.read())
            if self.high_score is None:
                self.high_score = 0
        except:
            self.high_score = 0

    def save_high_score(self):
        with open(self.file_score_name, mode="w") as file_score:
            file_score.write(str(self.high_score))
