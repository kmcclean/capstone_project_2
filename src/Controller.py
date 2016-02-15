from src.DBManager import DBManager
from src.Analyzer import Analyzer


class Controller:
    db = DBManager()
    an = Analyzer

    def add_new_merch(self, new_merch_info):
        return self.db.add_new_merchandise(new_merch_info)

    def add_tour_date(self, tour_date_info):
        return self.db.add_new_tour_date(tour_date_info)

    def start_db_manager(self):
        self.db = DBManager()
        self.db.drop_database()
        self.db.startup_database()
        self.db.add_test_data()

        self.db.show_all()
        self.db.table_check()

    # This gets the information from the database and puts it into the form that will be needed by the merchandise GUI.
    def get_merch_info_for_merch_window(self):
        list_of_merch_tuples = self.db.get_table_data("merchandise")
        list_of_merch_list = []

        #This is stuff
        # This puts the items into a list, organized by the way they'll be needed for the merchandise_screen.
        for item in list_of_merch_tuples:
            item_list=[]
            item_list.append(item[0])
            item_list.append(item[1])
            item_list.append(item[3])
            item_list.append(item[4])
            item_list.append(item[2])
            item_list.append(item[5])
            list_of_merch_list.append(item_list)

        return list_of_merch_list

    def get_sales_info_for_sales_window(self):
        list_of_sales_tuples = self.db.get_table_data("sales")
        list_of_sales_list = []

        # This puts the items into a list, organized by the way they'll be needed for the sales_screen.
        for item in list_of_sales_tuples:
            item_list=[]
            item_list.append(item[0])
            item_list.append(item[1])
            item_list.append(item[2])
            item_list.append(item[4])
            item_list.append(item[3])
            list_of_sales_list.append(item_list)

        return list_of_sales_list

    def get_tour_info_for_tour_window(self):
        list_of_tour_tuples = self.db.get_table_data("tour_schedule")
        list_of_tour_list = []

        # This puts the items into a list, organized by the way they'll be needed for the tour_screen.
        for item in list_of_tour_tuples:
            item_list=[]
            item_list.append(item[0])
            item_list.append(item[7])
            item_list.append(item[6])
            item_list.append(item[5])
            item_list.append(item[1])
            item_list.append(item[2])
            item_list.append(item[3])
            item_list.append(item[4])
            item_list.append(item[8])
            item_list.append(item[10])
            item_list.append(item[9])
            list_of_tour_list.append(item_list)

        return list_of_tour_list

    def show_all(self):
        self.db.show_all()

    def show_best_selling_units(self):
        best_selling = self.db.show_best_units_sold()
        #self.an.best_units_total(best_selling)

    def show_best_gross_units(self):
        best_gross = self.db.show_best_units_sold_gross()
        # self.an.best_units_gross(best_gross)

    def show_best_net(self):
        best_net = self.db.show_best_units_sold_net()
        # self.an.best_units_net(best_net)

    def close_database(self):
        return self.db.close_database()