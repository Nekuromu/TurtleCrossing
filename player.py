from turtle import Turtle

PLAYER_SIZE = 20
SPEED = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -300 + PLAYER_SIZE)

    def move(self):
        self.setpos(0, self.ycor() + SPEED)
