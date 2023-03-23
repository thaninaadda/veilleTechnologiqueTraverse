#
# Nom du Fichier : Traverse.py
# Auteur: Thanina Adda
# But: contient la classe Traverse
#
#

import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)
# Classe Traverse
class Traverse(tk.Frame):
    def __init__(self, parent, controleur, noTraverse=0, dateHeure="", villeDepart="", employeInscription="", listeVehicule=0, listeClient=0):

        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = listeVehicule or []
        self.listeClient = listeClient or []



        super().__init__(parent)
        
        # Label pour le titre de la page
        label = ttk.Label(self, text="Ajout d'une Traverse", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Label pour le no Traverse
        self.noTraverse_label = tk.Label(self, text="Numéro d'identification")
        self.noTraverse_label.grid(row=1, column=0)

        # Champ pour le no Traverse
        self.noTraverse_entry = tk.Entry(self)
        self.noTraverse_entry.grid(row=1, column=1)

        # Label pour la date et Heure
        self.dateHeure_label = tk.Label(self, text="date et heure")
        self.dateHeure_label.grid(row=2, column=0)

        # Champ pour la date et Heure
        self.dateHeure_entry = tk.Entry(self)
        self.dateHeure_entry.grid(row=2, column=1)

        # Label pour le ville de Depart
        self.villeDepart_label = tk.Label(self, text="ville de Depart")
        self.villeDepart_label.grid(row=3, column=0)

        # Champ pour le ville de Depart
        self.villeDepart_entry = tk.Entry(self)
        self.villeDepart_entry.grid(row=3, column=1)

        # Label pour l'employe Inscription
        self.employeInscription_label = tk.Label(self, text="employe Inscription")
        self.employeInscription_label.grid(row=4, column=0)

        # Champ pour l'employe Inscription
        self.employeInscription_entry = tk.Entry(self)
        self.employeInscription_entry.grid(row=4, column=1)

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=6, column=0, columnspan=2, pady=10)
