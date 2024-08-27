# 19.14 Adding dictionary objects to a CSV file
import csv
# create three rows of data; item order is not important because each dictionary
# uses keys to identify each value
row_1 = {"employee_id":"EMP4564576566","first_name":"rodney","last_name":"evans"}
row_2 = {"first_name":"lesa","last_name":"clapper","employee_id":"EMP9807976875"}
row_3 = {"employee_id":"EMP4564564566","last_name":"cruz","first_name":"mario"}
fieldnames = ["employee_id","first_name","last_name"]
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file,delimiter=',',fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(row_1) # write the first row
    writer.writerow(row_2) # write the second row
    writer.writerow(row_3) # writethe third row
f = open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'r')
print(f.read())
f.close()