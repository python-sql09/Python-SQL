# 22.9 Using multiple try statements
import sys
b = 0
a = 1
c = 'd'
try:
    # This will throw an exception, which will trigger an except statement
    y = a/c
    # This would also throw an exception, but python ignores it because
    # it is the second exception
    x = a/b
    print(x)
    print(y)
except ZeroDivisionError as e:
    print("Oops, ZeroDivisionError! We cannot divide by zero. Try again...")
except TypeError as t:
    print("Oops, TypeError! That was not a valid number. Try again...")
except:
    print("Unexpected error. Try again.", sys.exc_info()[0])
    raise