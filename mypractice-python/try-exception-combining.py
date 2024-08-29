# 22.7 Combining exceptions
a = 1
b = 'c'
try:
    x = a/b
except (ZeroDivisionError,TypeError) as e:
    print("Input is not a valid number")
    print(format(e))