import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)

for i in range(4):
    pen.forward(100)
    pen.right(90)
turtle.done()   