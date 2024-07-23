"""
Chapter 3 challenge.
The world is your Turtle! 
"""
import turtle
import random

screen = turtle.Screen()
screen.title("Challenge 1")
screen.bgcolor("cyan")
screen.setup(width=600, height=600)

# Chenquered flag
pen = turtle.Turtle(visible=False)
pen.speed(10)
pen.color("black")
pen.penup()
pen.shape("square")
pen.goto(200, 200)
pen.pendown()
pen.setheading(270)

for i in range(20):
    pen.forward(20)
    pen.stamp()
    if 1 % 2 == 0:
        pen.color("white")
    else:
        pen.color("black")

# First contestant
momo = turtle.Turtle()
momo.shape("turtle")
momo.color("red")
momo.penup()
momo.goto(-200, -100)

for i in range(10):
    momo.right(36)

# Second contestant
mochi = turtle.Turtle()
mochi.shape("turtle")
mochi.color("blue")
mochi.penup()
mochi.goto(-200, 100)

for i in range(10):
    mochi.right(36)


# The race!
while momo.xcor() < 200 and mochi.xcor() < 200:
    momo.forward(random.randint(1, 10))
    mochi.forward(random.randint(1, 10))
