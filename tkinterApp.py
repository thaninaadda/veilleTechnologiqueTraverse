import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 20)

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
		for F in (StartPage,Traverse,Traversier,TypeTraverse, Client, Employe,Vehicule):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame
			

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		
        label = ttk.Label(self, text="projet Traverse", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Type Traverse",
                             command=lambda: controller.show_frame(TypeTraverse))
        button1.grid(row=1, column=6, padx=10, pady=10)
        
        button2 = ttk.Button(self, text="Vehicule",
                             command=lambda: controller.show_frame(Vehicule))
        button2.grid(row=2, column=6, padx=10, pady=10)
        
        button3 = ttk.Button(self, text="Traverse",
                             command=lambda: controller.show_frame(Traverse))
        button3.grid(row=3, column=6, padx=10, pady=10)
        
        button4 = ttk.Button(self, text="Client",
                             command=lambda: controller.show_frame(Client))
        button4.grid(row=4, column=6, padx=10, pady=10)
        
        button5 = ttk.Button(self, text="Employee",
                             command=lambda: controller.show_frame(Employe))
        button5.grid(row=5, column=6, padx=10, pady=10)
        
        button6 = ttk.Button(self, text="Traversier",
                             command=lambda: controller.show_frame(Traversier))
        button6.grid(row=6, column=6, padx=10, pady=10)

   
class Traversier(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un Traversier", font=LARGEFONT)
		# Label pour le no Traverse
        self.nom_label = tk.Label(self, text="nom traversier")
        self.nom_label.grid(row=0, column=0)

        # Champ pour le no Traverse
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=0, column=1)

        # Label pour la date et Heure
        self.capaciteVehicule_label = tk.Label(self, text="capacite du Vehicule")
        self.capaciteVehicule_label.grid(row=1, column=0)

        # Champ pour la date et Heure
        self.capaciteVehicule_entry = tk.Entry(self)
        self.capaciteVehicule_entry.grid(row=1, column=1)

        # Label pour le capacitePersonne de Depart
        self.capacitePersonneDepart_label = tk.Label(self, text="capacite en Personne ")
        self.capacitePersonneDepart_label.grid(row=2, column=0)

        # Champ pour le capacitePersonne de Depart
        self.capacitePersonneDepart_entry = tk.Entry(self)
        self.capacitePersonneDepart_entry.grid(row=2, column=1)

        # Label pour l'employe Inscription
        self.anneeFabrication_label = tk.Label(self, text="annee Fabrication")
        self.anneeFabrication_label.grid(row=3, column=0)

        # Champ pour l'annee de Fabrication
        self.anneeFabrication_entry = tk.Entry(self)
        self.anneeFabrication_entry.grid(row=3, column=1)

         # Label pour l'employe Inscription
        self.dateMiseService_label = tk.Label(self, text="date Mise Service")
        self.dateMiseService_label.grid(row=3, column=0)

        # Champ pour l'employe Inscription
        self.dateMiseService_entry = tk.Entry(self)
        self.dateMiseService_entry.grid(row=3, column=1)


        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)


        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=6, padx=10, pady=10)
        

class Traverse(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'une Traverse", font=LARGEFONT)
        # Label pour le nom du type
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(row=0, column=0)

		# Label pour le no Traverse
        self.noTraverse_label = tk.Label(self, text="Numéro d'identification")
        self.noTraverse_label.grid(row=0, column=0)

        # Champ pour le no Traverse
        self.noTraverse_entry = tk.Entry(self)
        self.noTraverse_entry.grid(row=0, column=1)

        # Label pour la date et Heure
        self.dateHeure_label = tk.Label(self, text="date et heure")
        self.dateHeure_label.grid(row=1, column=0)

        # Champ pour la date et Heure
        self.dateHeure_entry = tk.Entry(self)
        self.dateHeure_entry.grid(row=1, column=1)

        # Label pour le ville de Depart
        self.villeDepart_label = tk.Label(self, text="ville de Depart")
        self.villeDepart_label.grid(row=2, column=0)

        # Champ pour le ville de Depart
        self.villeDepart_entry = tk.Entry(self)
        self.villeDepart_entry.grid(row=2, column=1)

        # Label pour l'employe Inscription
        self.employeInscription_label = tk.Label(self, text="employe Inscription")
        self.employeInscription_label.grid(row=3, column=0)

        # Champ pour l'employe Inscription
        self.employeInscription_entry = tk.Entry(self)
        self.employeInscription_entry.grid(row=3, column=1)

        label.grid(row=0, column=4, padx=10, pady=10)


        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=6, padx=10, pady=10)
        

