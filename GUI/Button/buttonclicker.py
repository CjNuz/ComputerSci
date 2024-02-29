from tkinter import *

def btn_click():
    print("Button Click")

window = Tk()

btn = Button(window, text="click me!",command=btn_click)

btn.pack()

window.mainloop()
