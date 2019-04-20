import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
sides = 697
colors = ["red", "orange", "green", "green", "yellow", "blue", "purple"]

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*2*1265*sides+x)
    t.left(360/sides+108)
    t.width(x*sides/200)
