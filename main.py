from turtle import Turtle
from turtle import Screen
import random

color_list = ("red", "blue", "black", "yellow")


tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)


def draw_shape(number_of_sides):
    tim.color(random.choice(color_list))
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    draw_shape(i)






screen = Screen()






screen.exitonclick()


