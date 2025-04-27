from turtle import Turtle
import random


class Food():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        area = self.food_area()
        self.circle = Turtle()

    def food_area(self):
        self.area = []
        start = int(-1 * (self.width / 2) + 20)
        end = int((self.width / 2) - 20)
        for x in range(start, end, 20):
            for y in range(start, end, 20):
                self.area.append((x, y))
        return self.area

    def create(self,snake):
        self.circle.reset()
        self.circle.hideturtle()
        self.circle.penup()
        self.circle.pencolor("white")
        points = set(self.area) - set(snake.position())
        position = ()
        if points:
            position = random.choice(tuple(points))
        self.circle.setposition(position)
        self.circle.dot(size=20)
        return True, position