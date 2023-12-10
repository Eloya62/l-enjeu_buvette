# Ajoutez des widgets ici
import tkinter as tk
from tkinter import font as tkfont
import menu
import caisse
import parametre
import json


background = "#333333"


class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18,
                                      weight="bold", slant="italic")
        self.title("Lenjeux Buvette")
        self.configure(bg=background)
        self.attributes("-fullscreen", True)
        self.bind('<Escape>', lambda e: self.destroy())
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (menu.Menu, caisse.Caisse, parametre.Parametre):
            page_name = F.__name__
            frame = F(parent=container, controller=self,
                      background=background, textColor="white")
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


def sauvegarder_donnees():
    data = {"nom": nom_entry.get(), "age": age_entry.get(), "ville": ville_entry.get()}
    with open("donnees.json", "w") as fichier_json:
        json.dump(data, fichier_json)
    print("Données sauvegardées")


def construction():
    fenetre = tk.Tk()
    fenetre.attributes("-fullscreen", True)
    fenetre.bind('<Escape>', lambda e: fenetre.destroy())
    fenetre.title("Test")

    nom_label = tk.Label(fenetre, text="Nom :")
    nom_entry = tk.Entry(fenetre)
    age_label = tk.Label(fenetre, text="Âge :")
    age_entry = tk.Entry(fenetre)
    ville_label = tk.Label(fenetre, text="Ville :")
    ville_entry = tk.Entry(fenetre)
    sauvegarder_bouton = tk.Button(fenetre, text="Sauvegarder",
                                   command=sauvegarder_donnees)
    fenetre.grid_rowconfigure(0, weight=1)
    fenetre.grid_rowconfigure(1, weight=1)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_rowconfigure(2, weight=1)
    fenetre.grid_rowconfigure(3, weight=2)

    nom_label.grid(row=0, column=0)
    nom_entry.grid(row=0, column=1)
    age_label.grid(row=1, column=0)
    age_entry.grid(row=1, column=1)
    ville_label.grid(row=2, column=0)
    ville_entry.grid(row=2, column=1)
    sauvegarder_bouton.grid(row=3, column=0, columnspan=2)
    return fenetre
