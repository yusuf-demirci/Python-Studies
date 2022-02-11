import turtle
from turtle import Screen, Turtle
import random
# import colorgram
#
# rgb_list = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     rgb_list.append(new_tuple)
#
# print(rgb_list)

color_list = [(236, 34, 107), (145, 28, 65), (239, 74, 34), (6, 149, 94), (230, 169, 39), (185, 158, 46), (45, 191, 233), (28, 127, 195), (253, 223, 0), (126, 193, 72), (86, 28, 93), (247, 218, 44), (173, 35, 100), (34, 171, 117), (218, 129, 162), (18, 190, 232), (236, 164, 188), (237, 171, 158), (142, 210, 229), (153, 25, 24), (162, 209, 180), (168, 59, 53), (112, 115, 166), (0, 125, 55)]

tim = Turtle()
turtle.colormode(255)

def random_color():
    return random.choice(color_list)
tim.penup()
tim.hideturtle()
tim.speed(0)
a = -250

for j in range(10):
    tim.setposition((-250, a))
    for i in range(10):
        tim.dot(20, random_color())
        tim.forward(50)
    a += 50









screen = Screen()
screen.exitonclick()

