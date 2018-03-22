import turtle

turtle.color("yellow")
turtle.pensize(8)

turtle.begin_fill()
for _ in range (50):
	turtle.forward(300)
	turtle.left(170)
turtle.end_fill()

turtle.done()
