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
        id_label = tk.Label(self, text="ID")
        type_label = tk.Label(self, text="Type")
        desc_label = tk.Label(self, text="Description")
        unit_cost_label = tk.Label(self, text="Unit Cost")
        quant_label = tk.Label(self, text="Quantity")
        price_label = tk.Label(self, text="Price")
        total_sold_label = tk.Label(self, text="Total Sold")

        # # --Form fields--
        id_entry = tk.Entry(self)
        type_entry = Entry(self)
        desc_entry = tk.Entry(self)
        unit_cost_entry = tk.Entry(self)
        quant_entry = tk.Entry(self)
        price_entry = tk.Entry(self)
        total_sold_entry = tk.Entry(self)

        # --Grid Layouts--
        #ID
        id_label.grid(row=1, column=2)
        id_entry.grid(row=1, column=3)

        #Type
        type_label.grid(row=3, column=2)
        type_entry.grid(row=3, column=3)

        #Description
        desc_label.grid(row=3, column=5)
        desc_entry.grid(row=3, column=6, columnspan=3)

        #Unit Cost
        unit_cost_label.grid(row=5, column=2)
        unit_cost_entry.grid(row=5, column=3)

        #Quantity
        quant_label.grid(row=5, column=5)
        quant_entry.grid(row=5, column=6)

        #Price
        price_label.grid(row=5, column=8)
        price_entry.grid(row=5, column=9)

        #TotalSold
        total_sold_label.grid(row=5, column=11)
        total_sold_entry.grid(row=5, column=12)




# Sales class
class SalesPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New Sale", font="LARGE_FONT")
        label.grid(row=0, column=0, columnspan=8)

        # --Field labels--
        sale_id_label = tk.Label(self, text="Sale ID")
        merch_id_label = tk.Label(self, text="Merch ID")
        tour_id_label = tk.Label(self, text="Tour ID")
        item_sold_label = tk.Label(self, text="Item Sold")
        description_label = tk.Label(self, text="Description")
        quantity_label = tk.Label(self, text="Quantity")
        subtotal_label = tk.Label(self, text="Subtotal")
        total_label = tk.Label(self, text="Total")

        # --Form fields--
        sale_id_entry = tk.Entry(self)
        merch_id_entry = Entry(self)
        tour_id_entry = tk.Entry(self)
        item_sold_entry = tk.Entry(self)
        description_entry = tk.Entry(self)
        quantity_entry = tk.Entry(self)
        subtotal_entry = tk.Entry(self)
        total_entry = tk.Entry(self)

        # --Buttons--
        applyButton = tk.Button(self, text="Apply")
        cancelButton = tk.Button(self, text="Cancel")

        # --Grid layout--
        #Sale ID
        sale_id_label.grid(row=1, column=0)
        sale_id_entry.grid(row=1, column=1)
        #Merch ID
        merch_id_label.grid(row=1, column=2)
        merch_id_entry.grid(row=1, column=3)
        #Tour ID
        tour_id_label.grid(row=1, column=4)
        tour_id_entry.grid(row=1, column=5)
        #Item sold
        item_sold_label.grid(row=2, column=0)
        item_sold_entry.grid(row=2, column=1)
        #Description
        description_label.grid(row=2, column=2)
        description_entry.grid(row=2, column=3)
        #Quantity
        quantity_label.grid(row=2, column=4)
        quantity_entry.grid(row=2, column=5)
        #Subtotal
        subtotal_label.grid(row=2, column=6)
        subtotal_entry.grid(row=2, column=7)
        #Total
        total_label.grid(row=3, column=6)
        total_entry.grid(row=3, column=7)

        applyButton.grid(row=5, column=6)
        cancelButton.grid(row=5, column=7)

# Schedule class
class SchedulePage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Schedule", font="LARGE_FONT")
        label.grid(row=0, column=0, columnspan=12)

        # --Field labels--
        id_label = tk.Label(self, text="ID")
        date_label = tk.Label(self, text="Date")
        phone_label = tk.Label(self, text="Phone")
        location_label = tk.Label(self, text="Location")
        address_label = tk.Label(self, text="Address")
        cap_label = tk.Label(self, text="Capacity")
        door_pay_label = tk.Label(self, text="Door Pay")
        cover_charge_label = tk.Label(self, text="Cover Charge")

        # --Form fields--
        id_entry = tk.Entry(self)
        date_entry = Entry(self)
        phone_entry = tk.Entry(self)
        location_entry = tk.Entry(self)
        address_entry = tk.Entry(self)
        cap_entry = tk.Entry(self)
        door_pay_entry = tk.Entry(self)
        cover_charge_entry = tk.Entry(self)

        # --Buttons--
        applyButton = tk.Button(self, text="Apply")
        deleteButton = tk.Button(self, text="Delete")

        # --Grid layout--
        #ID
        id_label.grid(row=1, column=0)
        id_entry.grid(row=1, column=1)
        #Date
        date_label.grid(row=1, column=2)
        date_entry.grid(row=1, column=3)
        #Phone
        phone_label.grid(row=1, column=4)
        phone_entry.grid(row=1, column=5)
        #Location
        location_label.grid(row=2, column=0)
        location_entry.grid(row=2, column=1)
        #Address
        address_label.grid(row=2, column=2)
        address_entry.grid(row=2, column=3)
        #Capacity
        cap_label.grid(row=3, column=0)
        cap_entry.grid(row=3, column=1)
        #Door pay
        door_pay_label.grid(row=3, column=2)
        door_pay_entry.grid(row=3, column=3)
        #Cover charge
        cover_charge_label.grid(row=3, column=4)
        cover_charge_entry.grid(row=3, column=5)
        #Buttons
        applyButton.grid(row=5, column=4)
        deleteButton.grid(row=5, column=5)


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
app.geometry("1200x720")
app.mainloop()