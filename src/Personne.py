#
# Nom du Fichier : Personne.py
# Auteur: Thanina Adda
# But: contient la classe Personne
#
#
import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)
class Personne:
    def __init__(self, nom, addresse, ville, province, postal_code, telephone, email):
        self.nom = nom
        self.addresse = addresse
        self.ville = ville
        self.province = province
        self.postal_code = postal_code
        self.telephone = telephone
        self.email = email


    #Fonction GetHashCode  pour la classe Personne
    def GetHashCode(self):
        return hash(self.codePostal + self.telephone)

    #Fontion Equals  pour la classe Personne
    def Equals(self, obj):
        if isinstance(obj, Personne):
            return (self.nom == obj.nom and self.adresse == obj.adresse and self.ville == obj.ville
                    and self.province == obj.province and self.codePostal == obj.codePostal
                    and self.telephone == obj.telephone and self.courriel == obj.courriel)
        else:
            return False



    # Fonction toString pour la classe Personne
    def toString(self):
        return f"Nom: {self.nom}\nAdresse: {self.adresse}\nVille: {self.ville}\nProvince: {self.province}\nCode Postal: {self.codePostal}\nTéléphone: {self.telephone}\nCourriel: {self.courriel}"