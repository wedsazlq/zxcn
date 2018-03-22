

from turtle import*

setup(800,800)

penup()
backward(50)

pendown()

color("yellow","red")

begin_fill()

i = 0
while i < 5:
	forward(200)
	right(144)
	i = i + 1
end_fill()

penup()
goto(50,-75)
pendown()
color("black","red")
begin_fill()
circle(40,360,5)
end_fill()

done()



