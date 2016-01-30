__author__ = 'casey'
from src.DBManager import DBManager

class Main():


    def run(self):
        #Comment
        db = DBManager()
        db.startup_database()
        db.add_test_data()

        db.show_best_units_sold()
        db.close_database()


m = Main()
m.run()