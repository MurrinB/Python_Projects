#
# Create a program that transfers files from one folder to another
# program iterates through files to transfer files only modified current day
#

import shutil
import os
import time

# set where the source of the files are
source = '/Users/Britnee Murrin/OneDrive/Desktop/FolderA/'

# set the destination path
destination = '/Users/Britnee Murrin/OneDrive/Desktop/FolderB/'


seconds_in_day = 24 * 60 * 60

# list files in source folder
FolderA = os.listdir(source)

# Get current date without the seconds in the day for comparison
currentDate = time.time()
currentDate_mod = currentDate - seconds_in_day

# create method to get the modification date of each file 
def file_Mod_Time(file):
    return os.path.getmtime(file)


# Create loop to iterate through files 
for file in FolderA:
    src_file = os.path.join(source, file)
    if file_Mod_Time(src_file) > currentDate_mod: # loop to compare the modification date with the current date
        dst_file = os.path.join(destination, file)
        shutil.move(src_file, dst_file) # transfer to destination folder
