


import turtle
turtle.pensize(6)

turtle.color("yellow","red")
turtle.begin_fill()
turtle.begin_poly()




for _ in range(50):
	turtle.forward(100)
	turtle.left(170)
turtle.end_fill()
turtle.penup()
turtle.goto(200,200)
turtle.pendown()

turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,300)
turtle.pendown()
turtle.begin_fill()
turtle.forward(200)
turtle.right(144)
turtle.forward(200)

turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)
turtle.forward(200)
turtle.right(144)


#turtle.left(90)

#turtle.forward(100)
turtle.end_fill()
#turtle.end_poly()
turtle.done()

