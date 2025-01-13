import turtle
from turtle import Turtle
from turtle import *

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score:{self.score} highscore: {self.highscore}", False, align="center",font=("arial", 22, "normal"))
        self.hideturtle()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font=("arial", 22, "normal"))
    def increment(self):
        self.score+=1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score:{self.score} high score {self.highscore}", False, align="center", font=("arial", 22, "normal"))