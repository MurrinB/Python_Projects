# Python Ver: 3.9
#
# Author: Britnee Murrin
#
# Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships.
#
# Tested OS: This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Import additional modules for access to them
import phoneBook_func
import phoneBook_gui


# Use Frame class from Tkinter to inherit from for our class
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,300) # (Height, Width)
        self.master.maxsize(500,300)
        # Center app on users screen
        phoneBook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # call protocol method to catch user click on upper corner 'X'
        self.master.protocol("WM_DELETE_WINDOW", lambda: phoneBook_func.ask_quit(self))
        arg = self.master

        # load in gui widgets from seperate created module
        phoneBook_gui.load_gui(self)

        # create menu dropdown object, menu at top of window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phoneBook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down column, tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascade parent
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        # display menu and add functionality/appearance
        self.master.config(menu=menubar, borderwidth='1')

    

# establish order for Python to run the code    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
