#
# Create simple window with tkinter thats has 4 buttons and two input areas
#
# Author: Britnee Murrin
#

from tkinter import *
import tkinter as tk
import tkinter.filedialog

import gui_challenge_gui
import gui_challenge

# Create method to retain user's selected file path
def OnClick(self):
    path = tk.filedialog.askdirectory()
    return self.txt_browse1.insert(0,path)
    
