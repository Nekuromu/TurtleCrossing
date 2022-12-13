from turtle import Turtle


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1.2, 2.3)
        self.goto(300, 0)
        self.speed = -10

    def move(self):
        self.goto(self.xcor() + self.speed, self.ycor())