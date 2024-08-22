'''def display(message1, message2 = "Hello World"):
    print(str(message1) + str(message2))
# this will throw an error because the parameter with the default
# value precedes the parameter that does not have a default value
def display2(message1 = "Hello World", message2):
    print(str(message1) + str(message2))'''
# 13.7 Order matters with default parameters
def display(message1, message2="Hello World"):
    print(str(message1) + str(message2))
# Call the function
display("Hi, ")

def display2(message1, message2="Hello World"):
    print(str(message1) + str(message2))
# Call the function
display2("Hi, ")
