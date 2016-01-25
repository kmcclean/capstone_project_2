__author__ = 'casey'
from tkinter import *


class GUI():

    # Initialize GUI elements
    def __init__(self, master):


        top_frame = Frame(master, width=600, height=200)
        bottom_frame = Frame(master, width=600, height=200)
        top_frame.pack()
        bottom_frame.pack()

        self.print_button = Button(top_frame, text="Print", command=self.printMessage)
        self.print_button.pack(side="left")

        self.quit_button = Button(top_frame, text='Quit', command=top_frame.quit)
        self.quit_button.pack(side="left")

    # Test function
    def printMessage(self):
        print("Nice!")

window = Tk()

gui = GUI(window)

# Makes sure window constantly displays until window is closed
window.mainloop()

