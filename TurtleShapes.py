from turtle import *
import math


myrtle = Turtle()


x = int(input("How many sides do you want?"))
#intx = int(x)
color = input("What color do you want?")
#pencolor(x)
degree = 360/x

pendown()
pencolor(color)

for turns in range(x):
    forward(150)
    left(degree)


#pendown()
#forward(300)
#left(90)
#forward(300)
#left(90)
#forward(300)
#left(90)
#forward(300)
#penup()

#goto(-100,100)
#pendown()
#right(120)
#forward(300)
#left(120)
#forward(300)
#left(120)
#forward(300)

exitonclick()
