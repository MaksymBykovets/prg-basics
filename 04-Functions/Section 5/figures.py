###
# Draw a square
#
import turtle

def draw_square(side_length):
    pen = turtle.Turtle()
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)


def draw_trangle(side_lenght):
    pen = turtle.Turtle()
    for i in range(3):
        pen.forward(side_lenght)
        pen.left(120)

def draw_rectangle(lenght_a, lenght_b):
    pen = turtle.Turtle()
    for i in range (2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

    