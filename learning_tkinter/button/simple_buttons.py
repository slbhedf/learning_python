# -*- coding: utf-8 -*-
'''
simple_buttons.py
'''

import tkinter as tk

top = tk.Tk()
top.geometry("400x400")

simple_button1 = tk.Button ( top, text="simple button")
simple_button1.place(x=0,y=0)

simple_button2 = tk.Button(top, text="background color turns blue when pressing", activebackground="blue")
simple_button2.place(x=0,y=100)

simple_button3 = tk.Button(top, text="text becomes green when pressing", activeforeground="green")
simple_button3.place(x=0,y=150)

red_button = tk.Button(top, text="backgroud color is always red except when pressing", bg="red")
red_button.place(x=0,y=50)

button_with_bold_border = tk.Button(top, text="border is 6", bd="6")
button_with_bold_border.place(x=0,y=200)
    
wide_button = tk.Button(top)
wide_button.config(text='wide button', width=30, height=5, justify="center")
wide_button.place(x=0,y=250)

top.mainloop()
