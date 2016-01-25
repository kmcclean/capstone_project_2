__author__ = 'casey'

from tkinter import *


class GuiTesting():

    def welcome(self):
        print("Welcome!")

    # GUI window
    window = Tk()

    # Frames for top and bottom of window
    topFrame = Frame(window, width=600, height=200)
    topFrame.pack()

    bottomFrame = Frame(window, width=600, height=200)
    bottomFrame.pack(side=BOTTOM)

    # Widgets

    # Example of name/pass in grid layout
    name_label = Label(topFrame, text="Name")
    password_label = Label(topFrame, text="Password")
    c = Checkbutton(topFrame, text="Keep me logged in")

    # Example of handling events with buttons
    # Button(location, text, function)
    login = Button(topFrame, text="Login", command="welcome")
    # Optional method
    # NOTE: function needs "event" parameter
    # login.bind("<Button-1>", welcome)

    # Entries take user input
    name_entry = Entry(topFrame)
    pass_entry = Entry(topFrame)

    # Grid layout parameters(row, column, sticky=(N,E,S,W))
    name_label.grid(row=0, sticky=E)
    password_label.grid(row=1, sticky=E)

    name_entry.grid(row=0, column=1)
    pass_entry.grid(row=1, column=1)
    c.grid(columnspan=2)
    login.grid(columnspan=2)


    # Makes sure window constantly displays until window is closed
    window.mainloop()