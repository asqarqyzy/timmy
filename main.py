# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.color("firebrick")
# timmy.shape('turtle')
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()
# print(timmy)

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("pockemon_name", ["pikachu", "sou"])
table.add_column("pockemon_type", ["electric", "water"])

table.align = 'l'
print(table)


