import datetime as dt
now = dt.datetime.now()
print(now)
year = now.year
print(year)
day_of_weak = now.weekday() #print the current day in the weak
print(day_of_weak)


date_of_birth = dt.datetime(year=2004,month=3,day=6)
print(date_of_birth.strftime("%A")) # it will return the day of the date
print(date_of_birth.strftime("%a")) # day in shortcut
print(date_of_birth.strftime("%B")) # return month in letter
print(date_of_birth.strftime("%m")) #return the month number
print(date_of_birth.strftime("%Y"))# print year
print(date_of_birth.strftime("%y")) #last 2 digit of year
