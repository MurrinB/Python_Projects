# Tech Academy Python Challenge
# Create database

import sqlite3

# Create values for table in database
rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))


with sqlite3.connect("Roster.db") as connection: # create and connect to database
    conn = connection.cursor() # gain control of database
    conn.execute("CREATE TABLE IF NOT EXISTS tbl_Roster(Name TEXT, Species TEXT, IQ INT)") # create table in database
    conn.executemany("INSERT INTO tbl_Roster VALUES(?, ?, ?)", rosterValues) #insert values into database

    conn.execute("UPDATE tbl_Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'") # change a value in table
    conn.execute("SELECT Name, IQ FROM tbl_Roster WHERE Species == 'Human'") # create a query to display certian values
    while True:
        row = conn.fetchone()
        if row is None:
            break
        print(row) # display the values in IDLE
    

    
    
