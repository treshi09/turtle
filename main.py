#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle? 

import turtle

turtle.Screen().bgcolor("Gold")
turtle.Screen().setup(300,400)

no_of_side = 6
length = 80
angle = 360/no_of_side

draw = turtle.Turtle()

for i in range(no_of_side):
   draw.forward(length)
   draw.right(angle)

turtle.done()