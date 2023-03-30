
#
# Nom du Fichier : Traversier.py
# Auteur: Thanina Adda
# But: contient la classe Traversier
#

import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('donnees.xml')
root = tree.getroot()
import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)
class Traversier(tk.Frame):
    def __init__(self, parent, controleur, nom="",capaciteVehicule="",capacitePersonne="",anneeFabrication="",dateMiseService=""):

        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService 
        


        super().__init__(parent)
        
        self.listeTraversier =[]
        # Label pour le titre
        label = ttk.Label(self, text="Ajout d'un Traversier", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Label pour le Nom du Traversier
        self.nom_label = tk.Label(self, text="Nom du traversier")
        self.nom_label.grid(row=1, column=0)

        # Champ pour le Nom du Traversier
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=1, column=1)

        # Label pour la Capacité du Véhicule
        self.capaciteVehicule_label = tk.Label(self, text="Capacité du Véhicule")
        self.capaciteVehicule_label.grid(row=2, column=0)

        # Champ pour la Capacité du Véhicule
        self.capaciteVehicule_entry = tk.Entry(self)
        self.capaciteVehicule_entry.grid(row=2, column=1)

        # Label pour la Capacité de Personne  au Départ
        self.capacitePersonneDepart_label = tk.Label(self, text="Capacité en personne")
        self.capacitePersonneDepart_label.grid(row=3, column=0)

        # Champ pour la Capacité de Personne  au Départ
        self.capacitePersonneDepart_entry = tk.Entry(self)
        self.capacitePersonneDepart_entry.grid(row=3, column=1)

        # Label pour l'Année De Fabrication
        self.anneeFabrication_label = tk.Label(self, text="Année de fabrication")
        self.anneeFabrication_label.grid(row=4, column=0)

        # Champ pour l'Année De Fabrication
        self.anneeFabrication_entry = tk.Entry(self)
        self.anneeFabrication_entry.grid(row=4, column=1)

        # Label pour la Date De Mise en Service
        self.dateMiseService_label = tk.Label(self, text="Date de mise en service")
        self.dateMiseService_label.grid(row=5, column=0)

        # Champ pour la Date De Mise en Service
        self.dateMiseService_entry = tk.Entry(self)
        self.dateMiseService_entry.grid(row=5, column=1)

        # liste des traversiers
        self.listeboxTraversier = tk.Listbox(self, height=5, width=50)
        self.listeboxTraversier.grid(row=6, column=0, columnspan=2, pady=10)


        self.fonctionLireDonneesTraversierXml()

        # Bouton pour ajouter un Véhicule
        button1 = ttk.Button(self, text="Ajouter", command=self.fonctionEcrireDonneesTraversierXml)
        button1.grid(row=7, column=0, pady=10)

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=7, column=1, columnspan=2, pady=10)


    #Fonction GetHashCode pour la classe Traversier
    def GetHashCode(self):
        return hash(self.capacitePersonne + self.dateMiseService)

    #Fontion Equals pour la classe Traversier
    def Equals(self, obj):
        if isinstance(obj, Traversier):
            return (self.nom == obj.nom and self.capacitePersonne == obj.capacitePersonne and self.anneeFabrication == obj.anneeFabrication
                    and self.dateMiseService == obj.dateMiseService)
        else:
            return False

    # Fonction toString pour la classe Traversier
    def toString(self):
        return f"nom : {self.nom}\ncapacite Personne: {self.capacitePersonne}\nannee Fabrication: {self.anneeFabrication}\ndate Mise en Service: {self.dateMiseService}"


    #Foncton qui permet de lire les informations du fichier xml 
    def fonctionLireDonneesTraversierXml(self):
        for traversier in root.findall('traversier'):
            nom = traversier.find('nom').text
            capacitePersonneDepart= traversier.find('capacitePersonne').text
            anneeFabrication = traversier.find('anneeFabrication').text
            dateMiseService = traversier.find('dateMiseService').text
           

            self.listeTraversier.append(traversier)
            self.listeboxTraversier.insert(tk.END, nom + " " )

        print(self.listeTraversier)

    #Foncton qui permet d'ajouter les informations d'un Véhicule dans le fichier xml 
    def fonctionEcrireDonneesTraversierXml(self):
        traversier = ET.SubElement(root, 'traversier')
        nom = ET.SubElement(traversier, 'nom')
        nom.text = self.nom_entry.get()
        capacitePersonneDepart_label = ET.SubElement(traversier, 'capacitePersonne')
        capacitePersonneDepart_label.text = self.capacitePersonneDepart_entry.get()
        anneeFabrication = ET.SubElement(traversier, 'anneeFabrication')
        anneeFabrication.text = self.anneeFabrication_entry.get()
        dateMiseService = ET.SubElement(traversier, 'dateMiseService')
        dateMiseService.text = self.dateMiseService_entry.get()
        print("Ecriture Vehicule dans le fichier XML")
        tree.write('donnees.xml')
        self.fonctionLireDonneesTraversierXml()


        
        
