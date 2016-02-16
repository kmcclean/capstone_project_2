__author__ = 'casey'

import tkinter as tk
from tkinter import ttk
from tkinter import *
from src.Controller import Controller
from src.ErrorHandling import ErrorHandling
import tkinter.messagebox
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

        #User greeting
        greet_str = "Welcome to Inventory Manager. \n" \
                    "To get started, choose one of the buttons below, \n" \
                    "or choose an option from the 'Navigation' menu"
        greeting = tk.Label(self, text=greet_str, font="NORM_FONT")

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
        greeting.grid(row=1, column=1, columnspan=5)
        merchButton.grid(row=2, column=2)
        salesButton.grid(row=2, column=3)
        schedButton.grid(row=2, column=4)
        analysisButton.grid(row=2, column=5)


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
        self.merch_tree = ttk.Treeview(self)
        self.merch_tree["columns"] = ("merch_id", "type", "unit_cost", "quant", "price", "total_sold")
        #Merch ID
        self.merch_tree.column("merch_id", width=80)
        self.merch_tree.heading("merch_id", text="Merch ID")
        #Type
        self.merch_tree.column("type", width=100)
        self.merch_tree.heading("type", text="Type")
        #Unit Cost
        self.merch_tree.column("unit_cost", width=80)
        self.merch_tree.heading("unit_cost", text="Unit Cost")
        #Quantity
        self.merch_tree.column("quant", width=80)
        self.merch_tree.heading("quant", text="Quantity")
        #Price
        self.merch_tree.column("price", width=80)
        self.merch_tree.heading("price", text="Price")
        #Total Sold
        self.merch_tree.column("total_sold", width=80)
        self.merch_tree.heading("total_sold", text="Total Sold")

        self.merch_tree['show'] = 'headings'
        self.merch_tree.grid(row=10, column=3, columnspan=7, sticky="ew")

        # This adds the data from the database to the GUI.
        # con = Controller()
        merch_list = db_controller.get_merch_info_for_merch_window()
        for item in merch_list:
            self.merch_tree.insert("", 0, values=(item[0], item[1], item[2], item[3], item[4], item[5]))

        # ** Use merch_tree.insert("", <linenumber>, text="merch_id", values=("field1", "field2", etc.))

    def submitMerchEntry(self):
        new_merch_list = []
        new_merch_list.append(self.type.get())
        new_merch_list.append(self.price.get())
        new_merch_list.append(self.unit_cost.get())
        new_merch_list.append(self.quantity.get())

        merch_test_results = self.merch_list_testing(new_merch_list)
        if merch_test_results[0]:
            results_list = db_controller.add_new_merch(new_merch_list)
            if results_list[0] == True:
                new_addition_to_list = results_list[1]
                self.merch_tree.insert("", 0, values=(new_addition_to_list[0], new_addition_to_list[1], new_addition_to_list[2], new_addition_to_list[3], new_addition_to_list[4], new_addition_to_list[5]))
            else:
                print("Addition failed.")

        else:
            self.alert_errors(merch_test_results[1])

    def merch_list_testing(self, merch_list):
        eh = ErrorHandling()
        if eh.nonblank_string(merch_list[0]) == False:
            failure_list = [False, "The type field must be filled."]
            return failure_list
        elif eh.float_check_range(merch_list[1], 0, float('inf')) == False:
            failure_list = [False, "The price field must be an number."]
            return failure_list
        elif eh.float_check_range(merch_list[2], 0, float('inf')) == False:
            failure_list = [False, "The unit cost must be a positive number."]
            return failure_list
        elif eh.range_integer_input_checking(merch_list[3], 0, float('inf')) == False:
            failure_list = [False, "The quanitity must be a positive number."]
            return failure_list
        else:
            success_list = [True, "All input fields have been entered correctly."]
            return success_list

    #Error messagebox
    def alert_errors(self, string):
        tk.messagebox.showinfo("Input Error", string)


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
        self.sales_tree = ttk.Treeview(self)
        self.sales_tree["columns"] = ("sales_id", "tour_id", "quant", "total_units_cost", "total")
        #Sale ID
        self.sales_tree.column("sales_id", width=80)
        self.sales_tree.heading("sales_id", text="Sales ID")
        #Tour ID
        self.sales_tree.column("tour_id", width=100)
        self.sales_tree.heading("tour_id", text="Tour ID")
        #Quantity
        self.sales_tree.column("quant", width=100)
        self.sales_tree.heading("quant", text="Quantity")
        #Total Units Cost
        self.sales_tree.column("total_units_cost", width=100)
        self.sales_tree.heading("total_units_cost", text="Total Units Cost")
        #Total
        self.sales_tree.column("total", width=100)
        self.sales_tree.heading("total", text="Total")

        self.sales_tree['show'] = 'headings'
        self.sales_tree.grid(row=6, column=3, columnspan=7, sticky="ew")

        sales_list = db_controller.get_sales_info_for_sales_window()
        for sale in sales_list:
            self.sales_tree.insert("", 0, values=(sale[0], sale[1], sale[2], sale[3], sale[4]))


    def submitSalesEntry(self):

        print(self.sale_id.get() +
              "\n" + self.tour_id.get() +
              "\n" + self.quantity.get() +
              "\n" + self.total_units_cost.get() +
              "\n" + self.total.get())

    #Error messagebox
    def alert_errors(self, string):
        tk.messagebox.showinfo("Input Error", string)


