# 22.11 Using the general IOError exception
try:
    f = open("data/another_file_do_not_exist.txt", "r")
    print(f.read())
    f.close()
except IOError as e:
    print("Oops! File Not Found.")
    print(format(e))