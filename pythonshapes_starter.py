from turtle import *
import math
import time

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.

x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
showturtle()
begin_fill()
pendown()
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)
forward(120)
left(90)

color("violet")
end_fill()
penup()

reset()
time.sleep(2)
begin_fill()
pendown()
for i in range(3):
    forward(120)
    left(120)


color("red")
end_fill()

done()




# Close window on click.
exitonclick()
