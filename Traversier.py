import tkinter as tk

class Traversier:
    def __init__(self, nom,capaciteVehicule,capacitePersonne,anneeFabrication,dateMiseService,listeEmploye):

        self.nom = nom
        self.capaciteVehicule = capaciteVehicule
        self.capacitePersonne = capacitePersonne
        self.anneeFabrication = anneeFabrication
        self.dateMiseService = dateMiseService 
        self.listeEmploye = listeEmploye or []

class TraversierRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Formulaire d'inscription d'un traversier")

        # Label pour le no Traverse
        self.nom_label = tk.Label(master, text="nom traversier")
        self.nom_label.grid(row=0, column=0)

        # Champ pour le no Traverse
        self.nom_entry = tk.Entry(master)
        self.nom_entry.grid(row=0, column=1)

        # Label pour la date et Heure
        self.capaciteVehicule_label = tk.Label(master, text="capacite du Vehicule")
        self.capaciteVehicule_label.grid(row=1, column=0)

        # Champ pour la date et Heure
        self.capaciteVehicule_entry = tk.Entry(master)
        self.capaciteVehicule_entry.grid(row=1, column=1)

        # Label pour le capacitePersonne de Depart
        self.capacitePersonneDepart_label = tk.Label(master, text="capacite en Personne ")
        self.capacitePersonneDepart_label.grid(row=2, column=0)

        # Champ pour le capacitePersonne de Depart
        self.capacitePersonneDepart_entry = tk.Entry(master)
        self.capacitePersonneDepart_entry.grid(row=2, column=1)

        # Label pour l'employe Inscription
        self.anneeFabrication_label = tk.Label(master, text="annee Fabrication")
        self.anneeFabrication_label.grid(row=3, column=0)

        # Champ pour l'annee de Fabrication
        self.anneeFabrication_entry = tk.Entry(master)
        self.anneeFabrication_entry.grid(row=3, column=1)

         # Label pour l'employe Inscription
        self.dateMiseService_label = tk.Label(master, text="date Mise Service")
        self.dateMiseService_label.grid(row=3, column=0)

        # Champ pour l'employe Inscription
        self.dateMiseService_entry = tk.Entry(master)
        self.dateMiseService_entry.grid(row=3, column=1)

        # Bouton de soumission
        self.submit_button = tk.Button(master, text="S'inscrire", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2)

    def submit(self):
        
        # Récupérer les valeurs du formulaire
        nom = self.nom_entry.get()
        capaciteVehicule = self.capaciteVehicule_entry.get()
        capacitePersonneDepart = self.capacitePersonneDepart_entry.get()
        anneeFabrication= self.anneeFabrication_entry.get()
        dateMiseService= self.dateMiseService_entry.get()
       

        # Créer une instance de la classe Vehicle avec les valeurs du formulaire
        traversier = Traversier(nom, capaciteVehicule, capacitePersonneDepart, anneeFabrication, dateMiseService)

        # Afficher les valeurs du formulaire dans la console
        print(f"Numéro de traverse:, {nom}")
        print(f"date et Heure:, {capaciteVehicule}")
        print(f"capacitePersonne de Depart:, {capacitePersonneDepart}")
        print(f"annee de Fabrication:, {anneeFabrication}")
        print(f"employe Inscription:, {dateMiseService}")
    
    

if __name__ == "__main__":
        root = tk.Tk()
        form = TraversierRegistrationForm(root)
        root.mainloop()
