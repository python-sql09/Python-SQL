# 18.18 Checking for a file’s existence
import os
if os.path.exists("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/missing_file.txt"):
    print("The file exists.")
else:
    print("The file doesn't exist.")
    
if os.path.exists("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/example.txt"):
    print("The file exists.")
else:
    print("The file doesn't exist.")