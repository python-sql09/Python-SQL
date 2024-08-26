# 17.10 Creating a custom date with named parameters
import datetime
t1 = datetime.date(year=2013, day=4, month=12)
t2 = datetime.date(year=2013, month=12, day=4)
t3 = datetime.date(day=4, year=2013, month=12)
t4 = datetime.date(day=4, month=12, year=2013)
t5 = datetime.date(month=12, year=2013, day=4)
t6 = datetime.date(month=12, day=4, year=2013)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)