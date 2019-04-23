"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

##take input in from sys.argv

if len(sys.argv) > 3:
  #if they input more than 2 things
  print("You have input too many variables")
elif len(sys.argv) == 3:
  #if they input 2 things
  path, month, year = [x for x in sys.argv]
  print("month, year", month, year)
  try:
    #make sure they input numbers
    month, year = [int(month), int(year)]
    print(calendar.month(year, month))
  except:
    #if we can't cast as integers, warn
    print("There was an error. Please check your inputs and try again.")
elif len(sys.argv) == 2:
  #if they input 1 thing
  path, month = [x for x in sys.argv]
  print("month", month)
  try:
    #make sure they input a number
    month = int(month)
    year = datetime.now().year
    print(calendar.month(year, month))
  except:
    #if we can't cast as integer, warn
    print("There was an error. Please check your inputs and try again.")
else:
  #if they input nothing, return the current month
  month = datetime.now().month
  year = datetime.now().year
  print(calendar.month(year, month))