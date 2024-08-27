# 19.13 Writing multiple rows to a file at once
import csv
dataset = [["EMP9807976877","vicki","gallegos"],["EMP9807976872","hector","bowen"],
["EMP4564564598","cassandra","wang"]]
# open file in append mode, which will add the data at the end of the file
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'a') as csv_file:
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter=',')
    # write multiple rows at once using writerows
    writer.writerows(dataset)
f = open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'r')
print(f.read())
f.close()