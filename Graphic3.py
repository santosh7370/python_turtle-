import turtle
import colorsys

turtle.speed(2)
turtle.hideturtle()

for i in range(360):
    h = i / 360.0
    turtle.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
    turtle.forward(2)
    turtle.left(1)

turtle.done()
