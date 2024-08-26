# 18.2 Opening a the flatland01.txt file
# Open our file in read mode
#f = open("data/flatland01.txt", mode="r")
# f = open("/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/open-flatland01-file.txt", mode="r") 
f = open("/data/open-flatland01-file.txt", mode="r")
# Read and display text file
print(f.read())
# Close our file resource
f.close()