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
import webpage_main
import webpage_func

# define user interface design and structure
def load_gui(self):

    # create label/button/input area and their locations
    self.lbl_slogan = tk.Label(self.master,text='Enter Your Slogan Here: ')
    self.lbl_slogan.grid(row=0,column=0,columnspan=2,padx=(25,0),pady=(10,0),sticky=N+W)
    self.lbl_slogan.configure(bg='lightblue')

    self.txt_slogan = tk.Entry(self.master,width=50,text='')
    self.txt_slogan.grid(row=1,column=1,columnspan=3,rowspan=2,padx=(50,30),pady=(10,0),sticky=N+S+E+W)

    self.btn_create = tk.Button(self.master,width=12,height=1,text='Create Webpage')
    self.btn_create.grid(row=4,column=3,padx=(25,0),pady=(10,50))

if __name__ == "__main__":
    pass
