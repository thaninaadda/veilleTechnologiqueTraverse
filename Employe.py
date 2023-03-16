#
# Nom du Fichier : Employe.py
# Auteur: Thanina Adda
# But: contient la classe Employe
#
#
import tkinter as tk;
import Personne;
class Employe(Personne):
    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel, noEmploye, nAS,dateArret):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateArret = dateArret


