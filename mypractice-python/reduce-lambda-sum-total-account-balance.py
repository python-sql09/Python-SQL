# 21.19 Summing the total account balance
from functools import reduce
value_list = []
prev_bal = int(input("Enter your previous balance: "))
while True:
    user_input = input("Enter the deposits to add to the series to sum [type quit to exit]: ")
    if user_input.lower() == 'quit':
        break
    else:
        value_list.append(int(user_input))
product = reduce(lambda x, y: x + y,value_list,prev_bal)
print("New balance is: " + str(product))