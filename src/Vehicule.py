#
# Nom du Fichier : Véhicule.py
# Auteur: Thanina Adda
# But: contient la classe Véhicule
#
#
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('donnees.xml')
root = tree.getroot()
import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)

#Classe Véhicule
class Vehicule(tk.Frame):
    def __init__(self, parent, controleur, noIdentification = 0, marque ="", modele="", couleur="", annee=2000, immatriculation=""):

        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation

        super().__init__(parent)

        self.listeVehicule = []
    
        # label pour le titre du Véhicule
        label = ttk.Label(self, text="Ajout d'un Véhicule", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10) # correction de la ligne du label

        # Label pour le no d'identification
        self.noIdentification_label = ttk.Label(self, text="no Identification:")
        self.noIdentification_label.grid(row=1, column=0)
        
        # Champ pour le noIdentification
        self.noIdentification_entry = tk.Entry(self)
        self.noIdentification_entry.grid(row=1, column=1)

        # Label pour la marque
        self.marque_label = tk.Label(self, text="Marque:")
        self.marque_label.grid(row=2, column=0)

        # Champ pour la marque
        self.marque_entry = tk.Entry(self)
        self.marque_entry.grid(row=2, column=1)

        # Label pour le Modèle
        self.modele_label = tk.Label(self, text="Modèle:")
        self.modele_label.grid(row=3, column=0)

        # Champ pour le Modèle
        self.modele_entry = tk.Entry(self)
        self.modele_entry.grid(row=3, column=1)

        # Label pour la date et Heure
        self.couleur_label = tk.Label(self, text="Couleur:")
        self.couleur_label.grid(row=4, column=0)

        # Champ pour la date et Heure
        self.couleur_entry = tk.Entry(self)
        self.couleur_entry.grid(row=4, column=1)

        # Label pour année 
        self.annee_label = tk.Label(self, text="Année:")
        self.annee_label.grid(row=5, column=0)

        # Champ pour année
        self.annee_entry = tk.Entry(self)
        self.annee_entry.grid(row=5, column=1)

        # Label pour l'immatriculation
        self.immatriculation_label = tk.Label(self, text="Immatriculation:")
        self.immatriculation_label.grid(row=6, column=0)

        # Champ pour l'immatriculation
        self.immatriculation_entry = tk.Entry(self)
        self.immatriculation_entry.grid(row=6, column=1)

        # liste des Véhiculea
        self.listeboxVehicule = tk.Listbox(self, height=5, width=50)
        self.listeboxVehicule.grid(row=7, column=0, columnspan=2, pady=10)

        self.fonctionLireDonneesVehiculeXml()

        # Bouton pour ajouter un Véhicule
        button1 = ttk.Button(self, text="Ajouter", command=self.fonctionEcrireDonneesVehiculeXml)
        button1.grid(row=8, column=0, pady=10)

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=8, column=1, columnspan=2, pady=10)

    #Foncton qui permet de lire les informations du fichier xml 
    def fonctionLireDonneesVehiculeXml(self):
        for vehicule in root.findall('vehicule'):
            noIdentification = vehicule.find('noIdentification').text
            marque = vehicule.find('marque').text
            modele = vehicule.find('modele').text
            couleur = vehicule.find('couleur').text
            annee = vehicule.find('annee').text
            immatriculation = vehicule.find('immatriculation').text

            self.listeVehicule.append(vehicule)
            self.listeboxVehicule.insert(tk.END, noIdentification + " " + marque + " " + modele + " " + couleur)

        print(self.listeVehicule)

    #Foncton qui permet d'ajouter les informations d'un Véhicule dans le fichier xml 
    def fonctionEcrireDonneesVehiculeXml(self):
        vehicule = ET.SubElement(root, 'vehicule')
        noIdentification = ET.SubElement(vehicule, 'noIdentification')
        noIdentification.text = self.noIdentification_entry.get()
        marque = ET.SubElement(vehicule, 'marque')
        marque.text = self.marque_entry.get()
        modele = ET.SubElement(vehicule, 'modele')
        modele.text = self.modele_entry.get()
        couleur = ET.SubElement(vehicule, 'couleur')
        couleur.text = self.couleur_entry.get()
        annee = ET.SubElement(vehicule, 'annee')
        annee.text = self.annee_entry.get()
        immatriculation = ET.SubElement(vehicule, 'immatriculation')
        immatriculation.text = self.immatriculation_entry.get()
        print("Ecriture Vehicule dans le fichier XML")
        tree.write('donnees.xml')
        self.fonctionLireDonneesVehiculeXml()


     #Fonction GetHashCode pour la classe Véhicule
    def GetHashCode(self):
        return hash(self.marque + self.modele)

    #Fontion Equals pour la classe Véhicule
    def Equals(self, obj):
        if isinstance(obj, Vehicule):
            return (self.noIdentification == obj.noIdentification and self.marque == obj.marque and self.modele == obj.modele
                    and self.couleur == obj.couleur and self.annee == obj.annee and self.immatriculation == obj.immatriculation)
        else:
            return False

    # Fonction toString pour la classe Véhicule
    def toString(self):
        return f"noIdentification: {self.noIdentification}\nmarque: {self.marque}\nmodele: {self.modele}\ncouleur: {self.couleur}\nannee: {self.annee}\nimmatriculation: {self.immatriculation}"
