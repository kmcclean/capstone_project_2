__author__ = 'casey'

from src.MainWindow import MainWindow
from src.Controller import Controller
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

    def start_gui(self):
        mw = MainWindow()


m = Main()
m.run()