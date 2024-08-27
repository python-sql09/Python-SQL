import os
print(os.getcwd())
with open("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/working-with-text.txt", "r") as file:
    content = file.read()
    print(content)