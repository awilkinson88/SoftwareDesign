from swampy.TurtleWorld import *
world = TurtleWorld()
t = Turtle()
import math
t.delay = .01
length = 50
n= 8
r= 20
d=180

def square(t,length):
   
   print t

   for i in range(4):
	   fd(t, length)
	   lt(t)

#square(t,length)

def polygon(t,length,n):
   
   print t

   for i in range(n):
	   fd(t, length)
	   lt(t,360/n)

#polygon (t,length,n)

def circle(t,r):
    n = 50
    circumf = 2*math.pi*r
    length = circumf/n
    polygon (t,length,n)

#circle (t,r)

def arc(t,r,d):
  n=50
  circumf = d*math.pi/180*r
  length = circumf/n
  for i in range(n):
    fd(t, length)
    lt(t,d/n)

arc (t,r,d)

  




