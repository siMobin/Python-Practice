# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import datetime
import calendar

# MM DD YYYY Formate...
x = input().split()

month, day, year = int(x[0]), int(x[1]), int(x[2])
# Get the day name
print(calendar.day_name[(datetime.date(year, month, day)).weekday()].upper())
