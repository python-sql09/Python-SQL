# 17.6 Splitting a date
d = "2022-07-23 11:26:26.047342"
(d,t) = d.split()
(year,month,day) = d.split("-")
print(year)
print(month)
print(day)