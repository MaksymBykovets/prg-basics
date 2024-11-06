import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100
lenght_a = 100
lenght_b = 50


# Draw a square

figures.draw_square(side_length)

pen.penup()
pen.goto(-300, -150)
pen.pendown()
figures.draw_trangle(side_length)


pen.penup()
pen.goto(-500, 100)
pen.pendown()
figures.draw_rectangle(lenght_a, lenght_b)
# Hide the turtle and finish
pen.hideturtle()
window.mainloop()