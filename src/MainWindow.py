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


LARGE_FONT = ("Verdana", 6)
NORM_FONT = ("Veranda", 12)
SMALL_FONT = ("Veranda", 8)

db_controller = Controller()

# style.use("ggplot")
#
# f = Figure()

# Main Window
class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        db_controller.start_db_manager()
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

        db_controller.show_best_selling_units()
        db_controller.show_best_gross_units()
        db_controller.show_best_net()

    # Show frame
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() # <- raises to front of window

    # Quit program
    def client_exit(self):
        if (db_controller.close_database()):
            print("Database closed.")
        else:
            print("Database not closed.")
        print("This is client_exit.")
        exit()


# NavPage class
class NavigationPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page", font="LARGE_FONT")
        label.grid(row=0, column=0)

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
        merchButton.grid(row=1, column=2)
        salesButton.grid(row=1, column=3)
        schedButton.grid(row=1, column=4)
        analysisButton.grid(row=1, column=5)


# MerchPage class
class MerchPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        merch_label = tk.Label(self, text="Merchandise", font="LARGE_FONT")
        merch_label.grid(row=0, column=0)
        # self.root = Tk()

        # merch_label_frame = LabelFrame(self.root, text="This is a LabelFrame")


        # --String variables--
        self.merch_id = StringVar()
        self.type = StringVar()
        self.unit_cost = StringVar()
        self.quantity = StringVar()
        self.price = StringVar()
        self.total_sold = StringVar()

        # --Field labels--
        # merch_id_label = tk.Label(self, text="ID", font="NORM_FONT")
        type_label = tk.Label(self, text="Type", font="NORM_FONT")
        unit_cost_label = tk.Label(self, text="Unit Cost", font="NORM_FONT")
        quant_label = tk.Label(self, text="Quantity", font="NORM_FONT")
        price_label = tk.Label(self, text="Price", font="NORM_FONT")
        # total_sold_label = tk.Label(self, text="Total Sold", font="NORM_FONT")

        # # --Form fields--
        # merch_id_entry = tk.Entry(self, textvariable=self.merch_id)
        type_entry = Entry(self, textvariable=self.type)
        unit_cost_entry = tk.Entry(self, textvariable=self.unit_cost)
        quant_entry = tk.Entry(self, textvariable=self.quantity)
        price_entry = tk.Entry(self, textvariable=self.price)
        # total_sold_entry = tk.Entry(self, textvariable=self.total_sold)

        # --Buttons--
        submitButton = tk.Button(self, text="Submit", command=self.submitMerchEntry)

        # --Grid Layouts--
        #ID
        # merch_id_label.grid(row=1, column=2, sticky="e")
        # merch_id_entry.grid(row=1, column=3)
        #Type
        type_label.grid(row=1, column=2, sticky="e")
        type_entry.grid(row=1, column=3)
        #Unit Cost
        unit_cost_label.grid(row=3, column=2, sticky="e")
        unit_cost_entry.grid(row=3, column=3)
        #Quantity
        quant_label.grid(row=3, column=4, sticky="e")
        quant_entry.grid(row=3, column=5)
        #Price
        price_label.grid(row=3, column=6, sticky="e")
        price_entry.grid(row=3, column=7)
        #TotalSold
        # total_sold_label.grid(row=3, column=6, sticky="e")
        # total_sold_entry.grid(row=3, column=7)

        #Submit Button
        submitButton.grid(row=5, column=7, sticky="e")

        #Treeview
        #LabelFrame
        # merch_label_frame.grid(row=6, column=0, columnspan=13, rowspan=8)
        merch_tree = ttk.Treeview(self)
        merch_tree["columns"] = ("merch_id", "type", "unit_cost", "quant", "price", "total_sold")
        #Merch ID
        merch_tree.column("merch_id", width=80)
        merch_tree.heading("merch_id", text="Merch ID")
        #Type
        merch_tree.column("type", width=100)
        merch_tree.heading("type", text="Type")
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

        merch_tree['show'] = 'headings'
        merch_tree.grid(row=10, column=3, columnspan=7, sticky="ew")

        # This adds the data from the database to the GUI.
        # con = Controller()
        merch_list = db_controller.get_merch_info_for_merch_window()
        for item in merch_list:
            merch_tree.insert("", 0, values=(item[0], item[1], item[2], item[3], item[4], item[5]))

        # ** Use merch_tree.insert("", <linenumber>, text="merch_id", values=("field1", "field2", etc.))

    def submitMerchEntry(self):
        new_merch_list = []
        new_merch_list.append(self.type.get())
        new_merch_list.append(self.price.get())
        new_merch_list.append(self.unit_cost.get())
        new_merch_list.append(self.quantity.get())

        if(db_controller.add_new_merch(new_merch_list)):
            print("Merchandise Added.")
        else:
            print("Addition failed.")

        # print(self.merch_id.get() +
        #       "\n" + self.type.get() +
        #       "\n" + self.unit_cost.get() +
        #       "\n" + self.quantity.get() +
        #       "\n" + self.price.get() +
        #       "\n" + self.total_sold.get())


