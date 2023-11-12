import turtle
def circle(color, radius, x1, y2):
    turtle.shape('turtle')
    turtle.bgcolor("white")
    turtle.penup()
    turtle.goto(x1, y2 - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def trafficlight():
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-20, -60)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)
    turtle.end_fill()

    circle("red", 20, 0, 50)

    circle("yellow", 20, 0, 10)

    circle("green", 20, 0, -30)

    turtle.hideturtle()
    turtle.done()

trafficlight()
