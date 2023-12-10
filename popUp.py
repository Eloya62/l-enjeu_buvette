from tkinter import *
from tkinter import ttk

win = Tk()

win.geometry("570x270")

def open_popup():
    top = Toplevel(win)
    top.geometry("300x200")
    top.title("child")
    texte = Label(top, text="Hello")
    texte.pack()
    button = Button(top, text="destroy", command=lambda: top.destroy())
    button.pack()

Label(win, text="main window").pack()
ttk.Button(win, text="child", command=open_popup).pack()
win.mainloop()