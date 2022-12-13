from turtle import Turtle
from random import randint


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1.21, 2.3)
        self.goto(300, 0)
        self.speed = -10
        self.reset_pos = 0

    def move(self):
        self.goto(self.xcor() + (self.speed + randint(-1, 1)), self.ycor())

    def reset_car(self):
        self.goto(300, self.reset_pos)
