#
# Create simple window with tkinter thats has 4 buttons and two input areas
#
# Author: Britnee Murrin
#

from tkinter import *
import tkinter as tk

import gui_challenge
import gui_challenge_func

def load_gui(self):
    # Create button and location
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: gui_challenge_func.OnClick(self))
    self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(50,5),sticky=S+W)
    

    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(5,5),sticky=S+W)

    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_check.grid(row=3,column=0,rowspan=2,padx=(25,0),pady=(5,50),sticky=S+W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=3,column=5,rowspan=2,padx=(25,5),pady=(5,50),sticky=S+E)

    # Create input spaces
    self.txt_browse1 = tk.Entry(self.master,width=50,text='')
    self.txt_browse1.grid(row=1,column=1,columnspan=5,padx=(25,5),pady=(50,0))

    self.txt_browse2 = tk.Entry(self.master,width=50,text='')
    self.txt_browse2.grid(row=2,column=1,columnspan=5,padx=(25,5),pady=(0,0))
                          

if __name__ == '__main__':
    pass

