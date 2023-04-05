"""
Classes and objects

Constructing objects and accessing their attributes and methods
"""

from turtle import Turtle, Screen

if __name__ == "__main__":
    my_turtle = Turtle()
    print(my_turtle)
    my_turtle.shape("turtle")
    my_turtle.color("coral")
    my_turtle.forward(100)

    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()
