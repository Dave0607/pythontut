import turtle
from turtle import Turtle


FONT_SIZE = 20
FONT = ('Courier', FONT_SIZE, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0


    def print_score(self):
        self.reset()
        self.clear()
        self.penup()
        self.goto(0, 600 / 2 - 40)
        self.color("white")
        self.hideturtle()
        self.write(f"score:{self.score} High Score:{self.high_score}", font=FONT, align="center")

    def game_over(self):
        self.reset()
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0,0)
        if self.score > self.high_score:
            self.write(f"GAME OVER\nyour score:{self.score} is new High score", font=FONT, align="center")
        else:
            self.write(f"GAME OVER\nyour score:{self.score}\nHigh score:{self.high_score}", font=FONT, align="center")
        self.resett()

    def resett(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0