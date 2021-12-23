from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.back(10)

def move_clockwise():
    timmy.right(10)

def move_anticlockwise():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=move_anticlockwise, key="a")
screen.onkey(fun=clear, key="c")












screen.exitonclick()

