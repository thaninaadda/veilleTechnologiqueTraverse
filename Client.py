class Client:
    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel
        self.numeroIdentification : numeroIdentification
        self.sexe= sexe
        self.dateDeNaissance= dateDeNaissance


        def GetHashCode(self):
        return hash(self.codePostal + self.telephone)


        def Equals(self, obj):
        if isinstance(obj, Client):
            return (self.nom == obj.nom and self.adresse == obj.adresse and self.ville == obj.ville
                    and self.province == obj.province and self.codePostal == obj.codePostal
                    and self.telephone == obj.telephone and self.courriel == obj.courriel)
        else:
            return False


        def ToString(self):
        return f"Nom: {self.nom}, 
                Adresse: {self.adresse}, 
                Ville: {self.ville}, 
                Province: {self.province}, 
                Code Postal: {self.codePostal}, 
                Telephone: {self.telephone}, 
                Courriel: {self.courriel}"