import tkinter as tk 


class Menu(tk.Frame):
    
    def __init__(self, parent, controller, background, textColor):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=background)
        label = tk.Label(self, text="This is the menu page",
                         font=controller.title_font,
                         bg=background, fg=textColor)
        buttonCaisse = tk.Button(self, text="Caisse", width=20,
                                 height=5, cursor="hand2",
                                 command=lambda: controller.show_frame("Caisse"))
        buttonParameter = tk.Button(self, text="Parametre",
                                    width=20, height=5, cursor="hand2",
                                    command=lambda: controller.show_frame("Parametre"))
        buttonSave = tk.Button(self, text="Save", width=20,
                               height=5, cursor="hand2",
                               command=lambda: print("Save"))
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=3)

        label.grid(row=0, columnspan=3, sticky="N", pady=10)
        buttonCaisse.grid(row=1, column=0)
        buttonParameter.grid(row=1, column=1)
        buttonSave.grid(row=1, column=2)
