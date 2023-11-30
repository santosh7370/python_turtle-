import turtle
import colorsys

turtle.speed(0)
turtle.hideturtle()

for i in range(36):
    h = i / 36.0
    turtle.color(colorsys.hsv_to_rgb(h, 1.0, 1.0))
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.right(10)

turtle.done()
