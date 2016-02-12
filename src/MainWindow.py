__author__ = 'casey'

import tkinter as tk
from tkinter import ttk
from tkinter import *
from src.Controller import Controller

# For Analysis
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
# import matplotlib.animation as animation
# from matplotlib import style
# from matplotlib import pyplot as plt


LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Veranda", 10)
SMALL_FONT = ("Veranda", 8)

db_controller = Controller()

# style.use("ggplot")
#
# f = Figure()

def setString(sv):
        sv.set(sv)

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

        # --Grid layout--
        merchButton.grid(row=1, column=1)
        salesButton.grid(row=1, column=2)
        schedButton.grid(row=1, column=3)
        analysisButton.grid(row=1, column=4)


# Merch class
class MerchPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        merch_label = tk.Label(self, text="Merchandise", font="LARGE_FONT")
        merch_label.grid(row=0, column=7)

        # --String variables--
        self.merch_id = StringVar()
        self.type = StringVar()
        self.description = StringVar()
        self.unit_cost = StringVar()
        self.quantity = StringVar()
        self.price = StringVar()
        self.total_sold = StringVar()

        # --Field labels--
        merch_id_label = tk.Label(self, text="ID")
        type_label = tk.Label(self, text="Type")
        desc_label = tk.Label(self, text="Description")
        unit_cost_label = tk.Label(self, text="Unit Cost")
        quant_label = tk.Label(self, text="Quantity")
        price_label = tk.Label(self, text="Price")
        total_sold_label = tk.Label(self, text="Total Sold")

        # # --Form fields--
        merch_id_entry = tk.Entry(self, textvariable=self.merch_id)
        type_entry = Entry(self, textvariable=self.type)
        desc_entry = tk.Entry(self, textvariable=self.description)
        unit_cost_entry = tk.Entry(self, textvariable=self.unit_cost)
        quant_entry = tk.Entry(self, textvariable=self.quantity)
        price_entry = tk.Entry(self, textvariable=self.price)
        total_sold_entry = tk.Entry(self, textvariable=self.total_sold)

        # --Buttons--
        submitButton = tk.Button(self, text="Submit", command=self.submitMerchEntry)

        # --Grid Layouts--
        #ID
        merch_id_label.grid(row=1, column=2)
        merch_id_entry.grid(row=1, column=3)
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

        #Treeview
        merch_tree = ttk.Treeview(self)
        merch_tree["columns"] = ("type", "desc", "unit_cost", "quant", "price", "total_sold")
        #Merch ID
        # blank column on left
        #Type
        merch_tree.column("type", width=100)
        merch_tree.heading("type", text="Type")
        #Description
        merch_tree.column("desc", width=300)
        merch_tree.heading("desc", text="Description")
        #Unit Cost
        merch_tree.column("unit_cost", width=80)
        merch_tree.heading("unit_cost", text="Unit Cost")
        #Quantity
        merch_tree.column("quant", width=80)
        merch_tree.heading("quant", text="Quantity")
        #Price
        merch_tree.column("price", width=80)
        merch_tree.heading("price", text="Price")
        #Total Sold
        merch_tree.column("total_sold", width=80)
        merch_tree.heading("total_sold", text="Total Sold")

        merch_tree.grid(row=10, column=0, columnspan=13)

        submitButton.grid(row=6, column=12)


        # This adds the data from the database to the GUI.
        # con = Controller()
        merch_list = db_controller.get_merch_info_for_merch_window()
        for item in merch_list:
            merch_tree.insert("", "end", values = (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

        # ** Use merch_tree.insert("", <linenumber>, text="merch_id", values=("field1", "field2", etc.))

    def submitMerchEntry(self):

        print(self.merch_id.get() +
              "\n" + self.type.get() +
              "\n" + self.description.get() +
              "\n" + self.unit_cost.get() +
              "\n" + self.quantity.get() +
              "\n" + self.price.get() +
              "\n" + self.total_sold.get())

# Sales class
class SalesPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sales", font="LARGE_FONT")
        label.grid(row=0, column=4)

        # --String variables--
        self.sale_id = StringVar()
        self.tour_id = StringVar()
        self.item_sold = StringVar()
        self.description = StringVar()
        self.quantity = StringVar()
        self.unit_total = StringVar()
        self.total = StringVar()

        # --Field labels--
        sale_id_label = tk.Label(self, text="Sale ID")
        tour_id_label = tk.Label(self, text="Tour ID")
        item_sold_label = tk.Label(self, text="Item Sold")
        description_label = tk.Label(self, text="Description")
        quantity_label = tk.Label(self, text="Quantity")
        unit_total_label = tk.Label(self, text="Subtotal")
        total_label = tk.Label(self, text="Total")

        # --Form fields--
        sale_id_entry = tk.Entry(self, textvariable=self.sale_id)
        tour_id_entry = tk.Entry(self, textvariable=self.tour_id)
        item_sold_entry = tk.Entry(self, textvariable=self.item_sold)
        description_entry = tk.Entry(self, textvariable=self.description)
        quantity_entry = tk.Entry(self, textvariable=self.quantity)
        unit_total_entry = tk.Entry(self, textvariable=self.unit_total)
        total_entry = tk.Entry(self, textvariable=self.total)


        # --Buttons--
        submitButton = tk.Button(self, text="Submit", command=self.submitSalesEntry)

        # --Grid layout--
        #Sale ID
        sale_id_label.grid(row=1, column=0)
        sale_id_entry.grid(row=1, column=1)
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
        unit_total_label.grid(row=2, column=6)
        unit_total_entry.grid(row=2, column=7)
        #Total
        total_label.grid(row=3, column=6)
        total_entry.grid(row=3, column=7)

        submitButton.grid(row=5, column=6)

        #Treeview
        sales_tree = ttk.Treeview(self)
        sales_tree["columns"] = ("tour_id", "item_sold", "desc", "quant", "unit_total", "total")
        #Sale ID
        # blank column
        #Tour ID
        sales_tree.column("tour_id", width=80)
        sales_tree.heading("tour_id", text="Tour ID")
        #Item Sold
        sales_tree.column("item_sold", width=150)
        sales_tree.heading("item_sold", text="Item Sold")
        #Description
        sales_tree.column("desc", width=300)
        sales_tree.heading("desc", text="Description")
        #Quantity
        sales_tree.column("quant", width=80)
        sales_tree.heading("quant", text="Quantity")
        #Subtotal
        sales_tree.column("unit_total", width=80)
        sales_tree.heading("unit_total", text="Unit Total")
        #Total
        sales_tree.column("total", width=80)
        sales_tree.heading("total", text="Total")

        sales_tree.grid(row=10, column=0, columnspan=13)

    def submitSalesEntry(self):

        print(self.sale_id.get() +
              "\n" + self.tour_id.get() +
              "\n" + self.item_sold.get() +
              "\n" + self.description.get() +
              "\n" + self.quantity.get() +
              "\n" + self.unit_total.get() +
              "\n" + self.total.get())


# Schedule class
class SchedulePage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Schedule", font="LARGE_FONT")
        label.grid(row=0, column=0, columnspan=12)

        # --String variables--
        self.schedule_id = StringVar()
        self.schedule_id.set("schedule id")
        self.date = StringVar()
        self.date.set("date")
        self.phone = StringVar()
        self.phone.set("phone")
        self.venue = StringVar()
        self.venue.set("venue")
        self.address = StringVar()
        self.address.set("address")
        self.capacity = StringVar()
        self.capacity.set("capacity")
        self.door_pay = StringVar()
        self.door_pay.set("door pay")
        self.cover_charge = StringVar()
        self.cover_charge.set("cover charge")

        # --Field labels--
        sched_id_label = tk.Label(self, text="Schedule ID")
        date_label = tk.Label(self, text="Date")
        phone_label = tk.Label(self, text="Phone")
        venue_label = tk.Label(self, text="Venue")
        address_label = tk.Label(self, text="Address")
        cap_label = tk.Label(self, text="Capacity")
        door_pay_label = tk.Label(self, text="Door Pay")
        cover_charge_label = tk.Label(self, text="Cover Charge")

        # --Form fields--
        sched_id_entry = tk.Entry(self)
        sched_id_entry["textvariable"] = self.schedule_id
        # sched_id_entry.bind('<Key-Return>', MainWindow.getEntry)
        date_entry = Entry(self)
        date_entry["textvariable"] = self.date
        # date_entry.bind('<Key-Return>', MainWindow.getEntry)
        phone_entry = tk.Entry(self)
        phone_entry["textvariable"] = self.phone
        # phone_entry.bind('<Key-Return>', MainWindow.getEntry)
        venue_entry = tk.Entry(self)
        venue_entry["textvariable"] = self.location
        # venue_entry.bind('<Key-Return>', MainWindow.getEntry)
        address_entry = tk.Entry(self)
        address_entry["textvariable"] = self.address
        # address_entry.bind('<Key-Return>', MainWindow.getEntry)
        cap_entry = tk.Entry(self)
        cap_entry["textvariable"] = self.capacity
        # cap_entry.bind('<Key-Return>', MainWindow.getEntry)
        door_pay_entry = tk.Entry(self)
        door_pay_entry["textvariable"] = self.door_pay
        # door_pay_entry.bind('<Key-Return>', MainWindow.getEntry)
        cover_charge_entry = tk.Entry(self)
        cover_charge_entry["textvariable"] = self.cover_charge
        # cover_charge_entry.bind('<Key-Return>', MainWindow.getEntry)

        # --Buttons--
        applyButton = tk.Button(self, text="Apply")
        deleteButton = tk.Button(self, text="Delete")

        # --Grid layout--
        #ID
        sched_id_label.grid(row=1, column=0)
        sched_id_entry.grid(row=1, column=1)
        #Date
        date_label.grid(row=1, column=2)
        date_entry.grid(row=1, column=3)
        #Phone
        phone_label.grid(row=1, column=4)
        phone_entry.grid(row=1, column=5)
        #Venue
        venue_label.grid(row=2, column=0)
        venue_entry.grid(row=2, column=1)
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

        #Treeview
        schedule_tree = ttk.Treeview(self)
        schedule_tree["columns"] = ("date", "phone", "venue", "address", "cap", "door_pay", "cover_charge")
        #Schedule ID
        # blank column
        #Merch ID
        schedule_tree.column("date", width=80)
        schedule_tree.heading("date", text="Date")
        #Tour ID
        schedule_tree.column("phone", width=80)
        schedule_tree.heading("phone", text="Phone")
        #Item Sold
        schedule_tree.column("venue", width=150)
        schedule_tree.heading("venue", text="Venue")
        #Description
        schedule_tree.column("address", width=200)
        schedule_tree.heading("address", text="Address")
        #Quantity
        schedule_tree.column("cap", width=80)
        schedule_tree.heading("cap", text="Capacity")
        #Subtotal
        schedule_tree.column("door_pay", width=80)
        schedule_tree.heading("door_pay", text="Door Pay")
        #Total
        schedule_tree.column("cover_charge", width=80)
        schedule_tree.heading("cover_charge", text="Cover Charge")

        schedule_tree.grid(row=10, column=0, columnspan=13)

# Analysis Class
class AnalysisPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Analysis", font="LARGE_FONT")
        label.grid(row=0, column=5)

        # Order items by units sold
            # checkbox?

        # Order items by gross sales

        # Order items by net sales

        # Treeview
        analysis_tree = ttk.Treeview(self)
        analysis_tree["columns"] = ("type", "desc", "unit_cost", "quant", "price", "total_sold")
        #Merch ID
        # blank column on left
        #Type
        analysis_tree.column("type", width=100)
        analysis_tree.heading("type", text="Type")
        #Description
        analysis_tree.column("desc", width=300)
        analysis_tree.heading("desc", text="Description")
        #Unit Cost
        analysis_tree.column("unit_cost", width=80)
        analysis_tree.heading("unit_cost", text="Unit Cost")
        #Quantity
        analysis_tree.column("quant", width=80)
        analysis_tree.heading("quant", text="Quantity")
        #Price
        analysis_tree.column("price", width=80)
        analysis_tree.heading("price", text="Price")
        #Total Sold
        analysis_tree.column("total_sold", width=80)
        analysis_tree.heading("total_sold", text="Total Sold")

        analysis_tree.grid(row=5, column=1, columnspan=11)

        # # Canvas for graph
        # canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        #
        # #Toolbar
        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        # canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


app = MainWindow()
app.geometry("1000x720")
app.mainloop()