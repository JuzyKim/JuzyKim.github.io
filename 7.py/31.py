import turtle
def draw_rectangle(color, width, height, x, y):
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def drawrectangle(width, height, x, y):
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def draw_smartphone():
    turtle.speed(2)
    draw_rectangle("black", 200, 400, -100, -200)
    draw_rectangle("white", 180, 380, -90, -190)
    drawrectangle("black", 160, 360, -90 )
    
    draw_circle("black", 20, 0, -170)
    turtle.hideturtle()
    turtle.done()
draw_smartphone()
