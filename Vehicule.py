import tkinter as tk

class Vehicle:
    def __init__(self, noIdentification, marque, modele, couleur, annee, immatriculation):

        self.noIdentification = noIdentification
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.immatriculation = immatriculation

class VehicleRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Formulaire d'inscription de véhicule")

        # Label pour le numéro d'identification
        self.noIdentification_label = tk.Label(master, text="Numéro d'identification")
        self.noIdentification_label.grid(row=0, column=0)

        # Champ pour le numéro d'identification
        self.noIdentification_entry = tk.Entry(master)
        self.noIdentification_entry.grid(row=0, column=1)

        # Label pour la marque
        self.marque_label = tk.Label(master, text="Marque")
        self.marque_label.grid(row=1, column=0)

        # Champ pour la marque
        self.marque_entry = tk.Entry(master)
        self.marque_entry.grid(row=1, column=1)

        # Label pour le modèle
        self.modele_label = tk.Label(master, text="Modèle")
        self.modele_label.grid(row=2, column=0)

        # Champ pour le modèle
        self.modele_entry = tk.Entry(master)
        self.modele_entry.grid(row=2, column=1)

        # Label pour la couleur
        self.couleur_label = tk.Label(master, text="Couleur")
        self.couleur_label.grid(row=3, column=0)

        # Champ pour la couleur
        self.couleur_entry = tk.Entry(master)
        self.couleur_entry.grid(row=3, column=1)

        # Label pour l'année
        self.annee_label = tk.Label(master, text="Année")
        self.annee_label.grid(row=4, column=0)

        # Champ pour l'année
        self.annee_entry = tk.Entry(master)
        self.annee_entry.grid(row=4, column=1)

        # Label pour l'immatriculation
        self.immatriculation_label = tk.Label(master, text="Immatriculation")
        self.immatriculation_label.grid(row=5, column=0)

        # Champ pour l'immatriculation
        self.immatriculation_entry = tk.Entry(master)
        self.immatriculation_entry.grid(row=5, column=1)

        # Bouton de soumission
        self.submit_button = tk.Button(master, text="S'inscrire", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2)

    def submit(self):
        # Récupérer les valeurs du formulaire
        noIdentification = self.noIdentification_entry.get()
        marque = self.marque_entry.get()
        modele = self.modele_entry.get()
        couleur = self.couleur_entry.get()
        annee = self.annee_entry.get()
        immatriculation = self.immatriculation_entry.get()

        # Créer une instance de la classe Vehicle avec les valeurs du formulaire
        vehicle = Vehicle(noIdentification, marque, modele, couleur, annee, immatriculation)

        # Afficher les valeurs du formulaire dans la console
        print(f"Numéro d'identification:, {noIdentification}")
        print(f"Marque:, {marque}")
        print(f"Modèle:, {modele}")
        print(f"Couleur:, {couleur}")
        print(f"Annee:, {annee}")
        print(f"immatriculation:, {immatriculation}")
       


if __name__ == "__main__":
        root = tk.Tk()
        form = VehicleRegistrationForm(root)
        root.mainloop()
