# 21.17 Using reduce and a lambda to calculate a sum
from functools import reduce
value_list = []
while True:
    user_input = input("Enter the deposits to add to the series to sum [type quit to exit]: ")
    if user_input.lower() == 'quit':
        break
    else:
        value_list.append(int(user_input))
product = reduce(lambda x, y: x + y,value_list)
print("The total is: " + str(product))