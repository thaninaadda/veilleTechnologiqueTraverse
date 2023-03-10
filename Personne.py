
import tkinter as tk
class Personne:
    def __init__(self, nom, addresse, ville, province, postal_code, telephone, email):
        self.nom = nom
        self.addresse = addresse
        self.ville = ville
        self.province = province
        self.postal_code = postal_code
        self.telephone = telephone
        self.email = email

class UserRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Formulaire d'inscription Personne:")

        # Label pour le nom
        self.nom_label = tk.Label(master, text="Nom")
        self.nom_label.grid(row=0, column=0)

        # Champ pour le nom
        self.nom_entry = tk.Entry(master)
        self.nom_entry.grid(row=0, column=1)

        # Label pour l'adresse
        self.addresse_label = tk.Label(master, text="Adresse")
        self.addresse_label.grid(row=1, column=0)

        # Champ pour l'adresse
        self.addresse_entry = tk.Entry(master)
        self.addresse_entry.grid(row=1, column=1)

        # Label pour la ville
        self.ville_label = tk.Label(master, text="Ville")
        self.ville_label.grid(row=2, column=0)

        # Champ pour la ville
        self.ville_entry = tk.Entry(master)
        self.ville_entry.grid(row=2, column=1)

        # Label pour la province
        self.province_label = tk.Label(master, text="Province")
        self.province_label.grid(row=3, column=0)

        # Champ pour la province
        self.province_entry = tk.Entry(master)
        self.province_entry.grid(row=3, column=1)

        # Label pour le code postal
        self.postal_code_label = tk.Label(master, text="Code postal")
        self.postal_code_label.grid(row=4, column=0)

        # Champ pour le code postal
        self.postal_code_entry = tk.Entry(master)
        self.postal_code_entry.grid(row=4, column=1)

        # Label pour le téléphone
        self.phone_label = tk.Label(master, text="Téléphone")
        self.phone_label.grid(row=5, column=0)

        # Champ pour le téléphone
        self.telephone_entry = tk.Entry(master)
        self.telephone_entry.grid(row=5, column=1)

        # Label pour le courriel
        self.email_label = tk.Label(master, text="Courriel")
        self.email_label.grid(row=6, column=0)

        # Champ pour le courriel
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=6, column=1)

        # Bouton de soumission
        self.submit_button = tk.Button(master, text="S'inscrire", command=self.submit)
        self.submit_button.grid(row=7, column=0, columnspan=2)

    def submit(self):
        # Récupérer les valeurs du formulaire
        nom = self.nom_entry.get()
        addresse = self.addresse_entry.get()
        ville = self.ville_entry.get()
        province = self.province_entry.get()
        postal_code = self.postal_code_entry.get()
        telephone = self.telephone_entry.get()
        email = self.email_entry.get()

        # Créer une instance de la classe Perosnne avec les valeurs du formulaire
        personne = Personne(nom, addresse, ville, province, postal_code, telephone,email)
        # Afficher les valeurs dans la console
        print(f"Nom: {nom}")
        print(f"Adresse: {addresse}")
        print(f"Ville: {ville}")
        print(f"Province: {province}")
        print(f"Code postal: {postal_code}")
        print(f"Téléphone: {telephone}")
        print(f"Courriel: {email}")


if __name__ == "__main__":
    root = tk.Tk()
    form = UserRegistrationForm(root)
    root.mainloop()


   