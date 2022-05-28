import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)


walk = [0, 90, 180, 270]
timmy.speed("fastest")


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


def random_walk():
    timmy.color(random_color())
    timmy.pensize(10)
    timmy.forward(30)
    timmy.setheading(random.choice(walk))


for _ in range(200):
    random_walk()

my_screen = Screen()
my_screen.exitonclick()
