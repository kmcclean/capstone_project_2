__author__ = 'casey'

import tkinter as tk
from tkinter import ttk
from tkinter import *

# For Analysis
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Veranda", 10)
SMALL_FONT = ("Veranda", 8)
style.use("ggplot")

f = Figure()

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Inventory Manager")

        # Container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --Menu--
        mainMenu = tk.Menu(container)

        # --File submenu--
        file = tk.Menu(mainMenu)
        file.add_command(label="Save")
        file.add_command(label="Exit", command=self.client_exit)
        mainMenu.add_cascade(label='File', menu=file)

        # --Edit submenu--
        edit = tk.Menu(mainMenu)
        edit.add_command(label='Undo')
        mainMenu.add_cascade(label="Edit", menu=edit)

        # --Navigation submenu--
        nav = tk.Menu(mainMenu)
        nav.add_command(label="Tour Schedule", command=lambda: self.show_frame(SchedulePage))
        nav.add_command(label="Sales", command=lambda: self.show_frame(SalesPage))
        nav.add_command(label="Merchandise", command=lambda: self.show_frame(MerchPage))
        nav.add_command(label="Analyzer", command=lambda: self.show_frame(AnalysisPage))
        mainMenu.add_cascade(label="Navigation", menu=nav)

        tk.Tk.config(self, menu=mainMenu)

        self.frames = {}

        # Loop through tuple of pages
        for F in (NavigationPage, MerchPage, SalesPage, SchedulePage, AnalysisPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(NavigationPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() # <- raises to front of window

    def client_exit(self):
        exit()

# Nav class
class NavigationPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", font="LARGE_FONT")
        label.grid(row=0, column=0, columnspan=4)

        # Buttons
        merchButton = tk.Button(self, text="Merchandise",
                            command=lambda: controller.show_frame(MerchPage))
        salesButton = tk.Button(self, text="Sales",
                            command=lambda: controller.show_frame(SalesPage))
        schedButton = tk.Button(self, text="Schedule",
                            command=lambda: controller.show_frame(SchedulePage))
        analysisButton = tk.Button(self, text="Analysis",
                            command=lambda: controller.show_frame(AnalysisPage))

        # Packs
        merchButton.grid(row=1, column=1)
        salesButton.grid(row=1, column=2)
        schedButton.grid(row=1, column=3)
        analysisButton.grid(row=1, column=4)

# Merch class
class MerchPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        merch_label = tk.Label(self, text="Merchandise", font="LARGE_FONT")
        merch_label.grid(row=0, column=0, columnspan=4)

        # --Field labels--
        id_label = tk.Label(text="ID")
        type_label = tk.Label(text="Type")
        desc_label = tk.Label(text="Description")
        unit_cost_label = tk.Label(text="Unit Cost")
        quant_label = tk.Label(text="Quantity")
        price_label = tk.Label(text="Price")
        total_sold_label = tk.Label(text="Total Sold")

        # # --Form fields--
        id_entry = tk.Entry(self)
        type_entry = Entry(self)
        desc_entry = tk.Entry(self)
        unit_cost_entry = tk.Entry(self)
        quant_entry = tk.Entry(self)
        price_entry = tk.Entry(self)
        total_sold_entry = tk.Entry(self)

        # # --Grid Layouts--
        # #ID
        id_label.grid(row=1, column=2)
        # id_entry.grid(row=1, column=3) # <--- when entries are added to the grid the program hangs on launch

        # #Type
        type_label.grid(row=3, column=2)
        # type_entry.grid(row=3, column=3)

        # #Description
        desc_label.grid(row=3, column=5)
        # desc_entry.grid(row=3, column=6, columnspan=3)

        # #Unit Cost
        unit_cost_label.grid(row=5, column=2)
        # unit_cost_entry.grid(row=5, column=3)

        # #Quantity
        quant_label.grid(row=5, column=5)
        # quant_entry.grid(row=5, column=6)

        # #Price
        price_label.grid(row=5, column=8)
        # price_entry.grid(row=5, column=9)

        # #TotalSold
        total_sold_label.grid(row=5, column=11)
        # total_sold_entry.grid(row=5, column=12)




# Sales class
class SalesPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sales", font="LARGE_FONT")
        label.pack(pady=10, padx=10)


# Schedule class
class SchedulePage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Schedule", font="LARGE_FONT")
        label.pack(pady=10, padx=10)



# Analysis Class
class AnalysisPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Analysis", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        # Canvas for graph
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        #Toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)




app = MainWindow()
app.geometry("800x600")
app.mainloop()