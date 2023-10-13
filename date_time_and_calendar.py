from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import calendar

# Today's date and time
dt = datetime.now()
print("The current date and time: " + str(dt))

# Today's date
d = dt.strftime("%A the %dth of %B %Y")
print("Today's date: "  + str(d))

# The current time
t = dt.strftime("%X")
print("The time: " + str(t) + "\n")

# The value of one week's time
one_week = timedelta(weeks=1)
print("A timedelta of one week: " + str(one_week) + "\n")


# How many days until Christmas?

today = date.today()
#today = date(date.today().year, 12, 26)
# Creating a date
christmas = date(date.today().year, 12, 25)

# Check to see Christmas hasn't past yet this year
if today > christmas:
    christmas = christmas + timedelta(days=365)

days_to_christmas = christmas - today
print("It's " + str(days_to_christmas) + " until Christmas.\n")


# Calendars

# Create a text calendar for 2020
#cal = calendar.TextCalendar(calendar.MONDAY)
#st = cal.formatyear(2020)
#print(st)  


# What are the dates of every first Saturday of the month in 2021? 

print("The first Saturday of every month in 2021:")
for m in range(1, 13):
    # iterate over the months of 2021 and create an array of weeks
    c = calendar.monthcalendar(2021, m)
    # see if the first Saturday of the month is in the first or second week
    week_one = c[0]
    week_two = c[1]
    if week_one[calendar.SATURDAY] != 0:
        first_sat = week_one[calendar.SATURDAY]
    else:
        first_sat = week_two[calendar.SATURDAY]        
    # formatting
    if first_sat == 1 or first_sat == 21 or first_sat == 31:
        suffix = "st"
    elif first_sat == 2 or first_sat == 22:
        suffix = "nd"
    elif first_sat == 3 or first_sat == 23:
        suffix = "rd"
    else:
        suffix = "th"
        
    print('  ' + str(first_sat) + suffix + ' ' + calendar.month_name[m] )
        
    



