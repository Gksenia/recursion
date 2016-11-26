import turtle
def line(l, n):
    turtle.pencolor("blue")
    if n == 0:
        turtle.forward(l)
    else:
        line(l/3, n-1)
        turtle.left(60)
        line(l/3, n-1)
        turtle.right(120)
        line(l/3, n-1)
        turtle.left(60)
        line(l/3, n-1)

def snow(p,n):
    for i in range (k):
        line(l,n)
        turtle.right(120)

turtle.penup()
turtle.setpos(-250, 0)
turtle.pendown()
l=150
n=3
k=6
p=100
snow(p,n)