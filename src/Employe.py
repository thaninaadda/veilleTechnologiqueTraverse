#
# Nom du Fichier : Employe.py
# Auteur: Thanina Adda
# But: contient la classe Employe
#
#
import tkinter as tk;
# import src.Personne as Personne;
from tkinter import ttk
LARGEFONT =("Verdana", 20)
class Employe(tk.Frame):
    def __init__(self, parent, controleur, nom="", adresse="", ville="", province="", codePostal="",
                  telephone="", courriel="", noEmploye="", nAS="",dateArret=""):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateArret = dateArret

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
        
        # Bouton pour revenir a la page StartPage
         # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=6, column=0, columnspan=2, pady=10)