class Employe(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un Employe", font=LARGEFONT)

        # Label pour le nom
        self.nom_label = tk.Label(self, text="Nom")
        self.nom_label.grid(row=0, column=0)

        # Champ pour le nom
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=0, column=1)

        # Label pour l'adresse
        self.addresse_label = tk.Label(self, text="Adresse")
        self.addresse_label.grid(row=1, column=0)

        # Champ pour l'adresse
        self.addresse_entry = tk.Entry(self)
        self.addresse_entry.grid(row=1, column=1)

        # Label pour la ville
        self.ville_label = tk.Label(self, text="Ville")
        self.ville_label.grid(row=2, column=0)

        # Champ pour la ville
        self.ville_entry = tk.Entry(self)
        self.ville_entry.grid(row=2, column=1)

        # Label pour la province
        self.province_label = tk.Label(self, text="Province")
        self.province_label.grid(row=3, column=0)

        # Champ pour la province
        self.province_entry = tk.Entry(self)
        self.province_entry.grid(row=3, column=1)

        # Label pour le code postal
        self.postal_code_label = tk.Label(self, text="Code postal")
        self.postal_code_label.grid(row=4, column=0)

        # Champ pour le code postal
        self.postal_code_entry = tk.Entry(self)
        self.postal_code_entry.grid(row=4, column=1)

        # Label pour le téléphone
        self.phone_label = tk.Label(self, text="Téléphone")
        self.phone_label.grid(row=5, column=0)

        # Champ pour le téléphone
        self.telephone_entry = tk.Entry(self)
        self.telephone_entry.grid(row=5, column=1)

        # Label pour le courriel
        self.email_label = tk.Label(self, text="Courriel")
        self.email_label.grid(row=6, column=0)

        # Champ pour le courriel
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=6, column=1)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)


        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=6, padx=10, pady=10)

        button3 = ttk.Button(self, text="Client",
                             command=lambda: controller.show_frame(Client))
        button3.grid(row=3, column=6, padx=10, pady=10)

class Client(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un Client", font=LARGEFONT)

        # Label pour le nom
        self.nom_label = tk.Label(self, text="Nom")
        self.nom_label.grid(row=0, column=0)

        # Champ pour le nom
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=0, column=1)

        # Label pour l'adresse
        self.addresse_label = tk.Label(self, text="Adresse")
        self.addresse_label.grid(row=1, column=0)

        # Champ pour l'adresse
        self.addresse_entry = tk.Entry(self)
        self.addresse_entry.grid(row=1, column=1)

        # Label pour la ville
        self.ville_label = tk.Label(self, text="Ville")
        self.ville_label.grid(row=2, column=0)

        # Champ pour la ville
        self.ville_entry = tk.Entry(self)
        self.ville_entry.grid(row=2, column=1)

        # Label pour la province
        self.province_label = tk.Label(self, text="Province")
        self.province_label.grid(row=3, column=0)

        # Champ pour la province
        self.province_entry = tk.Entry(self)
        self.province_entry.grid(row=3, column=1)

        # Label pour le code postal
        self.postal_code_label = tk.Label(self, text="Code postal")
        self.postal_code_label.grid(row=4, column=0)

        # Champ pour le code postal
        self.postal_code_entry = tk.Entry(self)
        self.postal_code_entry.grid(row=4, column=1)

        # Label pour le téléphone
        self.phone_label = tk.Label(self, text="Téléphone")
        self.phone_label.grid(row=5, column=0)

        # Champ pour le téléphone
        self.telephone_entry = tk.Entry(self)
        self.telephone_entry.grid(row=5, column=1)

        # Label pour le courriel
        self.email_label = tk.Label(self, text="Courriel")
        self.email_label.grid(row=6, column=0)

        # Champ pour le courriel
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=6, column=1)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)


        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=6, padx=10, pady=10)

        button4 = ttk.Button(self, text="Employe",
                             command=lambda: controller.show_frame(Employe))
        button4.grid(row=3, column=6, padx=10, pady=10)
        

class TypeTraverse(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un type de traverse", font=LARGEFONT)
        # Label pour le nom du type
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(row=0, column=0)
        
		 # Champ pour le no Traverse
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=0, column=1)
		# Label pour le no Traverse
        self.nombreRoue_label = tk.Label(self, text="Nombre de roue")
        self.nombreRoue_label.grid(row=1, column=0)

        # Champ pour le no Traverse
        self.nombreRoue_entry = tk.Entry(self)
        self.nombreRoue_entry.grid(row=1, column=1)

        # Label pour la date et Heure
        self.prixTraverse_label = tk.Label(self, text="prix")
        self.prixTraverse_label.grid(row=2, column=0)

		# Champ pour le no Traverse
        self.prixTraverse_entry = tk.Entry(self)
        self.prixTraverse_entry.grid(row=2, column=1)
        
        label.grid(row=0, column=4, padx=10, pady=10)


        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=6, padx=10, pady=10)


class Vehicule(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un Vehicule", font=LARGEFONT)
        # Label pour le nom du type
        self.nom_label = ttk.Label(self, text="Nom:")
        self.nom_label.grid(row=0, column=0)
        # Champ pour le nom du type
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=0, column=1)
        # Label pour le nombre Roue
        self.nombreRoue_label = tk.Label(self, text="le nombre de Roue:")
        self.nombreRoue_label.grid(row=1, column=0)
        # Champ pour le nombre Roue
        self.nombreRoue_entry = tk.Entry(self)
        self.nombreRoue_entry.grid(row=1, column=1)
        # Label pour le prix de Traverse
        self.prixTraverse_label = tk.Label(self, text="le prix de Traverse:")
        self.prixTraverse_label.grid(row=2, column=0)
        # Champ pour le prix de Traverse
        self.prixTraverse_entry = tk.Entry(self)
        self.prixTraverse_entry.grid(row=2, column=1)
	
        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)
        
		
        button2 = ttk.Button(self, text="Retour",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=6, padx=10, pady=10)

# Driver Code
app = tkinterApp()
app.mainloop()

