# 8.29 Copy a list
a = [1,2,3]
b = []
for i in a:
    b.append(i)
print(a)
print(b)
a[0]=0
print(a)
print(b)