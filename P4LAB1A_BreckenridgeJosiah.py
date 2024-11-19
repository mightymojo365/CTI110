# Josiah Breckenridge
# Date: MM/DD/YYYY
# P4LAB1A - Drawing a square and a triangle using turtle graphics

import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(2)

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Reposition turtle for triangle
t.penup()
t.goto(-50, -50)  # Adjust the position to avoid overlapping too much
t.pendown()

# Draw a triangle
for _ in range(3):
    t.forward(100)  # Move forward by 100 units
    t.left(120)     # Turn left by 120 degrees

# Finish
turtle.done()
