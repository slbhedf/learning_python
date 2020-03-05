# -*- coding: utf-8 -*-

import tkinter as tk
import random

top = tk.Tk()
top.geometry("300x200")

def turn_randomColor():
    colors = ['blue', 'cyan', 'green', 'pink', 'purple', 'red', 'yellow']
    index = random.randint(0, len(colors)-1)
    wide_button['bg'] = colors[index]
    
wide_button = tk.Button(top)
wide_button['text'] = 'press here to change background color'
#wide_button['wraplength'] = 9
wide_button['width'] = 30
wide_button.place(x=0,y=0)
wide_button['height'] = 5
wide_button['justify'] = "center"
wide_button['command'] = turn_randomColor

top.mainloop()



