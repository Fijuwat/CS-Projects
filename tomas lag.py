# File: PuertoRicoFlag.py
# Student: Tomas Chang
# UT EID: TC34448
# Course Name: CS303E
# 
# Date: 4/28/2022
# Description of Program: 

import turtle
import math
 
b = '#00205B'
r = '#EF3340'
w = '#FFFFFF'


def rec(ttl, x, y, x1, y1):
  ttl.penup()
  ttl.goto(x,y)
  ttl.pendown()
  ttl.goto(x1,y)
  ttl.goto(x1,y1)
  ttl.goto(x,y1)
  ttl.goto(x,y)

  
Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(1)

Bob.fillcolor(r)
Bob.begin_fill()
rec(Bob, 0,0,600,80)
Bob.end_fill()

Bob.fillcolor(w)
Bob.begin_fill()
rec(Bob, 0,80,600,160)
Bob.end_fill()

Bob.fillcolor(r)
Bob.begin_fill()
rec(Bob, 0,160,600,240)
Bob.end_fill()

Bob.fillcolor(w)
Bob.begin_fill()
rec(Bob, 0,240,600,320)
Bob.end_fill()

Bob.fillcolor(r)
Bob.begin_fill()
rec(Bob, 0,320,600,400)
Bob.end_fill()

Bob.fillcolor(b)
Bob.begin_fill()
Bob.penup()
Bob.goto(0,400)
Bob.pendown()
q = 200*math.sqrt(3)
Bob.goto(q,200)
Bob.goto(0,0)
Bob.end_fill()

Bob.fillcolor(b)
Bob.begin_fill()
Bob.penup()
Bob.goto(0,400)
Bob.pendown()
q = 200*math.sqrt(3)
Bob.goto(q,200)
Bob.goto(0,0)
Bob.end_fill()

def star (ttl,x,y,length,color ):
    ttl.penup()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.setheading(0)
    ttl.goto(x,y)
    ttl.pendown()
    ttl.right(72)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.end_fill()
    ttl.hideturtle()
    
star(Bob, 100, 267, 50 ,w)

turtle.done()