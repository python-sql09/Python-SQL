# 13.5 Using defaulted parameter values
def display(message="Hello Customer"):
    print(str(message))
# we can use the display method to print several messages.
display("Hello World")
display()
#Default value will be used
display(True)