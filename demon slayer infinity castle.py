import turtle
turtle.Screen().setup(600,600)
loadwindow = turtle.Screen()
turtle.speed(2)
colors = ["red","green","blue","purple","white","yellow"]
my_pen = turtle.pen()
turtle.bgcolor("black")
for x in range(360):
    i = x % 6
    my_pen.pencolor(colors[i])
    my_pen.width(x/100 + 1)
    my_pen.forward(x)
    my_pen.left(59)