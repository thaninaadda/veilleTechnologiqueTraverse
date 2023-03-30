#
# Nom du Fichier : Vehicule.py
# Auteur: Thanina Adda
# But: contient la classe Vehicule
#
#
import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('donnees.xml')
root = tree.getroot()
import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)
class Vehicule(tk.Frame):
    def __init__(self, parent, controleur, noIdentification = 0, marque ="", modele="", couleur="", annee=2000, immatriculation=""):
        #self.fonctionLireDonneesXml()
        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation

        super().__init__(parent)

        self.listeVehicule = []
    
        # label pour le titre Type Traversier
        label = ttk.Label(self, text="Ajout d'un vehciule", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10) # correction de la ligne du label

        # Label pour le nom du type
        self.noIdentification_label = ttk.Label(self, text="no Identification:")
        self.noIdentification_label.grid(row=1, column=0)
        
        # Champ pour le noIdentification
        self.noIdentification_entry = tk.Entry(self)
        self.noIdentification_entry.grid(row=1, column=1)

        # Label pour la marque
        self.marque_label = tk.Label(self, text="Marque:")
        self.marque_label.grid(row=2, column=0)

        # Champ pour la couleur
        self.marque_entry = tk.Entry(self)
        self.marque_entry.grid(row=2, column=1)

        # Label pour le modele
        self.modele_label = tk.Label(self, text="Modele:")
        self.modele_label.grid(row=3, column=0)

        # Champ pour le modele
        self.modele_entry = tk.Entry(self)
        self.modele_entry.grid(row=3, column=1)

        # Label pour la date et Heure
        self.couleur_label = tk.Label(self, text="couleur:")
        self.couleur_label.grid(row=4, column=0)

        # Champ pour lcouleur
        self.couleur_entry = tk.Entry(self)
        self.couleur_entry.grid(row=4, column=1)

        # Label pour annee
        self.annee_label = tk.Label(self, text="Annee:")
        self.annee_label.grid(row=5, column=0)

        # Champ pour annee
        self.annee_entry = tk.Entry(self)
        self.annee_entry.grid(row=5, column=1)

        # Label pour la date et Heure
        self.immatriculation_label = tk.Label(self, text="Immatriculation:")
        self.immatriculation_label.grid(row=6, column=0)

        # Champ pour lcouleur
        self.immatriculation_entry = tk.Entry(self)
        self.immatriculation_entry.grid(row=6, column=1)

        # liste des vehicules
        self.listeboxVehicule = tk.Listbox(self, height=5, width=50)
        self.listeboxVehicule.grid(row=7, column=0, columnspan=2, pady=10)

        self.fonctionLireDonneesVehiculeXml()

        # Bouton pour ajouter un vehicule
        button1 = ttk.Button(self, text="Ajouter", command=self.fonctionEcrireDonneesVehiculeXml)
        button1.grid(row=8, column=0, pady=10)

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=8, column=1, columnspan=2, pady=10)

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