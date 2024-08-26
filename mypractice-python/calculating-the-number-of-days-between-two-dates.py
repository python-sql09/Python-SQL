# 17.17 Calculating the number of days between two dates
import datetime
d_now = datetime.datetime.now()
d_other = datetime.datetime(2021,1,1)
print(d_now)
print(d_other)
days_passed = d_now - d_other
print(days_passed)
print(days_passed.days)