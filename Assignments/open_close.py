# Create a program that checks whether the businesses are open or closed
#
# Author: Britnee Murrin
#

from datetime import datetime
from pytz import timezone

# Timezones PST, EST, GMT

timeFormat = "%H:%M"

# create a variable for each cities current time
timeNow_Pacific = datetime.now(timezone('US/Pacific'))
Portland = timeNow_Pacific.strftime(timeFormat + ' is the time in Portland')


timeNow_NewYork = datetime.now(timezone('America/New_York'))
New_York = timeNow_NewYork.strftime(timeFormat + ' is the time in New York')


timeNow_London = datetime.now(timezone('GMT'))
London = timeNow_London.strftime(timeFormat + ' is the time in London')

# Create a list of the times to iterate through at anytime 
City_Tuple = (Portland, New_York, London)

# Create a loop to iterate through the tuple 
i = 0 
while i < len(City_Tuple):
    # Create a loop to compare the local times and display if the particular branch is open/closed
    if City_Tuple[i] >= '09:00' and City_Tuple[i] <= '17:00':
        print("{}. This branch is Open".format(City_Tuple[i]))

    else:
        print("{}. This branch is Closed".format(City_Tuple[i]))
    i = i + 1
    




      

      

