
#
# Nom du Fichier : Client.py
# Auteur: Thanina Adda
# But: contient la classe Personne
#
#
import tkinter as tk;
import src.Personne as Personne;
class Client(Personne):
    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel, numeroIdentification, sexe,dateDeNaissance):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe
        self.dateDeNaissance = dateDeNaissance


    def GetHashCode(self):
        return hash(self.codePostal + self.telephone)


    def Equals(self, obj):
        if isinstance(obj, Client):
            return (self.nom == obj.nom and self.adresse == obj.adresse and self.ville == obj.ville
                    and self.province == obj.province and self.codePostal == obj.codePostal
                    and self.telephone == obj.telephone and self.courriel == obj.courriel)
        else:
            return False


 