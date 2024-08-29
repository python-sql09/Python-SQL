# 22.4 Handling FileNotFoundError
try:
    file_object = open("data/bank_transacts.txt",'r')
except FileNotFoundError as e:
    print("The file was not found")
    print("The error was:\n" + str(e))