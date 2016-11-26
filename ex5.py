import turtle as t
def levi(l,n):
        t.pencolor("violet")
        if n == 0:
            t.forward(l)
        else:
            t.left(45)
            levi(l,n-1)
            t.right(90)
            levi(l,n-1)
            t.left(45)
t.penup()
t.setpos(-50, 0)
t.pendown()
l=5
n=10
levi(l,n)