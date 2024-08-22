# 13.8 Variable amount of information passed to a function
def display_customer_input(*argv):
    for arg in argv:
        print(arg)
customer_1 = ["John", "Doe", "Programmer", "80000"]
customer_2 = ["Jane", "Doe", "Scientist", "80000"]
customer_3 = ["Charles", "Painter"]
display_customer_input(*customer_1)
print("------")
display_customer_input(*customer_2)
print("------")
display_customer_input(*customer_3)