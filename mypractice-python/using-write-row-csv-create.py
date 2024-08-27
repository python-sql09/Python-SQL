# 19.9 Using writerow
import csv
row_1 = ["employee_id","first_name","last_name"] # header row
row_2 = ["EMP2345235636","robert","balti"] # first row
row_3 = ["EMP2498799899","mark","smith"] # second row
row_4 = ["EMP2498989890","mary","caldwell"] # third row
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'w') as csv_file: # open file in write mode
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(row_1) # writing the header row
    writer.writerow(row_2) # writing the first row
    writer.writerow(row_3) # writing the second row
    writer.writerow(row_4) # writing the third row
f = open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'r')
print(f.read())
f.close()