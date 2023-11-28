import turtle
import colorsys

turtle.speed(0)
turtle.hideturtle()

for i in range(6):
    h = i / 6.0
    turtle.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
    turtle.circle(50 + i * 20)

turtle.done()
