import turtle
import colorsys

turtle.speed(0)
turtle.hideturtle()

for i in range(4):
    h = i / 4.0
    turtle.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
    turtle.forward(100)
    turtle.left(90)

turtle.done()
