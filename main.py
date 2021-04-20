from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("forest green")
for shape in range(1,11):
    angle = 360 / shape

    for i in range (shape):
        tim.forward(100)
        tim.right(angle)

















screen = Screen()
screen.exitonclick()

