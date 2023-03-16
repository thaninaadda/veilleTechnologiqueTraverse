#
# Nom du Fichier : Vehicule.py
# Auteur: Thanina Adda
# But: contient la classe Vehicule
#
#

import tkinter as tk

class Vehicle:
    def __init__(self, noIdentification, marque, modele, couleur, annee, immatriculation):

        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation

