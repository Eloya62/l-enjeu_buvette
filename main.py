import tkinter as tk

# Créez une fenêtre
fenetre = tk.Tk()
fenetre.title("Mon Application")

# Ajoutez des widgets ici

# Boucle principale Tkinter
fenetre.mainloop()


def action():
    # Code à exécuter lorsqu'un bouton est cliqué
    pass


bouton = tk.Button(fenetre, text="Cliquez-moi", command=action)
