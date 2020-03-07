# -*- coding: utf-8 -*-
from tkinter import Tk, Canvas

top = Tk()

canvas = Canvas (top, bg="pink")
canvas['width'] = 300
canvas['height'] = 300

# draw a circle
coord_oval = 0, 0, 300, 300 # x0, y0, x1, y1 : two points of circumscribed square
oval = canvas.create_oval(coord_oval)

canvas.pack()

top.mainloop()
