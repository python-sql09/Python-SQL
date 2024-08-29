# 22.14 finally
try:
    f = open("data/text.txt", "r")
    # file does not exist so this line throws a FileNotFound exception
    print(len(f.read()))
    # This except statement runs only if Python does not find the file
except IOError as e:
    print("Oops! File Not Found.")
    # This finally statement runs whether or not Python finds
    # the file
finally:
    print("Thanks for trying!")