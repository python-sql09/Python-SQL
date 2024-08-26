# 17.18 What’s the date?
import datetime
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))
d1 = datetime.datetime(year,month,day)
dnow = datetime.datetime.now()
days_passed = dnow - d1
if days_passed.days < 0:
    past_date = dnow + datetime.timedelta(days_passed.days)
    print("That date is " + str(abs(days_passed.days)) +
        " days in the future. " + str(abs(days_passed.days)) +
        " days ago, the date was " + str(past_date.date())+".")
elif days_passed.days > 0:
    future_date = dnow + datetime.timedelta(days_passed.days)
    print("That date was " + str(abs(days_passed.days)) +
        " days ago. In " + str(abs(days_passed.days)) +
        " days, the date will be " + str(future_date.date())+".")
elif days_passed.days == 0:
    future_date = dnow + datetime.timedelta(weeks=26)
    print("That's today! In six months, the date will be " +
        str(future_date.date())+".")
    