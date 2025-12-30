from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(800, 600)
screen.listen()
is_race_on = False
all_turtles = []
user_bet = screen.textinput("Welcome to Turtle Race!", "Who is going to win the race? Enter the color: ")
colors = ["red", "blue", "green", "yellow", "purple", "cyan"]
y = 250
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-350, y)
    y -= 100
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! {winning_color} is the winner!")
            else:
                print(f"You lost! {winning_color} won the race!")
        turtle.speed("fastest")
        random_distance = random.randint(0, 15)
        turtle.forward(random_distance)


screen.exitonclick()