# Sales class
class SalesPage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sales", font="LARGE_FONT")
        label.grid(row=0, column=0)

        # --String variables--
        self.sale_id = StringVar()
        self.tour_id = StringVar()
        self.quantity = StringVar()
        self.total_units_cost = StringVar()
        self.total = StringVar()

        # --Field labels--
        # sale_id_label = tk.Label(self, text="Sale ID", font="NORM_FONT")
        tour_id_label = tk.Label(self, text="Tour ID", font="NORM_FONT")
        quantity_label = tk.Label(self, text="Quantity", font="NORM_FONT")
        total_units_cost_label = tk.Label(self, text="Total Units Cost", font="NORM_FONT")
        total_label = tk.Label(self, text="Total", font="NORM_FONT")

        # --Form fields--
        # sale_id_entry = tk.Entry(self, textvariable=self.sale_id)
        tour_id_entry = tk.Entry(self, textvariable=self.tour_id)
        quantity_entry = tk.Entry(self, textvariable=self.quantity)
        total_units_cost_entry = tk.Entry(self, textvariable=self.total_units_cost)
        total_entry = tk.Entry(self, textvariable=self.total)

        # --Buttons--
        submitButton = tk.Button(self, text="Submit", command=self.submitSalesEntry)

        # --Grid layout--
        #Sale ID
        # sale_id_label.grid(row=1, column=2, sticky="e")
        # sale_id_entry.grid(row=1, column=3)
        #Tour ID
        tour_id_label.grid(row=1, column=2, sticky="e")
        tour_id_entry.grid(row=1, column=3)
        #Quantity
        quantity_label.grid(row=2, column=2, sticky="e")
        quantity_entry.grid(row=2, column=3)
        #Total Units Cost
        total_units_cost_label.grid(row=2, column=4, sticky="e")
        total_units_cost_entry.grid(row=2, column=5)
        #Total
        total_label.grid(row=2, column=6, sticky="e")
        total_entry.grid(row=2, column=7)

        submitButton.grid(row=3, column=7, sticky="e")

        #Treeview
        sales_tree = ttk.Treeview(self)
        sales_tree["columns"] = ("sales_id", "tour_id", "quant", "total_units_cost", "total")
        #Sale ID
        sales_tree.column("sales_id", width=80)
        sales_tree.heading("sales_id", text="Sales ID")
        #Tour ID
        sales_tree.column("tour_id", width=100)
        sales_tree.heading("tour_id", text="Tour ID")
        #Quantity
        sales_tree.column("quant", width=100)
        sales_tree.heading("quant", text="Quantity")
        #Total Units Cost
        sales_tree.column("total_units_cost", width=100)
        sales_tree.heading("total_units_cost", text="Total Units Cost")
        #Total
        sales_tree.column("total", width=100)
        sales_tree.heading("total", text="Total")

        sales_tree['show'] = 'headings'
        sales_tree.grid(row=6, column=3, columnspan=7, sticky="ew")

        sales_list = db_controller.get_sales_info_for_sales_window()
        for sale in sales_list:
            sales_tree.insert("", 0, values=(sale[0], sale[1], sale[2], sale[3], sale[4]))


    def submitSalesEntry(self):

        print(self.sale_id.get() +
              "\n" + self.tour_id.get() +
              "\n" + self.quantity.get() +
              "\n" + self.total_units_cost.get() +
              "\n" + self.total.get())


