# 21.7 Using a lambda inside another function
def myfunc(n):
    return lambda a : a * n
doubler = myfunc(2) # we set the value of n
print(doubler(11)) # we set the value of a