import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

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
		for F in (StartPage, StartPage3, StartPage4 ,StartPage2):

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

        button2 = ttk.Button(self, text="StartPage2",
                             command=lambda: controller.show_frame(StartPage2))
        button2.grid(row=1, column=6, padx=10, pady=10)
        button2 = ttk.Button(self, text="StartPage3",
                             command=lambda: controller.show_frame(StartPage3))
        button2.grid(row=2, column=6, padx=10, pady=10)
	
        button3 = ttk.Button(self, text="Start Page4",
                             command=lambda: controller.show_frame(StartPage4))
        button3.grid(row=3, column=6, padx=10, pady=10)
        
	


class StartPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un type", font=LARGEFONT)
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

        
        button2 = ttk.Button(self, text="StartPage3",
                             command=lambda: controller.show_frame(StartPage3))
        button2.grid(row=2, column=6, padx=10, pady=10)
	
        button3 = ttk.Button(self, text="Start Page4",
                             command=lambda: controller.show_frame(StartPage4))
        button3.grid(row=3, column=6, padx=10, pady=10)
        



class StartPage3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un type", font=LARGEFONT)
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

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(StartPage2))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=4, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(StartPage4))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=4, padx=10, pady=10)
        


class StartPage4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

		# label of frame Layout 2
        label = ttk.Label(self, text="Ajout d'un type", font=LARGEFONT)
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

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(StartPage2))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=4, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=4, padx=10, pady=10)
# Driver Code
app = tkinterApp()
app.mainloop()
