import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()

# for _ in range(15):
#     timmy.forward(10)
#     timmy.color("white")
#     timmy.forward(10)
#     timmy.color("black")

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "bisque"]
# d = 3
#
# for d in range(3, 11):
#     n = 360 / d
#     timmy.color(random.choice(colors))
#     for _ in range(d):
#         # timmy.pencolor(colors[d-4])
#         timmy.forward(100)
#         timmy.right(n)

screen = Screen()
screen.setup(width=800, height=800)
direction = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
screen.exitonclick()
# my_tuple = (1, 3, 8) # Tuples are immutable, cannot be changed (like a stone carving)
