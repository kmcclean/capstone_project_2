from src.DBManager import DBManager

class Controller:
    db = DBManager()

    def start_db_manager(self):
        self.db = DBManager()
        self.db.startup_database()
        self.db.add_test_data()

    #This gets the information from the database and puts it into the form that will be needed by the
    def get_merch_info_for_merch_window(self):
        list_of_merch_tuples = self.db.get_table_data("merchandise")
        list_of_merch_list = []
        #This puts the items into a list, organized by the way they'll be needed for the merchandise_screen.
        for item in list_of_merch_tuples:
            item_list=[]
            item_list.append(item[0])
            item_list.append(item[1])
            item_list.append("")
            item_list.append(item[3])
            item_list.append(item[4])
            item_list.append(item[2])
            item_list.append(item[5])
            list_of_merch_list.append(item_list)

        return list_of_merch_list

    def get_sales_info_for_sales_window(self):
        list_of_sales_tuples = self.db.get_table_data("sales")
        list_of_sales_list = []
        #This puts the items into a list, organized by the way they'll be needed for the sales_screen.
        for item in list_of_sales_tuples:
            item_list=[]
            item_list.append(item[0])
            item_list.append(item[1])
            item_list.append("")
            item_list.append("")
            item_list.append(item[2])
            item_list.append(item[4])
            item_list.append(item[3])
            list_of_sales_list.append(item_list)

        return list_of_sales_list

    def get_tour_info_for_tour_window(self):
        list_of_tour_tuples = self.db.get_table_data("tour_schedule")
        list_of_tour_list = []
        #This puts the items into a list, organized by the way they'll be needed for the sales_screen.
        for item in list_of_tour_tuples:
            item_list=[]
            item_list.append(item[0])
            item_list.append(item[1])
            item_list.append("")
            item_list.append("")
            tour_address = item[1] + " " + item [2] + ", " + item[3] + " " + item [4]
            item_list.append(tour_address)
            item_list.append(item[6])
            item_list.append(item[8])
            item_list.append(item[7])
            list_of_tour_list.append(item_list)

        return list_of_tour_list

    def show_all(self):
        self.db.show_all()

    def close_database(self):
        self.db.close_database()