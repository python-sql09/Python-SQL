# 18.19 Checking for the entered file’s existence
import os
file_name = input("Please enter a file name to check for: ")
if os.path.exists("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/"+file_name):
    print("The file exists.")
else:
    print("The file doesn't exist.")