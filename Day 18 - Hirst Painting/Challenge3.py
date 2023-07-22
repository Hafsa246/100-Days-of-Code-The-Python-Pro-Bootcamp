from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("DeepPink4")


colours = ["dark gray", "teal", "yellow", "dark magenta", "brown", "medium purple", "light sky blue"]


def draw_shape(numsides):
    angle = 360/numsides
    for _ in range(numsides):
        tim.forward(50)
        tim.right(angle)


for i in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(i)


screen = Screen()
screen.exitonclick()
