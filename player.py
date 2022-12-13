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
        self.allowed_to_move = False
        self.reset_player()

    def move(self):
        if not self.allowed_to_move:
            return
        self.setpos(0, self.ycor() + SPEED)

    def reset_player(self):
        self.goto(0, -300 + PLAYER_SIZE)
        self.allowed_to_move = False

