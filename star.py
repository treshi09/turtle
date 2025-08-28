import turtle


turtle.Screen().bgcolor("blue")
draw = turtle.Turtle()

for i in range(3):
    draw.forward(200)
    draw.left(120)

draw.penup()
draw.left(60)
draw.forward(100)
draw.pendown()
draw.right(60)
draw.backward(40)
for i in range(3):
    draw.forward(200)
    draw.right(120)




turtle.done()