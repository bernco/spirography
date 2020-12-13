from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.speed(0)
my_color_mode = colormode(255)


def color_maker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spiral(gap_size):
    for _ in range(int(360/gap_size)):
        my_turtle.circle(100)
        my_turtle.left(gap_size)
        my_turtle.pencolor(color_maker())


draw_spiral(3)
my_turtle.hideturtle()

my_screen = Screen()
my_screen.exitonclick()

