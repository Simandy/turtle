sides = int(input("How many sides would you like? "))
angle = 360 / sides

import turtle
turtle.speed(0)
ts = turtle.getscreen()
win=turtle.Screen();
for count in range(sides):
    for x in range(360):
        turtle.forward(sides/angle*x)
        for y in range(30):
            turtle.fd(sides/angle*2-y)
            turtle.lt(angle+y)
win.exitonclick()
