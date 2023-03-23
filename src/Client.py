
#
# Nom du Fichier : Client.py
# Auteur: Thanina Adda
# But: contient la classe Personne
#
#
import tkinter as tk;
import src.Personne as Personne;
from tkinter import ttk
LARGEFONT =("Verdana", 20)
class Client(tk.Frame):
    def __init__(self, parent, controleur, nom="", adresse="", ville="", province="", 
                 codePostal="", telephone="", courriel="", numeroIdentification="", sexe="",dateDeNaissance=""):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateDeNaissance = dateDeNaissance

        super().__init__(parent)
    # label Pour le titre
        label = ttk.Label(self, text="Ajout d'un Employe", font=LARGEFONT)
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

        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                        command=lambda: controleur.pageDemarrage())
        button2.grid(row=6, column=0, columnspan=2, pady=10)


    def GetHashCode(self):
        return hash(self.codePostal + self.telephone)


    def Equals(self, obj):
        if isinstance(obj, Client):
            return (self.nom == obj.nom and self.adresse == obj.adresse and self.ville == obj.ville
                    and self.province == obj.province and self.codePostal == obj.codePostal
                    and self.telephone == obj.telephone and self.courriel == obj.courriel)
        else:
            return False


 