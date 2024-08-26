# 17.20 Days until Christmas
import datetime
dnow = datetime.date.today()
christmas = datetime.date(dnow.year,12,25)
days_until = christmas - dnow
print("Today is: ", dnow)
print("Christmas is just " + str(days_until.days) + " days away!")