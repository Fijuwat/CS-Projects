# File: DaysInMonth.py
# Student: Ting Wei Wu
# UT EID: tw28634
# Course: CS303E
# 
# Date: February 14, 2022
# Description of Program: This program is meant to find out how many days are in a specific month in a specific month.


# User input
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

# Set variables
days = 0 
monthName = ""

# If and elif and else statement
if month == 1:
  days = 31
  monthName = "January"
elif month == 2:
  if year%4 == 0 and year%100 != 0:
    days = 29
  elif year%400 == 0:
    days = 29
  else:
    days = 28
  monthName = "February"
elif month == 3:
  days = 31
  monthName = "March"
elif month == 4:
  days = 30
  monthName = "April"
elif month == 5:
  days = 31
  monthName = "May"
elif month == 6:
  days = 30
  monthName = "June"
elif month == 7:
  days = 31
  monthName = "July"
elif month == 8:
  days = 31
  monthName = "August"
elif month == 9:
  days = 30
  monthName = "September"
elif month == 10:
  days = 31
  monthName = "October"
elif month == 11:
  days = 30
  monthName = "November"
else:
  days = 31
  monthName = "December"

# Print out my result 
print(monthName, year, "has", days, "days")


