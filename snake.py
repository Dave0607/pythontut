import turtle
from turtle import Screen, Turtle

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake():
    def __init__(self,speed=1):
        self.seg_snake = []
        self.speed = speed
        self.segment = Turtle(shape="square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.speed(speed)
        self.seg_snake.append(self.segment)
        self.add_segment(2)
        self.direct = EAST

    def add_segment(self,how_many):
        for _ in range(0, how_many):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.speed(self.speed)
            how_many_seg = len(self.seg_snake)
            x_pos = self.seg_snake[how_many_seg - 1].xcor()
            y_pos = self.seg_snake[how_many_seg - 1].ycor()
            segment.goto(x=x_pos - 20, y=y_pos)
            self.seg_snake.append(segment)

    def move(self,direct):
        self.direct = direct
        for seg in range(0, len(self.seg_snake)):
            if seg == 0:
                if self.seg_snake[seg].heading() == NORTH and direct == SOUTH:
                    direct = NORTH
                elif self.seg_snake[seg].heading() == SOUTH and direct == NORTH:
                    direct = SOUTH
                elif self.seg_snake[seg].heading() == EAST and direct == WEST:
                    direct = EAST
                elif self.seg_snake[seg].heading() == WEST and direct == EAST:
                    direct = WEST

                x_old_pos = self.seg_snake[seg].xcor()
                y_old_pos = self.seg_snake[seg].ycor()

                if direct == NORTH:
                    self.seg_snake[seg].goto(self.seg_snake[seg].xcor(), round(self.seg_snake[seg].ycor() + 20))
                    self.seg_snake[0].seth(NORTH)

                elif direct == SOUTH:
                    self.seg_snake[seg].goto(self.seg_snake[seg].xcor(), round(self.seg_snake[seg].ycor() - 20))
                    self.seg_snake[0].seth(SOUTH)

                elif direct == WEST:
                    self.seg_snake[seg].goto(round(self.seg_snake[seg].xcor() - 20), self.seg_snake[seg].ycor())
                    self.seg_snake[0].seth(WEST)

                elif direct == EAST:
                    self.seg_snake[seg].goto(round(self.seg_snake[seg].xcor() + 20), self.seg_snake[seg].ycor())
                    self.seg_snake[0].seth(EAST)

            else:
                x_pos = self.seg_snake[seg].xcor()
                y_pos = self.seg_snake[seg].ycor()
                self.seg_snake[seg].goto(x_old_pos, y_old_pos)
                x_old_pos = x_pos
                y_old_pos = y_pos

    def position(self):
        position_of_snake = []
        for x in range(len(self.seg_snake)):
            position_of_snake.append(self.seg_snake[x].position())
        return position_of_snake

    def tail_collision(self):
        tail = self.position()
        if tail[0] in tail[1:]:
            return True
        else:
            return False

    def clear(self):
        self.seg_snake.clear()
        self.segment.color("white")
        self.segment.penup()
        self.seg_snake.append(self.segment)
        self.add_segment(2)
        self.direct = EAST

    def up(self):
        self.direct = NORTH

    def down(self):
        self.direct = SOUTH

    def left(self):
        self.direct = WEST

    def right(self):
        self.direct = EAST
