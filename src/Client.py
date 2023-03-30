
#
# Nom du Fichier : Client.py
# Auteur: Thanina Adda
# But: contient la classe Client
#
#
import xml.etree.ElementTree as ET

# charge du fichier xml
tree = ET.parse('donnees.xml')
root = tree.getroot()
import tkinter as tk
from tkinter import ttk
LARGEFONT =("Verdana", 20)

#Classe Client
class Client(tk.Frame):
    def __init__(self, parent, controleur, nom="", adresse="", ville="", province="", codePostal="", telephone="", courriel="", numeroIdentification="", sexe="",dateDeNaissance=""):
        
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateDeNaissance = dateDeNaissance

        self.listeClient = []
        super().__init__(parent)
        # label Pour le titre
        label = ttk.Label(self, text="Ajout d'un Client", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10)

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
        self.numeroIdentification_label = tk.Label(self, text="Numéro d'identification")
        self.numeroIdentification_label.grid(row=8, column=0)

        # Champ pour le numéro d'identification
        self.numeroIdentification_entry = tk.Entry(self)
        self.numeroIdentification_entry.grid(row=8, column=1)

        # Label pour le sexe
        self.sexe_label = tk.Label(self, text="Sexe")
        self.sexe_label.grid(row=9, column=0)

        # Champ pour le sexe
        self.sexe_entry = tk.Entry(self)
        self.sexe_entry.grid(row=9, column=1)

        # Label pour la date de naissance
        self.date_label = tk.Label(self, text="Date de naissance")
        self.date_label.grid(row=10, column=0)

        # Champ pour la date de naissance
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=10, column=1)

        # listbox des clients
        self.listbox = tk.Listbox(self, width=50, height=10)
        self.listbox.grid(row=11, column=0, columnspan=2, pady=10)

        #Fonction qui permet de lire les données du fichier xml
        self.fonctionLireDonneesClientXml()

        # Bouton pour ajouter un client, et écrit dans le fichier xml
        button1 = ttk.Button(self, text="Ajouter", command=self.fonctionEcrireDonneesClientXml)
        button1.grid(row=12, column=0, columnspan=2, pady=10)

        
        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=12, column=1, columnspan=2, pady=10)

    #Fonction GetHashCode
    def GetHashCode(self):
        return hash(self.codePostal + self.telephone)

    #Fontion Equals
    def Equals(self, obj):
        if isinstance(obj, Client):
            return (self.nom == obj.nom and self.adresse == obj.adresse and self.ville == obj.ville
                    and self.province == obj.province and self.codePostal == obj.codePostal
                    and self.telephone == obj.telephone and self.courriel == obj.courriel)
        else:
            return False



    # Fonction toString pour la classe Client
    def toString(self):
        return f"Nom: {self.nom}\nAdresse: {self.adresse}\nVille: {self.ville}\nProvince: {self.province}\nCode Postal: {self.codePostal}\nTéléphone: {self.telephone}\nCourriel: {self.courriel}"

    #Foncton qui permet de lire les informations du fichier xml 
    def fonctionLireDonneesClientXml(self):
        for client in root.findall('client'):
            nom = client.find('nom').text
            adresse = client.find('adresse').text
            ville = client.find('ville').text
            province = client.find('province').text
            codePostal = client.find('codePostal').text
            telephone = client.find('telephone').text
            courriel = client.find('courriel').text
            numeroIdentification = client.find('numeroIdentification').text
            sexe = client.find('sexe').text
            dateDeNaissance = client.find('dateDeNaissance').text
            self.listeClient.append(client)
            self.listbox.insert(tk.END, nom+ " ")
            
        print(self.listeClient)

    #Foncton qui permet d'ajouter les informations d'un client dans le fichier xml 
    def fonctionEcrireDonneesClientXml(self):
        client = ET.SubElement(root, 'client')
        nom = ET.SubElement(client, 'nom')
        nom.text = self.nom_entry.get()
        adresse = ET.SubElement(client, 'adresse')
        adresse.text = self.addresse_entry.get()
        ville = ET.SubElement(client, 'ville')
        ville.text = self.ville_entry.get()
        province = ET.SubElement(client, 'province')
        province.text = self.province_entry.get()
        codePostal = ET.SubElement(client, 'codePostal')
        codePostal.text = self.postal_code_entry.get()
        telephone = ET.SubElement(client, 'telephone')
        telephone.text = self.telephone_entry.get()
        courriel = ET.SubElement(client, 'courriel')
        courriel.text = self.email_entry.get()
        numeroIdentification = ET.SubElement(client, 'numeroIdentification')
        numeroIdentification.text = self.numeroIdentification_entry.get()
        sexe = ET.SubElement(client, 'sexe')
        sexe.text = self.sexe_entry.get()
        dateDeNaissance = ET.SubElement(client, 'dateDeNaissance')
        dateDeNaissance.text = self.date_entry.get()
        print("Client ajouté")
        tree.write('donnees.xml')
        self.fonctionLireDonneesClientXml()
