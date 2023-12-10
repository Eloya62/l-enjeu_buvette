import tkinter as tk


def add(liste):
    liste.append(tk.Label(root, text="test"))
    liste[-1].pack()


def supp(liste):
    liste[-1].pack_forget()
    liste.pop(-1)


listeText = []

root = tk.Tk()
root.geometry('200x150')
btn1 = tk.Button(root, text='Afficher', command=lambda: add(listeText))
btn1.pack(pady=20)
btn2 = tk.Button(root, text='Masquer', command=lambda: supp(listeText))
btn2.pack()
root.mainloop()
