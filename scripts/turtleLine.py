import turtle
ts = turtle.getscreen()
t = turtle.Pen()
t.speed(1)
turtle.bgcolor("white")
sides = 360
#colors = ["black"]
win=turtle.Screen();
for x in range(360):
    t.pencolor("black")
    t.forward(sides/240*x)
    t.left(120/sides+sides+sides-x*120*x)
    t.width(1)
ts.getcanvas().postscript(file="test.eps")
win.exitonclick()
