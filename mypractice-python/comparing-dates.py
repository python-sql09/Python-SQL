# 17.11 Comparing dates
import datetime
d1 = datetime.datetime(year=2013,month=12,day=4)
d2 = datetime.datetime(year=2014,month=3,day=12)
print(d1 > d2) # check if d1 is more recent than d2
print(d1 < d2)
print(d1 == d2)