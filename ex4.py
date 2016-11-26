import turtle as t
def m(l,n):
        t.pencolor("orange")
        if n == 0:
            t.forward(l)
        else:
            m(l,n-1)
            t.left(90)
            m(l,n-1)
            t.right(90)
            m(l,n-1)
            t.right(90)
            m(l,n-1)
            m(l,n-1)
            t.left(90)
            m(l,n-1)
            t.left(90)
            m(l,n-1)
            t.right(90)
            m(l,n-1)
t.penup()
t.setpos(-250, 0)
t.pendown()
l=5
n=4
m(l,n)

