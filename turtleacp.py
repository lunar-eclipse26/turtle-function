import turtle

turtle.Screen().bgcolor("lime")
turtle.Screen().setup(500,500)
polygon = turtle.Turtle()
num_sides = 4
side_length = 70
angle = 360.0 / num_sides
polygon.shape('square')
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()