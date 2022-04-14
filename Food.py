from turtle import Turtle
import random

class Food(Turtle):

    median_width = 300
    median_heigh = 300

    def __init__(self, max_width, max_height):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")

        self.median_width = (max_width / 2 - 20)
        self.median_height = (max_height / 2 - 20)

        self.refresh()

    def refresh(self):
        self.goto(random.randrange(- self.median_width, self.median_width, 30),
                  random.randrange(-self.median_height, self.median_height, 30))