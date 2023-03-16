#
# Nom du Fichier : Traverse.py
# Auteur: Thanina Adda
# But: contient la classe Traverse
#
#

import tkinter as tk

# Classe Traverse
class Traverse:
    def __init__(self, noTraverse, dateHeure, villeDepart, employeInscription, listeVehicule, listeClient):

        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = listeVehicule or []
        self.listeClient = listeClient or []



