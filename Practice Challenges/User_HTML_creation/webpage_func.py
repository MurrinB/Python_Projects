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
import webpage_gui
import webpage_main


# define function to create webpage on button click
def OnClick(self):
    getEntry = self.txt_slogan.get()
    htmlWeb = open("NewIndex.html", "w")
    htmlWeb.write(""" <html> \
                          <body> \
                              <h1> \
                              {} \
                              </h1> \
                          </body> \
                        </html>
                        """.format(getEntry))
    htmlWeb.close()


    webbrowser.open_new_tab('NewIndex.html')
