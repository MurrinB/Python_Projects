#
# Create a program that transfers files from one folder to another
#

import shutil
import os

# set where the source of the files are
source = '/Users/Britnee Murrin/OneDrive/Desktop/FolderA/'

# set the destination path
destination = '/Users/Britnee Murrin/OneDrive/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
