#
# Nom du Fichier : Employe.py
# Auteur: Thanina Adda
# But: contient la classe Employe
#
#
import xml.etree.ElementTree as ET

# charge du fichier xml
tree = ET.parse('donnees.xml')
root = tree.getroot()
import tkinter as tk;

from tkinter import ttk
LARGEFONT =("Verdana", 20)
#classe Employé
class Employe(tk.Frame):
    def __init__(self, parent, controleur, nom="", adresse="", ville="", province="", codePostal="",
                  telephone="", courriel="", noEmploye="",dateArret=""):
        super().__init__(parent)
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel
        self.noEmploye = noEmploye
        self.dateArret = dateArret
        self.listeEmploye = []
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

        # Label pour le nom
        self.nom_label = tk.Label(self, text="Nom")
        self.nom_label.grid(row=1, column=0)

        # Champ pour le nom
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=1, column=1)

        # Label pour l'adresse
        self.addresse_label = tk.Label(self, text="Adresse")
        self.addresse_label.grid(row=2, column=0)

        # Champ pour l'adresse
        self.addresse_entry = tk.Entry(self)
        self.addresse_entry.grid(row=2, column=1)

        # Label pour la ville
        self.ville_label = tk.Label(self, text="Ville")
        self.ville_label.grid(row=3, column=0)

        # Champ pour la ville
        self.ville_entry = tk.Entry(self)
        self.ville_entry.grid(row=3, column=1)

        # Label pour la province
        self.province_label = tk.Label(self, text="Province")
        self.province_label.grid(row=4, column=0)

        # Champ pour la province
        self.province_entry = tk.Entry(self)
        self.province_entry.grid(row=4, column=1)

        # Label pour le code postal
        self.postal_code_label = tk.Label(self, text="Code postal")
        self.postal_code_label.grid(row=5, column=0)

        # Champ pour le code postal
        self.postal_code_entry = tk.Entry(self)
        self.postal_code_entry.grid(row=5, column=1)

        # Label pour le téléphone
        self.phone_label = tk.Label(self, text="Téléphone")
        self.phone_label.grid(row=6, column=0)

        # Champ pour le téléphone
        self.telephone_entry = tk.Entry(self)
        self.telephone_entry.grid(row=6, column=1)

        # Label pour le courriel
        self.email_label = tk.Label(self, text="Courriel")
        self.email_label.grid(row=7, column=0)

        # Champ pour le courriel
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=7, column=1)

        # Label pour le numéro d'identification
        self.id_label = tk.Label(self, text="Numéro d'employé")
        self.id_label.grid(row=8, column=0)

        # Champ pour le numéro d'identification
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=8, column=1)

        # Label pour la date de naissance
        self.dateArret_label = tk.Label(self, text="date Arret")
        self.dateArret_label.grid(row=10, column=0)

        # Champ pour la date de naissance
        self.dateArret_entry = tk.Entry(self)
        self.dateArret_entry.grid(row=10, column=1)

        # listbox des Employés
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.grid(row=11, column=0, columnspan=2, pady=10)

        self.fonctionLireDonneesEmployesXml()
        # Bouton pour ajouter un Employé
        button1 = ttk.Button(self, text="Ajouter", command=self.fonctionEcrireDonneesEmployesXml)
        button1.grid(row=12, column=0, columnspan=2, pady=10)

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=12, column=1, columnspan=2, pady=10)

    #Fonction GetHashCode pour la classe Employé
    def GetHashCode(self):
        return hash(self.codePostal + self.telephone)

    #Fonction Equals pour la classe Employé
    def Equals(self, obj):
        if isinstance(obj, Employe):
            return (self.nom == obj.nom and self.adresse == obj.adresse and self.ville == obj.ville
                    and self.province == obj.province and self.codePostal == obj.codePostal
                    and self.telephone == obj.telephone and self.courriel == obj.courriel)
        else:
            return False


    # Fonction toString pour la classe Employé
    def toString(self):
        return f"Nom: {self.nom}\nAdresse: {self.adresse}\nVille: {self.ville}\nProvince: {self.province}\nCode Postal: {self.codePostal}\nTéléphone: {self.telephone}\nCourriel: {self.courriel}"

    #Foncton qui permet de lire les informations du fichier xml
    def fonctionLireDonneesEmployesXml(self):
        for employe in root.findall('employe'):
            nom = employe.find('nom').text
            adresse = employe.find('adresse').text
            ville = employe.find('ville').text
            province = employe.find('province').text
            codePostal = employe.find('codePostal').text
            telephone = employe.find('telephone').text
            courriel = employe.find('courriel').text
            noEmploye = employe.find('noEmploye').text
            dateArret = employe.find('dateArret').text
            self.listeEmploye.append(employe)
            self.listbox.insert(tk.END, nom)

        print(self.listeEmploye)

    #Foncton qui permet d'ajouter les informations d'un client dans le fichier xml 
    def fonctionEcrireDonneesEmployesXml(self):
        employe = ET.SubElement(root, 'employe')
        nom = ET.SubElement(employe, 'nom')
        nom.text = self.nom_entry.get()
        adresse = ET.SubElement(employe, 'adresse')
        adresse.text = self.addresse_entry.get()
        ville = ET.SubElement(employe, 'ville')
        ville.text = self.ville_entry.get()
        province = ET.SubElement(employe, 'province')
        province.text = self.province_entry.get()
        codePostal = ET.SubElement(employe, 'codePostal')
        codePostal.text = self.postal_code_entry.get()
        telephone = ET.SubElement(employe, 'telephone')
        telephone.text = self.telephone_entry.get()
        courriel = ET.SubElement(employe, 'courriel')
        courriel.text = self.email_entry.get()
        noEmploye = ET.SubElement(employe, 'noEmploye')
        noEmploye.text = self.id_entry.get()
        dateArret = ET.SubElement(employe, 'dateArret')
        dateArret.text = self.dateArret_entry.get()
        
        tree.write('donnees.xml')
        self.fonctionLireDonneesEmployesXml()

