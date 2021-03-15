#
# Create simple window with tkinter thats has 4 buttons and two input areas
#
# Author: Britnee Murrin
#

from tkinter import *
import tkinter as tk

import gui_challenge_gui
import gui_challenge_func

# Create window
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs): 
        Frame.__init__ (self, master, *args, **kwargs)

        # Frame configuration
        self.master = master
        self.master.minsize(500,450)
        self.master.maxsize(500,450)
        self.master.title("Easy File Transfer")

        # load gui widgets from a seperate module
        gui_challenge_gui.load_gui(self)


# establish order for Python to run code        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
