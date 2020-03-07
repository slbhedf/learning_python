# -*- coding: utf-8 -*-
'''
draw_simple_grid.py

draw grid on the 300x300 screen.
interval = 50
'''

from tkinter import Tk, Canvas

top = Tk()

canvas = Canvas (top, bg="pink")
canvas['width'] = 300
canvas['height'] = 300

# draw lines as grid
x = 0
while x <= 300:
    coord_line = x, 0, x, 300 # tuple
    canvas.create_line(coord_line, fill="black")
    x += 50

y = 0
while y <= 300:
    coord_line = 0, y, 300, y # tuple
    canvas.create_line(coord_line, fill="black")
    y += 50

canvas.pack()

top.mainloop()
