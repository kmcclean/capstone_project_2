__author__ = 'casey'
from src.DBManager import DBManager
from src.MainWindow import MainWindow
class Main():


    def run(self):
        #Comment
        # db = DBManager()
        # db.startup_database()
        # db.add_test_data()
        # db.show_all()
        self.start_gui
        # db.show_all()
        # db.show_best_units_sold_gross()
        # db.show_best_units_sold_net()
        # db.close_database()
        print("Database closed.")

    def start_gui(self):
        mw = MainWindow()


m = Main()
m.run()