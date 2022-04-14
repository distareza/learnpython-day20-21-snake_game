import time
from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    init = [(0, 0), (-20, 0), (-40, 0)]
    color = "white"
    snake = []
    move_step = 20
    snake_head = {}

    def __init__(self):
        for pos in self.init:
            self.add_segment(pos)
        self.snake_head = self.snake[0]

    def create_snake(self):
        self.snake = []
        for pos in self.init:
            self.add_segment(pos)
        self.snake_head = self.snake[0]

    def add_segment(self, position):
        snake = Turtle(shape="circle")
        snake.color(self.color)
        snake.penup()
        snake.goto(position)
        self.snake += [snake]

    def reset(self):
        time.sleep(1)
        for snake in self.snake:
            snake.goto(99999, 99999)
        self.snake.clear()
        self.create_snake()

    def move(self, direction="forward"):
        # move its head
        last_x = self.snake_head.xcor()
        last_y = self.snake_head.ycor()

        if direction == "left":
            self.snake_head.left(90)
        elif direction == "right":
            self.snake_head.right(90)
        self.snake_head.forward(self.move_step)

        # move its body
        for body in range(1, len(self.snake)):
            x = self.snake[body].xcor()
            y = self.snake[body].ycor()
            self.snake[body].goto(last_x, last_y)
            last_x = x
            last_y = y

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)

    def pos_x(self):
        return self.snake_head.xcor()

    def pos_y(self):
        return self.snake_head.ycor()

    def distance(self, pos):
        return self.snake_head.distance(pos)

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())

    def check_collision_with_tail(self):
        for segment in self.snake[1:]:
            if self.snake_head.distance(segment) < 15:
                return True
        return False

