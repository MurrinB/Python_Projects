#
# Create simple window with tkinter thats has 4 buttons and two input areas
#
# Author: Britnee Murrin
#

# import all needed libraries
from tkinter import *
import tkinter as tk
import tkinter.filedialog
import shutil
import os
import time

# import associated files
import gui_challenge_gui
import gui_challenge

# Create method to retain user's selected file path
def OnClick(self):
    path = tk.filedialog.askdirectory()
    return self.txt_browse1.insert(0,path)
    
def OnClick2(self):
    path = tk.filedialog.askdirectory()
    return self.txt_browse2.insert(0,path)

# create method to transfer files
#

# define seconds variable for later use
seconds_in_day = 24 * 60 * 60

# Get current date without the seconds in the day for comparison
currentDate = time.time()
currentDate_mod = currentDate - seconds_in_day

# create method to get the modification date of each file 
def file_Mod_Time(file):
    return os.path.getmtime(file)
    


# Create loop to iterate through files
def file_Transfer(self):
    source = self.txt_browse1.get()# set where the source of the files are
    destination = self.txt_browse2.get()# set the destination path
    FolderA = os.listdir(source)# list files in source folder
    for file in FolderA:
        src_file = os.path.join(source, file)
        if file_Mod_Time(src_file) > currentDate_mod: # loop to compare the modification date with the current date
            dst_file = os.path.join(destination, file)
            shutil.move(src_file, dst_file) # transfer to destination folder

def Check_File(self):
    source = self.txt_browse1.get()# set where the source of the files are
    FolderA = os.listdir(source)# list files in source folder
    for file in FolderA:
        src_file = os.path.join(source, file)
        if file_Mod_Time(src_file) > currentDate_mod:
            self.lst_listbox.insert(0,file)
