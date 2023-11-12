import turtle
from turtle import *

def draw_rectangle():
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-100, -200)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(90)
    turtle.end_fill()

def draw_rectangle1():
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-80, -130)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(160)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()

def draw_circle():
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(0, -160 - 20)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
def drawcircle():
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(30, 180 )
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
def drawline ():
    turtle.shape('turtle')
    turtle.penup()
    turtle.pensize(10)
    turtle.left(180)
    turtle.forward(30)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.end_fill()
    turtle.forward(30)
def draw_smartphone():
    turtle.speed(5)
    draw_rectangle()
    draw_rectangle1()
    draw_circle()
    drawcircle()
    drawline ()
    turtle.hideturtle()
    turtle.done()

draw_smartphone()