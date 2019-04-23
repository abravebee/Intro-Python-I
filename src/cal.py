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

def calend(calIn):
  print(calIn)
  month, year = [calIn[i] for i in calIn] 
  print (month, year)
  for i in calIn:
    try:
      print(int(i))
    except:
      print("Input expects integers, please try again.")
      sys.exit()

  if len(calIn) == 0:
    print("current month")
    #print current month
  elif len(calIn) == 1:
    #render month given of current year
    print("month given of current year")
  elif len(calIn) == 2:
    print("month and year given")
    #render month and year given
  else:
    print("expected input format")
    #expected input format
    #exit program

calIn = input("calendar.py ").split(' ')
calend(calIn)
