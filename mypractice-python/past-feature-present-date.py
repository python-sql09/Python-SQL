# 17.12 Past, future, or present?
import datetime
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))
d1 = datetime.date(year,month,day)
today = datetime.datetime.today().date()
if d1 > today:
    print("That date is in the future.")
elif d1 < today:
    print("That date is in the past.")
elif d1 == today:
    print("That date is today!")