import turtle
import colorsys

turtle.speed(0)
turtle.hideturtle()

for i in range(100):
    h = i / 100.0
    turtle.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
    turtle.circle(100)
    turtle.left(5)

turtle.done()