# Schedule class
class SchedulePage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Schedule", font="LARGE_FONT")
        label.grid(row=0, column=0)

        # --String variables--
        self.schedule_id = StringVar()
        self.date = StringVar()
        self.phone = StringVar()
        self.venue = StringVar()
        self.address = StringVar()
        self.cap = StringVar()
        self.door_pay = StringVar()
        self.cover_charge = StringVar()

        # --Field labels--
        # sched_id_label = tk.Label(self, text="Schedule ID", font="NORM_FONT")
        date_label = tk.Label(self, text="Date", font="NORM_FONT")
        phone_label = tk.Label(self, text="Phone", font="NORM_FONT")
        venue_label = tk.Label(self, text="Venue", font="NORM_FONT")
        address_label = tk.Label(self, text="Address", font="NORM_FONT")
        cap_label = tk.Label(self, text="Capacity", font="NORM_FONT")
        door_pay_label = tk.Label(self, text="Door Pay", font="NORM_FONT")
        cover_charge_label = tk.Label(self, text="Cover Charge", font="NORM_FONT")

        # --Form fields--
        # sched_id_entry = tk.Entry(self, textvariable=self.schedule_id)
        date_entry = Entry(self, textvariable=self.date)
        phone_entry = tk.Entry(self, textvariable=self.phone)
        venue_entry = tk.Entry(self, textvariable=self.venue)
        address_entry = tk.Entry(self, textvariable=self.address)
        cap_entry = tk.Entry(self, textvariable=self.cap)
        door_pay_entry = tk.Entry(self, textvariable=self.door_pay)
        cover_charge_entry = tk.Entry(self, textvariable=self.cover_charge)

        # --Buttons--
        submitButton = tk.Button(self, text="Submit", command=self.submitScheduleEntry)

        # --Grid layout--
        #ID
        # sched_id_label.grid(row=1, column=2, sticky="e")
        # sched_id_entry.grid(row=1, column=3)
        #Date
        date_label.grid(row=1, column=2, sticky="e")
        date_entry.grid(row=1, column=3)
        #Venue
        venue_label.grid(row=2, column=2, sticky="e")
        venue_entry.grid(row=2, column=3)
        #Address
        address_label.grid(row=2, column=4, sticky="e")
        address_entry.grid(row=2, column=5)
        #Phone
        phone_label.grid(row=2, column=6, sticky="e")
        phone_entry.grid(row=2, column=7)
        #Capacity
        cap_label.grid(row=3, column=2, sticky="e")
        cap_entry.grid(row=3, column=3)
        #Door pay
        door_pay_label.grid(row=3, column=4, sticky="e")
        door_pay_entry.grid(row=3, column=5)
        #Cover charge
        cover_charge_label.grid(row=3, column=6, sticky="e")
        cover_charge_entry.grid(row=3, column=7)
        #Buttons
        submitButton.grid(row=5, column=7, sticky="e")

        #Treeview
        schedule_tree = ttk.Treeview(self)
        schedule_tree["columns"] = ("tour_id", "date", "phone", "venue", "address", "cap", "door_pay", "cover_charge")
        #Schedule ID
        schedule_tree.column("tour_id", width=80)
        schedule_tree.heading("tour_id", text="Tour ID")
        #Merch ID
        schedule_tree.column("date", width=80)
        schedule_tree.heading("date", text="Date")
        #Tour ID
        schedule_tree.column("phone", width=80)
        schedule_tree.heading("phone", text="Phone")
        #Item Sold
        schedule_tree.column("venue", width=100)
        schedule_tree.heading("venue", text="Venue")
        #Description
        schedule_tree.column("address", width=150)
        schedule_tree.heading("address", text="Address")
        #Quantity
        schedule_tree.column("cap", width=60)
        schedule_tree.heading("cap", text="Capacity")
        #Subtotal
        schedule_tree.column("door_pay", width=60)
        schedule_tree.heading("door_pay", text="Door Pay")
        #Total
        schedule_tree.column("cover_charge", width=70)
        schedule_tree.heading("cover_charge", text="Cover Charge")

        schedule_tree['show'] = 'headings'
        schedule_tree.grid(row=6, column=3, columnspan=7, sticky="ew")

        tour_list = db_controller.get_tour_info_for_tour_window()
        for date in tour_list:
            schedule_tree.insert("", 0, values=(date[0], date[1], date[2], date[3], date[4], date[5], date[6], date[7]))

    def submitScheduleEntry(self):


        new_tour_date = []
        new_tour_date.append(self.address.get())
        new_tour_date.append("City")
        new_tour_date.append("State")
        new_tour_date.append(12345)
        new_tour_date.append(self.venue.get())
        new_tour_date.append(self.phone.get())
        new_tour_date.append(self.date.get())
        new_tour_date.append(self.cap.get())
        new_tour_date.append(self.cover_charge.get())
        new_tour_date.append(self.door_pay.get())

        if(db_controller.add_tour_date(new_tour_date)):
            print("Tour Date Added.")
        else:
            print("Tour Date Addition Failed.")

# Analysis Class
class AnalysisPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Analysis", font="LARGE_FONT")
        label.grid(row=0, column=0)

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

        analysis_tree.grid(row=5, column=3, columnspan=7, sticky="ew")

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
app.geometry("900x500")
app.mainloop()