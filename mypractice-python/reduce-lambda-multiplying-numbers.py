# 21.16 Multiplying numbers together
from functools import reduce
list_numbers = [2, 4, 6, 8]
product = reduce(lambda x, y: x * y,list_numbers) # 2 * 4 * 6 * 8 = 384
print(type(product))
print(product) 