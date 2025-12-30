from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times new roman", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.number}", align=ALIGNMENT, font=FONT)
        self.number += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)