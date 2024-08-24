# 17.7 Splitting the time
d = "2022-07-23 11:26:26.047342"
(d,t) = d.split()
(hour, minute,second) = t.split(":")
print(hour)
print(minute)
print(second)