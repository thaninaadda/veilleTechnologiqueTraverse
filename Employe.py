
import tkinter as tk;
import Personne;
class Employe(Personne):
    def __init__(self, nom, adresse, ville, province, codePostal, telephone, courriel, noEmploye, nAS,dateArret):
        super().__init__(nom, adresse, ville, province, codePostal, telephone, courriel)
        self.noEmploye = noEmploye
        self.nAS = nAS
        self.dateArret = dateArret

class EmployeeRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Formulaire d'inscription Personne:")

        # Label pour le nom
        self.name_label = tk.Label(master, text="Nom")
        self.name_label.grid(row=0, column=0)

        # Champ pour le nom
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        # Label pour l'adresse
        self.address_label = tk.Label(master, text="Adresse")
        self.address_label.grid(row=1, column=0)

        # Champ pour l'adresse
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=1, column=1)

        # Label pour la ville
        self.city_label = tk.Label(master, text="Ville")
        self.city_label.grid(row=2, column=0)

        # Champ pour la ville
        self.city_entry = tk.Entry(master)
        self.city_entry.grid(row=2, column=1)

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
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=5, column=1)

        # Label pour le courriel
        self.email_label = tk.Label(master, text="Courriel")
        self.email_label.grid(row=6, column=0)

        # Champ pour le courriel
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=6, column=1)

        # Label pour le noEmploye
        self.noEmp_label = tk.Label(master, text="noEmploye")
        self.noEmp_label.grid(row=6, column=0)

        # Champ pour le noEmploye
        self.noEmp_entry = tk.Entry(master)
        self.noEmp_entry.grid(row=6, column=1)


        # Label pour le nAS
        self.nas_label = tk.Label(master, text="nAS")
        self.nas_label.grid(row=6, column=0)

        # Champ pour le nAS
        self.nas_entry = tk.Entry(master)
        self.nas_entry.grid(row=6, column=1)

        # Label pour le dateArret
        self.dateStop_label = tk.Label(master, text="dateArret")
        self.dateStop_label.grid(row=6, column=0)

        # Champ pour le dateArret
        self.dateStop_entry = tk.Entry(master)
        self.dateStop_entry.grid(row=6, column=1)

        # Bouton de soumission
        self.submit_button = tk.Button(master, text="S'inscrire", command=self.submit)
        self.submit_button.grid(row=7, column=0, columnspan=2)

    def submit(self):
        # Récupérer les valeurs du formulaire
        name = self.name_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        province = self.province_entry.get()
        postal_code = self.postal_code_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        noEmp = self.noEmp_entry.get()
        nas = self.nas_entry.get()
        dateStop= self.dateStop_entry.get()

        # Afficher les valeurs dans la console
        print(f"Nom: {name}")
        print(f"Adresse: {address}")
        print(f"Ville: {city}")
        print(f"Province: {province}")
        print(f"Code postal: {postal_code}")
        print(f"Téléphone: {phone}")
        print(f"Courriel: {email}")
        print(f"no employee: {noEmp}")
        print(f"Numero assurance social : {nas}")
        print(f"date de demission: {dateStop}")


if __name__ == "__main__":
    root = tk.Tk()
    form = EmployeeRegistrationForm(root)
    root.mainloop()