# new_date = starting_date + datetime.timedelta(days=0, seconds=0,
# microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# myDate = myDate + datetime.timedelta(days=3)
# 17.16 Arithmetic and dates
import datetime
print(datetime.datetime.now())
# add one day to the current datetime
d1 = datetime.datetime.now() + datetime.timedelta(days = 1)
print(d1)
# subtract 4 weeks from the current datetime
d2 = datetime.datetime.now() - datetime.timedelta(weeks = 4)
print(d2)
# add one hour to the current datetime
d3 = datetime.datetime.now() + datetime.timedelta(minutes = 60, hours=1)
print(d3)