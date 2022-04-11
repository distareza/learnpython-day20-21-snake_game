"""
    Introduction OOP through Snake Game with Turtle Graphic

    Challenge Create (Nokia) Snake Game
    screen refresh rate :
    https://docs.python.org/3/library/turtle.html#turtle.tracer
    https://docs.python.org/3/library/turtle.html#turtle.update

"""
import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
from GameOver import print_game_over

screen_width: int = 600
screen_height = 600

# 1. setup screen
screen = Screen()
screen.setup(screen_width + 20, screen_height + 20)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# Wall
box = Turtle()
box.color("red")
box.hideturtle()
box.penup()
box.goto(-screen_width / 2 + 2, screen_height / 2 - 2)
box.pendown()
box.goto(screen_width / 2 - 2, screen_height / 2 - 2)
box.goto(screen_width / 2 - 2, -screen_height / 2 + 2)
box.goto(-screen_width / 2 + 2, -screen_height / 2 + 2)
box.goto(-screen_width / 2 + 2, screen_height / 2 - 2)
box.penup()

screen.tracer(0)

# 2. create snake
snake = Snake()
screen.update()

# 4. detecting user key input
screen.listen()
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)

# 5. Create a food
food = Food(screen_width, screen_height)

# 7. Create Score Board
score_board = ScoreBoard()

while True:

    # 3. move snake
    if snake.pos_x() > (screen_width / 2 - 20) or \
            snake.pos_x() < -(screen_width / 2 - 20) or \
            snake.pos_y() > (screen_height / 2 - 20) or \
            snake.pos_y() < - (screen_height / 2 - 20):
        print("Hit the wall")
        break

    # 8. Detect collision with tail
    if snake.check_collision_with_tail():
        print("Hit the body")
        break

    # 6. Check if coalition with food
    if snake.distance(food) < 15:
        score_board.increase_score()
        snake.extend_snake()
        food.refresh()

    snake.move()

    time.sleep(0.1)
    screen.update()

print_game_over()

screen.exitonclick()
