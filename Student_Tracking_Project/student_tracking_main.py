# Python Ver: 3.9
#
# Author: Britnee Murrin
#
# Purpose: To create a user interface for a database of students:
#           with their contact information and current course. Using Tkinter.
#
# Tested OS: This code was written and tested on Windows 10
#

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# import other modules that associate with this main module
import student_tracking_gui
import student_tracking_func

# use tkinters Frame class to inherit form for student tracking interface
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        # create master frame configuration
        self.master = master
        self.master.minsize(500,400)
        self.master.maxsize(500,400)
        # center app on users screen
        student_tracking_func.center_window(self,500,400)
        self.master.title("Student Tracking")
        self.master.configure(bg="lightblue")
        # establish the close out with the user clicking 'X'
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master

        # load in gui module
        student_tracking_gui.load_gui(self)

# establish order for Python to run code
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
