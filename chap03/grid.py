"""Solution to an exercise in Think Python.

Author: Anne Wilkinson
"""

def draw_horiz ():
	print ('+ - - - - + - - - - +')

def draw_vert ():
	print ('|         |         |')

def draw_twobyone ():
    draw_horiz ()
    draw_vert ()
    draw_vert ()
    draw_vert ()
    draw_vert ()

def draw_grid ():
    draw_twobyone()
    draw_twobyone()
    draw_horiz ()

draw_grid ()
