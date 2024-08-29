# 21.18 Starting with an initial value
from functools import reduce
list_numbers = [2, 4, 6, 8]
product = reduce(lambda x, y: x * y,list_numbers,5) #initial value = 5
print(type(product))
print(product) # 5 * 2 * 4 * 6 * 8 = 1920