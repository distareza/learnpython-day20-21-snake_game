"""
    Challenge Create (Nokia) Snake Game
    screen refresh rate :
    https://docs.python.org/3/library/turtle.html#turtle.tracer
    https://docs.python.org/3/library/turtle.html#turtle.update

"""
import time
from turtle import Screen
from Snake import Snake

screen_width = 600
screen_height = 600

# 1. setup screen
screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# 2. create snake
snake = Snake()
screen.update()

screen.listen()
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)

while True:

    # 3. move snake
    print(str(snake.pos_x()) + "," + str(snake.pos_y()))
    if snake.pos_x() > 280 or snake.pos_x() < -280 or snake.pos_y() > 280 or snake.pos_y() < -280:
        print("Hit the wall")
        break

    snake.move()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
