# 22.5 Adding muiltiple exceptions
import sys
a = 1
b = 'c'
try:
    x = a/b
# if we have a division by zero, this block will execute
except ZeroDivisionError as e:
    print("Oops, ZeroDivisionError! We cannot divide a number by zero. Try again...")
# if we have an error type (a non-­valid integer such as char or string), this block will
# execute
except TypeError as t:
    print("Oops, TypeError! That was not a valid number. Try again...")
# the following will execute if the try statement fails with a different exception from
# those above
except:
    print("Unexpected error. Try again.", sys.exc_info()[0])
    raise