import tkinter as tk
import scroll


class Caisse(tk.Frame):
    
    def __init__(self, parent, controller, background, textColor):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=background)
        label = tk.Label(self, text="This is page Caisse",
                         font=controller.title_font,
                         bg=background, fg=textColor)
        label.pack(side="top", fill="x", pady=10)
        buttonBack = tk.Button(self, text="Retour", cursor="hand2",
                               command=lambda: controller.show_frame("Menu"))
        buttonBack.pack(side="bottom", pady=10)
        inputArea = tk.Frame(self, bg=background)
        inputArea.pack()
        inputArea.grid_rowconfigure(0, weight=1)
        inputArea.grid_columnconfigure(0, weight=1)
        inputArea.grid_columnconfigure(1, weight=1)
        inputArea.grid_columnconfigure(2, weight=1)
        inputMenu = tk.Frame(inputArea, bg=background)
        hMenu = tk.Scrollbar(inputMenu, orient='horizontal')
        hMenu.pack(side=tk.BOTTOM, fill=tk.X)
        vMenu = tk.Scrollbar(inputMenu, orient='vertical')
        vMenu.pack(side=tk.RIGHT, fill=tk.Y)
        tMenu = tk.Text(inputMenu, wrap=tk.NONE,
                        xscrollcommand=hMenu.set, yscrollcommand=vMenu.set)
        for i in range(200):
            tMenu.insert(tk.END, "this is some text\n")
        tMenu.pack(side=tk.TOP, fill=tk.X)
        hMenu.config(command=tMenu.xview)
        vMenu.config(command=tMenu.yview)
        inputMenu.grid(row=0, column=0, sticky="nsew")
        inputProduct = tk.Frame(inputArea, bg=background)
        hProduct = tk.Scrollbar(inputProduct, orient='horizontal')
        hProduct.pack(side=tk.BOTTOM, fill=tk.X)
        vProduct = tk.Scrollbar(inputProduct, orient='vertical')
        vProduct.pack(side=tk.RIGHT, fill=tk.Y)
        tProduct = tk.Text(inputProduct, wrap=tk.NONE,
                           xscrollcommand=hProduct.set,
                           yscrollcommand=vProduct.set)
        for i in range(200):
            tProduct.insert(tk.END, "this is some text\n")
        tProduct.pack(side=tk.TOP, fill=tk.X)
        hProduct.config(command=tProduct.xview)
        vProduct.config(command=tProduct.yview)   
        inputProduct.grid(row=0, column=1, sticky="nsew")
        inputCommand = tk.Frame(inputArea, bg=background)
        hCommand = tk.Scrollbar(inputCommand, orient='horizontal')
        hCommand.pack(side=tk.BOTTOM, fill=tk.X)
        vCommand = tk.Scrollbar(inputCommand, orient='vertical')
        vCommand.pack(side=tk.RIGHT, fill=tk.Y)
        tCommand = tk.Text(inputCommand, wrap=tk.NONE,
                           xscrollcommand=hCommand.set,
                           yscrollcommand=vCommand.set)
        for i in range(200):
            tCommand.insert(tk.END, "this is some text\n")
        tCommand.pack(side=tk.TOP, fill=tk.X)
        hCommand.config(command=tCommand.xview)
        vCommand.config(command=tCommand.yview)
        inputCommand.grid(row=0, column=2, sticky="nsew")