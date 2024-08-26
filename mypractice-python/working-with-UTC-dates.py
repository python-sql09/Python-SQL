# 17.13 Working with UTC dates
import datetime
time_utc_now = datetime.datetime.utcnow()
print(time_utc_now)
print("------")
print(time_utc_now.year)
print(time_utc_now.month)
print(time_utc_now.day)
print(time_utc_now.hour)
print(time_utc_now.minute)
print(time_utc_now.second)
print(time_utc_now.microsecond)
print(time_utc_now.tzinfo)