#
# Nom du Fichier : tkinterApp.py
# Auteur: Thanina Adda
# But: contient toutes les interfaces.
#
#
import tkinter as tk
from tkinter import ttk
from Vehicule import Vehicule 
from Traverse import Traverse 
# represente la police choisit pour le projet .
LARGEFONT =("Verdana", 20)

# Classe tkinterApp, cette classe appel la page Principale au debut du programme.
class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Traverse, Traversier, TypeTraverse, Client, Employe, Vehicule):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        # démarrage de la page StartPage
        self.pageDemarrage()

    def pageDemarrage(self):
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

                
# Page StartPage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
       
        tk.Frame.__init__(self, parent)
	
    
		# Titre du Projet.
        label = ttk.Label(self, text="projet Traverse", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

		# Bouton Type Traverse qui appel justement la page Type Traverse.
        button1 = ttk.Button(self, text="Type Traverse",
                             command=lambda: controller.show_frame(TypeTraverse))
        button1.grid(row=1, column=6, padx=10, pady=10)

        # Bouton Type Traverse qui appel justement la page Vehicule.
        button2 = ttk.Button(self, text="Vehicule",
                             command=lambda: controller.show_frame(Vehicule))
        button2.grid(row=2, column=6, padx=10, pady=10)
        
        # Bouton Type Traverse qui appel justement la page Traverse.
        button3 = ttk.Button(self, text="Traverse",
                             command=lambda: controller.show_frame(Traverse))
        button3.grid(row=3, column=6, padx=10, pady=10)
        
        # Bouton Type Traverse qui appel justement la page Client.
        button4 = ttk.Button(self, text="Client",
                             command=lambda: controller.show_frame(Client))
        button4.grid(row=4, column=6, padx=10, pady=10)

        # Bouton Type Traverse qui appel justement la page Employee.
        button5 = ttk.Button(self, text="Employee",
                             command=lambda: controller.show_frame(Employe))
        button5.grid(row=5, column=6, padx=10, pady=10)

        # Bouton Type Traverse qui appel justement la page Traversier.
        button6 = ttk.Button(self, text="Traversier",
                             command=lambda: controller.show_frame(Traversier))
        button6.grid(row=6, column=6, padx=10, pady=10)

class Traversier(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label pour le titre
        label = ttk.Label(self, text="Ajout d'un Traversier", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Label pour le Nom du Traversier
        self.nom_label = tk.Label(self, text="Nom du traversier")
        self.nom_label.grid(row=1, column=0)

        # Champ pour le Nom du Traversier
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=1, column=1)

        # Label pour la Capacite du Vehicule
        self.capaciteVehicule_label = tk.Label(self, text="Capacite du vehicule")
        self.capaciteVehicule_label.grid(row=2, column=0)

        # Champ pour la Capacite du Vehicule
        self.capaciteVehicule_entry = tk.Entry(self)
        self.capaciteVehicule_entry.grid(row=2, column=1)

        # Label pour la Capacite en Personne de Depart
        self.capacitePersonneDepart_label = tk.Label(self, text="Capacite en personne")
        self.capacitePersonneDepart_label.grid(row=3, column=0)

        # Champ pour la Capacite en Personne de Depart
        self.capacitePersonneDepart_entry = tk.Entry(self)
        self.capacitePersonneDepart_entry.grid(row=3, column=1)

        # Label pour l'Annee De Fabrication
        self.anneeFabrication_label = tk.Label(self, text="Annee de fabrication")
        self.anneeFabrication_label.grid(row=4, column=0)

        # Champ pour l'Annee De Fabrication
        self.anneeFabrication_entry = tk.Entry(self)
        self.anneeFabrication_entry.grid(row=4, column=1)

        # Label pour la Date De Mise en Service
        self.dateMiseService_label = tk.Label(self, text="Date de mise en service")
        self.dateMiseService_label.grid(row=5, column=0)

        # Champ pour la Date De Mise en Service
        self.dateMiseService_entry = tk.Entry(self)
        self.dateMiseService_entry.grid(row=5, column=1)

        # Bouton Pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=6, column=1, pady=10)

        # Bouton Pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Ajout", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=6, column=0, pady=10)

        

        
        
class Employe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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

        # Bouton pour revenir à la page StartPage
        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=8, column=0, padx=10, pady=10)

        # Bouton pour aller à la page Client
        button3 = ttk.Button(self, text="Client",
                             command=lambda: controller.show_frame(Client))
        button3.grid(row=8, column=1, padx=10, pady=10)


#Page Client
class Client(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label pour le titre de la page
        label = ttk.Label(self, text="Ajout d'un Client", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

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
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=8, column=0, padx=10, pady=10)

        # Bouton pour Aller a la page Employee
        button4 = ttk.Button(self, text="Employe",
                             command=lambda: controller.show_frame(Employe))
        button4.grid(row=8, column=1, padx=10, pady=10)

   
        
 #Page Type Traversier
class TypeTraverse(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label pour le titre Type Traversier
        label = ttk.Label(self, text="Ajout d'un type de traverse", font=LARGEFONT)
        label.grid(row=0, column=0, columnspan=2, pady=10) # correction de la ligne du label

        # Label pour le nom du type
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(row=1, column=0)
        
        # Champ pour le no Traverse
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=1, column=1)

        # Label pour le no Traverse
        self.nombreRoue_label = tk.Label(self, text="Nombre de roue")
        self.nombreRoue_label.grid(row=2, column=0)

        # Champ pour le no Traverse
        self.nombreRoue_entry = tk.Entry(self)
        self.nombreRoue_entry.grid(row=2, column=1)

        # Label pour la date et Heure
        self.prixTraverse_label = tk.Label(self, text="prix")
        self.prixTraverse_label.grid(row=3, column=0)

        # Champ pour le no Traverse
        self.prixTraverse_entry = tk.Entry(self)
        self.prixTraverse_entry.grid(row=3, column=1)
        
        # Bouton pour revenir a la page StartPage
        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=4, column=0, columnspan=2, pady=10)



# Driver Code
app = tkinterApp()
app.mainloop()

