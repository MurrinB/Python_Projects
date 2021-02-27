# Create a database and use python to communicate with sqlite3 to preform a query on a DB

import sqlite3

conn = sqlite3.connect('assignment.db') # Create new DB

with conn :
    cur = conn.cursor() # Connect to DB to create a table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit() # commit changes to DB
conn.close() # close connection with DB 

# create tuple of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


conn = sqlite3.connect('assignment.db') # open connection 
# loop through each object in the tuple for the .txt files
for txt in fileList:
    if txt.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # Add .txt files to tbl_assignment 
            cur.execute("INSERT INTO tbl_assignment (col_file) VALUES (?)", (txt,))
            print(txt)
conn.close() 
