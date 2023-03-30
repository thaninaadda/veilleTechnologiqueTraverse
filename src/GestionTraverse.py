#
# Nom du Fichier : GestionTraverse.py
# Auteur: Thanina Adda
# But: Permet de faire appel aux autres classes et aux intérfaces pour pouvoir ajouter des clients, Employés et véhicules.
#
#
import tkinter as tk
from tkinter import ttk
from Vehicule import Vehicule 
from Traverse import Traverse 
from Traversier import Traversier 
from Type import Type
from Client import Client
from Employe import Employe



# Représente la police choisit pour le projet .
LARGEFONT =("Verdana", 20)

# Classe GestionTraverse, cette classe appel la page Principale au debut du programme.
class GestionTraverse(tk.Tk):
    
    # __init__ function de la classe GestionTraverse
    def __init__(self, *args, **kwargs):
        # __init__ function  de la classe Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Création du container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Intialisation du frame
        self.frames = {}

        for F in (StartPage,Type,Vehicule,Traverse,Client,Employe,Traversier):

            frame = F(container, self)

            # appel des pages 
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        # démarrage de la page StartPage
        self.pageDemarrage()

    #Ouverture de la page StartPage
    def pageDemarrage(self):
        self.show_frame(StartPage)

    
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

		# Bouton Type Traverse qui appel la page Type Traverse.
        button1 = ttk.Button(self, text="Type Traverse",
                             command=lambda: controller.show_frame(Type))
        button1.grid(row=1, column=6, padx=10, pady=10)

        # Bouton Type Traverse qui appel la page Véhicule.
        button2 = ttk.Button(self, text="Véhicule",
                             command=lambda: controller.show_frame(Vehicule))
        button2.grid(row=2, column=6, padx=10, pady=10)
        
        # Bouton Type Traverse qui appel la page Traverse.
        button3 = ttk.Button(self, text="Traverse",
                             command=lambda: controller.show_frame(Traverse))
        button3.grid(row=3, column=6, padx=10, pady=10)
        
        # Bouton Type Traverse qui appel la page Client.
        button4 = ttk.Button(self, text="Client",
                             command=lambda: controller.show_frame(Client))
        button4.grid(row=4, column=6, padx=10, pady=10)

        # Bouton Type Traverse qui appel la page Employés.
        button5 = ttk.Button(self, text="Employés",
                             command=lambda: controller.show_frame(Employe))
        button5.grid(row=5, column=6, padx=10, pady=10)

        # Bouton Type Traverse qui appel la page Traversier.
        button6 = ttk.Button(self, text="Traversier",
                             command=lambda: controller.show_frame(Traversier))
        button6.grid(row=6, column=6, padx=10, pady=10)


app = GestionTraverse()
app.mainloop()

