import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#const
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
SPEED = 1
WIDTH = 600 #x
HEIGHT = 600 #y
FONT_SIZE = 20
FONT = ('Courier', FONT_SIZE, 'bold')

#setup
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
game_over = False
food_taken = False
sc = Scoreboard()
snake = Snake(SPEED)
food = Food(WIDTH,HEIGHT)

def is_wall(position):
    x_pos = position.xcor()
    y_pos = position.ycor()
    frame = 20
    if x_pos > (WIDTH/2)-frame or x_pos < -1*(WIDTH/2)+frame or y_pos > (HEIGHT/2)-frame or y_pos < -1*(HEIGHT/2)+frame:
        return True
    else:
        return False

def print_gameover():
    screen.reset()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    sc.game_over()

direction = WEST
sc.print_score()

while not game_over:
    turtle.onkey(fun=snake.up, key="Up")
    turtle.onkey(fun=snake.down, key="Down")
    turtle.onkey(fun=snake.left, key="Left")
    turtle.onkey(fun=snake.right, key="Right")
    snake.move(snake.direct)

    screen.listen()
    screen.update()

    if is_wall(snake.seg_snake[0]) or snake.tail_collision():
        print_gameover()
        time.sleep(3)
        sc.reset()
        snake.clear()
        sc.print_score()
        food_taken = False

    if not food_taken:
        food_taken, dot_position = food.create(snake)
        sc.print_score()

    if tuple(map(int,snake.seg_snake[0].position())) == tuple(map(int,dot_position)):
        snake.add_segment(1)
        sc.score += 10
        sc.print_score()
        food_taken = False

    time.sleep(0.1)

screen.exitonclick()