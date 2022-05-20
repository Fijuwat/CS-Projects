# File: PuertoRicoFlag.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course Name: CS303E
# 
# Date: 2022/04/29
# Description of Program: This program is design for drawing out the flag of Puerto Rico.
import turtle

myBlue   = '#00205B'
myRed    = '#EF3340'
myWhite  = '#FFFFFF'

def drawRectangle (ttl, x, y, width, height, color):
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.fillcolor(color)
    ttl.begin_fill()
    for count in range (2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.end_fill()
    
def fillRectangle( ttl, x, y, width, height, color ):
    if y < 0:
        return
    elif (y//80)%2 == 0:
        ttl.fillcolor(color)
        ttl.begin_fill()
        drawRectangle (ttl, x, y, width, height, color)
        fillRectangle(ttl, x, y-80, width, height, myWhite )
    else:
        ttl.fillcolor(color)
        ttl.begin_fill()
        drawRectangle (ttl, x, y, width, height, color)
        fillRectangle(ttl, x, y-80, width, height, myRed )

def triangle (ttl, x, y, toX, toY, color):
    ttl.goto(x, y)
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.goto(toX, toY)
    ttl.goto(0, 320)
    ttl.goto(x,y)
    ttl.end_fill()

def star (ttl, x, y, length, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.right(72)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.setheading(0)
    ttl.right(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.right(144)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.setheading(0)
    ttl.forward(length)
    ttl.left(72)
    ttl.forward(length)
    ttl.end_fill()
        
n = turtle.Turtle()       

fillRectangle( n, 0, 320, 600, 80, myRed )
triangle(n, 0, -80, 300, 120, myBlue)
star (n, 100, 187, 50, myWhite)


