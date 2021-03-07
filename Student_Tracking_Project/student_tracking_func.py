# Python Ver: 3.9
#
# Author: Britnee Murrin
#
# Purpose: To create a user interface for a database of students:
#           with their contact information and current course. Using Tkinter.
#
# Tested OS: This code was written and tested on Windows 10
#

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

# import other modules that associate with this func module
import student_tracking_gui
import student_tracking_main

# create functions to run the app close/submit/delete/refresh/senter/create_db/etc
def center_window(self, w, h):
    # get users screen width/height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calc coordinates of screen to display in center
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# window pop up to confirm close after user press 'X'
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to exit application?"):
        # close app
        self.master.destroy()
        os._exit(0)

# create database and table to store student info
def create_db(self):
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

# create first run data to get database running properly
def first_run(self):
    data = ('Britnee', 'Murrin', 'Britnee Murrin', '625-303-3445', 'bmurrin@gmail.com', 'Python Course')
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",
                        (data))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count

# functions for selecting list box item
def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
        varBody = cur.fetchall()
        # return tuple
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

# create submitting function
def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize for db consistancy
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format.")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and(len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('student.db')
        with conn:
            cur = conn.cursor()
            # check db for fullname, if so alert user
            cur.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
            count = cur.fetchone()[0]
            chkName = count
            if chkName == 0: # if == 0 new data will be added
                cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",
                           (var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.studentList.insert(END, var_fullname) # update listbox with new fullname and course
                onClear(self) # clear textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database, Please choose different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that all fields are filled.")

# create delete function
def onDelete(self):
    var_select = self.studentList.get(self.studentList.curselection())
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        # unable to delete last record. Check to make sure user isn't deleting last record
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information for ({}) \nwill be permenantly deleted from databse. \nWould you like to proceed with delete request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('student.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # clear text boxes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record before trying to delete the last record.".format(var_select))
    conn.close()

def onDeleted(self):
    # clear textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    try:
        index = self.studentList.curselection()[0]
        self.studentList.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    self.studentList.delete(0,END)
    conn = sqlite3.connect('student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SELECT col_fullname FROM tbl_students""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.studentList.insert(0,str(item))
                i = i + 1
    conn.close()

# make sure the app is running from the main.py doc and not this one
if __name__ == "__main__":
    pass 

    
    
    
                            
        
    
