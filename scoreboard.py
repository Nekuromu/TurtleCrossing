from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.level = 1
        self.update_board("Ready?")

    def update_board(self, text):
        self.clear()
        self.goto(-300 + 20, -300 + 15)
        self.write(text, align="left", font=("Courier", 14, "normal"))
        self.goto(-300 + 20, 300 - 30)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 14, "normal"))
        self.draw_map()

    def draw_map(self):
        self.goto(-300, -260)
        self.pendown()
        self.goto(300, -260)
        self.penup()
        self.goto(-300, 260)
        self.pendown()
        self.goto(300, 260)
        self.penup()
