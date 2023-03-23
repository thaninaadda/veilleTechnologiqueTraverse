
#
# Nom du Fichier : Traversier.py
# Auteur: Thanina Adda
# But: contient la classe Traversier
#


import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)
class Traversier(tk.Frame):
    def __init__(self, parent, controleur, nom="",capaciteVehicule=0,capacitePersonne=0,anneeFabrication=2000,dateMiseService=2000,listeEmploye=0):

        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService 
        self.listeEmploye = listeEmploye or []


        super().__init__(parent)
        

        # Label pour le titre
        label = ttk.Label(self, text="Ajout d'un Traversier", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Label pour le Nom du Traversier
        self.nom_label = tk.Label(self, text="Nom du traversier")
        self.nom_label.grid(row=1, column=0)

        # Champ pour le Nom du Traversier
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=1, column=1)

        # Label pour la Capacite du Vehicule
        self.capaciteVehicule_label = tk.Label(self, text="Capacite du vehicule")
        self.capaciteVehicule_label.grid(row=2, column=0)

        # Champ pour la Capacite du Vehicule
        self.capaciteVehicule_entry = tk.Entry(self)
        self.capaciteVehicule_entry.grid(row=2, column=1)

        # Label pour la Capacite en Personne de Depart
        self.capacitePersonneDepart_label = tk.Label(self, text="Capacite en personne")
        self.capacitePersonneDepart_label.grid(row=3, column=0)

        # Champ pour la Capacite en Personne de Depart
        self.capacitePersonneDepart_entry = tk.Entry(self)
        self.capacitePersonneDepart_entry.grid(row=3, column=1)

        # Label pour l'Annee De Fabrication
        self.anneeFabrication_label = tk.Label(self, text="Annee de fabrication")
        self.anneeFabrication_label.grid(row=4, column=0)

        # Champ pour l'Annee De Fabrication
        self.anneeFabrication_entry = tk.Entry(self)
        self.anneeFabrication_entry.grid(row=4, column=1)

        # Label pour la Date De Mise en Service
        self.dateMiseService_label = tk.Label(self, text="Date de mise en service")
        self.dateMiseService_label.grid(row=5, column=0)

        # Champ pour la Date De Mise en Service
        self.dateMiseService_entry = tk.Entry(self)
        self.dateMiseService_entry.grid(row=5, column=1)

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=6, column=0, columnspan=2, pady=10)
        
