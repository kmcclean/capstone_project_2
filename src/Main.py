__author__ = 'casey'

from src.MainWindow import MainWindow
class Main():

    # runs the program.
    def run(self):
        self.start_gui()

    #starts the gui
    def start_gui(self):
        mw = MainWindow()


m = Main()
m.run()