from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=800)
tim = Turtle()

def move_forward():
    return tim.forward(100)
def turn_left():
    return tim.left(10)
def turn_right():
    return tim.right(-10)
def move_backward():
    return tim.backward(100)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# keys = ["W", "S", "A", "D", "C"]
screen.listen()
screen.onkey(move_forward, "W".lower())
screen.onkey(turn_left, "D".lower())
screen.onkey(turn_right, "A".lower())
screen.onkey(move_backward, "S".lower())
screen.onkey(clear_screen, "C".lower())

screen.exitonclick()