#Author: Anne Wilkinson

from swampy.TurtleWorld import *
world = TurtleWorld()
t = Turtle()
t.delay = 0

def dcurve (t,n):
   """Draws n iterations of a dragon curve"""

   def x_func(t,n):
      if n ==0:
         return
      x_func(t,n-1)
      rt(t)
      y_func (t,n-1)
      fd (t,20)

   def y_func(t,n):
      if n ==0:
        return
      fd(t,20)
      x_func(t,n-1)
      lt(t)
      y_func(t,n-1)

   fd (t,20)
   x_func(t,n)

t.delay = 0
dcurve(t,10)
wait_for_user()