# Schedule class
class SchedulePage (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Schedule", font="LARGE_FONT")
        label.grid(row=0, column=0)

        # --String variables--
        self.schedule_id = StringVar()
        self.date = StringVar()
        self.venue = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.zip = StringVar()
        self.phone = StringVar()
        self.cap = StringVar()
        self.door_pay = StringVar()
        self.cover_charge = StringVar()

        # --Field labels--
        # sched_id_label = tk.Label(self, text="Schedule ID", font="NORM_FONT")
        date_label = tk.Label(self, text="Date", font="NORM_FONT")
        venue_label = tk.Label(self, text="Venue", font="NORM_FONT")
        address_label = tk.Label(self, text="Address", font="NORM_FONT")
        city_label = tk.Label(self, text="City", font="NORM_FONT")
        state_label = tk.Label(self, text="State", font="NORM_FONT")
        zip_label = tk.Label(self, text="Zip", font="NORM_FONT")
        phone_label = tk.Label(self, text="Phone", font="NORM_FONT")
        cap_label = tk.Label(self, text="Capacity", font="NORM_FONT")
        door_pay_label = tk.Label(self, text="Door Pay", font="NORM_FONT")
        cover_charge_label = tk.Label(self, text="Cover Charge", font="NORM_FONT")

        # --Form fields--
        # sched_id_entry = tk.Entry(self, textvariable=self.schedule_id)
        date_entry = Entry(self, textvariable=self.date)
        venue_entry = tk.Entry(self, textvariable=self.venue)
        address_entry = tk.Entry(self, textvariable=self.address)
        city_entry = tk.Entry(self, textvariable=self.city)
        state_entry = tk.Entry(self, textvariable=self.state)
        zip_entry = tk.Entry(self, textvariable=self.zip)
        phone_entry = tk.Entry(self, textvariable=self.phone)
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
        venue_label.grid(row=1, column=4, sticky="e")
        venue_entry.grid(row=1, column=5)
        #Address
        address_label.grid(row=2, column=2, sticky="e")
        address_entry.grid(row=2, column=3)
        #City
        city_label.grid(row=2, column=4, sticky="e")
        city_entry.grid(row=2, column=5)
        #State
        state_label.grid(row=2, column=6, sticky="e")
        state_entry.grid(row=2, column=7)
        #Zip
        zip_label.grid(row=2, column=8, sticky="e")
        zip_entry.grid(row=2, column=9)
        #Phone
        phone_label.grid(row=3, column=2, sticky="e")
        phone_entry.grid(row=3, column=3)
        #Capacity
        cap_label.grid(row=3, column=4, sticky="e")
        cap_entry.grid(row=3, column=5)
        #Door pay
        door_pay_label.grid(row=3, column=6, sticky="e")
        door_pay_entry.grid(row=3, column=7)
        #Cover charge
        cover_charge_label.grid(row=3, column=8, sticky="e")
        cover_charge_entry.grid(row=3, column=9)
        #Buttons
        submitButton.grid(row=5, column=9, sticky="e")

        #Treeview
        self.schedule_tree = ttk.Treeview(self)
        self.schedule_tree["columns"] = ("tour_id", "date", "phone", "venue", "address", "city", "state", "zip", "cap", "door_pay", "cover_charge")
        #Tour ID
        self.schedule_tree.column("tour_id", width=80)
        self.schedule_tree.heading("tour_id", text="Tour ID")
        #Date
        self.schedule_tree.column("date", width=80)
        self.schedule_tree.heading("date", text="Date")
        #Phone
        self.schedule_tree.column("phone", width=80)
        self.schedule_tree.heading("phone", text="Phone")
        #Venue
        self.schedule_tree.column("venue", width=100)
        self.schedule_tree.heading("venue", text="Venue")
        #Address
        self.schedule_tree.column("address", width=150)
        self.schedule_tree.heading("address", text="Address")
        #City
        self.schedule_tree.column("city", width=100)
        self.schedule_tree.heading("city", text="City")
        #State
        self.schedule_tree.column("state", width=60)
        self.schedule_tree.heading("state", text="State")
        #Zip
        self.schedule_tree.column("zip", width=80)
        self.schedule_tree.heading("zip", text="Zip Code")
        #Capacity
        self.schedule_tree.column("cap", width=60)
        self.schedule_tree.heading("cap", text="Capacity")
        #Door Pay
        self.schedule_tree.column("door_pay", width=60)
        self.schedule_tree.heading("door_pay", text="Door Pay")
        #Cover Charge
        self.schedule_tree.column("cover_charge", width=70)
        self.schedule_tree.heading("cover_charge", text="Cover Charge")

        self.schedule_tree['show'] = 'headings'
        self.schedule_tree.grid(row=6, column=3, columnspan=7, sticky="ew")

        tour_list = db_controller.get_tour_info_for_tour_window()
        for date in tour_list:
            self.schedule_tree.insert("", 0, values=(date[0], date[1], date[2], date[3], date[4], date[5], date[6], date[7], date[8], date[9], date[10]))

    def submitScheduleEntry(self):

        new_tour_date = []
        new_tour_date.append(self.address.get())
        new_tour_date.append(self.city.get())
        new_tour_date.append(self.state.get())
        new_tour_date.append(self.zip.get())
        new_tour_date.append(self.venue.get())
        new_tour_date.append(self.phone.get())
        new_tour_date.append(self.date.get())
        new_tour_date.append(self.cap.get())
        new_tour_date.append(self.cover_charge.get())
        new_tour_date.append(self.door_pay.get())

        results_list = self.test_new_tour_date(new_tour_date)

        if results_list[0]:
            new_tour_date_gui_info = db_controller.add_tour_date(new_tour_date)
            if new_tour_date_gui_info[0]:
                new_tour_date_gui_list = new_tour_date_gui_info[1]
                self.schedule_tree.insert("", 0, values=(new_tour_date_gui_list[0], new_tour_date_gui_list[7],
                                                      new_tour_date_gui_list[6], new_tour_date_gui_list[5],
                                                      new_tour_date_gui_list[1], new_tour_date_gui_list[2],
                                                      new_tour_date_gui_list[3], new_tour_date_gui_list[4],
                                                      new_tour_date_gui_list[8], new_tour_date_gui_list[10],
                                                         new_tour_date_gui_list[9]))
                print("Tour Date Added.")
            else:
                print("Tour Date Addition Failed.")
        else:
            self.alert_errors(results_list[1])

    def test_new_tour_date(self, new_date):
        eh = ErrorHandling()
        if eh.nonblank_string(new_date[0]) == False:
            failure_list = [False, "The address field must be filled."]
            return failure_list
        elif eh.nonblank_string(new_date[1]) == False:
            failure_list = [False, "The city field must be filled."]
            return failure_list
        elif eh.variable_length_checking(new_date[2], 2) == False:
            failure_list = [False, "The state field must be with a state abbreviation."]
            return failure_list
        elif eh.variable_length_checking(new_date[3], 5) == False:
            failure_list = [False, "The zip code field must be filled."]
            return failure_list
        elif eh.nonblank_string(new_date[4]) == False:
            failure_list = [False, "The venue field must be filled."]
            return failure_list
        elif eh.variable_length_checking(new_date[5], 10) == False:
            failure_list = [False, "The phone number field must be filled."]
            return failure_list
        elif eh.nonblank_string(new_date[6]) == False:
            failure_list = [False, "The date field must be filled."]
            return failure_list
        elif eh.range_integer_input_checking(new_date[7], 0, 99999) == False:
            failure_list = [False, "The capacity field must be filled."]
            return failure_list
        elif eh.float_check_range(new_date[8], 0, float('inf')) == False:
            failure_list = [False, "The cover charge field must be a positive integer."]
            return failure_list
        elif eh.float_check_range(new_date[9], 0, float('inf')) == False:
            failure_list = [False, "The door pay field must be filled."]
            return failure_list
        else:
            success_list = [True, "All input fields have been entered correctly."]
            return success_list

    #Error messagebox
    def alert_errors(self, string):
        tk.messagebox.showinfo("Input Error", string)


# Analysis Class
class AnalysisPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Analysis", font="LARGE_FONT")
        label.grid(row=0, column=0)

        var = IntVar()
        # Order items by units sold
        units_sold_radio = Radiobutton(self,
                                       text="Save Units Sold to file",
                                       variable=var,
                                       value=1,
                                       command=lambda: db_controller.show_best_selling_units())
        # Order items by gross sales
        gross_sales_radio = Radiobutton(self,
                                       text="Save Gross Sales to file",
                                       variable=var,
                                       value=2,
                                       command=lambda: db_controller.show_best_gross_units())
        # Order items by net sales
        net_sales_radio = Radiobutton(self,
                                       text="Save Net Sales to file",
                                       variable=var,
                                       value=3,
                                       command=lambda: db_controller.show_best_net())

        # Treeview
        self.analysis_tree = ttk.Treeview(self)
        self.analysis_tree["columns"] = ("type", "desc", "unit_cost", "quant", "price", "total_sold")
        #Merch ID
        # blank column on left
        #Type
        self.analysis_tree.column("type", width=100)
        self.analysis_tree.heading("type", text="Type")
        #Description
        self.analysis_tree.column("desc", width=300)
        self.analysis_tree.heading("desc", text="Description")
        #Unit Cost
        self.analysis_tree.column("unit_cost", width=80)
        self.analysis_tree.heading("unit_cost", text="Unit Cost")
        #Quantity
        self.analysis_tree.column("quant", width=80)
        self.analysis_tree.heading("quant", text="Quantity")
        #Price
        self.analysis_tree.column("price", width=80)
        self.analysis_tree.heading("price", text="Price")
        #Total Sold
        self.analysis_tree.column("total_sold", width=80)
        self.analysis_tree.heading("total_sold", text="Total Sold")

        #--Grid Layout--
        units_sold_radio.grid(row=2, column=3, sticky="w")
        gross_sales_radio.grid(row=3, column=3, sticky="w")
        net_sales_radio.grid(row=4, column=3, sticky="w")
        self.analysis_tree.grid(row=5, column=3, columnspan=7, sticky="ew")

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
app.geometry("1160x500")
app.mainloop()