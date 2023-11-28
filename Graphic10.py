import turtle
import colorsys

turtle.speed(0)
turtle.hideturtle()

for i in range(360):
    h = i / 360.0
    turtle.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
    turtle.forward(1)
    turtle.left(1)

turtle.done()
