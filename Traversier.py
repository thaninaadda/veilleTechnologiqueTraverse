import tkinter as tk

class Traversier:
    def __init__(self, nom,capaciteVehicule,capacitePersonne,anneeFabrication,dateMiseService,listeEmploye):

        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService 
        self.listeEmploye = listeEmploye or []

