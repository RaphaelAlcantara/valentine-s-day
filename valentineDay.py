import turtle


def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.speed(25)
turtle.bgcolor('black')
turtle.pensize(5)

turtle.color('red', 'pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.165)
func()
turtle.left(120)
func()
turtle.forward(111.165)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
