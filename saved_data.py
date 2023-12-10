import json


# Écrivez le dictionnaire dans un fichier JSON
def saveProduct(products):
    with open("menu.json", "r") as menu:
        pastProducts = json.load(menu)
    products = ["felicitation, tu sais écrire dans un json"]
    pastProducts.append(products)
    with open("menu.json", "w") as menu:
        json.dump(products, menu)


def saveCommand(command):
    with open("commands.json", "r") as commands:
        pastCommand = json.load(commands)
    command = {"commande": "commande"}
    pastCommand.append(command)
    with open("commands.json", "w") as commands:
        json.dump(pastCommand, commands, indent=4)


# Lisez les données depuis un fichier JSON
def loadProduct():
    with open("commands.json", "r") as save:
        data_lu = json.load(save)
    print(data_lu)


saveCommand("commandes")


"""
produits et commandes sont des listes de dictionnaires
"""
