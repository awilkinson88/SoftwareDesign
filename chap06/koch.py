from swampy.TurtleWorld import *
world = TurtleWorld()
t = Turtle()
t.delay = 0

#Author Anne Wilkinson with code from Allen 
#Downey

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

#draw (t,5,5)

def koch (t,length):
    if length<3:
        fd(t, length)
        return
    x = length/3.0
    koch(t, x)
    lt(t, 60)
    koch(t, x)
    rt(t, 120)
    koch(t, x)
    lt(t, 60)
    koch(t, x)

koch (t,200)

