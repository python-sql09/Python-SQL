# 17.8 Splitting the date and time
import datetime
d = datetime.datetime.now()
d = str(d)
(d,t) = d.split()
(year,month,day) = d.split("-")
(hour, minute, second) = t.split(":")
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)