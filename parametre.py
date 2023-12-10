import tkinter as tk


class Parametre(tk.Frame):
    
    def __init__(self, parent, controller, background, textColor):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=background)
        label = tk.Label(self, text="This is page parameter", font=controller.title_font,
                         bg=background, fg=textColor)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()
