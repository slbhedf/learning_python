# -*- coding: utf-8 -*-
from tkinter import Tk, Canvas

top = Tk()

canvas = Canvas (top, bg="pink")
canvas['width'] = 300
canvas['height'] = 300

# draw a line from left top to right bottom
coord_line = 0, 0, 300, 300
line = canvas.create_line(coord_line, fill="black")

canvas.pack()

top.mainloop()