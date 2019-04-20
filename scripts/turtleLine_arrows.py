import turtle
ts = turtle.getscreen()
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("white")
sides = 1200
#colors = ["black"]
win=turtle.Screen();
for x in range(360):
    t.pencolor("black")
    t.forward(x*2/sides+x)
    t.left(360/sides+2-x*24*x)
    t.width(1)
ts.getcanvas().postscript(file="test.eps")
win.exitonclick()
