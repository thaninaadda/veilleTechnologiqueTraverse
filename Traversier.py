import tkinter as tk

class Traversier:
    def __init__(self, noTraverse, dateHeure, villeDepart, employeInscription, listeVehicule, listeClient):

        self.noTraverse = noTraverse
        self.dateHeure = dateHeure
        self.villeDepart = villeDepart
        self.employeInscription = employeInscription
        self.listeVehicule = listeVehicule or []
        self.listeClient = listeClient or []

class TraversierRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Formulaire d'inscription d'un traversier")

        # Label pour le no Traverse
        self.noTraverse_label = tk.Label(master, text="Numéro d'identification")
        self.noTraverse_label.grid(row=0, column=0)

        # Champ pour le no Traverse
        self.noTraverse_entry = tk.Entry(master)
        self.noTraverse_entry.grid(row=0, column=1)

        # Label pour la date et Heure
        self.dateHeure_label = tk.Label(master, text="date et heure")
        self.dateHeure_label.grid(row=1, column=0)

        # Champ pour la date et Heure
        self.dateHeure_entry = tk.Entry(master)
        self.dateHeure_entry.grid(row=1, column=1)

        # Label pour le ville de Depart
        self.villeDepart_label = tk.Label(master, text="ville de Depart")
        self.villeDepart_label.grid(row=2, column=0)

        # Champ pour le ville de Depart
        self.villeDepart_entry = tk.Entry(master)
        self.villeDepart_entry.grid(row=2, column=1)

        # Label pour l'employe Inscription
        self.employeInscription_label = tk.Label(master, text="employe Inscription")
        self.employeInscription_label.grid(row=3, column=0)

        # Champ pour l'employe Inscription
        self.employeInscription_entry = tk.Entry(master)
        self.employeInscription_entry.grid(row=3, column=1)


        # Bouton de soumission
        self.submit_button = tk.Button(master, text="S'inscrire", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2)

    def submit(self):
        
        # Récupérer les valeurs du formulaire
        noTraverse = self.noTraverse_entry.get()
        dateHeure = self.dateHeure_entry.get()
        villeDepart = self.villeDepart_entry.get()
        employeInscription= self.employeInscription_entry.get()
       

        # Créer une instance de la classe Vehicle avec les valeurs du formulaire
        traversier = Traversier(noTraverse, dateHeure, villeDepart, employeInscription)

        # Afficher les valeurs du formulaire dans la console
        print(f"Numéro de traverse:, {noTraverse}")
        print(f"date et Heure:, {dateHeure}")
        print(f"ville de Depart:, {villeDepart}")
        print(f"employe Inscription:, {employeInscription}")
    
    

if __name__ == "__main__":
        root = tk.Tk()
        form = TraversierRegistrationForm(root)
        root.mainloop()
