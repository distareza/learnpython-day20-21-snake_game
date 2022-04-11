from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    starting = [(0, 0), (-20, 0), (-40, 0)]
    color = "white"
    snake = []
    move_step = 20

    def __init__(self):
        for pos in self.starting:
            snake = Turtle(shape="square")
            snake.color(self.color)
            snake.penup()
            snake.goto(pos)
            self.snake += [snake]

    def move(self, direction = "forward"):
        # move its head
        last_x = self.snake[0].xcor()
        last_y = self.snake[0].ycor()

        if direction == "left":
            self.snake[0].left(90)
        elif direction == "right":
            self.snake[0].right(90)
        self.snake[0].forward(self.move_step)

        # move its body
        for body in range(1, len(self.snake)):
            x = self.snake[body].xcor()
            y = self.snake[body].ycor()
            self.snake[body].goto(last_x, last_y)
            last_x = x
            last_y = y

    def move_up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(90)

    def move_down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(270)

    def move_right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(0)

    def move_left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(180)

    def pos_x(self):
        return self.snake[0].xcor()

    def pos_y(self):
        return self.snake[0].ycor()