# 21.21 Finding the lowest value
from functools import reduce
value_list = []
while True:
    user_input = input("Enter the deposits to determine the lowest deposit [type stop to exit]: ")
    if user_input.lower() == 'stop':
        break
    else:
        value_list.append(int(user_input))
if len(value_list) > 0:
    product = reduce(lambda x, y: x if y > x else y,value_list)
else:
    product = "Nothing."
print("The values you entered were: "+ str(value_list))
print("The lowest value is: " + str(product))