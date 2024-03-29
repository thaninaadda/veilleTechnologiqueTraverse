#
# Nom du Fichier : Type.py
# Auteur: Thanina Adda
# But: contient la classe Type
#
#


import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)

#Classe type Traverse
class Type(tk.Frame):
    def __init__(self, parent, controleur, nom="", nombreRoue="", prixTraverse=""):

        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse



        super().__init__(parent)
        # label pour le titre Type Traversier
        label = ttk.Label(self, text="Ajout d'un type de traverse", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10) # correction de la ligne du label

        # Label pour le nom du type
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(row=1, column=0)
        
        # Champ pour le no Traverse
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=1, column=1)

        # Label pour le no Traverse
        self.nombreRoue_label = tk.Label(self, text="Nombre de roue")
        self.nombreRoue_label.grid(row=2, column=0)

        # Champ pour le no Traverse
        self.nombreRoue_entry = tk.Entry(self)
        self.nombreRoue_entry.grid(row=2, column=1)

        # Label pour la date et Heure
        self.prixTraverse_label = tk.Label(self, text="prix")
        self.prixTraverse_label.grid(row=3, column=0)

        # Champ pour le no Traverse
        self.prixTraverse_entry = tk.Entry(self)
        self.prixTraverse_entry.grid(row=3, column=1)

        # listbox des types de traverse
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.grid(row=13, column=0, columnspan=2, pady=10)

        # Bouton pour ajouter un client, et écrit dans le fichier xml
        button1 = ttk.Button(self, text="Ajouter", command=self)
        button1.grid(row=12, column=0, columnspan=2, pady=10)
        
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=12, column=1, columnspan=2, pady=10)


    #Fonction GetHashCode pour la classe Type
    def GetHashCode(self):
        return hash(self.prixTraverse + self.nombreRoue)

    #Fontion Equals pour la classe Type
    def Equals(self, obj):
        if isinstance(obj, Type):
            return (self.nom == obj.nom and self.nombreRoue == obj.nombreRoue and self.prixTraverse == obj.prixTraverse)
        else:
            return False

    # Fonction toString pour la classe Type
    def toString(self):
        return f"nom : {self.nom}\nnombre de Roue: {self.nombreRoue}\nprixTraverse: {self.prixTraverse}"


        


