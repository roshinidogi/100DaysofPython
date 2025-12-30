import turtle as t
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800, height=800)
tim = Turtle()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

def draw_spirograph(left_angle):
    n = int(360/left_angle)
    for _ in range(n):
        tim.color(random_color())
        tim.circle(100)
        tim.left(left_angle)

draw_spirograph(5)


screen.exitonclick()