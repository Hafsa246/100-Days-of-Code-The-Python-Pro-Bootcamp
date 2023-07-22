import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
tim = Turtle()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


def spiral(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading()+size_of_gap)

        
spiral(5)


screen = Screen()
screen.exitonclick()
