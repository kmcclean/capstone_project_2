from src.DBManager import DBManager

class Controller:
    db = DBManager()

    def start_db_manager(self):
        self.db = DBManager()
        self.db.startup_database()
        self.db.add_test_data()

    #This gets the information from the database and puts it into the form that will be needed by the
    def get_merch_info_for_merch_window(self):
        merch_tuples = self.db.get_merch()
        list_of_merch_list = []
        print("Merch_tuples: " + str(merch_tuples))

        #This puts the items into a list, organized by the way they'll be needed for the merchandise_screen.
        for item in merch_tuples:
            print("Merch tuple item: " + str(item))
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

    def show_all(self):
        self.db.show_all()