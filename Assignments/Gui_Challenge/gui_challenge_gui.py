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
    self.btn_browse1 = tk.Button(self.master,width=18,height=1,text='Browse Source File',command=lambda: gui_challenge_func.OnClick(self))
    self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(50,5),sticky=S+W)
    

    self.btn_browse2 = tk.Button(self.master,width=18,height=1,text='Browse Destination File', command=lambda: gui_challenge_func.OnClick2(self))
    self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(5,5),sticky=S+W)

    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check For Files', command=lambda: gui_challenge_func.Check_File(self))
    self.btn_check.grid(row=3,column=0,rowspan=2,padx=(25,0),pady=(5,50),sticky=S+W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Transfer Files', comman=lambda: gui_challenge_func.file_Transfer(self))
    self.btn_close.grid(row=3,column=5,rowspan=2,padx=(25,5),pady=(5,50),sticky=S+E)

    # Create input spaces
    self.txt_browse1 = tk.Entry(self.master,width=50,text='')
    self.txt_browse1.grid(row=1,column=1,columnspan=5,padx=(25,5),pady=(50,0))

    self.txt_browse2 = tk.Entry(self.master,width=50,text='')
    self.txt_browse2.grid(row=2,column=1,columnspan=5,padx=(25,5),pady=(0,0))

    # create listbox for files
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lst_listbox = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.scrollbar1.config(command=self.lst_listbox.yview)
    self.scrollbar1.grid(row=4,column=7,rowspan=3,padx=(0,0),pady=(0,0),sticky=E)
    self.lst_listbox.grid(row=4,column=0,rowspan=3,columnspan=6,padx=(50,25),pady=(80,0),sticky=N+E+W+S)
    
    

    
                          

if __name__ == '__main__':
    pass

