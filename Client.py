class Client:
    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel):
        self.nom = nom
        self.adresse = adresse
        self.ville = ville
        self.province = province
        self.codePostal = codePostal
        self.telephone = telephone
        self.courriel = courriel


        def GetHashCode(self):
        return hash(self.codePostal + self.telephone)