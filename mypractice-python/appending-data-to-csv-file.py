# 19.11 Appending data to a CSV file
import csv
row_1 = ["EMP4564576566","rodney","evans"] # first row
row_2 = ["EMP9807976875","lesa","clapper"] # second row
row_3 = ["EMP4564564566","mario","cruz"]
# third row
# open file in append mode, which will add the data at the end of the file
with open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'a') as csv_file:
    # use the writer class to create a writer object
    # that we will use to write data into the file
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(row_1) # writing the first row
    writer.writerow(row_2) # writing the second row
    writer.writerow(row_3) # writing the third row
f = open('/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/employee.csv', 'r')
print(f.read())
f.close()