# 18.14 Overwriting a file
f = open("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/test_file.txt", "w")
f.write("This will overwrite whatever existed in the file.")
f.close()