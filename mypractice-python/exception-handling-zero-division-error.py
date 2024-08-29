# 22.3 Handling a ZeroDivisionError exception
a = 1
b = 0
try: # check that the operation is valid
    x = a/b
except ZeroDivisionError as e: # The type of exception is division by zero.
    # print a custom message when the execption occurs
    print("Oops! We cannot divide a number by zero. Try again...")
    print(format(e)) #print the exception error message