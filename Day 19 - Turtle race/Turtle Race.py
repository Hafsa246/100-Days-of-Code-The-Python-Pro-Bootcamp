from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False


for turtle_index in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.goto(x = -250, y = y_pos[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)


if user_bet:
  race_is_on = True

while race_is_on:
  
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      race_is_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} is the winning turtle. ")
      else:
        print(f"You've lost! The {winning_color} is the winning turtle. ")
    
    rand_dist = random.randint(0,10)
    turtle.forward(rand_dist)

screen.exitonclick()