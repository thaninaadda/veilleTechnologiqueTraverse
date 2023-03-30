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
from Traversier import Traversier 
from Type import Type
from Client import Client
from Employe import Employe
# from Personne import Personne


# represente la police choisit pour le projet .
LARGEFONT =("Verdana", 20)

# Classe tkinterApp, cette classe appel la page Principale au debut du programme.
class GestionTraverse(tk.Tk):
    
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
        for F in (StartPage,Type,Vehicule,Traverse,Client,Employe,Traversier):

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
                             command=lambda: controller.show_frame(Type))
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

# Driver Code
app = GestionTraverse()
app.mainloop()

