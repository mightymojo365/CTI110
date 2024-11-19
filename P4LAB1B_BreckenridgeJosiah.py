# Josiah Breckenridge
# Date: MM/DD/YYYY
# P4LAB1B - Drawing initials using turtle graphics

import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(2)
t.pensize(3)       # Set pen size
t.pencolor("blue") # Set pen color

# Draw the first initial 'J'
t.penup()
t.goto(-50, 50)    # Position for "J"
t.pendown()
t.setheading(270)  # Face downward
t.forward(75)      # Draw vertical line of 'J'
t.circle(-25, 180) # Create the bottom curve of 'J'

# Move to position for the next initial 'B'
t.penup()
t.goto(50, 100)    # Position for "B"
t.pendown()

# Draw the vertical line of 'B'
t.setheading(270)  # Face downward
t.forward(100)     # Draw vertical line of 'B'
t.backward(100)    # Return to starting point for top curve

# Draw the top half-circle for "B"
t.setheading(0)    # Face right
t.circle(-25, 180) # Draw top half-circle

# Move down to start the bottom half-circle for "B"
t.penup()
t.goto(50, 50)     # Move to position directly below the top half-circle
t.pendown()
t.setheading(0)    # Face right for the bottom curve
t.circle(-25, 180) # Draw bottom half-circle

# Finish
turtle.done()
