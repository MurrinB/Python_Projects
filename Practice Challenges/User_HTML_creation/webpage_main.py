# Python Ver: 3.9
#
# Author: Britnee Murrin
#
# Purpose: create a user interface to create a one line webpage, using Tkinter
#

from tkinter import *
import tkinter as tk
import webbrowser

# import associated module files
import webpage_gui
import webpage_func

# create user window
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        # define window configuration
        self.master = master
        self.master.minsize(400,125)
        self.master.maxsize(400,125)
        self.master.title("Create Webpage!")
        self.master.configure(bg="lightblue")

        # load in widgets from gui module
        webpage_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
