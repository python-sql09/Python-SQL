# value = datetime.datetime.timestamp(some_date)
# 17.14 Using timestamps
import datetime
import math
#included for the math.floor() method
d_now = datetime.datetime.now()
tstamp = math.floor(datetime.datetime.timestamp(d_now))
print(d_now)
print(tstamp)