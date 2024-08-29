# 21.20 Finding the highest value in a collection of values
from functools import reduce
list_numbers = [1,20,300,560,4]
max_element =reduce(lambda a,b : a if a > b else b,list_numbers)
print(max_element)