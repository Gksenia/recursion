import turtle as t
t.pencolor("blue violet")
def dragon(l,n,s = 1):
        if n == 0:

            t.forward(l)
        else:
            t.left(45*s)
            dragon(l,n-1,1)
            t.right(90*s)
            dragon(l,n-1,-1)
            t.left(45*s)

def dragon2(l, n, s=1):
    dragon(l,n,s = 1)
    t.penup()
    t.setpos(0,0)
    t.right(90)
    t.pendown()
    t.pencolor("aquamarine")
    dragon(l,n,s = 1)
    t.penup()
    t.setpos(0, 0)
    t.right(90)
    t.pendown()
    t.pencolor("DarkBlue")
    dragon(l, n, s=1)
    t.penup()
    t.setpos(0, 0)
    t.right(90)
    t.pendown()
    t.pencolor("violet")
    dragon(l, n, s=1)
t.penup()
t.setpos(0, 0)
t.pendown()
t.speed(20000000000000000000)
l=5
n=10
dragon2(l,n)
