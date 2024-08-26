# 17.21 Using only time without a date
import datetime
# we create a time object, for 1:45:30 pm, using 24-hour time format
t = datetime.time(13,45,30)
print(t)
print(type(t))
current_time = datetime.datetime.now().time()
print(current_time)
print(type(current_time))