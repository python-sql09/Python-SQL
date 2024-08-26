# 17.15 Checking multiple timestamps
import datetime
d_now = datetime.datetime.now()
now_stamp = datetime.datetime.timestamp(d_now)
print(d_now)
print(now_stamp)
print("------")
for ctr in range(0, 10):
    for ctr2 in range(0, 1000000):
        x = 1 # doing something to take some time...
        x = x + 1
    print(".")
d_later = datetime.datetime.now()
later_stamp = datetime.datetime.timestamp(d_later)
print(d_later)
print(later_stamp)
print("------")
print(later_stamp - now_stamp)