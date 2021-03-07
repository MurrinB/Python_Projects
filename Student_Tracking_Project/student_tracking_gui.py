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

# import other modules that associate with this gui module
import student_tracking_main
import student_tracking_func

# create func to build the app interface
def load_gui(self):

    # create labels and input boxes (location and size)
    self.lbl_fname = tk.Label(self.master,text='First Name: ')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_lname = tk.Label(self.master,text='Last Name: ')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_phone = tk.Label(self.master,text='Phone Number: ')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_email = tk.Label(self.master,text='Email: ')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_course = tk.Label(self.master,text='Current Course: ')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_students = tk.Label(self.master,text='Student List: ')
    self.lbl_students.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    # create student list box with scroll bar
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.studentList = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.studentList.bind('<<ListboxSelect>>',lambda event: student_tracking_func.onSelect(self,event))
    self.scrollbar1.config(command=self.studentList.yview)
    self.scrollbar1.grid(row=1,column=7,rowspan=9,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.studentList.grid(row=1,column=2,rowspan=9,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    # create buttons submit/delete
    self.btn_submit = tk.Button(self.master,width=12,height=2,text="Submit",command=lambda: student_tracking_func.addToList(self))
    self.btn_submit.grid(row=10,column=1,padx=(25,0),pady=(45,10),sticky=W)

    self.btn_delete = tk.Button(self.master,width=12,height=2,text="Delete",command=lambda: student_tracking_func.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(25,0),pady=(45,10),sticky=W)

    # use functions to clear boxes and manage database
    student_tracking_func.create_db(self)
    student_tracking_func.onRefresh(self)

# make sure the app is running from the main.py doc and not this one
if __name__ == "__main__":
    pass 

    

    
    

