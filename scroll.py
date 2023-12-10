import tkinter as tk


class ScrollBar:
    # constructor
    def __init__(self, parent):
        h = tk.Scrollbar(parent, orient='horizontal')
        h.pack(side=tk.BOTTOM, fill=tk.X)
        v = tk.Scrollbar(parent, orient='vertical')
        v.pack(side=tk.RIGHT, fill=tk.Y)
        t = tk.Text(parent, width=15, height=15, wrap=tk.NONE,
                    xscrollcommand=h.set, yscrollcommand=v.set)
        for i in range(20):
            t.insert(tk.END, "this is some text\n")
        t.pack(side=tk.TOP, fill=tk.X)
        h.config(command=t.xview)
        v.config(command=t.yview)
