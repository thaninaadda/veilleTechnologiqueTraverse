import tkinter as tk

class Type:
    def __init__(self, nom, nombreRoue, prixTraverse,):

        self.nom = nom
        self.nombreRoue = nombreRoue
        self.prixTraverse = prixTraverse

class TypeRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Formulaire d'inscription d'un type")

        # Label pour le nom du type
        self.nom_label = tk.Label(master, text="Nom:")
        self.nom_label.grid(row=0, column=0)

        # Champ pour le nom du type
        self.nom_entry = tk.Entry(master)
        self.nom_entry.grid(row=0, column=1)

        # Label pour le nombre Roue
        self.nombreRoue_label = tk.Label(master, text="le nombre de Roue:")
        self.nombreRoue_label.grid(row=1, column=0)

        # Champ pour le nombre Roue
        self.nombreRoue_entry = tk.Entry(master)
        self.nombreRoue_entry.grid(row=1, column=1)

        # Label pour le prix de Traverse
        self.prixTraverse_label = tk.Label(master, text="le prix de Traverse:")
        self.prixTraverse_label.grid(row=2, column=0)

        # Champ pour le prix de Traverse
        self.prixTraverse_entry = tk.Entry(master)
        self.prixTraverse_entry.grid(row=2, column=1)

    
        # Bouton de soumission
        self.submit_button = tk.Button(master, text="S'inscrire", command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=2)

    def submit(self):
        
        # Récupérer les valeurs du formulaire

        nom = self.nom_entry.get()
        nombreRoue = self.nombreRoue_entry.get()
        prixTraverse = self.prixTraverse_entry.get()
        
       

        # Créer une instance de la classe Vehicle avec les valeurs du formulaire
        type = Type(nom, nombreRoue, prixTraverse)

        # Afficher les valeurs du formulaire dans la console
        print(f"Nom:, {nom}")
        print(f"nombre de Roue:, {nombreRoue}")
        print(f"prix de la Traverse:, {prixTraverse}")
    
    
    

if __name__ == "__main__":
        root = tk.Tk()
        form = TypeRegistrationForm(root)
        root.mainloop()
