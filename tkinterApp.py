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
		for F in (StartPage, Vehicule ,TypeTraverse,Traverse,Traversier,Client,Employe):

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

        

        
