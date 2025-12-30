# # OOPS
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red", "coral")
# # timmy.forward(100)
# timmy.circle(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from docutils.parsers.rst.directives.tables import align
from prettytable import PrettyTable
table = PrettyTable() #Now we created a new object table from the PrettyTable

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)