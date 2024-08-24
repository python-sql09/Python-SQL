# 17.2 Prompting for a date
# user_date = datetime.date(int(year),int(month),int(day))
import datetime
year = input("Please enter a year from 1900 to 2100: ")
while True:
    if int(year) >= 1900 and int(year) <= 2100:
        break
else:
    year = input("Please enter a VALID year from 1900 to 2100: ")
month = input("Please enter a month from 1 to 12: ")
while True:
    if int(month) >= 1 and int(month) <= 12:
        break
else:
    month = input("Please enter a VALID month from 1 to 12: ")
day = input("Please enter a day from 1 to 31: ")
while True:
    if int(day) >= 1 and int(day) <= 31:
        break
    else:
        day = input("Please enter a VALID day from 1 to 31: ")
user_date = datetime.date(int(year),int(month),int(day))
print(user_date)